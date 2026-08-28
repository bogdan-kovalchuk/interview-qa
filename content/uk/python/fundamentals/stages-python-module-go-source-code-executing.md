---
id: py-fund-0001
title: "Які основні етапи проходить модуль Python від source code до виконання інструкцій runtime, і на якому етапі може з’явитися bytecode?"
description: "У CPython source code спочатку компілюється в code object із bytecode, а потім цей code object виконується інтерпретатором."
track: python
section: fundamentals
level: middle
type: mechanism
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/general.md#L38-L67
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**У CPython source code спочатку компілюється в code object із bytecode, а потім цей code object виконується інтерпретатором.**[^py314-reference-executionmodel] До створення code object код проходить parsing та побудову AST, тому bytecode з’являється на етапі компіляції ще до виконання. Під час import придатний bytecode може додатково кешуватися у файлі `.pyc`.

## Detailed explanation

Шлях від тексту програми до виконання в CPython складається з двох великих фаз: компіляція і
виконання. Компіляція перетворює текст на code object; виконання – це робота віртуальної машини над
bytecode всередині цього code object.[^py314-reference-executionmodel]

Компіляція, своєю чергою, ділиться на кроки. Спочатку токенізація розбиває текст на лексеми, далі
parser будує з них abstract syntax tree, і лише потім компілятор обходить це дерево й видає bytecode
разом із таблицями констант та імен. Саме тому синтаксична помилка виявляється до того, як
виконається бодай один рядок.

```python
source text  ->  tokens  ->  AST  ->  code object (bytecode + constants + names)
                                            |
                                            v
                                   the VM executes it frame by frame
```

Результат компіляції – code object – доступний і зсередини мови: `compile()` дає його явно, а
`dis.dis()` показує bytecode у читабельному вигляді. Це зручно для розуміння, але формат сам по собі
є деталлю реалізації CPython.[^py314-faq-general]

Виконання починається з того, що інтерпретатор створює frame – контекст із локальним namespace,
посиланням на globals і позицією в bytecode – і виконує інструкції по черзі. Кожен виклик функції
створює новий frame; повернення знищує його.

**Де в цьому ланцюжку з'являється import і `.pyc`:**
- при import модуля CPython спершу шукає готовий code object у `__pycache__`;
- якщо кеш відсутній або застарів, модуль компілюється заново і кеш перезаписується;
- далі code object **виконується**: тіло модуля йде згори вниз, створюючи функції, класи та інші
  імена в namespace модуля;
- повторний import того самого модуля не повторює нічого з цього – модуль береться з
  `sys.modules`.[^py314-reference-datamodel]

Головне, що варто винести: bytecode з'являється на етапі компіляції, до виконання, а не «на льоту
під час роботи». А `.pyc` – це лише кеш першої фази, який не змінює ні другу фазу, ні семантику.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
