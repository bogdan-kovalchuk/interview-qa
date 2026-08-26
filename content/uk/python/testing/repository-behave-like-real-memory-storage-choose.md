---
id: py-testing-0010
title: "Для repository, який має поводитися як real in-memory storage, коли обрати Fake, а коли Stub чи interaction-verifying Mock?"
description: "Fake – спрощена, але робоча реалізація контракту (in-memory dict замість БД); Stub – пасивний об'єкт із фіксованими відповідями; Mock – записує виклики для interaction verification."
track: python
section: testing
level: middle
type: comparison
tags: []
status: published
updated: 2026-09-04
content_revision: 1
reconciled_with:
  en: 1
anki:
  export: true
sources:
  - source_id: py314-library-unittest
    title: "Python 3.14: Library/unittest"
    url: https://docs.python.org/3.14/library/unittest.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-unittest-mock
    title: "Python 3.14: Library/unittest.mock"
    url: https://docs.python.org/3.14/library/unittest.mock.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: pytest-docs
    title: "pytest documentation"
    url: https://docs.pytest.org/en/stable/
    accessed: 2026-09-04
    kind: official
    version: null
    applicability: "Офіційна документація pytest."
  - source_id: hypothesis-docs
    title: "Hypothesis documentation"
    url: https://hypothesis.readthedocs.io/en/latest/
    accessed: 2026-09-04
    kind: official
    version: null
    applicability: "Офіційна документація Hypothesis (property-based testing)."
  - source_id: mutmut-docs
    title: "mutmut documentation"
    url: https://mutmut.readthedocs.io/en/latest/
    accessed: 2026-09-04
    kind: official
    version: null
    applicability: "Офіційна документація mutmut (mutation testing)."
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/computer_science/testing.md#L212-L346
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**Fake – спрощена, але робоча реалізація контракту (in-memory dict замість БД); Stub – пасивний об'єкт із фіксованими відповідями; Mock – записує виклики для interaction verification.**[^py314-library-unittest] Для repository, що має поводитися як real storage, потрібен Fake, бо він реалізує повний контракт: `save`/`get`/`delete`/`find` з реальною логікою зберігання. Stub підходить, коли потрібна лише одна фіксована відповідь (`Mock(return_value=[user])`), але не підтримує довільні query. Interaction-verifying Mock (`mock.assert_called_with(...)`) доречний, коли важливий протокол викликів, а не стан сховища. <span class="warn">Fake має проходити ті самі interface-тести, що й реальна імплементація, інакше розбіжність поведінки залишиться непоміченою.</span>

## Detailed explanation

TODO

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
