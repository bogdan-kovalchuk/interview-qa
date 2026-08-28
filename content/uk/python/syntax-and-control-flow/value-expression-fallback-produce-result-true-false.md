---
id: py-syntax-0002
title: "Яке значення матиме вираз `[] or \"fallback\"`, і чому його результат не є `True` або `False`?"
description: "Результат – 'fallback', тому що [] є falsy і or повертає другий operand."
track: python
section: syntax-and-control-flow
level: middle
type: mechanism
tags: [or-fallback]
status: published
updated: 2026-09-05
content_revision: 2
reconciled_with:
  en: 2
execution:
  language: python
  standard: null
  toolchain:
    name: cpython
    version: "3.14.7"
  flags: []
anki:
  export: true
sources:
  - source_id: py314-reference-expressions
    title: "Python 3.14: Reference/expressions"
    url: https://docs.python.org/3.14/reference/expressions.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-reference-simple-stmts
    title: "Python 3.14: Reference/simple Stmts"
    url: https://docs.python.org/3.14/reference/simple_stmts.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-reference-compound-stmts
    title: "Python 3.14: Reference/compound Stmts"
    url: https://docs.python.org/3.14/reference/compound_stmts.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/coding.md#L3-L20
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**Результат – `'fallback'`, тому що `[]` є falsy і `or` повертає другий operand.**[^py314-reference-expressions] Оператор `or` не зводить результат до `bool`, а повертає сам об'єкт, який визначив результат. Порожній список має `__bool__` -> `False`, тому `or` обчислює та повертає `"fallback"` як є.

```text
>>> [] or "fallback"
'fallback'
```

## Detailed explanation

`or` не є перетворювачем у `bool`. Він обчислює лівий операнд, питає в нього truthiness і повертає
**об'єкт**: лівий, якщо той truthy, інакше правий – як
є.[^py314-reference-expressions]

Тут лівий операнд – порожній список. Список визначає `__len__`, і нульова довжина робить його falsy,
тому `or` переходить до правого операнда й повертає рядок `'fallback'`, а не `True`.

```python
[] or 'fallback'      # 'fallback' - the str object itself
[1] or 'fallback'     # [1]        - the list, because it is truthy
[] or []              # []         - the second empty list; still falsy
bool([] or 'fallback')  # True     - only bool() actually converts
```

Правило truthiness просте: об'єкт falsy, якщо його `__bool__` повернув `False`, або, за відсутності
`__bool__`, якщо `__len__` повернув нуль. Усе інше truthy, включно з непорожніми контейнерами,
ненульовими числами і будь-яким об'єктом без обох
методів.[^py314-reference-simple-stmts]

**Що з цього випливає:**
- тип результату `or` – це об'єднання типів операндів, а не `bool`; анотація `-> bool` буде
  неправильною;
- ланцюжок `a or b or c` повертає перший truthy операнд, а якщо всі falsy – останній, тобто `c`;
- `x or default` не відрізняє «значення не задане» від «задане falsy значення»: `0` і `''` теж
  замінюються;
- якщо потрібен саме булевий результат, це треба сказати явно: `bool(x or y)`;
- у `if` різниці не видно, бо `if` сам зводить результат до truthiness – тому помилку помічають лише
  тоді, коли значення зберігають або повертають.

Те саме стосується `and`, лише дзеркально: `[] and 'x'` дає `[]`, бо перший операнд falsy й одразу
визначає результат.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
