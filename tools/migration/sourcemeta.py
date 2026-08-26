"""Turn a legacy source URL into a `sources[]` entry.

front-sources.csv gives us URLs only (official_refs, community_answer_ref).
QUESTIONS.md requires seven keys per source, most of which the CSV does not
carry (source_id, title, applicability). This module derives them
deterministically from the URL so the same page always gets the same
source_id/title across every question that cites it.
"""
from __future__ import annotations

import re
from urllib.parse import urlparse

KEBAB_RE = re.compile(r"[^a-z0-9]+")


def kebab(text: str) -> str:
    text = text.lower()
    text = text.replace("__", " ")
    text = KEBAB_RE.sub("-", text).strip("-")
    text = re.sub(r"-{2,}", "-", text)
    return text or "src"


def _titlecase_slug(slug: str) -> str:
    words = slug.replace("-", " ").replace("_", " ").split()
    small = {"a", "an", "the", "of", "and", "or", "in", "on", "to", "vs", "with"}
    acronyms = {
        "api", "url", "sql", "json", "io", "ci", "cd", "orm", "acid", "http",
        "https", "tcp", "udp", "jwt", "gil", "ast", "ddl", "dml", "ipc",
        "redos", "ttl", "rest", "grpc", "cap",
    }
    out = []
    for i, w in enumerate(words):
        lw = w.lower()
        if lw in acronyms:
            out.append(lw.upper())
        elif i > 0 and lw in small:
            out.append(lw)
        else:
            out.append(lw.capitalize())
    return " ".join(out)


def _python_docs(parsed) -> tuple[str, str, str | None]:
    """(source_id, title, uk_applicability, version) for a docs.python.org URL."""
    parts = [p for p in parsed.path.split("/") if p]
    version = None
    if parts and re.fullmatch(r"\d+\.\d+", parts[0]):
        version = parts[0]
        parts = parts[1:]
    parts = [re.sub(r"\.html$", "", p) for p in parts]
    last = parts[-1] if parts else "index"
    section = parts[0] if len(parts) > 1 else None
    anchor = parsed.fragment or None
    id_parts = ["py" + version.replace(".", "") if version else "py"] + parts
    if anchor:
        id_parts.append(anchor)
    source_id = kebab("-".join(id_parts))[:60].rstrip("-")
    label = last if last != "index" else (section or "index")
    title_slug = f"{section}/{last}" if section and section != last else last
    title = f"Python {version}: {_titlecase_slug(title_slug)}" if version else f"Python: {_titlecase_slug(title_slug)}"
    return source_id, title, version


def build_source_meta(url: str) -> dict:
    """Return {source_id, title, version, kind_hint, uk_applicability, en_applicability}."""
    parsed = urlparse(url)
    host = parsed.netloc

    if host == "docs.python.org":
        source_id, title, version = _python_docs(parsed)
        return {
            "source_id": source_id,
            "title": title,
            "version": version,
            "uk_applicability": f"Офіційна документація Python {version}." if version else "Офіційна документація Python.",
            "en_applicability": f"Official Python {version} documentation." if version else "Official Python documentation.",
        }

    if host == "peps.python.org":
        m = re.search(r"pep-(\d+)", parsed.path)
        number = m.group(1).lstrip("0") or "0" if m else "0"
        return {
            "source_id": f"pep-{number}",
            "title": f"PEP {number}",
            "version": None,
            "uk_applicability": f"Специфікація PEP {number}.",
            "en_applicability": f"PEP {number} specification.",
        }

    if host == "packaging.python.org":
        return {
            "source_id": "py-packaging-guide",
            "title": "Python Packaging User Guide",
            "version": None,
            "uk_applicability": "Офіційний посібник із packaging для Python.",
            "en_applicability": "Official Python Packaging User Guide.",
        }

    if host == "docs.pytest.org":
        return {
            "source_id": "pytest-docs",
            "title": "pytest documentation",
            "version": None,
            "uk_applicability": "Офіційна документація pytest.",
            "en_applicability": "Official pytest documentation.",
        }

    if host == "hypothesis.readthedocs.io":
        return {
            "source_id": "hypothesis-docs",
            "title": "Hypothesis documentation",
            "version": None,
            "uk_applicability": "Офіційна документація Hypothesis (property-based testing).",
            "en_applicability": "Official Hypothesis (property-based testing) documentation.",
        }

    if host == "mutmut.readthedocs.io":
        return {
            "source_id": "mutmut-docs",
            "title": "mutmut documentation",
            "version": None,
            "uk_applicability": "Офіційна документація mutmut (mutation testing).",
            "en_applicability": "Official mutmut (mutation testing) documentation.",
        }

    if host == "owasp.org":
        last = [p for p in parsed.path.split("/") if p][-1] if parsed.path.strip("/") else "owasp"
        return {
            "source_id": kebab("owasp-" + last)[:60],
            "title": f"OWASP: {_titlecase_slug(last)}",
            "version": None,
            "uk_applicability": "Матеріал спільноти OWASP з безпеки застосунків.",
            "en_applicability": "OWASP application-security community material.",
        }

    if host == "docs.github.com":
        parts = [p for p in parsed.path.split("/") if p and p != "en"]
        last = parts[-1] if parts else "github"
        return {
            "source_id": kebab("github-" + last)[:60],
            "title": f"GitHub Docs: {_titlecase_slug(last)}",
            "version": None,
            "uk_applicability": "Офіційна документація GitHub.",
            "en_applicability": "Official GitHub documentation.",
        }

    if host == "docs.cloud.google.com":
        parts = [p for p in parsed.path.split("/") if p]
        last = parts[-1] if parts else "gcloud"
        return {
            "source_id": kebab("gcloud-" + last)[:60],
            "title": f"Google Cloud docs: {_titlecase_slug(last)}",
            "version": None,
            "uk_applicability": "Офіційна документація Google Cloud.",
            "en_applicability": "Official Google Cloud documentation.",
        }

    if host == "google.github.io":
        parts = [p for p in parsed.path.split("/") if p]
        last = re.sub(r"\.html$", "", parts[-1]) if parts else "google-eng-practices"
        return {
            "source_id": kebab("google-" + last)[:60],
            "title": f"Google Engineering Practices: {_titlecase_slug(last)}",
            "version": None,
            "uk_applicability": "Офіційний матеріал Google Engineering Practices.",
            "en_applicability": "Official Google Engineering Practices material.",
        }

    if host == "www.postgresql.org":
        parts = [p for p in parsed.path.split("/") if p]
        version = parts[1] if len(parts) > 1 else None
        last = re.sub(r"\.html$", "", parts[-1]) if parts else "postgresql"
        return {
            "source_id": kebab("postgres-" + last)[:60],
            "title": f"PostgreSQL docs: {_titlecase_slug(last)}",
            "version": version if version and version != "current" else None,
            "uk_applicability": "Офіційна документація PostgreSQL.",
            "en_applicability": "Official PostgreSQL documentation.",
        }

    if host == "git-scm.com":
        parts = [p for p in parsed.path.split("/") if p]
        last = parts[-1] if parts else "git"
        return {
            "source_id": kebab("git-" + last)[:60],
            "title": f"Git docs: {_titlecase_slug(last)}",
            "version": None,
            "uk_applicability": "Офіційна документація Git.",
            "en_applicability": "Official Git documentation.",
        }

    if "tavor118" in host or "tavor118" in parsed.path:
        return {
            "source_id": "predecessor-answer",
            "title": "tavor118/pj_python_interview_questions_and_answers (community)",
            "version": None,
            "uk_applicability": (
                "Джерело виявлення теми з попередньої (community) бази питань; "
                "текст відповіді написаний окремо і не копіює це джерело."
            ),
            "en_applicability": (
                "Community source used to discover the topic; the answer text is "
                "independently written and does not copy this source."
            ),
        }

    # Fallback: generic, still deterministic.
    parts = [p for p in parsed.path.split("/") if p]
    last = parts[-1] if parts else host
    return {
        "source_id": kebab(f"{host}-{last}")[:60] or kebab(host),
        "title": f"{host}: {_titlecase_slug(last)}" if last else host,
        "version": None,
        "uk_applicability": f"Матеріал з {host}.",
        "en_applicability": f"Material from {host}.",
    }
