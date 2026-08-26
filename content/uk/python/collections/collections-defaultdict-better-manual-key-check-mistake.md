---
id: py-coll-0009
title: "Коли `collections.defaultdict` кращий за ручну перевірку key і яку помилку може приховати неправильна default factory?"
description: "defaultdict кращий, коли потрібно групувати або акумулювати значення за ключами: він автоматично створює default-значення через default_factory при зверненні через __getitem__."
track: python
section: collections
level: middle
type: comparison
tags: [collections-defaultdict]
status: published
updated: 2026-09-04
content_revision: 1
reconciled_with:
  en: 1
anki:
  export: true
sources:
  - source_id: py314-library-stdtypes
    title: "Python 3.14: Library/stdtypes"
    url: https://docs.python.org/3.14/library/stdtypes.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-collections
    title: "Python 3.14: Library/collections"
    url: https://docs.python.org/3.14/library/collections.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-howto-sorting
    title: "Python 3.14: Howto/sorting"
    url: https://docs.python.org/3.14/howto/sorting.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/set_and_dict.md#L173-L190
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**`defaultdict` кращий, коли потрібно групувати або акумулювати значення за ключами: він автоматично створює default-значення через `default_factory` при зверненні через `__getitem__`.**[^py314-library-stdtypes] <span class="warn">Будь-яке звернення `d[key]` для відсутнього ключа тихо створює запис, тому випадковий lookup збільшує словник помилковими записами. Метод `d.get(key)` не викликає `default_factory` і не створює ключ.</span>

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
