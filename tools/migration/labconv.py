"""Embedded Interview Lab HTML -> the Markdown the content contract expects.

The Lab deck uses the same HTML dialect as the migrated predecessor deck
(`<span class="key">`, `<span class="warn">`, `<code>`, `<pre class="code-block">`,
`<br>`), so the shared primitives live in `htmlconv` and only the three
differences are handled here:

* the Lab uses `<br><br>` as a paragraph break and a single `<br>` as a soft
  wrap - `htmlconv` flattens both to a space, which would glue three
  paragraphs into one run-on `Short answer`;
* code blocks carry syntax-highlight spans (`code-kw`, `code-type`, ...) that
  must be stripped before the block becomes a fence;
* 29% of the records put the code *in the question*. Per the owner's decision
  the title stays a plain phrase and the snippet moves into the body, so the
  Front has to be split rather than flattened.
"""
from __future__ import annotations

import html
import re

from . import htmlconv

PRE_BLOCK_RE = re.compile(r'<pre class="code-block"><code>(.*?)</code></pre>', re.DOTALL)
HL_SPAN_RE = re.compile(r'</?span(?: class="code-[a-z]+")?>')
PARAGRAPH_BR_RE = re.compile(r"(?:<br\s*/?>\s*){2,}", re.IGNORECASE)
SOFT_BR_RE = re.compile(r"<br\s*/?>", re.IGNORECASE)

_CPP_MARKERS = re.compile(
    r"\b(?:class|template|namespace|std::|nullptr|constexpr|public:|private:|new |delete )"
)
_C_MARKERS = re.compile(r"[;{}]|#include|#define|\b(?:int|void|char|struct|union|return)\b")


def _fence_language(code: str) -> str:
    if _CPP_MARKERS.search(code):
        return "cpp"
    return "c" if _C_MARKERS.search(code) else "text"


def unescape_code(raw: str) -> str:
    """A `<pre class="code-block">` body -> real source text.

    Highlight spans go first: `htmlconv.unescape_code` decodes entities, and a
    `&lt;` decoded before the tags are stripped would turn into a `<` that the
    stripper then eats along with the rest of the line.
    """
    return htmlconv.unescape_code(HL_SPAN_RE.sub("", raw))


def _extract_code(fragment: str) -> tuple[str, str | None]:
    """(fragment without its code block, the code) - first block only.

    A record with two blocks would break the one-code-block limit on
    `Short answer`; none of the 646 source records has two, and a second one
    is left in place on purpose so the gate reports it instead of the
    converter silently dropping it.
    """
    match = PRE_BLOCK_RE.search(fragment)
    if match is None:
        return fragment, None
    code = unescape_code(match.group(1))
    return fragment[: match.start()] + "\x00CODE\x00" + fragment[match.end() :], code


def _inline_to_markdown(fragment: str) -> str:
    """Inline HTML -> Markdown, paragraph structure preserved.

    Entities stay escaped until every tag has been removed. Decoding them
    earlier - which is what the inherited `htmlconv` does - turns `&lt;` into a
    real `<`, and the tag stripper that runs next eats everything up to the
    following `>`: `return (x &gt; y) - (x &lt; y);` silently became
    `return (x > y) - (x `. The legacy deck happened never to hit it; this one
    does, in comparators and template code.

    The `.warn` wrapper the contract allows in `Short answer` travels as a
    sentinel for the same reason: written back as a real tag, the very next
    line strips it along with the source's other markup, and 136 imported
    answers lost the highlight that marks the dangerous half of the sentence.
    """
    text = PARAGRAPH_BR_RE.sub("\x00PARA\x00", fragment)
    text = SOFT_BR_RE.sub(" ", text)

    def _warn(match: re.Match[str]) -> str:
        inner = htmlconv.CODE_INLINE_RE.sub(lambda c: f"`{c.group(1)}`", match.group(1))
        inner = re.sub(r"<[^>]+>", "", inner)
        return f"\x00WARNOPEN\x00{inner}\x00WARNCLOSE\x00"

    text = htmlconv.WARN_SPAN_RE.sub(_warn, text)
    text = htmlconv.CODE_INLINE_RE.sub(lambda m: f"`{m.group(1)}`", text)
    text = re.sub(r"<[^>]+>", "", text)
    text = html.unescape(text)
    text = htmlconv.fix_typography(text)
    text = re.sub(r"[ \t]+", " ", text)
    text = text.replace("\x00PARA\x00", "\n\n").strip()
    return text.replace("\x00WARNOPEN\x00", '<span class="warn">').replace(
        "\x00WARNCLOSE\x00", "</span>"
    )


def split_front(front_html: str) -> tuple[str, str | None, str | None]:
    """A Front field -> (question title, code block or None, fence language).

    The title is plain text with backtick inline code: `mirror.title_markup`
    renders exactly that and HTML-escapes everything else, which is why the
    earlier import's raw `<pre>` titles print as literal tags on the site.
    """
    stripped, code = _extract_code(front_html)
    title = _inline_to_markdown(stripped).replace("\x00CODE\x00", "").strip()
    title = re.sub(r"\s{2,}", " ", title.replace("\n", " ")).strip()
    return title, code, (None if code is None else _fence_language(code))


def back_to_short_answer(back_html: str) -> tuple[str, str | None]:
    """A Back field -> (`Short answer` Markdown, fence language or None).

    A leading `<span class="key">` becomes the `**bold**` lead the exporter
    renders as `.key`; a `.warn` nested inside it is unwrapped, because the
    contract forbids that nesting outright and the gate rejects it.
    """
    body, code = _extract_code(back_html)

    key = htmlconv._match_key_span(body)
    if key:
        inner, end = key
        inner = _inline_to_markdown(re.sub(r'</?span(?: class="warn")?>', "", inner))
        body = "**" + inner.replace("\n", " ").strip() + "**" + body[end:]
        text = _inline_to_markdown(body)
    else:
        text = _inline_to_markdown(body)

    if code is not None:
        lang = _fence_language(code)
        text = text.replace("\x00CODE\x00", f"\n\n```{lang}\n{code}\n```\n\n")
    else:
        lang = None
    return re.sub(r"\n{3,}", "\n\n", text).strip(), lang
