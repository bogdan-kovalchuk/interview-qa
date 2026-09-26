---
id: py-ctxmgr-0007
title: "Як `ExitStack` зберігає LIFO порядок cleanup і що має статися, якщо acquisition одного з ресурсів не вдалося?"
description: "ExitStack зберігає список callback у порядку реєстрації та викликає їх у зворотному порядку (LIFO), як вкладені with."
track: python
section: context-managers
level: senior
type: mechanism
tags: [exitstack]
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

**`ExitStack` зберігає список callback у порядку реєстрації та викликає їх у зворотному порядку (LIFO), як вкладені `with`.**[^py314-reference-datamodel-with-statement-context-managers] Якщо `enter_context()` для чергового ресурсу кидає exception, `ExitStack` все одно викликає `__exit__` для всіх раніше зареєстрованих менеджерів – вже набутих ресурсів. Це забезпечує коректний cleanup навіть при частковому failure.

## Detailed explanation

`contextlib.ExitStack` реалізує динамічний стек контекстних менеджерів та довільних callbacks за принципом LIFO (Last-In, First-Out), зберігаючи їх у внутрішньому списку `_exit_callbacks`.[^py314-library-contextlib] Коли викликається метод `stack.enter_context(cm)`, `ExitStack` спочатку отримує незв'язаний метод `__exit__` класу менеджера, викликає `__enter__()`, і лише після успішного повернення додає `__exit__` у стек.[^py314-reference-datamodel-with-statement-context-managers] Якщо черговий acquisition кидає виняток, щойно викликаний менеджер не встигає зареєструватися, але виняток виходить назовні в блок `with ExitStack()`, ініціюючи негайне розгортання стека для вже зареєстрованих ресурсів.

Розгортання стека повністю відтворює семантику вкладених блоків `with`: callbacks витягуються за допомогою `pop()` і викликаються з аргументами поточного винятку.[^py314-library-contextlib] Якщо один із callbacks повертає істинне значення, виняток вважається придушеним, і наступні (зовнішні) callbacks отримують `None, None, None`, немовби внутрішній блок самостійно перехопив помилку. Якщо ж під час розгортання сам callback викидає новий виняток або виникає помилка в наступному менеджері, Python автоматично пов'язує їх через механізм exception chaining (`__context__`), запобігаючи прихованій втраті первинної причини збою.

У senior-дизайні `ExitStack` є ключовим інструментом для забезпечення транзакційності під час набуття декількох ресурсів (pattern all-or-nothing). Для цього використовується метод `stack.pop_all()`, який переносить усі зареєстровані callbacks у новий `ExitStack` і очищає поточний.[^py314-library-contextlib] Якщо всі ресурси успішно отримано, фабрична функція повертає `stack.pop_all()`, уникаючи виклику `__exit__` під час виходу з тимчасового блоку і передаючи обов'язок очищення викликачу.

Демонстрація LIFO-очищення вже набутих ресурсів у разі збою під час створення чергового об'єкта:

```python
from contextlib import ExitStack

class Resource:
    def __init__(self, name: str, fail_on_enter: bool = False):
        self.name = name
        self.fail_on_enter = fail_on_enter

    def __enter__(self):
        if self.fail_on_enter:
            raise RuntimeError(f"Failed to acquire {self.name}")
        print(f"Acquired: {self.name}")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Cleaned up: {self.name} (exc: {exc_type.__name__ if exc_type else None})")
        return False  # Do not suppress exceptions

# When acquiring resource 'res3' fails, res2 and res1 are cleaned up in LIFO order
try:
    with ExitStack() as stack:
        r1 = stack.enter_context(Resource("res1"))
        r2 = stack.enter_context(Resource("res2"))
        r3 = stack.enter_context(Resource("res3", fail_on_enter=True))
except RuntimeError as err:
    print(f"Caught: {err}")

# Output:
# Acquired: res1
# Acquired: res2
# Cleaned up: res2 (exc: RuntimeError)
# Cleaned up: res1 (exc: RuntimeError)
# Caught: Failed to acquire res3
```

**Практичні наслідки та архітектурні нюанси:**
- часткова ініціалізація не залишає витоків: кожен раніше відкритий файловий дескриптор, сокет або lock гарантовано закривається;
- порядок очищення протилежний порядку відкриття: залежні ресурси закриваються раніше за ресурси, від яких вони залежать;
- для безпечного перенесення володіння ресурсами поза межі локального блоку слід застосовувати `stack.pop_all()`, а не намагатися вручну маніпулювати внутрішнім списком callbacks.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
