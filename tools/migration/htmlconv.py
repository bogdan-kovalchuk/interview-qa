"""HTML fragment -> plain text / Markdown helpers shared by the migration scripts.

The legacy deck stores Front/Back as small HTML fragments (`<span class="key">`,
`<code>`, `<pre class="code-block">`, `<div class="source">`, `<br>`, `&nbsp;`,
occasional `<span class="warn">`). This module turns those into the Markdown the
content contract expects, without ever touching content/.
"""
from __future__ import annotations

import html
import re

SOURCE_DIV_RE = re.compile(r'<div class="source">.*?</div>\s*$', re.DOTALL)
KEY_SPAN_OPEN = '<span class="key">'
SPAN_TAG_RE = re.compile(r"<span\b[^>]*>|</span>")
WARN_SPAN_RE = re.compile(r'<span class="warn">(.*?)</span>', re.DOTALL)
CODE_INLINE_RE = re.compile(r'<code>(.*?)</code>', re.DOTALL)
PRE_BLOCK_RE = re.compile(r'<pre class="code-block"><code>(.*?)</code></pre>', re.DOTALL)


def _match_key_span(body: str) -> tuple[str, int] | None:
    """(inner_html, end_offset) for a leading `<span class="key">`, or None.

    Finds the span's *true* matching close by tracking nesting depth over
    every `<span ...>`/`</span>` in the text, instead of the non-greedy
    `.*?</span>` a plain regex would use - which stops at the first close it
    sees, even one belonging to a tag nested inside (see the call site for
    why that matters here).
    """
    if not body.startswith(KEY_SPAN_OPEN):
        return None
    depth = 1
    pos = len(KEY_SPAN_OPEN)
    for tag in SPAN_TAG_RE.finditer(body, pos):
        depth += 1 if tag.group(0) != "</span>" else -1
        if depth == 0:
            return body[pos : tag.start()], tag.end()
    return None

# Typography the project forbids anywhere in content (AGENTS.md).
EM_DASH = "—"
EN_DASH = "–"
ARROW_RIGHT = "→"
ARROW_LEFT = "←"
DOUBLE_ARROW = "⇒"
BIDI_ARROW = "↔"


def strip_source_div(back_html: str) -> str:
    return SOURCE_DIV_RE.sub("", back_html).strip()


# A handful of legacy rows contain a literal backslash-u escape (typed as text,
# never decoded by whatever produced the .txt export) instead of the real
# character. Arrow code points still have to become words/`->` per AGENTS.md;
# everything else is a genuine example character and gets decoded for real.
LITERAL_UESCAPE_RE = re.compile(r"\\u([0-9a-fA-F]{4})")
_ARROW_CODEPOINTS = {"2192": " -> ", "2190": " <- ", "21d2": " -> ", "21D2": " -> "}


def _decode_literal_uescape(match: re.Match[str]) -> str:
    code = match.group(1)
    if code.lower() in {"2192", "2190", "21d2"}:
        return _ARROW_CODEPOINTS[code if code in _ARROW_CODEPOINTS else code.lower()]
    return chr(int(code, 16))


def fix_typography(text: str) -> str:
    text = LITERAL_UESCAPE_RE.sub(_decode_literal_uescape, text)
    text = text.replace(EM_DASH, EN_DASH)
    text = re.sub(r"\s*" + ARROW_RIGHT + r"\s*", " -> ", text)
    text = re.sub(r"\s*" + ARROW_LEFT + r"\s*", " <- ", text)
    text = re.sub(r"\s*" + DOUBLE_ARROW + r"\s*", " -> ", text)
    text = re.sub(r"\s*" + BIDI_ARROW + r"\s*", " vs ", text)
    text = re.sub(r"[ \t]{2,}", " ", text)
    return text


def unescape_code(raw_code: str) -> str:
    """A <pre class="code-block"><code>...</code></pre> body -> a real code string.

    AGENTS.md forbids em dash/arrows everywhere in content, including inside
    a fenced code block's comments (the `schema` gate scans the whole file).
    Only the forbidden characters themselves are touched here - a plain `-`
    reads more naturally than an en dash inside a `#` comment, and code
    otherwise keeps its exact original whitespace/formatting.
    """
    code = raw_code.replace("<br>", "\n")
    code = html.unescape(code)
    code = code.replace(EM_DASH, "-")
    code = code.replace(ARROW_RIGHT, "->").replace(ARROW_LEFT, "<-")
    code = code.replace(DOUBLE_ARROW, "->").replace(BIDI_ARROW, "<->")
    return code.strip("\n")


def html_fragment_to_plain(fragment: str) -> str:
    """Convert a Front (title) HTML fragment into a single-line plain string.

    `<code>` -> backticks, `<br>`/`&nbsp;` -> single spaces, entities decoded.
    """
    text = fragment
    text = CODE_INLINE_RE.sub(lambda m: f"`{html.unescape(m.group(1))}`", text)
    text = text.replace("<br>", " ")
    text = text.replace("&nbsp;", " ")
    text = re.sub(r"<[^>]+>", "", text)
    text = html.unescape(text)
    text = fix_typography(text)
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\s*\n\s*", " ", text)
    return text.strip()


def back_to_short_answer_md(back_html: str) -> tuple[str, str | None]:
    """Convert a legacy Back HTML field into (short_answer_markdown, code_lang_or_None).

    Returns Markdown text using the subset meta/QUESTIONS.md section 7 allows:
    a leading **bold** key sentence, plain prose, at most one fenced code block,
    inline code as backticks, and `<span class="warn">` passed through raw.
    """
    body = strip_source_div(back_html)

    # Pull the one fenced code block out first (if any) so later regexes don't
    # have to worry about backticks/entities inside it.
    code_block: str | None = None
    match = PRE_BLOCK_RE.search(body)
    if match:
        code_block = unescape_code(match.group(1))
        body = body[: match.start()] + "\x00CODEBLOCK\x00" + body[match.end() :]

    # Leading key sentence -> **bold**.
    #
    # `KEY_SPAN_RE`'s non-greedy `.*?</span>` is only correct when the key
    # span has no nested tag of its own. 4 of the 392 legacy cards
    # (PYI_03_007, PYI_03_008, PYI_12_013, PYI_16_014) nest a
    # `<span class="warn">` inside `<span class="key">` - a structure the new
    # contract forbids outright (".warn" may never nest in ".key"), but which
    # existed in the old deck. A naive non-greedy match stops at the warn's
    # own `</span>`, truncates the bold text, and leaves a stray closing
    # `</span>` dangling in the output. `_match_key_span` below finds the
    # *true* matching close by tracking nesting depth, and any `.warn` found
    # inside is unwrapped (its text folded into the bold, tags dropped) since
    # the two spans coincide or overlap in every legacy case that does this -
    # there is no version of "partially bold, partially warn" to preserve.
    key_span = _match_key_span(body)
    if key_span:
        inner, end = key_span
        inner = re.sub(r'</?span(?: class="warn")?>', "", inner)
        body = "**" + inner + "**" + body[end:]

    # warn spans: keep the wrapper, convert nested <code> to backticks.
    def _warn_sub(m: re.Match[str]) -> str:
        inner = CODE_INLINE_RE.sub(lambda c: f"`{html.unescape(c.group(1))}`", m.group(1))
        inner = html.unescape(re.sub(r"<[^>]+>", "", inner))
        return f'<span class="warn">{inner}</span>'

    body = WARN_SPAN_RE.sub(_warn_sub, body)

    # Remaining inline code.
    body = CODE_INLINE_RE.sub(lambda m: f"`{html.unescape(m.group(1))}`", body)

    body = html.unescape(body)
    body = fix_typography(body)
    body = re.sub(r"[ \t]+", " ", body)
    body = re.sub(r"\n{3,}", "\n\n", body)
    body = body.strip()

    if code_block is not None:
        lang = "python" if re.search(r"\bdef |\bclass |import |lambda", code_block) else "text"
        fence = f"```{lang}\n{code_block}\n```"
        body = body.replace("\x00CODEBLOCK\x00", "\n\n" + fence + "\n\n")
        body = re.sub(r"\n{3,}", "\n\n", body)

    return body.strip(), (None if code_block is None else lang)


def key_sentence(back_html: str) -> str:
    """The bold lead sentence, plain text - used as the seed for `description`."""
    body = strip_source_div(back_html)
    key = _match_key_span(body)
    inner = key[0] if key else body
    inner = CODE_INLINE_RE.sub(lambda m: f"`{html.unescape(m.group(1))}`", inner)
    inner = re.sub(r"<[^>]+>", "", inner)
    inner = html.unescape(inner)
    inner = fix_typography(inner)
    inner = re.sub(r"\s+", " ", inner).strip()
    return inner
