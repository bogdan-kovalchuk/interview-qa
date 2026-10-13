---
id: py-modimp-0006
title: "Коли absolute import доречніший за explicit relative import усередині package?"
description: "Absolute import (from package.module import name) – форма, яку рекомендує PEP 8: вона читабельніша, не змінюється, коли файл переміщують на інший рівень пакета, і дає зрозуміліші помилки."
track: python
section: modules-and-imports
level: middle
type: comparison
tags: []
status: published
updated: 2026-10-13
content_revision: 2
reconciled_with:
  en: 2
anki:
  export: true
sources:
  - source_id: py314-reference-import
    title: "Python 3.14: Reference/import"
    url: https://docs.python.org/3.14/reference/import.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-importlib
    title: "Python 3.14: Library/importlib"
    url: https://docs.python.org/3.14/library/importlib.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py-packaging-guide
    title: "Python Packaging User Guide"
    url: https://packaging.python.org/en/latest/tutorials/packaging-projects/
    accessed: 2026-09-04
    kind: official
    version: null
    applicability: "Офіційний посібник із packaging для Python."
  - source_id: pep-8-imports
    title: "PEP 8: Style Guide for Python Code (Imports)"
    url: https://peps.python.org/pep-0008/#imports
    accessed: 2026-10-13
    kind: official
    version: null
    applicability: "Рекомендація щодо абсолютних import і прийнятності відносних import у складних макетах пакетів; це стиль, а не специфікація import system."
  - source_id: py314-reference-import-package-relative-imports
    title: "Python 3.14: Reference/import (Package Relative Imports)"
    url: https://docs.python.org/3.14/reference/import.html#package-relative-imports
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Синтаксис відносних import у Python 3.14: крапки відраховуються від поточного пакета."
---

## Short answer

**Absolute import (`from package.module import name`) – форма, яку PEP 8 рекомендує, бо вона читабельніша і дає кращі повідомлення про помилки, якщо import system налаштовано неправильно.**[^pep-8-imports] Відносний import (`from .module import name`) PEP 8 визнає прийнятним для складних макетів пакетів, де абсолютні імена були б надто довгими.[^pep-8-imports] Absolute import працює, коли тека, що містить верхній пакет, є в `sys.path`, наприклад після `python -m` з кореня проєкту; при переміщенні файлу на інший рівень пакета крапки відносного import треба перерахувати.

## Detailed explanation

Абсолютний import записує повний шлях від верхнього пакета: `from pkg.models import User`. Відносний import називає той самий модуль через крапки від поточного пакета: одна крапка означає поточний пакет, кожна наступна – ще один рівень вгору.[^py314-reference-import-package-relative-imports] Обидві форми знаходять один і той самий модуль, тож вибір стосується читабельності, стійкості до переміщень і поведінки при помилковій конфігурації, а не того, чи код узагалі працюватиме.

PEP 8 називає абсолютні import рекомендованими, бо вони читабельніші й дають кращі повідомлення про помилки, якщо import system налаштовано неправильно.[^pep-8-imports] Той самий стандарт визнає відносний import прийнятною альтернативою для складних макетів пакетів, де абсолютні імена були б зайво довгими.[^pep-8-imports]

Найпомітніша різниця проявляється під час запуску. Абсолютний import шукає `pkg` у `sys.path`. Після `python -m pkg.service` з кореня проєкту корінь є в `sys.path`, і рядок працює. При `python pkg/service.py` першим у `sys.path` стає сама тека `pkg/`, тому той самий рядок падає з `ModuleNotFoundError: No module named 'pkg'`. Відносний import у такому запуску падає з `ImportError`, бо файл не знає свого пакета.

Ілюстративний файл (запуск перевірено на 3.12, 3.13 і 3.14):

```python
# pkg/service.py, run from the project root as: python -m pkg.service
from pkg.models import User   # absolute: the full path from the top-level package
# from .models import User    # explicit relative: same module, but the dots change if the file moves
```

Переміщення файлу – головний аргумент на користь абсолютного import. Якщо `service.py` переїде в `pkg/api/`, рядок `from pkg.models import User` лишиться правильним, а відносний варіант треба переписати як `from ..models import User`. Відносний import коротший і зазвичай зручніший у великих внутрішніх пакетах, де файли переміщуються разом, тому PEP 8 його не забороняє.

**Типові помилки:**
- вважати, що absolute import працює незалежно від способу запуску: йому потрібна тека, що містить верхній пакет, у `sys.path`;
- змішувати обидві форми в одному пакеті без причини, тож при переміщенні файлу доводиться перевіряти обидва типи рядків;
- переписувати всі відносні import на абсолютні лише заради стилю, не перевіривши, як пакет запускається й тестується.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
