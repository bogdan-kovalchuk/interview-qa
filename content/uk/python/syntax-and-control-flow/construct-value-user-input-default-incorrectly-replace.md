---
id: py-syntax-0003
title: "Чому конструкція `value = user_input or default` може помилково замінити коректне значення `0` або порожній рядок?"
description: "or повертає перший truthy operand, тому будь-яке falsy значення (0, \"\", [], None) буде замінено на default."
track: python
section: syntax-and-control-flow
level: middle
type: pitfall
tags: [value-user-input-or-default]
status: published
updated: 2026-09-05
content_revision: 2
reconciled_with:
  en: 2
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

**`or` повертає перший truthy operand, тому будь-яке falsy значення (`0`, `""`, `[]`, `None`) буде замінено на `default`.**[^py314-reference-expressions] Якщо `0` або `""` є валідними вхідними даними, ця конструкція не розрізняє «відсутнє значення» та «коректне falsy значення». Для точної перевірки треба явно порівнювати з `None`: `value = default if user_input is None else user_input`.

## Detailed explanation

`or` не перевіряє «чи значення задане» – він перевіряє truthiness. Оператор обчислює лівий операнд,
питає в нього `__bool__` (або `__len__`) і повертає лівий операнд, якщо той truthy, інакше повертає
правий.[^py314-reference-expressions]

Проблема в тому, що в Python falsy не означає «порожньо» чи «не задано». Falsy – це `None`, `False`,
`0`, `0.0`, `''`, `[]`, `{}`, `set()` і будь-який об'єкт, чий `__len__` повернув нуль. Половина з
цього – цілком коректні дані користувача.

```python
def make_port(user_input, default=8080):
    return user_input or default

make_port(0)        # 8080 - but 0 was a deliberate value, not "unset"
make_port('')       # 8080 - an empty string can be a valid name
make_port(None)     # 8080 - this is the only case that was actually meant
```

Правильна перевірка порівнює саме з тим, що позначає відсутність. Якщо відсутність позначається
`None`, то й перевіряти треба `is None` – це порівняння identity з єдиним об'єктом-сентинелом, і воно
не залежить від truthiness.

```python
def make_port(user_input, default=8080):
    return default if user_input is None else user_input
```

Коли `None` сам є валідним значенням, потрібен власний сентинел – унікальний об'єкт, який ніхто
ззовні передати не може.

```python
MISSING = object()

def make_port(user_input=MISSING, default=8080):
    return default if user_input is MISSING else user_input
```

**Де ця помилка зустрічається найчастіше:**
- значення за замовчуванням для числових параметрів, де `0` – легітимний вхід (timeout, offset,
  retries);
- рядкові параметри, де порожній рядок означає «явно порожньо», а не «не вказано»;
- колекції: `items = items or []` тихо підмінює переданий порожній список на новий, і виклик, який
  розраховував мутувати оригінал, перестає працювати;
- читання конфігурації, де `False` – валідне значення прапорця, а `or True` перетворює його на
  `True`.

`or` лишається доречним там, де truthiness і є критерієм: `name = user_name or 'anonymous'`, коли
порожній рядок справді має трактуватися як відсутність
імені.[^py314-reference-simple-stmts]

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
