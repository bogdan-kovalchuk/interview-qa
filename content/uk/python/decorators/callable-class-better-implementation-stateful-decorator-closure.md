---
id: py-decor-0007
title: "Коли callable class є кращою реалізацією stateful decorator за closure?"
description: "Callable class зручніша для stateful decorator, коли стан треба явно ініціалізувати, скидати чи тестувати; для декорування методів їй потрібен `__get__`."
track: python
section: decorators
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
  - source_id: py314-glossary-term-decorator
    title: "Python 3.14: Glossary"
    url: https://docs.python.org/3.14/glossary.html#term-decorator
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-functools-functools-wraps
    title: "Python 3.14: Library/functools"
    url: https://docs.python.org/3.14/library/functools.html#functools.wraps
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-reference-compound-stmts-function-definitions
    title: "Python 3.14: Reference/compound Stmts"
    url: https://docs.python.org/3.14/reference/compound_stmts.html#function-definitions
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-glossary-term-descriptor
    title: "Python 3.14: Glossary, descriptor"
    url: https://docs.python.org/3.14/glossary.html#term-descriptor
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Визначення дескриптора: об’єкт, що визначає `__get__()`, `__set__()` або `__delete__()`. Не описує, як декоратори зв’язуються з методами."
  - source_id: py314-reference-datamodel-invoking-descriptors
    title: "Python 3.14: Reference/datamodel, Invoking Descriptors"
    url: https://docs.python.org/3.14/reference/datamodel.html#invoking-descriptors
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Протокол дескрипторів: якщо об’єкт в атрибуті класу визначає `__get__`, доступ через instance викликає його. Об’єкт без `__get__`, `__set__` і `__delete__` не є дескриптором."
---

## Short answer

**Callable class краща, коли стан декоратора треба явно ініціалізувати, скидати або перевіряти, чи коли логіка складається з кількох методів.** Для одного лічильника closure з `nonlocal` простіший. Декоратор є callable, який викликається з функцією як єдиним аргументом.[^py314-reference-compound-stmts-function-definitions] Клас дає явний `__init__`, атрибути стану для тестів, метод reset та `__repr__`. Але instance такого класу не є дескриптором: якщо він декорує метод, без `__get__` він не зв’язується з `self`.[^py314-reference-datamodel-invoking-descriptors]

## Detailed explanation

Декоратор – це функція, що повертає іншу функцію і зазвичай застосовується синтаксисом `@`.[^py314-glossary-term-decorator] Довідка уточнює, що результат виразу декоратора має бути callable, який викликається з функцією як єдиним аргументом, а повернене значення прив’язується до імені функції.[^py314-reference-compound-stmts-function-definitions] Closure і callable class задовольняють цей контракт, тож різниця лише в тому, де живе стан.

У closure лічильник – це змінна зовнішньої функції, яку wrapper змінює через `nonlocal`. Доступ до стану ззовні потребує додаткового прив’язування, наприклад `wrapper.reset = reset`. У callable class стан є атрибутом instance: `__init__` приймає функцію і може перевірити параметри, а `reset()` і `calls` доступні як звичайні атрибути для тестів. Для одного лічильника closure коротша й достатня, а класовий варіант виправданий, коли стану й методів багато.

В обох варіантах варто зберегти метадані оригінальної функції. `functools.wraps` копіює `__name__`, `__doc__` та інші атрибути на wrapper; для класу той самий ефект дає `functools.update_wrapper(self, func)`.[^py314-library-functools-functools-wraps]

Головна пастка callable class – методи. Функція є дескриптором, тож `s.ping` при доступі через instance отримує `self`.[^py314-reference-datamodel-invoking-descriptors] Екземпляр класу без `__get__` дескриптором не є, бо дескриптор – це об’єкт, що визначає `__get__()`, `__set__()` або `__delete__()`.[^py314-glossary-term-descriptor] Якщо декорувати метод таким класом, `s.ping(1)` викликає `__call__` з `1`, а оригінальна функція отримує це значення як `self` і падає з `TypeError` про відсутній аргумент `x`. Приклад нижче містить виправлення: `__get__` повертає `functools.partial(self, obj)`. Лічильник у ньому спільний для всіх екземплярів `Service`, бо зберігається в декораторі, а не в `self`.

```python
import functools

class Counted:
    def __init__(self, func):
        self.func = func
        self.calls = 0                         # state lives on the decorator instance
        functools.update_wrapper(self, func)   # copies __name__, __doc__, ...

    def __call__(self, *args, **kwargs):
        self.calls += 1
        return self.func(*args, **kwargs)

    def __get__(self, obj, objtype=None):      # without this, self is not passed
        if obj is None:
            return self
        return functools.partial(self, obj)

    def reset(self):
        self.calls = 0

class Service:
    @Counted
    def ping(self, x):
        return x

s = Service()
s.ping(1)
s.ping(2)
print(Service.ping.calls)   # 2: the state is shared by all Service instances
Service.ping.reset()
print(Service.ping.calls)   # 0
```

Якщо лічильник має бути окремим для кожного екземпляра, його варто зберігати в атрибутах `self`, а не в декораторі.

**Типові помилки:**
- вважати callable class завжди кращою: для одного лічильника closure коротший і достатній;
- декорувати метод класом без `__get__` і отримати `TypeError`, бо `self` не передається;
- очікувати окремий лічильник для кожного екземпляра, коли декоратор зберігає стан один раз для функції.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
