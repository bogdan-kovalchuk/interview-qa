---
id: py-objtypes-0011
title: "Коли custom class має реалізувати `__copy__` або `__deepcopy__` замість довіри стандартній поведінці?"
description: "Власні __copy__/__deepcopy__ потрібні, коли стандартна поведінка порушує інваріанти класу: клас керує зовнішнім ресурсом або має shared state, який не слід копіювати (цикли deepcopy безпечно обробляє через memo)."
track: python
section: objects-and-types
level: middle
type: comparison
tags: [copy, deepcopy]
status: published
updated: 2026-09-04
content_revision: 1
reconciled_with:
  en: 1
anki:
  export: true
sources:
  - source_id: py314-reference-datamodel
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-stdtypes
    title: "Python 3.14: Library/stdtypes"
    url: https://docs.python.org/3.14/library/stdtypes.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-copy
    title: "Python 3.14: Library/copy"
    url: https://docs.python.org/3.14/library/copy.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-typing
    title: "Python 3.14: Library/typing"
    url: https://docs.python.org/3.14/library/typing.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/syntax.md#L442-L558
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**Власні `__copy__`/`__deepcopy__` потрібні, коли стандартна поведінка порушує інваріанти класу: клас керує зовнішнім ресурсом або має shared state, який не слід копіювати (цикли `deepcopy` безпечно обробляє через memo).**[^py314-reference-datamodel] За замовчуванням `copy.copy` створює новий об'єкт і копіює посилання на атрибути, а `copy.deepcopy` рекурсивно копіює все через `memo` dict. <span class="warn">Якщо клас містить, наприклад, кеш або logging handler, ці атрибути часто мають залишатися спільними між копіями – це контролюють саме через `__deepcopy__`.</span>

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
