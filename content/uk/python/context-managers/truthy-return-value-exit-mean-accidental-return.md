---
id: py-ctxmgr-0002
title: "Що означає truthy return value з `__exit__` і чому випадкове `return True` небезпечне?"
description: "Truthy return з __exit__ пригнічує exception – вона не поширюється далі за межі with."
track: python
section: context-managers
level: middle
type: pitfall
tags: [exit, return-true]
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

**Truthy return з `__exit__` пригнічує exception – вона не поширюється далі за межі `with`.**[^py314-reference-datamodel-with-statement-context-managers] <span class="warn">Випадкове `return True` ковтає будь-який exception, включно з `TypeError`, `KeyboardInterrupt` та помилками в самому cleanup-коді.</span> Це ускладнює діагностику: баг у тілі `with` стає невидимим. Зазвичай безпечніше повертати `False` або `None` і подавлювати лише очікувані типи через явну перевірку.

## Detailed explanation

Метод `__exit__(exc_type, exc_val, exc_tb)` контекстного менеджера викликається інтерпретатором при виході з блоку `with`, і його булеве значення визначає долю винятку: будь-яке truthy значення сигналізує Python, що виняток успішно оброблено і його подальше поширення слід зупинити.[^py314-reference-datamodel-with-statement-context-managers]

Якщо в тілі `with` не виникло помилки, всі три аргументи `exc_type`, `exc_val` та `exc_tb` дорівнюють `None`. Коли ж виникає виняток, інтерпретатор передає його тип, екземпляр та об'єкт traceback у `__exit__`. За замовчуванням, якщо метод завершується без явного `return` (повертаючи `None`) або явно повертає `False`, Python відновлює поширення винятку вгору по стеку викликів.

Небезпека полягає в тому, що розробники іноді пишуть `return True` за звичкою, вважаючи це індикатором успішного виконання самого cleanup-коду. У результаті контекстний менеджер мовчки поглинає критичні системні помилки, друкарські помилки у змінних (`NameError`), невідповідності типів (`TypeError`) і навіть `KeyboardInterrupt` або `asyncio.CancelledError`.[^py314-library-asyncio-task-task-cancellation] Наслідком стає виконання наступного коду в некоректному або пошкодженому стані без жодного запису в логах про першопричину збою.

Демонстрація небезпечного та безпечного повернення значень з `__exit__`:

```python
class SwallowingManager:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # DANGEROUS: unconditional truthy return swallows all exceptions!
        return True


class SafeManager:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Safe: inspect exc_type and only suppress specific, expected errors
        if exc_type is not None and issubclass(exc_type, KeyError):
            return True  # Suppress only KeyError
        return False  # Propagate TypeError, NameError, KeyboardInterrupt, etc.


# 1. Dangerous pattern hides critical bugs
with SwallowingManager():
    typo_name_error  # NameError is silently swallowed; bug goes unnoticed

# 2. Safe pattern suppresses only intended exceptions
with SafeManager():
    data = {}
    _ = data["missing"]  # KeyError is cleanly handled and suppressed

print("Execution continued safely")
```

Щоб уникнути подібних прихованих помилок, стандартна бібліотека також пропонує готові утиліти, наприклад `contextlib.suppress`, де список дозволених до пригнічення винятків декларується явно.[^py314-library-contextlib]

**Типові помилки та рекомендації:**
- повернення `True` як статусу «cleanup виконався без помилок», що призводить до непомітної втрати справжнього винятку;
- відсутність перевірки `exc_type` перед пригніченням – перевіряти тип слід через `issubclass(exc_type, ExpectedException)` або `isinstance(exc_val, ExpectedException)`;
- випадкове пригнічення системних винятків (`KeyboardInterrupt`, `SystemExit`, `CancelledError`), які ніколи не повинні зупинятися звичайним менеджером контексту;
- явне повернення `False` або просто опущення `return` (повертається `None`), якщо менеджер займається лише звільненням ресурсів без обробки винятків.

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
