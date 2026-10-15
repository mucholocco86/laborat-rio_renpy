# -*- coding: utf-8 -*-
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
from wells_guia_ptbr import validar_revisao, analisar_registro
from wells_isolador_renpy import segmentar
from wells_base_linguistica import BaseLinguistica, preservar_caixa

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


def diagnosticar_texto(text):
    """Detecta anomalias fortes sem inventar uma reescrita.

    Esta camada é deliberadamente separada de review_text: problemas de
    concordância/ordem podem ser inequívocos como defeito, mas ainda admitir
    mais de uma correção válida no contexto narrativo.
    """
    protegido, _tokens = _protect_renpy(text)
    issues = []

    def add(code, message, trecho):
        issues.append({"code": code, "message": message, "trecho": trecho})

    for m in re.finditer(r"\bSeu\s+(Mãe|Irmã|Filha|Avó|Tia|Esposa|Namorada|Amiga)\b", protegido, re.I):
        add("concordancia_possessivo", "Possessivo masculino antes de termo feminino.", m.group(0))

    for m in re.finditer(r"\bO\s+nome\s+de\s+é\b", protegido, re.I):
        add("ordem_nome_quebrada", "Construção 'o nome de é' indica ordem sintática quebrada.", m.group(0))

    for m in re.finditer(r"\b(?:dela|dele)\s+(Filho|Filha|Irmão|Irmã)\b", protegido):
        add("parentesco_pos_pronome", "Parentesco aparece solto após pronome relacional.", m.group(0))

    for m in re.finditer(r"[.!?]\s+(Irmão|Irmã|Filho|Filha)\s+E\b", protegido):
        add("fragmento_parentesco", "Termo de parentesco isolado como fragmento de frase.", m.group(1))

    return issues

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

def review_file(path: Path, base_dir: Path, progress=None, native_path=None, blindagem_path=None):
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

    natives = None
    lists = None
    if native_path is not None:
        from wells_blindagem import carregar_listas
        native_path = Path(native_path).resolve()
        if native_path == path or native_path.suffix.lower() != path.suffix.lower():
            raise ValueError("OLD e NEW devem ser arquivos distintos do mesmo formato.")
        natives = _read_txt(native_path) if path.suffix.lower() == ".txt" else _read_docx(native_path)
        if len(natives) != len(records):
            raise ValueError("Par OLD/NEW desalinhado. Nada foi alterado.")
        # Valida todos os registros antes de qualquer gravação.
        for label, values in (("OLD", natives), ("NEW", records)):
            for index, value in enumerate(values, 1):
                if not _QUOTED.fullmatch(value):
                    raise ValueError(f"Registro {index} inválido no {label}; mantenha as aspas.")
                try:
                    decoded = ast.literal_eval(value.strip())
                except Exception as exc:
                    raise ValueError(f"Registro {index} inválido no {label}.") from exc
                if not isinstance(decoded, str):
                    raise ValueError(f"Registro {index} não textual no {label}.")
        lists = carregar_listas(blindagem_path) if blindagem_path else {"NOMES_BLINDADOS": [], "NOMES_TRADUZIVEIS": []}

    total = len(records)
    if total == 0:
        raise ValueError("O documento não possui linhas/parágrafos para revisar.")

    changed_lines = 0
    changes = 0
    token_count = 0
    linguistic_issues = []
    protected_names = reconstructed_names = conflict_records = 0
    unresolved_names = []
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
        for issue in diagnosticar_texto(text):
            linguistic_issues.append({"record": idx, **issue, "text": text})
        if natives is None:
            reviewed, count, tokens = review_text(text, dictionary=dictionary, base_linguistica=base_linguistica)
        else:
            from wells_blindagem_review import revisar_com_blindagem
            native = ast.literal_eval(natives[idx - 1].strip())
            reviewed, count, tokens, stats = revisar_com_blindagem(
                native, text, lists,
                lambda value: review_text(value, dictionary=dictionary, base_linguistica=base_linguistica),
            )
            protected_names += stats["protected_names"]
            reconstructed_names += stats["reconstructed_names"]
            conflict_records += int(stats["conflict"])
            unresolved_names.extend({"record": idx, "term": term, "native": native, "translated": text}
                                    for term in stats["missing"])

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
        "linguistic_issues": linguistic_issues,
        "protected_names": protected_names,
        "reconstructed_names": reconstructed_names,
        "unresolved_names": unresolved_names,
        "conflict_records": conflict_records,
        "native_unchanged": str(native_path) if native_path is not None else None,
        "dictionary": str(dictionary_path) if dictionary_path else None,
    }

