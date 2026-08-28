---
id: py-syntax-0007
title: "Коли виконується блок `else` циклу `for` або `while`, і як `break` змінює цю поведінку?"
description: "else виконується, коли цикл завершується природним шляхом (iterable вичерпано або умова стала хибною), але пропускається, якщо спрацював break."
track: python
section: syntax-and-control-flow
level: middle
type: mechanism
tags: [break]
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/loops.md#L3-L34
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**`else` виконується, коли цикл завершується природним шляхом (iterable вичерпано або умова стала хибною), але пропускається, якщо спрацював `break`.**[^py314-reference-expressions] Для `for`: `else` виконується після вичерпання iterator. Для `while`: `else` виконується, коли умова стає хибною. `continue` не перешкоджає виконанню `else`, якщо цикл згодом завершиться нормально.

## Detailed explanation

`else` при циклі означає не «інакше», а «якщо цикл дійшов до кінця сам». Він виконується рівно тоді,
коли цикл завершився природно: iterable вичерпався у `for`, або умова стала хибною у
`while`.[^py314-reference-compound-stmts]

Єдине, що його скасовує, – `break`. Ані `continue`, ані виняток, ані `return` тут ні до чого: перший
не заважає циклу дійти до кінця, а два останніх взагалі виводять керування з конструкції, тож до
`else` справа не доходить.

Найкорисніший випадок – пошук, де треба відрізнити «знайшли» від «перебрали все й не знайшли». Без
`else` для цього заводять прапорець.

```python
for item in items:
    if item.matches(query):
        found = item
        break
else:
    raise LookupError('nothing matched')   # runs only if the loop was not broken
```

Той самий код з прапорцем довший і має зайву змінну, стан якої треба тримати в голові:

```python
found = None
for item in items:
    if item.matches(query):
        found = item
        break
if found is None:
    raise LookupError('nothing matched')
```

Назва справді невдала – це визнавав і сам автор мови. Читати її варто як `for ... else` = «нічого не
перервало цикл», а не як пару до `if`.

**Що варто пам'ятати про поведінку:**
- порожній iterable – це теж природне завершення, тож `else` виконається, хоч тіло циклу не
  виконалося жодного разу;
- `while` з умовою, хибною одразу, поводиться так само: тіло не виконалось, `else` виконався;
- `continue` не впливає ні на що: цикл усе одно може завершитися природно і виконати `else`;
- виняток усередині циклу пропускає `else`, бо керування залишає конструкцію не через нормальне
  завершення.[^py314-reference-simple-stmts]

Через невідому більшості семантику `for ... else` варто або супроводжувати коротким коментарем, або
використовувати там, де альтернатива з прапорцем справді помітно
гірша.[^py314-reference-expressions]

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
