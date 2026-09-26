---
id: py-ctxmgr-0010
title: "Чим reusable context manager відрізняється від reentrant context manager?"
description: "Reusable можна використовувати в кількох окремих with blocks, але не можна вкладати всередину самого себе; reentrant можна і повторно використовувати, і вкладати рекурсивно."
track: python
section: context-managers
level: middle
type: comparison
tags: []
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

**Reusable можна використовувати в кількох окремих `with` blocks, але не можна вкладати всередину самого себе; reentrant можна і повторно використовувати, і вкладати рекурсивно.**[^py314-reference-datamodel-with-statement-context-managers] Приклад reusable: `contextlib.ExitStack`, `threading.Lock` – новий `with` працює, але вкладений `with` на тому ж instance зламає стан. Приклад reentrant: `threading.RLock`, `contextlib.redirect_stdout` – вони коректно обробляють вкладеність, зберігаючи попередній стан у внутрішньому стеку.

## Detailed explanation

Різниця між reusable і reentrant контекстними менеджерами полягає у здатності коректно підтримувати одночасну активність у кількох вкладених блоках `with` одного потоку.[^py314-library-contextlib] Reusable (багаторазовий) менеджер дозволяє повторні виклики `__enter__` і `__exit__` лише послідовно: після виходу з першого блоку його внутрішній стан скидається, і об'єкт готовий до нового використання. Проте спроба увійти в нього повторно до завершення попереднього блоку (вкладений `with`) призводить до пошкодження стану, винятку або взаємного блокування (deadlock).

Reentrant (повторно-вхідний) контекстний менеджер не лише придатний для багаторазового послідовного використання, але й безпечно витримує довільну кількість рекурсивних чи вкладених входів.[^py314-reference-datamodel-with-statement-context-managers] Замість єдиного бінарного прапорця активності він підтримує лічильник глибини входження (як у `threading.RLock`) або внутрішній стек збережених станів (як у `contextlib.redirect_stdout`). Кожен виклик `__enter__` збільшує лічильник або зберігає поточний контекст у стек, а парний виклик `__exit__` зменшує лічильник або відновлює попереднє значення, звільняючи базовий ресурс лише тоді, коли зовнішній блок повністю завершується.

Більшість стандартних менеджерів контексту, таких як відкриті файли (`open()`) або функції-генератори з декоратором `@contextlib.contextmanager`, є одноразовими (single-use): спроба повторно використати той самий екземпляр у новому блоці `with` кидає помилку `ValueError` або `RuntimeError`. Створення справжнього reentrant менеджера вимагає проектування структури даних, яка ізолює стан кожного вкладеного рівня виклику замість перезапису спільних атрибутів об'єкта.

Демонстрація різниці між прапорцем послідовного повторного використання та лічильником глибини вкладеності:

```python
class ReusableContext:
    def __init__(self):
        self._active = False

    def __enter__(self):
        if self._active:
            raise RuntimeError("Cannot re-enter an already active context")
        self._active = True
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._active = False

class ReentrantContext:
    def __init__(self):
        self._depth = 0

    def __enter__(self):
        self._depth += 1
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._depth -= 1

# Sequential reuse: both work
reusable = ReusableContext()
with reusable:
    pass
with reusable:
    pass  # Succeeds sequentially

# Nested entry: Reusable fails, Reentrant succeeds
reentrant = ReentrantContext()
with reentrant:
    with reentrant:
        print(f"Reentrant depth: {reentrant._depth}")

try:
    with reusable:
        with reusable:
            pass
except RuntimeError as err:
    print(f"Reusable error: {err}")

# Output:
# Reentrant depth: 2
# Reusable error: Cannot re-enter an already active context
```

**Типові помилки та практичні обмеження:**
- використання менеджера з `@contextlib.contextmanager` як reusable: генератори неможливо перезапустити після завершення, тому кожен `with` потребує нового виклику функції;
- очікування, що `threading.Lock` поводиться як reentrant: спроба повторно захопити звичайний lock у тому самому потоці викликає deadlock, тоді як `threading.RLock` зберігає ідентифікатор власника та лічильник;
- змішування reentrancy між потоками: властивість reentrant зазвичай стосується вкладеності в межах одного потоку, а не одночасного паралельного доступу з різних потоків виконання.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
