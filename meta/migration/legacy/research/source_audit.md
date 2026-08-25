# Source audit for the interview question bank

Audit date: 2026-09-02.

## Recovered project intent

The original scaffold was created in Codex session
`01a060a3-a79a-7253-9211-8527ad76588c` under
`C:\Users\bogdan\.codex-bogdan\sessions\2026\09\02`.

That session established the following content policy:

- Python is the primary subject.
- Web, API, frameworks, frontend, cloud, detailed architecture, and system design are excluded.
- Algorithms/data structures, databases/SQL, and Git/CI/CD/SDLC are overview topics only.
- The tavor118 wiki supplies a broad topic and interview-popularity map, not factual authority.
- Python documentation and PEPs are the authority for technical claims.
- Community wording must not be copied when licensing is absent or unclear.

## Recovered source set

| Source | Intended role | Current assessment |
|---|---|---|
| [Python 3.14 Programming FAQ](https://docs.python.org/3.14/faq/programming.html) | Authoritative explanations and interview-shaped questions | Primary source for language behavior and common traps |
| [tavor118 website](https://tavor118.github.io/pj_python_interview_questions_and_answers/) | Broad taxonomy and popularity signals | Candidate map only; answers require independent verification |
| [tavor118 GitHub repository](https://github.com/tavor118/pj_python_interview_questions_and_answers) | Inspectable source behind the website | No license file detected; do not copy text |
| [Devinterview Python questions](https://github.com/Devinterview-io/python-interview-questions) | Additional general interview candidate pool | Secondary source; no license statement was detected on the repository page during this audit |
| [WTFPython](https://github.com/satwikkansal/wtfpython) | Non-obvious behavior and code-based traps | Useful for Middle/Senior prompts; WTFPL-licensed, but every behavior still needs current Python verification |
| [Interactive Coding Challenges](https://github.com/donnemartin/interactive-coding-challenges) | Algorithms/data-structures candidate pool | Apache-2.0; intentionally used only for the small overview topic and normalized to Python 3.14 |

## tavor118 snapshot

- Repository commit: `02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141`.
- Commit timestamp: 2026-07-02 20:59:09 +03:00.
- The site and repository expose eight major areas and 57 named subcategories.
- The repository contains 764 level-three question sections across 56 source pages when the
  generated `top_questions.md` page is excluded.
- Of those sections, 270 carry a popularity badge, 64 score at least 30/100, and 17 score at
  least 50/100.
- `top_questions.md` is generated from badged source sections and must not be counted as new
  material.

The raw count is not a card target. It includes out-of-scope areas, Junior-level definitions,
duplicates, composite questions, outdated premises, and uneven answers. The next stage maps
the in-scope concepts to atomic Middle/Senior learning objectives before assigning any count.

## Reliability and licensing rules

1. Do not reproduce tavor118 or Devinterview wording because no reusable content license was
   detected.
2. Use community sources only to identify candidate concepts and recognizable interview forms.
3. Rewrite every front independently in Ukrainian.
4. Verify version-sensitive premises against Python 3.14 documentation or an applicable PEP.
5. Mark CPython-only and free-threaded/GIL-enabled assumptions explicitly.
6. Exclude a candidate when it cannot be made atomic, current, and useful at Middle+ level.
7. Keep the three overview topics small even though the source wiki contains much more material.

## Source-of-truth hierarchy

1. Python 3.14 Language Reference and Standard Library documentation.
2. PEPs and CPython documentation for implementation-specific behavior.
3. Official documentation for Git, SQL/database standards or products, and CI concepts.
4. Community interview collections as discovery aids only.

