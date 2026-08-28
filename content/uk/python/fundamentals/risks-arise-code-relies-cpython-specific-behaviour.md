---
id: py-fund-0007
title: "Які ризики виникають, якщо код покладається на CPython-specific поведінку під час перенесення на PyPy або іншу реалізацію Python?"
description: "Такий код може втратити коректність, переносимість або очікувані performance characteristics."
track: python
section: fundamentals
level: senior
type: practical
tags: []
status: published
updated: 2026-09-05
content_revision: 2
reconciled_with:
  en: 2
applies_to:
  - product: "CPython"
    version: null
anki:
  export: true
sources:
  - source_id: py314-reference-executionmodel
    title: "Python 3.14: Reference/executionmodel"
    url: https://docs.python.org/3.14/reference/executionmodel.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-reference-datamodel
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-faq-general
    title: "Python 3.14: Faq/general"
    url: https://docs.python.org/3.14/faq/general.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/interpreter.md#L27-L46
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**Такий код може втратити коректність, переносимість або очікувані performance characteristics.**[^py314-reference-executionmodel] Інша реалізація може мати інший garbage collector, момент finalization, bytecode, JIT та object layout. Слід покладатися на задокументовану семантику мови, керувати ресурсами через context managers і тестувати на цільових реалізаціях.

## Detailed explanation

Мова Python і її реалізація – різні речі. Language Reference описує семантику, якої мусить
дотримуватися будь-яка реалізація; усе інше – як саме CPython цього досягає – може відрізнятися в
PyPy, GraalPy чи MicroPython.[^py314-reference-executionmodel]

Найпоширеніша неявна залежність – момент знищення об'єкта. У CPython працює reference counting, тож
об'єкт зникає одразу після втрати останнього посилання, і файл, відкритий без `with`, закривається
«сам». У PyPy збирач інший, момент finalization не визначений, і той самий код тримає file
descriptor до наступного збирання.

```python
data = open('report.csv').read()   # CPython: the file closes right away
                                   # PyPy: the descriptor stays open, unpredictably long

with open('report.csv') as f:      # both: closed at the end of the block, by contract
    data = f.read()
```

Друга залежність – ідентичність малих об'єктів. CPython кешує невеликі цілі та деякі рядки, тому
`a is b` для однакових малих значень часто істинне. Це кеш реалізації, а не правило мови: порівняння
значень робиться через `==`, а `is` перевіряє identity.[^py314-reference-datamodel]

Третя – bytecode і `dis`. Формат code object, набір опкодів і результат `dis` описані як деталь
CPython і змінюються між версіями, тож будь-який код, що парсить дизасембльований вивід, ламається на
наступному релізі.[^py314-faq-general]

**Категорії ризику, які варто називати окремо:**
- **коректність**: покладання на негайне finalization або на порядок знищення дає витік ресурсів на
  іншій реалізації;
- **переносимість**: C-extension, зібраний під CPython ABI, просто не запуститься там, де ABI інший;
- **performance**: припущення «конкатенація рядків у циклі дешева» спирається на оптимізацію
  CPython, якої в іншій реалізації може не бути – і навпаки, JIT робить швидким те, що в CPython
  повільне;
- **сумісність у часі**: деталь реалізації може змінитися між 3.13 і 3.14 без жодного попередження,
  бо на неї не давали гарантій.

Практичне правило просте: якщо поведінку не знайдено в Language Reference або вона позначена як
implementation detail, її не можна робити частиною контракту свого коду. Ресурси закриваються через
context managers, рівність перевіряється через `==`, а припущення про швидкість перевіряються
вимірюванням на тій реалізації, де код справді працюватиме.

## Environment

TODO

## Deliverable

TODO

## Acceptance criteria

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
