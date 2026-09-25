---
id: py-ctxmgr-0001
title: "Які значення отримує `__exit__` при нормальному завершенні та при exception усередині `with`?"
description: "При нормальному завершенні __exit__ отримує (None, None, None), а при exception – (exc_type, exc_val, exc_tb): клас, екземпляр і traceback."
track: python
section: context-managers
level: middle
type: mechanism
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

**При нормальному завершенні `__exit__` отримує `(None, None, None)`, а при exception – `(exc_type, exc_val, exc_tb)`: клас, екземпляр і traceback.**[^py314-reference-datamodel-with-statement-context-managers] Якщо exception не стався, всі три аргументи дорівнюють `None`; якщо стався – вони відповідають `sys.exc_info()`. Return value з `__exit__` визначає, чи буде exception suppressed.

## Detailed explanation

Протокол контекстного менеджера у Python базується на двох парних методах: `__enter__()` та `__exit__(self, exc_type, exc_val, exc_tb)`.[^py314-reference-datamodel-with-statement-context-managers] Метод `__enter__` викликається перед входом у тіло інструкції `with`, а `__exit__` гарантовано викликається при виході з блоку за будь-яких умов – як при успішному завершенні, так і при виникненні винятку або передчасному виході через `return`, `break` чи `continue`.

Значення трьох аргументів, які Python передає у `__exit__`, чітко розмежовують сценарії завершення:
- нормальне завершення: якщо тіло блоку `with` виконалося без помилок або завершилося інструкціями керування потоком (`return`, `break`), `__exit__` викликається зі значеннями `(None, None, None)`;
- виникнення винятку: якщо всередині блоку стався необроблений виняток, аргументи отримують кортеж значень, аналогічний результату виклику `sys.exc_info()`: `exc_type` отримує тип винятку (клас), `exc_val` – конкретний екземпляр винятку, а `exc_tb` – об'єкт трасування стека (`traceback`).

Поведінка інтерпретатора після повернення з `__exit__` повністю визначається типом повернутого значення. Якщо `__exit__` повертає істинне значення (truthy, наприклад `True`), Python пригнічує виняток (suppress exception), і виконання програми продовжується з наступної інструкції після блоку `with`. Якщо ж повернуто `False`, `None` (стандартне повернення за відсутності оператора `return`) або будь-яке інше хибне значення (falsy), інтерпретатор автоматично повторно піднімає оригінальний виняток зі збереженням початкового traceback.[^py314-reference-datamodel-with-statement-context-managers] Для контекстних менеджерів на основі генераторів (`@contextlib.contextmanager`) цей механізм транслюється у виклик методу `generator.throw()` у точці `yield`.[^py314-library-contextlib]

Демонстрація отриманих аргументів та логіки пригнічення винятків у методі `__exit__`:

```python
class TrackerContext:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            print("Normal exit:", (exc_type, exc_val, exc_tb))
            return None  # return value is ignored on normal completion
        print(f"Exception caught: {exc_type.__name__}: {exc_val}")
        # Suppress ValueError, propagate any other exception
        return issubclass(exc_type, ValueError)

# Case 1: Normal completion
with TrackerContext():
    print("Executing body normally")
# Output:
# Executing body normally
# Normal exit: (None, None, None)

# Case 2: Exception raised and suppressed
with TrackerContext():
    raise ValueError("demonstration failure")
print("Continued execution after suppressed ValueError")
# Output:
# Exception caught: ValueError: demonstration failure
# Continued execution after suppressed ValueError
```

**Типові помилки та практичні правила:**
- явний повторний виклик `raise exc_val` усередині `__exit__` є антипатерном: він додає зайвий рівень у стек викликів і спотворює контекст помилки; для прокидання винятку слід просто повернути `False` або `None`;
- випадкове повернення істинного значення (наприклад, результат виклику функції логування чи вираз `return 1`) призводить до мовчазного пригнічення всіх винятків у блоці, маскуючи баги;
- при нормальному завершенні значення повернення `__exit__` повністю ігнорується мовою; воно впливає на потік виконання лише тоді, коли `exc_type is not None`;
- якщо `__exit__` сам викидає новий виняток під час очищення ресурсів, цей новий виняток замінює оригінальний, зв'язуючи його через атрибут `__context__`.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
