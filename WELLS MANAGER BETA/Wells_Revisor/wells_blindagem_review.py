# -*- coding: utf-8 -*-
"""Blindagem RPY: mesmo cadastro, sem executar o motor JSON."""
import re
from wells_isolador_renpy import segmentar
from wells_blindagem import LISTA_BLINDADOS, LISTA_TRADUZIVEIS, conflitos
WORD_RE = re.compile(r"[A-Za-zÀ-ÖØ-öø-ÿ]+(?:[-'][A-Za-zÀ-ÖØ-öø-ÿ]+)*", re.UNICODE)

def _term_pattern(term: str):
    """Fronteira lexical conservadora para termos cadastrados manualmente."""
    escaped = re.escape(term)
    left = r"(?<![A-Za-zÀ-ÖØ-öø-ÿ0-9_])" if term[:1].isalnum() else ""
    right = r"(?![A-Za-zÀ-ÖØ-öø-ÿ0-9_])" if term[-1:].isalnum() else ""
    return re.compile(left + escaped + right, re.IGNORECASE)


def _native_blindados(native: str, blindados, overlap):
    """Retorna termos manuais encontrados somente no texto humano do NATIVO.

    Conteúdo estrutural protegido pelo isolador Ren'Py (por exemplo [variavel]
    e {tag}) não participa da blindagem nominal. Isso evita transformar um
    identificador estrutural apenas porque seu texto coincide com um nome
    cadastrado pelo usuário.
    """
    texto_humano = "".join(
        seg.valor if seg.tipo != "protegido" else " "
        for seg in segmentar(native)
    )
    encontrados = []
    for term in blindados:
        if term.casefold() in overlap:
            continue
        if _term_pattern(term).search(texto_humano):
            encontrados.append(term)
    # Termos maiores primeiro evita sobreposição acidental entre cadastros.
    return sorted(encontrados, key=len, reverse=True)


def _protect_manual_terms(text: str, terms):
    """Protege termos que sobreviveram na tradução antes da revisão linguística.

    Se um nome já foi destruído pelo tradutor automático, não inventamos onde
    recolocá-lo: esse caso é reportado como unresolved e fica para a camada de
    reconstrução nativo↔traduzido.
    """
    protected = text
    tokens = []
    for term in terms:
        rx = _term_pattern(term)
        def repl(match):
            marker = f"__WELLS_NAME_{len(tokens):06d}__"
            tokens.append((marker, term))
            return marker
        protected = rx.sub(repl, protected)
    return protected, tokens


def _restore_manual_terms(text: str, tokens):
    for marker, term in tokens:
        text = text.replace(marker, term)
    return text


def _lexical_slots(text: str):
    """Separa palavras e o esqueleto não lexical sem interpretar semântica."""
    matches = list(WORD_RE.finditer(text))
    words = [m.group(0) for m in matches]
    separators = []
    last = 0
    for m in matches:
        separators.append(text[last:m.start()])
        last = m.end()
    separators.append(text[last:])
    return words, separators, matches


def _reconstruct_composite_slot(native: str, translated: str, missing,
                                blindados, traduziveis):
    """Reconstrói UM nome ausente apenas por alinhamento estrutural manual.

    A regra não tenta descobrir traduções. Ela só é válida quando:
    - há exatamente um blindado ausente;
    - todos os termos cadastrados envolvidos são uma única unidade lexical;
    - cada palavra do nativo foi classificada manualmente como blindada ou
      traduzível;
    - nativo e traduzido mantêm a mesma quantidade de slots lexicais e o mesmo
      esqueleto de separadores.

    Assim, o slot correspondente ao nome ausente é determinado pela estrutura,
    não por semelhança entre a tradução automática e o nome original.
    """
    if len(missing) != 1:
        return None

    term = missing[0]
    if WORD_RE.fullmatch(term) is None:
        return None

    native_words, native_sep, _ = _lexical_slots(native)
    translated_words, translated_sep, translated_matches = _lexical_slots(translated)
    if not native_words or len(native_words) != len(translated_words):
        return None
    if native_sep != translated_sep:
        return None

    blind_keys = {
        x.casefold() for x in blindados
        if WORD_RE.fullmatch(x) is not None
    }
    trans_keys = {
        x.casefold() for x in traduziveis
        if WORD_RE.fullmatch(x) is not None
    }
    classified = blind_keys | trans_keys
    if any(word.casefold() not in classified for word in native_words):
        return None

    target_positions = [
        i for i, word in enumerate(native_words)
        if word.casefold() == term.casefold()
    ]
    if len(target_positions) != 1:
        return None
    target = target_positions[0]

    # Blindados que não são o alvo precisam sobreviver no próprio slot. Isso
    # impede que um rearranjo silencioso de nomes seja tratado como alinhado.
    for i, word in enumerate(native_words):
        key = word.casefold()
        if i != target and key in blind_keys:
            if translated_words[i].casefold() != key:
                return None

    m = translated_matches[target]
    return translated[:m.start()] + term + translated[m.end():]




def revisar_com_blindagem(native, text, lists, reviewer):
    overlap = {x.casefold() for x in conflitos(lists)}
    terms = _native_blindados(native, lists[LISTA_BLINDADOS], overlap)
    # Detecta presença no texto original, antes de criar marcadores. Assim,
    # termos cadastrados sobrepostos não geram falsa ausência.
    human = "".join(s.valor if s.tipo != "protegido" else " " for s in segmentar(text))
    missing = [t for t in terms if not _term_pattern(t).search(human)]
    reconstructed = 0
    if len(missing) == 1 and native.strip().casefold() == missing[0].casefold():
        text = missing[0]
        missing = []
        reconstructed = 1
    elif missing:
        rebuilt = _reconstruct_composite_slot(native, text, missing,
                                              lists[LISTA_BLINDADOS], lists[LISTA_TRADUZIVEIS])
        if rebuilt is not None:
            text = rebuilt
            missing = []
            reconstructed = 1
    # Só o texto humano participa da proteção manual; identificadores Ren'Py
    # continuam sob responsabilidade do isolador estrutural.
    parts, names = [], []
    for seg in segmentar(text):
        if seg.tipo == "protegido":
            parts.append(seg.valor)
            continue
        part = seg.valor
        for term in terms:
            def replace(match):
                marker = f"__WELLS_NAME_{len(names):06d}__"
                names.append((marker, term))
                return marker
            part = _term_pattern(term).sub(replace, part)
        parts.append(part)
    reviewed, adjustments, tokens = reviewer("".join(parts))
    reviewed = _restore_manual_terms(reviewed, names)
    return reviewed, adjustments, tokens, {
        "protected_names": len(names), "reconstructed_names": reconstructed,
        "missing": missing,
        "conflict": any(_term_pattern(t).search(native) for t in conflitos(lists)),
    }
