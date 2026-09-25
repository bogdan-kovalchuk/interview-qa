---
id: py-ctxmgr-0006
title: "Коли `contextlib.ExitStack` кращий за статично вкладені `with` blocks?"
description: "ExitStack потрібен, коли кількість ресурсів або cleanup-дій визначається динамічно під час виконання."
track: python
section: context-managers
level: middle
type: comparison
tags: [contextlib-exitstack]
status: published
updated: 2026-09-27
content_revision: 2
reconciled_with:
  en: 2
anki:
  export: true
sources:
  - source_id: py314-reference-datamodel-with-statement-context-managers
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html#with-statement-context-managers
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-contextlib
    title: "Python 3.14: Library/contextlib"
    url: https://docs.python.org/3.14/library/contextlib.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-asyncio-task-task-cancellation
    title: "Python 3.14: Library/asyncio Task"
    url: https://docs.python.org/3.14/library/asyncio-task.html#task-cancellation
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
---

## Short answer

**`ExitStack` потрібен, коли кількість ресурсів або cleanup-дій визначається динамічно під час виконання.**[^py314-reference-datamodel-with-statement-context-managers] Статичні вкладені `with` працюють, коли ресурси відомі наперед. `ExitStack` дозволяє реєструвати контекст-менеджери та довільні callback у циклі або умовно, з гарантованим LIFO cleanup. Також зручний для "all-or-nothing" acquisition: якщо один ресурс не відкрився, вже відкриті все одно закриються.

## Detailed explanation

Клас `contextlib.ExitStack` надає програмний інтерфейс для керування динамічним набором контекстних менеджерів і функцій очищення, склад та кількість яких стають відомими лише під час виконання програми.[^py314-library-contextlib]

Статична конструкція `with` (як окремими вкладеними рівнями, так і через кому `with A() as a, B() as b:`) вимагає жорсткої фіксації кількості ресурсів ще на етапі написання коду. Крім того, вираз із комою приховує небезпеку: якщо при створенні другого ресурсу `B()` виникає помилка, перший ресурс `A()` може залишитися незакритим або потребуватиме ручного збирання сміття. Статичний синтаксис також не дозволяє відкривати змінний список файлів або додавати ресурси умовно всередині циклів і розгалужень.

`ExitStack` розв'язує цю проблему через внутрішній стек зворотних викликів очищення, організований за принципом LIFO (Last-In, First-Out). Метод `stack.enter_context(cm)` спочатку викликає `__enter__`, і лише в разі успіху додає `__exit__` у стек. Якщо на N-му кроці стається виняток, `ExitStack` автоматично розгортає стек у зворотному порядку, гарантовано закриваючи всі успішно відкриті до цього моменту ресурси.[^py314-reference-datamodel-with-statement-context-managers] Крім того, метод `stack.callback()` дозволяє реєструвати звичайні функції закриття, а `stack.pop_all()` дає змогу реалізувати транзакційне захоплення «все або нічого» (all-or-nothing).

Динамічне відкриття списку файлів та гарантоване очищення через `ExitStack`:

```python
from contextlib import ExitStack
from tempfile import NamedTemporaryFile


def process_dynamic_files(file_paths):
    # Static 'with' cannot handle a variable-length list of paths.
    # ExitStack guarantees LIFO cleanup even if an error occurs mid-loop.
    with ExitStack() as stack:
        handles = [stack.enter_context(open(path, "r")) for path in file_paths]
        # Register an arbitrary cleanup callback without a full context manager
        stack.callback(print, "All files processed, closing resources")
        return [h.read() for h in handles]


# Demonstration with temporary files
with NamedTemporaryFile("w+", delete=False) as f1, NamedTemporaryFile(
    "w+", delete=False
) as f2:
    f1.write("file1")
    f2.write("file2")
    f1.flush()
    f2.flush()

    contents = process_dynamic_files([f1.name, f2.name])
    print(f"Read {len(contents)} files successfully")
```

**Переваги `ExitStack` порівняно зі статичними блоками:**
- динамічна кількість ресурсів: можливість відкривати довільну кількість об'єктів у циклі без створення штучної глибини відступів;
- атомарне захоплення ресурсів: у разі збою на середині циклу всі раніше відкриті дескриптори закриваються коректно;
- довільні callbacks: метод `callback()` позбавляє потреби писати класи-обгортки для простих функцій закриття (`close`, `release`, `disconnect`);
- передача відповідальності: метод `pop_all()` дозволяє успішно перенести стек закриття в довгоживучий об'єкт, якщо всі ресурси ініціалізувалися без помилок.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
