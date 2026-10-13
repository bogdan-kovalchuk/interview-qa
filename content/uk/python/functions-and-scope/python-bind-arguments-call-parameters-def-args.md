---
id: py-funcs-0004
title: "Як Python зв’яже аргументи у виклику `f(1, 2, 3, b=4, x=5)` із параметрами `def f(a, *args, b=0, **kwargs): ...`?"
description: "a = 1, args = (2, 3), b = 4, kwargs = {'x': 5}."
track: python
section: functions-and-scope
level: middle
type: mechanism
tags: [f-1-2-3-b-4-x-5, def-f-a-args-b-0-kwargs]
status: published
updated: 2026-10-13
content_revision: 2
reconciled_with:
  en: 2
anki:
  export: true
sources:
  - source_id: py314-reference-expressions-calls
    title: "Python 3.14: Reference/expressions"
    url: https://docs.python.org/3.14/reference/expressions.html#calls
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-reference-compound-stmts-function-definitions
    title: "Python 3.14: Reference/compound Stmts"
    url: https://docs.python.org/3.14/reference/compound_stmts.html#function-definitions
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
---

## Short answer

**`a = 1`, `args = (2, 3)`, `b = 4`, `kwargs = {'x': 5}`.**[^py314-reference-expressions-calls] Перший позиційний аргумент заповнює параметр `a`. Наступні позиційні `2, 3` не мають відповідних параметрів до `*`, тому збираються в `*args`. Keyword `b=4` збігається з keyword-only параметром `b`. Keyword `x=5` не збігається з жодним іменованим параметром і потрапляє до `**kwargs`.

## Detailed explanation

Python зіставляє аргументи з параметрами у два кроки. Спочатку позиційні аргументи заповнюють позиційні параметри по порядку: `a` отримує `1`. Зайві позиційні аргументи, яким не вистачило слота, збираються в tuple для `*args`. Потім кожен keyword аргумент шукає параметр з таким самим іменем: `b=4` заповнює keyword-only `b`, а `x=5` такого параметра не має і потрапляє до `**kwargs`.[^py314-reference-expressions-calls] Параметр після `*`, як `b`, можна заповнити лише за іменем.[^py314-reference-compound-stmts-function-definitions]

Приклад з трьома викликами; коментарі містять результат:

```python
def f(a, *args, b=0, **kwargs):
    return a, args, b, kwargs

print(f(1, 2, 3, b=4, x=5))   # (1, (2, 3), 4, {'x': 5})
print(f(1, 2, 3, 4))          # (1, (2, 3, 4), 0, {}): b is keyword-only, so 4 goes to *args
print(f(a=1, x=5))            # (1, (), 0, {'x': 5}): a can also be passed by keyword
```

Два наслідки варто запам’ятати. По-перше, `b` є keyword-only, тож позиційний `4` у другому виклику йде до `*args`, а не до `b`. По-друге, keyword, чиє ім’я збігається з іменованим параметром, не потрапляє до `**kwargs`: у третьому виклику `a=1` заповнює `a`.[^py314-reference-expressions-calls] Якщо ж `a` уже заповнено позиційно, як у `f(1, a=2)`, виникає `TypeError`, див. `qid:py-funcs-0002`.

**Типові помилки:**
- очікувати, що позиційний `4` у `f(1, 2, 3, 4)` стане значенням `b`: `b` доступний лише за іменем;
- вважати, що keyword з іменем параметра потрапить до `**kwargs`;
- вважати, що порожній `*args` дорівнює `None`: він завжди tuple, тобто `()`, а порожній `**kwargs` – це `{}`.[^py314-reference-expressions-calls]

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
