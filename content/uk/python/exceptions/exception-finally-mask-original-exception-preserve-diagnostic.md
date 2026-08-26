---
id: py-excpt-0006
title: "Як exception у `finally` може замаскувати original exception і як зберегти діагностичний контекст?"
description: "Якщо finally кидає новий exception, він стає зовнішнім, а оригінальний exception зберігається лише як __context__ – traceback показує переважно новий."
track: python
section: exceptions
level: senior
type: pitfall
tags: []
status: published
updated: 2026-09-04
content_revision: 1
reconciled_with:
  en: 1
anki:
  export: true
sources:
  - source_id: py314-tutorial-errors
    title: "Python 3.14: Tutorial/errors"
    url: https://docs.python.org/3.14/tutorial/errors.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-exceptions
    title: "Python 3.14: Library/exceptions"
    url: https://docs.python.org/3.14/library/exceptions.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-reference-compound-stmts-the-try-statement
    title: "Python 3.14: Reference/compound Stmts"
    url: https://docs.python.org/3.14/reference/compound_stmts.html#the-try-statement
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/exceptions.md#L141-L154
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**Якщо `finally` кидає новий exception, він стає зовнішнім, а оригінальний exception зберігається лише як `__context__` – traceback показує переважно новий.**[^py314-tutorial-errors] <span class="warn">Оригінальна причина може загубитися при логуванні, якщо не перевірити `__context__`.</span> Щоб зберегти контекст, у `finally` слід обгорнути cleanup у внутрішній `try/except`, залогувати помилку cleanup і дати оригінальному exception поширюватися, або використати `raise ... from` для явного chaining.

## Detailed explanation

TODO

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
