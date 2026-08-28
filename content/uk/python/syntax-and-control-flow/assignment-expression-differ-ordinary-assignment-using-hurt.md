---
id: py-syntax-0005
title: "Чим assignment expression `:=` відрізняється від звичайного присвоєння і коли його використання погіршує читабельність?"
description: ":= є виразом: присвоює значення і повертає його, тоді як = є інструкцією (statement) і не має значення."
track: python
section: syntax-and-control-flow
level: middle
type: comparison
tags: []
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/syntax.md#L229-L251
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**`:=` є виразом: присвоює значення і повертає його, тоді як `=` є інструкцією (statement) і не має значення.**[^py314-reference-expressions] `:=` корисний, коли обчислене значення потрібне і в умові, і в тілі блоку (наприклад, `while (chunk := f.read(8192)):`). <span class="warn">Надмірне використання у складних умовах або вкладених виразах погіршує читабельність</span>, бо змішує побічний ефект присвоєння з логікою виразу. Доданий у Python 3.8 (PEP 572).

## Detailed explanation

Різниця між `=` і `:=` – це різниця між інструкцією і виразом. Інструкція виконується і не має
значення; вираз обчислюється і значення має. Саме тому `=` не можна поставити всередину умови, а
`:=` можна.[^py314-reference-simple-stmts]

Практична користь від цього одна: значення потрібне двічі – у самій умові й у тілі блоку – і без
`:=` доводиться або дублювати виклик, або писати цикл з `while True` і `break` посередині.

```python
# without :=  - the read is duplicated, once before the loop and once inside it
chunk = f.read(8192)
while chunk:
    process(chunk)
    chunk = f.read(8192)

# with :=  - one call, in one place
while chunk := f.read(8192):
    process(chunk)
```

Той самий виграш у comprehension, де без `:=` дороге обчислення довелося б робити двічі: раз в умові
фільтра, раз у виразі результату.

```python
results = [y for x in data if (y := transform(x)) is not None]
```

Пріоритет у `:=` найнижчий серед операторів, тому дужки потрібні майже завжди, коли вираз не є цілим
операндом. `if (n := len(items)) > 10:` без дужок означало б `n := (len(items) > 10)` – зовсім інше
присвоєння.[^py314-reference-expressions]

**Коли `:=` шкодить читабельності:**
- у складеній умові з `and`/`or`, де читачеві доводиться відстежувати, які операнди взагалі
  обчислилися через short-circuit;
- коли присвоєне ім'я використовується далеко нижче по коду – змінна з'явилася «десь у дужках», і
  місце її народження важко знайти;
- у вкладених виразах, де кілька `:=` в одному рядку перетворюють вираз на послідовність побічних
  ефектів;
- там, де звичайний рядок з `=` перед `if` читається так само добре – тоді `:=` економить рядок і
  витрачає увагу.

Обмеження, яке інколи дивує: `:=` не можна використовувати як самостійну інструкцію верхнього рівня.
`x := 5` – синтаксична помилка, бо це вираз, а не присвоєння; для звичайного присвоєння є `=`. Так
само `:=` не працює з атрибутами й індексами: цілями можуть бути лише прості
імена.[^py314-reference-expressions]

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
