---
id: py-stdlib-0017
title: "Коли runtime introspection через `inspect.signature()` виправдана, а коли explicit protocol зменшує coupling до implementation details?"
track: python
section: standard-library
sources:
  - source_id: py314-library-functools
    title: "Python 3.14: Library/functools"
    url: https://docs.python.org/3.14/library/functools.html
  - source_id: py314-library-inspect-inspect-signature
    title: "Python 3.14: Library/inspect"
    url: https://docs.python.org/3.14/library/inspect.html#inspect.signature
  - source_id: py314-library-typing-protocol
    title: "Python 3.14: Library/typing (typing.Protocol)"
    url: https://docs.python.org/3.14/library/typing.html#typing.Protocol
---

## Short answer

**`inspect.signature()` виправдана в generic-інструментах (DI-контейнери, decorators, wrapper-и), які мають приймати довільні callable без заздалегідь відомого інтерфейсу.**[^py314-library-inspect-inspect-signature] Якщо компоненту потрібна лише певна поведінка, explicit `Protocol` описує її в коді, а type checker перевіряє реалізації, тож залежність іде від контракту, а не від імен параметрів конкретного класу.[^py314-library-typing-protocol] `signature()` читає сигнатуру, яку оголосила реалізація, і піднімає `ValueError`, коли сигнатуру отримати не можна.[^py314-library-inspect-inspect-signature]

## Detailed explanation

`inspect.signature(callable)` повертає об’єкт `Signature` з іменами параметрів, їхніми значеннями за замовчуванням і анотаціями.[^py314-library-inspect-inspect-signature] Це інтроспекція під час виконання: код дізнається сигнатуру, коли програма вже працює. Такий підхід доречний там, де код не знає callable заздалегідь. DI-контейнер, наприклад, збирає аргументи конструктора за іменами.

Ціна такого рішення – залежність від реалізації. Контейнер нижче зіставляє ключі реєстру з іменами параметрів. Якщо перейменовано обов’язковий параметр, виклик падає з `TypeError` лише під час виконання. Якщо ж перейменовано параметр зі значенням за замовчуванням, помилки немає: контейнер мовчки передає значення за замовчуванням, і результат хибний (`('db', 8080)` замість `('db', 5432)`). Жодна статична перевірка цього не бачить, бо реєстр – звичайний `dict`.

```python
import inspect

class Server:
    def __init__(self, host: str, port: int = 8080):
        self.address = (host, port)

def build(factory, registry):
    # Runtime introspection: the container reads parameter names.
    params = inspect.signature(factory).parameters
    kwargs = {name: registry[name] for name in params if name in registry}
    return factory(**kwargs)

print(build(Server, {"host": "db", "port": 5432}).address)  # ('db', 5432)

class RenamedHost:  # required parameter renamed: the call fails
    def __init__(self, hostname: str, port: int = 8080):
        self.address = (hostname, port)

try:
    build(RenamedHost, {"host": "db", "port": 5432})
except TypeError as error:
    print(error)  # RenamedHost.__init__() missing 1 required positional argument: 'hostname'

class RenamedPort:  # defaulted parameter renamed: no error, the default is used silently
    def __init__(self, host: str, portnum: int = 8080):
        self.address = (host, portnum)

print(build(RenamedPort, {"host": "db", "port": 5432}).address)  # ('db', 8080)
```

Explicit protocol зменшує цю залежність. Споживач описує поведінку, яка йому потрібна, а `typing.Protocol` дозволяє type checker перевірити, що клас їй відповідає, без явного успадкування.[^py314-library-typing-protocol] Реалізація може змінювати внутрішні деталі, а споживач не читає її сигнатуру під час виконання. Для коду застосунку, де інтерфейс відомий заздалегідь, це зазвичай кращий кордон.

Інтроспекція має власні межі. `signature()` піднімає `ValueError`, коли сигнатуру отримати не можна, і `TypeError`, коли тип об’єкта не підтримується.[^py314-library-inspect-inspect-signature] За спостереженням у CPython 3.13 і 3.14, `inspect.signature(dict)` і `inspect.signature(int)` дають `ValueError`: для цих builtin-типів сигнатури немає. За замовчуванням функція йде за атрибутом `__wrapped__`, який додає `functools.wraps`,[^py314-library-functools] тому wrapper показує сигнатуру оригіналу. Якщо передати `follow_wrapped=False`, видно сигнатуру самого wrapper, тобто `(*args, **kwargs)`.[^py314-library-inspect-inspect-signature]

Практичне правило: використовуйте introspection на межі, де тип справді невідомий, і обробляйте її помилки. Там, де інтерфейс відомий заздалегідь, явний Protocol або звичайний параметр з анотацією робить залежність видимою і перевіреною до запуску.

**Типові помилки:**
- вважати, що `signature()` описує контракт, а не поточний стан коду: перейменування параметра змінює результат без попередження;
- використовувати `signature()` там, де інтерфейс відомий заздалегідь, і отримувати зайву залежність від імен параметрів;
- не обробляти `ValueError` і `TypeError` у контейнері, який приймає довільні callable;
- обгорнути функцію без `functools.wraps` і через це сховати її справжню сигнатуру від introspection.
