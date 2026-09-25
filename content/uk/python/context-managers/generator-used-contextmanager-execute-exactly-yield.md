---
id: py-ctxmgr-0005
title: "Чому generator, використаний з `@contextmanager`, повинен виконати рівно один `yield`?"
description: "Протокол @contextmanager відображає один yield на одну пару enter/exit; нуль або більше yield ламає цей контракт."
track: python
section: context-managers
level: middle
type: pitfall
tags: [contextmanager]
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

**Протокол `@contextmanager` відображає один `yield` на одну пару enter/exit; нуль або більше yield ламає цей контракт.**[^py314-reference-datamodel-with-statement-context-managers] Якщо generator не виконує `yield` (наприклад, достроковий `return`), `@contextmanager` raise `RuntimeError: generator didn't yield`. Якщо виконує додатковий `yield` після першого – `RuntimeError: generator didn't stop`. Це гарантує, що enter і exit виконуються рівно один раз.

## Detailed explanation

Декоратор `@contextmanager` базується на строгому двофазному життєвому циклі, де єдина інструкція `yield` слугує чіткою межею між ініціалізацією та очищенням ресурсів.[^py314-library-contextlib]

Під час входу в блок `with` метод `__enter__` обгортки викликає `next(gen)`. Очікується, що генератор виконає підготовчий код і зупиниться на інструкції `yield`, повернувши значення для блоку `as`. Якщо через помилкову умову або достроковий `return` генератор завершується до досягнення `yield`, стандартний протокол ітератора генерує `StopIteration`, який декоратор перехоплює і перетворює на фатальну помилку `RuntimeError("generator didn't yield")`.[^py314-reference-datamodel-with-statement-context-managers]

Під час виходу з блоку `with` метод `__exit__` поновлює виконання генератора за допомогою `next(gen)` (або `gen.throw()`, якщо у блоці виник виняток). Контракт вимагає, щоб генератор завершив роботу та згенерував `StopIteration`. Якщо ж генератор містить цикл або повторний `yield`, обгортка отримує нове значення замість завершення і піднімає `RuntimeError("generator didn't stop")`. Обидві перевірки захищають цілісність програми: вони гарантують симетричність входу та виходу з контексту.

Помилки життєвого циклу генератора в `@contextmanager` та їхнє виправлення:

```python
from contextlib import contextmanager


# 1. Pitfall: early return causes "generator didn't yield"
@contextmanager
def faulty_guard_manager(enabled=False):
    if not enabled:
        return  # BUG: returns before yield -> RuntimeError: generator didn't yield
    yield "ready"


# 2. Pitfall: multiple yields cause "generator didn't stop"
@contextmanager
def faulty_loop_manager():
    for item in ["first", "second"]:
        yield item  # BUG: second iteration -> RuntimeError: generator didn't stop


# 3. Correct pattern: exactly one yield wrapped in try/finally
@contextmanager
def correct_manager(enabled=True):
    resource = None
    try:
        resource = "connected" if enabled else "disabled"
        yield resource
    finally:
        # Cleanup executes deterministically on normal exit or exception
        resource = None


with correct_manager() as status:
    print(f"Status: {status}")  # Status: connected
```

**Типові причини порушення контракту:**
- guard clauses із достроковим `return`: якщо ресурс не готовий, замість тихого `return` слід піднімати явний виняток (`ValueError`, `RuntimeError`);
- розміщення `yield` всередині циклів `for` або `while`: генератор повинен містити рівно одну точку перемикання контексту;
- відсутність `try...finally`: якщо в тілі `with` стається помилка, а код після `yield` не захищений `finally`, очищення ніколи не виконається або генератор завершиться некоректно;
- помилкове використання `yield from`: делегування ітератору, що повертає більше ніж один елемент, гарантовано призведе до помилки зупинки генератора.

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
