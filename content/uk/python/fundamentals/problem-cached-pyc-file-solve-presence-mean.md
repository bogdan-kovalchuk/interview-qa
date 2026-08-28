---
id: py-fund-0003
title: "Яку проблему вирішує кешований файл `.pyc` і чому його наявність не означає компіляцію Python-коду в native machine code?"
description: ".pyc дозволяє повторно використати скомпільований bytecode незміненого імпортованого модуля й не витрачати час на повторну компіляцію source code."
track: python
section: fundamentals
level: middle
type: mechanism
tags: [pyc]
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/interpreter.md#L382-L406
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**`.pyc` дозволяє повторно використати скомпільований bytecode незміненого імпортованого модуля й не витрачати час на повторну компіляцію source code.**[^py314-reference-executionmodel] Він містить bytecode для Python VM, а не інструкції процесора. Формат bytecode є деталлю реалізації CPython і може змінюватися між версіями.

## Detailed explanation

`.pyc` – це кеш результату компіляції, а не «скомпільована програма». Він містить marshalled code
object з bytecode для віртуальної машини Python, а не машинні інструкції
процесора.[^py314-reference-executionmodel]

Задача, яку він розв'язує, вузька: прибрати повторний parsing і компіляцію при кожному import.
Компіляція займає помітний час на великій кодовій базі, а результат для незміненого файлу завжди той
самий, тож його є сенс зберегти. Файли лежать у `__pycache__` поруч із модулем, з іменем, що містить
тег реалізації та версію.

Актуальність кешу перевіряється при кожному import. За замовчуванням у заголовку `.pyc` записані час
модифікації й розмір вихідного файлу; якщо вони не збігаються з тим, що на диску, кеш ігнорується і
модуль перекомпільовується.

```python
# my_module.py compiled once, then reused on every later import:
__pycache__/my_module.cpython-314.pyc

# the tag says which implementation and which version wrote it -
# a 3.13 interpreter will not read a 3.14 file, it will recompile
```

Три речі, які наявність `.pyc` **не** означає. Він не пришвидшує сам виконуваний код – bytecode
однаковий, економиться лише компіляція. Він не є способом приховати source: bytecode
дизасемблюється. І він не робить код переносимим між версіями Python, бо формат bytecode – це
внутрішня деталь CPython, яка змінюється між випусками.[^py314-faq-general]

**Що корисно знати про поведінку кешу:**
- кеш пишеться лише для **імпортованих** модулів; скрипт, запущений як `python script.py`, не
  кешується, бо компілюється рівно один раз за процес;
- якщо тека недоступна для запису, import усе одно спрацює – просто без кешу, повільніше;
- перевірка за mtime ненадійна при розгортанні, де файли отримують однаковий timestamp; для цього
  існує hash-based режим, який звіряє хеш вихідного файлу;
- видалення `__pycache__` безпечне: наступний import перестворить кеш.

Практичний висновок для інтерв'ю: `.pyc` – це деталь реалізації CPython, яка економить час import.
Будувати на його форматі, розташуванні чи самому факті наявності будь-яку логіку застосунку не
варто.[^py314-reference-datamodel]

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
