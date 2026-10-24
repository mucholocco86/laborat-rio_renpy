# -*- coding: utf-8 -*-
"""Revisor JSON independente. Não importa nem executa o núcleo RPY tradicional."""
from __future__ import annotations

import ast
import re
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path
from xml.sax.saxutils import escape
import io
import tempfile
import json
from docx import Document
from wells_guia_ptbr_json import validar_revisao, analisar_registro
from wells_isolador_renpy_json import segmentar
from wells_base_linguistica_json import BaseLinguistica, preservar_caixa

_QUOTED = re.compile(r'^\s*"((?:\\.|[^"\\])*)"\s*$')
WORD_RE = re.compile(r"[A-Za-zÀ-ÖØ-öø-ÿ]+(?:[-'][A-Za-zÀ-ÖØ-öø-ÿ]+)*", re.UNICODE)
ENGLISH_SAFE = {"have","has","had","the","this","that","these","those","they","them","their","there","where","what","when","why","who","which","with","without","would","could","should","will","shall","can","may","might","must","any","some","your","you","our","out","about","from","into","over","under","again","also","only","very","more","most","less","not","and","but","for","are","was","were","been","being","is","am","do","does","did"}

# Regras deliberadamente conservadoras. A ferramenta prefere não alterar
# uma frase a "inventar" uma correção incerta.
# Não fazemos contrações gramaticais cegas. Em traduções de jogos, sequências
# como "de A'nai" ou "em A'khan" podem conter nomes próprios; uma regra
# genérica transformaria o texto válido em "da'nai" / "na'khan".
REPLACEMENTS = ()

KINSHIP = (
    "mãe", "pai", "irmã", "irmão", "filha", "filho", "avó", "avô",
    "tia", "tio", "prima", "primo", "esposa", "marido", "namorada",
    "namorado", "amiga", "amigo"
)

ALPHABET = "abcdefghijklmnopqrstuvwxyzáàâãéêíóôõúüç"

def find_dictionary(base_dir: Path):
    candidates = [
        base_dir / "dados_linguisticos" / "Palavras_PT-BR.txt",
    ]
    for p in candidates:
        if p.is_file():
            return p
    return None

def _decode_record(value: str):
    value = value.strip()
    m = _QUOTED.match(value)
    if not m:
        # Também aceita texto comum fora do formato do Wells Translator.
        return value, False
    try:
        return ast.literal_eval(value), True
    except Exception:
        return value, False

def _encode_record(value: str, quoted: bool):
    if not quoted:
        return value
    return '"' + (
        value.replace("\\", "\\\\")
             .replace('"', '\\"')
             .replace("\r", "\\r")
             .replace("\n", "\\n")
    ) + '"'

def _protect_renpy(text: str):
    """
    Usa o isolador baseado na fronteira do Ren'Py e substitui SOMENTE os
    segmentos protegidos por marcadores temporários. Assim, as regras
    estruturais podem enxergar a posição da variável/tag sem receber seu
    conteúdo interno.
    """
    tokens = []
    out = []
    for seg in segmentar(text):
        if seg.tipo == "protegido":
            marker = f"__WELLS_TOKEN_{len(tokens):06d}__"
            tokens.append(seg.valor)
            out.append(marker)
        else:
            out.append(seg.valor)
    return "".join(out), tokens

def _restore_renpy(text: str, tokens):
    for idx, token in enumerate(tokens):
        text = text.replace(f"__WELLS_TOKEN_{idx:06d}__", token)
    return text

def _preserve_case(original, replacement):
    if original.isupper():
        return replacement.upper()
    if original[:1].isupper():
        return replacement[:1].upper() + replacement[1:]
    return replacement

def _load_dictionary(path: Path | None, progress=None):
    if not path:
        return None
    words = set()
    size = max(1, path.stat().st_size)
    read = 0
    with path.open("r", encoding="utf-8-sig", errors="ignore") as f:
        for line in f:
            read += len(line.encode("utf-8", errors="ignore"))
            w = line.strip().lower()
            if w:
                words.add(w)
            if progress and len(words) % 100000 == 0:
                progress(min(10, 10 * read / size), "Carregando dicionário PT-BR...", None)
    return words

def _edit1_candidates(word, dictionary):
    if not dictionary or len(word) < 4 or len(word) > 18:
        return []
    w = word.lower()
    if w in dictionary:
        return []

    found = set()
    n = len(w)

    # remoção
    for i in range(n):
        c = w[:i] + w[i+1:]
        if c in dictionary:
            found.add(c)
            if len(found) > 1:
                return list(found)

    # transposição
    for i in range(n - 1):
        c = w[:i] + w[i+1] + w[i] + w[i+2:]
        if c in dictionary:
            found.add(c)
            if len(found) > 1:
                return list(found)

    # substituição
    for i in range(n):
        left, right = w[:i], w[i+1:]
        for ch in ALPHABET:
            if ch == w[i]:
                continue
            c = left + ch + right
            if c in dictionary:
                found.add(c)
                if len(found) > 1:
                    return list(found)

    # inserção
    for i in range(n + 1):
        left, right = w[:i], w[i:]
        for ch in ALPHABET:
            c = left + ch + right
            if c in dictionary:
                found.add(c)
                if len(found) > 1:
                    return list(found)

    return list(found)

def _safe_spelling(text, dictionary):
    if not dictionary:
        return text, 0

    changes = 0
    pieces = []
    last = 0

    for m in WORD_RE.finditer(text):
        pieces.append(text[last:m.start()])
        word = m.group(0)
        lower = word.lower()

        # Nomes próprios e marcadores internos ficam intactos.
        if word[:1].isupper() or lower in dictionary:
            pieces.append(word)
        else:
            candidates = _edit1_candidates(word, dictionary)
            if len(candidates) == 1:
                replacement = _preserve_case(word, candidates[0])
                pieces.append(replacement)
                changes += 1
            else:
                pieces.append(word)
        last = m.end()

    pieces.append(text[last:])
    return "".join(pieces), changes

def _grammar(text):
    changes = 0
    original = text

    # espaços duplicados (sem tocar em quebras)
    new = re.sub(r"[ \t]{2,}", " ", text)
    if new != text:
        changes += 1
        text = new

    # remove espaço antes de pontuação
    new = re.sub(r"\s+([,.;:!?])", r"\1", text)
    if new != text:
        changes += 1
        text = new

    # adiciona espaço depois da pontuação quando claramente faltou
    new = re.sub(r"([,;:!?])(?=[A-Za-zÀ-ÖØ-öø-ÿ])", r"\1 ", text)
    if new != text:
        changes += 1
        text = new

    # contrações comuns
    for rx, repl in REPLACEMENTS:
        new = rx.sub(repl, text)
        if new != text:
            changes += 1
            text = new

    # Caso típico de tradução automática: "a mãe [nome] de"
    kin = "|".join(map(re.escape, KINSHIP))
    rx = re.compile(
        rf"\b({kin})\s+(__WELLS_TOKEN_\d{{6}}__)\s+de\b",
        re.I
    )
    new = rx.sub(r"\1 de \2", text)
    if new != text:
        changes += 1
        text = new

    # ------------------------------------------------------------------
    # Revisão estrutural PT-BR para traduções automáticas.
    #
    # Estas regras são intencionalmente contextuais: não tentam "reescrever"
    # qualquer frase. Elas corrigem padrões em que a tradução literal deixa
    # uma construção que não funciona em português, inclusive ao redor dos
    # marcadores protegidos do Ren'Py.
    # ------------------------------------------------------------------

    structural_rules = (
        # "desde [player] nasceu" -> "desde que [player] nasceu"
        (re.compile(r"\bdesde\s+(?!que\b)(?=(?:__WELLS_TOKEN_\d{6}__|[A-Za-zÀ-ÖØ-öø-ÿ]+)\s+(?:nasceu|chegou|voltou|saiu|entrou|partiu|começou|era|estava|ficou)\b)", re.I), "desde que "),

        # Traduções literais frequentes de English "returns" como substantivo.
        (re.compile(r"(__WELLS_TOKEN_\d{6}__)\s+devoluções\b", re.I), r"\1 voltar"),

        # English "where X lives?" -> português natural.
        (re.compile(r"\bonde\s+(__WELLS_TOKEN_\d{6}__)\s+vidas\?", re.I), r"onde \1 mora?"),

        # Gerúndio inglês depois de "de": "o pensamento de X estando...".
        (re.compile(r"\b(o\s+pensamento\s+de\s+)(__WELLS_TOKEN_\d{6}__)\s+estando\b", re.I), r"\1\2 estar"),

        # "Quando se trata de X Você..." precisa separar a oração.
        (re.compile(r"(\bquando\s+se\s+trata\s+de\s+__WELLS_TOKEN_\d{6}__)\s+Você\b", re.I), r"\1, você"),

        # Frases coladas após marcador: "Depende de X Ele...".
        (re.compile(r"(\bdepende\s+de\s+__WELLS_TOKEN_\d{6}__)\s+(?=(?:Ele|Ela|Isso|Este|Esta|Esse|Essa)\b)", re.I), r"\1. "),

        # "Você pode me chamar de X E ..." -> encerra a primeira oração.
        (re.compile(r"(\b(?:pode|podem)\s+me\s+chamar\s+de\s+__WELLS_TOKEN_\d{6}__)\s+E\s+(?=[A-ZÁÀÂÃÉÊÍÓÔÕÚÜÇ])", re.I), r"\1. E "),

        # "Deixaremos isso a cargo de X Para encontrar..." é calque de
        # "leave it to X to find...".
        (re.compile(r"(\b(?:deixaremos|deixe|deixem)\s+[^.!?]{0,80}?\ba\s+cargo\s+de\s+)(__WELLS_TOKEN_\d{6}__)\s+para\s+(?=encontrar\b)", re.I), r"\1\2 "),

        # Interjeição inglesa "Goodness, X" traduzida literalmente.
        (re.compile(r"(?<![A-Za-zÀ-ÖØ-öø-ÿ])Bondade\s+(__WELLS_TOKEN_\d{6}__)\s+(?=(?:Sinto|Você|Tu|Ele|Ela|Eu)\b)", re.I), r"Nossa, \1, "),

        # Regra removida na v2: sujeito/pronome exige contexto; não é seguro inferir localmente.

        # Calque interrogativo: "O que é [mc] O que está fazendo?" -> "O que [mc] está fazendo?"
        (re.compile(r"\bO\s+que\s+é\s+(__WELLS_TOKEN_\d{6}__)\s+O\s+que\s+(?=(?:está|estava|vai|iria)\b)", re.I), r"O que \1 "),
    )

    for rx, repl in structural_rules:
        new = rx.sub(repl, text)
        if new != text:
            # Conta ocorrências efetivamente substituídas, não apenas a regra.
            changes += 1
            text = new

    # Casos de "X dever..." costumam vir do inglês "X should...".
    # Sem o restante da oração não existe uma conjugação única segura; por isso
    # o revisor não inventa uma palavra. O mesmo vale para frases truncadas.

    # Repetições são preservadas. Em diálogo, "tchau tchau", "não não",
    # "vai vai" etc. podem ser intencionais; sem contexto não há correção
    # suficientemente segura para removê-las automaticamente.

    return text, changes

def review_text(text, dictionary=None, base_linguistica=None):
    protected, tokens = _protect_renpy(text)
    before_tokens = list(tokens)

    reviewed, grammar_changes = _grammar(protected)
    # v2: não usa distância de edição para trocar palavras válidas/ambíguas.
    # Apenas restaura acento quando a base inteira oferece UMA forma inequívoca.
    spelling_changes = 0
    if base_linguistica is not None:
        parts, last = [], 0
        for m in WORD_RE.finditer(reviewed):
            parts.append(reviewed[last:m.start()])
            w = m.group(0)
            sug = None if (w[:1].isupper() or "-" in w or "'" in w or w.casefold() in ENGLISH_SAFE) else base_linguistica.restaurar_acento_univoco(w)
            if sug:
                parts.append(preservar_caixa(w, sug))
                spelling_changes += 1
            else:
                parts.append(w)
            last = m.end()
        parts.append(reviewed[last:])
        reviewed = "".join(parts)
    else:
        reviewed, spelling_changes = _safe_spelling(reviewed, dictionary)
    reviewed = _restore_renpy(reviewed, tokens)

    # Garantia estrutural: todos os tokens precisam sobreviver idênticos.
    for token in before_tokens:
        if token not in reviewed:
            raise ValueError(f"Proteção Ren'Py falhou para o token: {token}")

    # Segunda camada: o Guia Linguístico revisa a própria revisão.
    # Se a proposta introduzir uma anomalia estrutural nova, ela é rejeitada.
    aprovado, motivo = validar_revisao(text, reviewed)
    if not aprovado:
        return text, 0, len(tokens)

    return reviewed, grammar_changes + spelling_changes, len(tokens)


def _correct_source_anchored_structures(native: str, translated: str):
    """Corrige calques de baixa ambiguidade usando o registro nativo pareado."""
    changes = 0
    protected_native, _ = _protect_renpy(native)
    protected, tokens = _protect_renpy(translated)

    new = re.sub(
        r"(?i)((?:__WELLS_TOKEN_\d{6}__)+Moralidade\s+Leve(?:__WELLS_TOKEN_\d{6}__)+\s+)aumentado\b",
        r"\1aumentada",
        protected,
    )
    if new != protected:
        protected = new
        changes += 1

    native_names = re.findall(
        r"(__WELLS_TOKEN_\d{6}__)\s*['’]s\s+(?:[A-Za-z-]+\s+){0,3}plan\b",
        protected_native,
        re.I,
    )
    if native_names:
        name = re.escape(native_names[0])
        rx = re.compile(
            rf"(?i)\b(concordo\s+com)\s+({name})\s+(o\s+(?:(?:[\wÀ-ÖØ-öø-ÿ-]+\s+){{0,3}})plano(?:\s+[\wÀ-ÖØ-öø-ÿ-]+){{0,3}})\s+de(\.)?(?=$|\s)"
        )

        def reorder(match):
            punctuation = match.group(4) or ""
            return f"{match.group(1)} {match.group(3)} de {match.group(2)}{punctuation}"

        new, count = rx.subn(reorder, protected, count=1)
        if count:
            protected = new
            changes += count

    return _restore_renpy(protected, tokens), changes

def _read_txt(path: Path):
    return path.read_text(encoding="utf-8-sig").splitlines()

def _write_txt(path: Path, records):
    path.write_text("\n".join(records) + ("\n" if records else ""), encoding="utf-8")

def _read_docx(path: Path):
    ns = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
    with zipfile.ZipFile(path, "r") as z:
        xml_data = z.read("word/document.xml")
    root = ET.fromstring(xml_data)
    records = []
    for p in root.iter(ns + "p"):
        parts = []
        for node in p.iter():
            if node.tag == ns + "t" and node.text:
                parts.append(node.text)
            elif node.tag == ns + "tab":
                parts.append("\t")
            elif node.tag in (ns + "br", ns + "cr"):
                parts.append("\n")
        records.append("".join(parts))
    return records

def _xml_safe(value):
    return "".join(ch for ch in str(value) if ch in "\t\n\r" or ord(ch) >= 0x20)

def _make_docx(records):
    template = Document()
    stream = io.BytesIO()
    template.save(stream)
    paragraphs = []
    for value in records:
        paragraphs.append(
            '<w:p><w:r><w:t xml:space="preserve">' +
            escape(_xml_safe(value)) +
            '</w:t></w:r></w:p>'
        )
    document_xml = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">'
        '<w:body>' + "".join(paragraphs) +
        '<w:sectPr><w:pgSz w:w="12240" w:h="15840"/>'
        '<w:pgMar w:top="1440" w:right="1440" w:bottom="1440" w:left="1440" '
        'w:header="720" w:footer="720" w:gutter="0"/></w:sectPr>'
        '</w:body></w:document>'
    ).encode("utf-8")
    out = io.BytesIO()
    stream.seek(0)
    with zipfile.ZipFile(stream, "r") as zin, zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as zout:
        for item in zin.infolist():
            if item.filename == "word/document.xml":
                zout.writestr(item, document_xml)
            else:
                zout.writestr(item, zin.read(item.filename))
    return out.getvalue()

def _write_docx(path: Path, records):
    path.write_bytes(_make_docx(records))

def review_file(path: Path, base_dir: Path, progress=None):
    path = Path(path).resolve()
    if path.suffix.lower() not in (".txt", ".docx"):
        raise ValueError("Selecione um arquivo TXT ou DOCX.")

    dictionary_path = find_dictionary(base_dir)
    dictionary = _load_dictionary(dictionary_path, progress=progress)
    try:
        base_linguistica = BaseLinguistica(base_dir)
    except Exception:
        base_linguistica = None

    if path.suffix.lower() == ".txt":
        records = _read_txt(path)
    else:
        records = _read_docx(path)

    total = len(records)
    if total == 0:
        raise ValueError("O documento não possui linhas/parágrafos para revisar.")

    changed_lines = 0
    changes = 0
    token_count = 0
    output_records = []

    start_pct = 10 if dictionary is not None else 0
    span = 88 - start_pct

    # Workspace efêmero: organiza cada diálogo por ID durante a revisão.
    # É removido no final; nunca vira arquivo de saída para o usuário.
    temp_handle = tempfile.NamedTemporaryFile(
        mode="w", encoding="utf-8", suffix=".wells_review.json",
        prefix="wells_revisor_", delete=False
    )
    temp_path = Path(temp_handle.name)
    temp_handle.write("[\n")
    first_temp = True

    for idx, record in enumerate(records, 1):
        text, quoted = _decode_record(record)
        reviewed, count, tokens = review_text(text, dictionary=dictionary, base_linguistica=base_linguistica)
        encoded = _encode_record(reviewed, quoted)

        item = analisar_registro(idx, text, reviewed, tokens)
        if not first_temp:
            temp_handle.write(",\n")
        json.dump(item, temp_handle, ensure_ascii=False)
        first_temp = False

        if encoded != record:
            changed_lines += 1
        changes += count
        token_count += tokens
        output_records.append(encoded)

        if progress and (idx == 1 or idx % 50 == 0 or idx == total):
            pct = start_pct + span * idx / total
            progress(
                pct,
                f"Revisando linhas: {idx}/{total}",
                f"Revisadas: {idx}/{total} | Alteradas: {changed_lines}"
                if idx % 500 == 0 or idx == total else None
            )

    temp_handle.write("\n]\n")
    temp_handle.close()

    # O revisor trabalha diretamente sobre o documento selecionado.
    # Isso mantém o fluxo do Wells Translator simples e evita cópias *_revisado.
    output = path

    if path.suffix.lower() == ".txt":
        _write_txt(output, output_records)
    else:
        _write_docx(output, output_records)

    try:
        temp_path.unlink(missing_ok=True)
    except Exception:
        pass

    if progress:
        progress(100, "Documento revisado.", None)

    return {
        "output": str(output),
        "records": total,
        "changed": changed_lines,
        "changes": changed_lines,
        "internal_adjustments": changes,
        "tokens": token_count,
        "dictionary": str(dictionary_path) if dictionary_path else None,
    }


# ---------------------------------------------------------------------------
# REVISÃO JSON PAREADA
# ---------------------------------------------------------------------------
def _name_case(term: str, *references):
    """Mantém gritos em caixa alta sem mudar a grafia nominal cadastrada."""
    if any(reference.isupper() for reference in references):
        return term.upper()
    return term


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
            tokens.append((marker, _name_case(term, match.group(0))))
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
    return translated[:m.start()] + _name_case(term, native_words[target], translated_words[target]) + translated[m.end():]



def diagnosticar_par_linguistico(native: str, translated: str):
    """Diagnósticos que só são seguros porque o JSON possui nativo + tradução.

    Não retraduz nem corrige. O nativo funciona apenas como âncora estrutural
    para apontar quando a tradução tornou específica uma relação originalmente
    aberta ou escolheu um sentido incompatível com a construção.
    """
    issues = []
    n = native.casefold()
    tr = translated.casefold()

    def add(code, message):
        issues.append({"code": code, "message": message})

    if ("she's your younger" in n or "she's your older" in n):
        if re.search(r"\b(?:filha|irmã)\b", tr):
            add("relacao_aberta_especificada", "A tradução fixa um parentesco onde o nativo deixa a relação aberta.")

    if re.search(r"\byou\s+call\b", n) and re.search(r"\bvoc[eê]\s+liga\b", tr):
        add("call_falso_cognato", "Em construção de tratamento/relação, 'call' foi traduzido como 'ligar'.")

    if "so i am her" in n and re.search(r"\b(?:eu\s+)?sou\s+ela\b", tr):
        add("relacao_pronominal_quebrada", "A tradução perdeu a construção relacional equivalente a 'I am her ...'.")

    return issues

def review_json_pair(native_path: Path, translated_path: Path, base_dir: Path,
                     blindagem_path: Path | None = None, progress=None):
    """Revisa o traduzido usando o nativo como âncora sem congelar o registro.

    NOMES_BLINDADOS são termos manuais procurados primeiro no NATIVO. Se o
    termo também sobreviveu no traduzido, ele é isolado durante a revisão e
    restaurado exatamente com a grafia cadastrada. O restante do registro
    continua revisável.

    Se o NATIVO inteiro for exatamente um termo blindado destruído pela tradução,
    a restauração é determinística e o termo é recuperado. Em registro composto,
    só há reconstrução quando todos os slots nativos foram classificados
    manualmente e o par preserva estrutura lexical equivalente; fora disso, o
    caso permanece em unresolved_names.

    NOMES_TRADUZIVEIS continuam explicitamente livres para revisão. Não existe
    inferência automática de nomes e conflitos entre listas não recebem
    prioridade escondida.
    """
    from wells_blindagem_json import (
        LISTA_BLINDADOS, LISTA_TRADUZIVEIS, carregar_listas, conflitos
    )

    native_path = Path(native_path).resolve()
    translated_path = Path(translated_path).resolve()
    if native_path.suffix.lower() != translated_path.suffix.lower():
        raise ValueError("Nativo e traduzido precisam usar o mesmo formato.")
    if native_path.suffix.lower() not in (".txt", ".docx"):
        raise ValueError("Selecione pares TXT ou DOCX.")

    reader = _read_txt if native_path.suffix.lower() == ".txt" else _read_docx
    writer = _write_txt if translated_path.suffix.lower() == ".txt" else _write_docx
    native_rows = reader(native_path)
    translated_rows = reader(translated_path)
    if len(native_rows) != len(translated_rows):
        raise ValueError(
            f"Par desalinhado: {len(native_rows)} registros nativos e "
            f"{len(translated_rows)} traduzidos."
        )
    if not native_rows:
        raise ValueError("O par não possui registros para revisar.")

    # Um mapa JSON Wells identifica a exportação limpa. Ele ancora a ordem,
    # valida o lado nativo e permite revisar textos sem aspas JSON externas.
    map_path = native_path.parent / "wells_json_translation_map.json"
    clean_meta = None
    clean_offset = 0
    if map_path.is_file():
        try:
            map_payload = json.loads(map_path.read_text(encoding="utf-8-sig"))
        except Exception as exc:
            raise ValueError(f"Mapa JSON Wells inválido: {exc}") from exc
        if (map_payload.get("schema") != "wells-json-translation-map"
                or map_payload.get("version") != 1
                or map_payload.get("record_encoding") != "wells-json-clean-v1"):
            raise ValueError("Mapa JSON incompatível com esta revisão.")
        mapped = map_payload.get("records")
        blocks = map_payload.get("blocks")
        if not isinstance(mapped, list) or not isinstance(blocks, list):
            raise ValueError("Mapa JSON sem registros/blocos válidos.")
        match = re.search(r"_(\d+)$", native_path.stem)
        block_number = int(match.group(1)) if match else 0
        block = next((item for item in blocks if item.get("number") == block_number), None)
        if block is None:
            raise ValueError(f"Bloco {block_number or 'completo'} não consta no mapa JSON.")
        clean_offset = int(block.get("start", -1))
        clean_count = int(block.get("count", -1))
        if clean_offset < 0 or clean_count != len(native_rows) or clean_count != len(translated_rows):
            raise ValueError("Par nativo/traduzido não corresponde ao bloco registrado no mapa.")
        clean_meta = mapped[clean_offset:clean_offset + clean_count]
        if len(clean_meta) != clean_count:
            raise ValueError("Faixa do bloco excede o mapa JSON.")
        translator_dir = Path(__file__).resolve().parents[1] / "Wells_Translator"
        if str(translator_dir) not in __import__("sys").path:
            __import__("sys").path.insert(0, str(translator_dir))
        from wells_json_transport import restore_transport, encode_transport, sha256_text
        natives, translated = [], []
        for local_idx, (meta, native_row, translated_row) in enumerate(
                zip(clean_meta, native_rows, translated_rows), 1):
            global_idx = clean_offset + local_idx
            if not isinstance(meta, dict) or meta.get("id") != f"J{global_idx:08d}":
                raise ValueError(f"Ordem/ID divergente no mapa JSON, registro {global_idx}.")
            native = restore_transport(
                native_row, meta.get("native_protected", []),
                meta.get("native_quotes", 0), global_idx, "nativo"
            )
            if sha256_text(native) != meta.get("native_sha256"):
                raise ValueError(f"Nativo divergente do mapa JSON no registro {global_idx}.")
            value = restore_transport(
                translated_row, meta.get("translated_protected", []),
                meta.get("translated_quotes", 0), global_idx, "traduzido"
            )
            natives.append(native)
            translated.append(value)
    else:
        # Compatibilidade com o formato antigo de strings JSON delimitadas.
        natives = native_rows
        translated = translated_rows

    lists = carregar_listas(blindagem_path) if blindagem_path else {
        LISTA_BLINDADOS: [], LISTA_TRADUZIVEIS: []
    }
    blindados = list(lists[LISTA_BLINDADOS])
    traduziveis = list(lists[LISTA_TRADUZIVEIS])
    overlap = {x.casefold() for x in conflitos(lists)}

    try:
        base_linguistica = BaseLinguistica(base_dir)
    except Exception:
        base_linguistica = None

    output = []
    changed = 0
    protected_records = 0
    protected_names = 0
    unresolved_names = []
    reconstructed_names = 0
    token_count = 0
    conflict_records = 0
    linguistic_issues = []
    total = len(natives)

    for idx, (native_record, translated_record) in enumerate(zip(natives, translated), 1):
        if clean_meta is not None:
            native, text, quoted = native_record, translated_record, False
        else:
            native, _native_quoted = _decode_record(native_record)
            text, quoted = _decode_record(translated_record)

        for issue in diagnosticar_par_linguistico(native, text):
            linguistic_issues.append({"record": idx, **issue, "native": native, "translated": text})

        terms = _native_blindados(native, blindados, overlap)
        if overlap and any(_term_pattern(term).search(native)
                           for term in lists[LISTA_BLINDADOS]
                           if term.casefold() in overlap):
            conflict_records += 1

        protected_text, manual_tokens = _protect_manual_terms(text, terms)
        present = {term.casefold() for _marker, term in manual_tokens}
        missing = [term for term in terms if term.casefold() not in present]

        # Caso determinístico 1: o registro NATIVO inteiro é exatamente um
        # termo blindado destruído pela tradução.
        reconstructed = []
        if missing:
            native_stripped = native.strip()
            exact_missing = [
                term for term in missing
                if native_stripped.casefold() == term.casefold()
            ]
            if len(exact_missing) == 1:
                term = exact_missing[0]
                text = _name_case(term, native_stripped, text)
                reconstructed.append(term)
                missing = [x for x in missing if x.casefold() != term.casefold()]

        # Caso determinístico 2: registro composto integralmente classificado
        # pelo usuário e com slots lexicais estruturalmente alinhados.
        if missing:
            rebuilt = _reconstruct_composite_slot(
                native, text, missing, blindados, traduziveis
            )
            if rebuilt is not None:
                term = missing[0]
                text = rebuilt
                reconstructed.append(term)
                missing = []

        # A proteção é refeita depois de qualquer reconstrução para que o nome
        # recuperado também atravesse a revisão linguística como token opaco.
        protected_text, manual_tokens = _protect_manual_terms(text, terms)

        for term in missing:
            unresolved_names.append({
                "record": idx,
                "term": term,
                "native": native,
                "translated": text,
            })

        reviewed, _count, tokens = review_text(
            protected_text, dictionary=None, base_linguistica=base_linguistica
        )
        reviewed = _restore_manual_terms(reviewed, manual_tokens)
        reviewed, _anchored_changes = _correct_source_anchored_structures(native, reviewed)

        if manual_tokens:
            protected_records += 1
            protected_names += len(manual_tokens)
        reconstructed_names += len(reconstructed)

        if clean_meta is not None:
            meta = clean_meta[idx - 1]
            clean_encoded, protected_after, quotes_after = encode_transport(reviewed)
            if protected_after != meta.get("translated_protected", []) or quotes_after != meta.get("translated_quotes", 0):
                raise ValueError(
                    f"A revisão alteraria tags Ren'Py ou aspas protegidas no registro {clean_offset + idx}."
                )
            encoded = clean_encoded
        else:
            encoded = _encode_record(reviewed, quoted)
        if encoded != translated_record:
            changed += 1
        token_count += tokens
        output.append(encoded)

        if progress and (idx == 1 or idx % 50 == 0 or idx == total):
            progress(
                98 * idx / total,
                f"Revisando par JSON: {idx}/{total}",
                f"Revisados: {idx}/{total} | Alterados: {changed}"
                if idx % 500 == 0 or idx == total else None
            )

    writer(translated_path, output)
    if progress:
        progress(100, "Documento traduzido JSON revisado.", None)

    return {
        "output": str(translated_path),
        "records": total,
        "changed": changed,
        "protected_records": protected_records,
        "protected_names": protected_names,
        "unresolved_names": unresolved_names,
        "reconstructed_names": reconstructed_names,
        "conflict_records": conflict_records,
        "linguistic_issues": linguistic_issues,
        "tokens": token_count,
        "native_unchanged": str(native_path),
    }

