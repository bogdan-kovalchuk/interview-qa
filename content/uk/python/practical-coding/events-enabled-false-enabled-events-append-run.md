---
id: py-prac-0002
title: "Що надрукує `events = []; enabled = False; enabled and events.append(\"run\"); print(events)` і чому side effect не відбувся?"
description: "Надрукує [] – метод append не викликається."
track: python
section: practical-coding
level: middle
type: mechanism
tags: [events-enabled-false-enabled-and-events-append-run-print-events]
status: published
updated: 2026-10-13
content_revision: 2
reconciled_with:
  en: 2
anki:
  export: true
sources:
  - source_id: py314-tutorial
    title: "Python 3.14: Tutorial"
    url: https://docs.python.org/3.14/tutorial/
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-reference
    title: "Python 3.14: Reference"
    url: https://docs.python.org/3.14/reference/
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-reference-expressions
    title: "Python 3.14: Reference/expressions"
    url: https://docs.python.org/3.14/reference/expressions.html#boolean-operations
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14, розділ Boolean operations: and обчислює лівий операнд першим, а правий – лише тоді, коли лівий не визначив результат; повертається значення операнда, а не bool."
---

## Short answer

**Надрукує `[]` – метод `append` не викликається.** Оператор `and` обчислює лівий операнд першим; якщо він хибний, значенням виразу стає сам цей операнд, і правий операнд не обчислюється.[^py314-reference-expressions] Оскільки `enabled` дорівнює `False`, вираз `events.append("run")` не виконується, і список лишається порожнім.

## Detailed explanation

`and` – це не функція, яка отримує два вже обчислені значення, а вираз із визначеним порядком обчислення. Python спочатку обчислює лівий операнд, `enabled`. Якщо його значення хибне, вираз повертає його без обчислення правого операнда.[^py314-reference-expressions] Тому `events.append("run")` не викликається, а `print(events)` бачить порожній список.

Щоб побачити це без списку, замініть правий операнд на виклик функції з видимим побічним ефектом:

```python
def log(message):
    print("called:", message)
    return True


enabled = False
enabled and log("run")  # no output: the right operand is never evaluated
enabled = True
enabled and log("run")  # called: run
```

Значення `and` не зводиться до `bool`: повертається останній обчислений операнд. Тому `0 and "x"` дає `0`, а `"a" and "b"` дає `"b"`.[^py314-reference-expressions] Вираз `enabled and events.append("run")` дає `False`, але це значення ніхто не використовує. Для побічного ефекту чистіше писати `if enabled:` з окремим блоком: тоді умова читається як команда, а не як обчислення значення.

**Типові помилки:**
- вважати, що правий операнд `and` обчислюється завжди і `append` хоча б викликається;
- сприймати `and` як функцію, яка завжди повертає `True` або `False`;
- ставити побічні ефекти в `and` або `or` замість `if`.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
