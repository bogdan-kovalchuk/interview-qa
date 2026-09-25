---
id: py-ctxmgr-0003
title: "Як гарантувати cleanup у `__exit__`, не приховавши original exception новою помилкою cleanup-коду?"
description: "Cleanup-код у __exit__ треба огортати у власний try/except, щоб exception під час cleanup не замінив оригінальний."
track: python
section: context-managers
level: senior
type: practical
tags: [exit]
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

**Cleanup-код у `__exit__` треба огортати у власний `try/except`, щоб exception під час cleanup не замінив оригінальний.**[^py314-reference-datamodel-with-statement-context-managers] Якщо `__exit__` викликано з exception-аргументами і cleanup кидає нову помилку без обробки, Python втратить початкову exception. Безпечний патерн: огорнути `self.resource.close()` у `try/except Exception`, залогувати помилку cleanup і повернути `False`. Якщо оригінальної exception немає, помилка cleanup може вільно поширюватися.

## Detailed explanation

Коли інтерпретатор викликає `__exit__(exc_type, exc_val, exc_tb)` через виняток у тілі `with`, будь-яка нова необроблена помилка всередині самого `__exit__` негайно перериває виконання методу та поширюється вгору по стеку, витісняючи первинну проблему.[^py314-reference-datamodel-with-statement-context-managers]

Хоча механізм неявного ланцюжка винятків (exception chaining) у Python зв'язує нову помилку з попередньою через атрибут `__context__`, у продакшені це часто призводить до спотворення моніторингу: алерти спрацьовують на вторинний `OSError` чи `ConnectionResetError` при закритті сокета замість реальної бізнес-помилки або багу валідації. Крім того, якщо `__exit__` відповідає за звільнення декількох пов'язаних ресурсів, аварійне завершення на першому кроці залишить усі наступні ресурси незакритими.

Зрілий інженерний підхід вимагає розділяти два сценарії: нормальний вихід (`exc_type is None`) та вихід через помилку (`exc_type is not None`). Якщо первинного винятку не було, помилка cleanup є єдиним збоєм, тому її слід пропустити нагору (наприклад, коли скидання буфера на диск не вдалося і дані втрачено). Якщо ж первинний виняток уже існує, помилки очищення необхідно перехоплювати, детально логувати в діагностичних цілях і повертати `False`, дозволяючи первинному винятку безперешкодно сигналізувати про справжню причину аварії.[^py314-library-contextlib]

Патерн надійного звільнення ресурсів у `__exit__` із захистом первинного винятку:

```python
import logging

logger = logging.getLogger(__name__)


class ResilientResource:
    def __init__(self, resource):
        self.resource = resource

    def __enter__(self):
        return self.resource

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            self.resource.close()
        except Exception as cleanup_err:
            if exc_type is not None:
                # An exception already occurred in the with-block:
                # Log cleanup failure so original exc_val continues propagating
                logger.error(
                    "Cleanup failed during exception handling: %s",
                    cleanup_err,
                    exc_info=True,
                )
                return False  # Propagate the original exception from with-block
            # Normal exit had no errors, so let the cleanup exception surface
            raise
        return False  # Normal clean exit or propagation
```

**Інженерні компроміси та найкращі практики:**
- логування помилок очищення замість їхнього глушіння: `logger.error(..., exc_info=True)` зберігає повний traceback аварії cleanup без переривання первинного збою;
- ізоляція декількох cleanup-дій: якщо звільняються два або більше ресурсів, кожне закриття має бути обгорнуте в окремий блок або делеговане до `contextlib.ExitStack`;
- не маскувати помилки нормального закриття: збій `close()` чи `flush()` без винятку в тілі `with` свідчить про реальну втрату цілісності даних і повинен генерувати виняток;
- уникати перехоплення `BaseException` у cleanup: системні сигнали (`KeyboardInterrupt`, `SystemExit`) повинні негайно зупиняти процес без затримки на повторні спроби.

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
