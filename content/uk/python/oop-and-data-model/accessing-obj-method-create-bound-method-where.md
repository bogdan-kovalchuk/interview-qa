---
id: py-oop-0013
title: "Чому доступ `obj.method` створює bound method і звідки береться implicit `self` під час виклику?"
track: python
section: oop-and-data-model
sources:
  - source_id: py314-reference-datamodel
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html
  - source_id: py314-howto-descriptor
    title: "Python 3.14: Howto/descriptor"
    url: https://docs.python.org/3.14/howto/descriptor.html
  - source_id: py314-howto-mro
    title: "Python 3.14: Howto/mro"
    url: https://docs.python.org/3.14/howto/mro.html
  - source_id: py314-library-dataclasses
    title: "Python 3.14: Library/dataclasses"
    url: https://docs.python.org/3.14/library/dataclasses.html
  - source_id: py314-howto-descriptor-functions-and-methods
    title: "Python 3.14: Howto/descriptor"
    url: https://docs.python.org/3.14/howto/descriptor.html#functions-and-methods
  - source_id: py314-reference-datamodel-invoking-descriptors
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html#invoking-descriptors
  - source_id: py314-library-dis-load-attr
    title: "Python 3.14: Library/dis"
    url: https://docs.python.org/3.14/library/dis.html#opcode-LOAD_ATTR
  - source_id: cpython-funcobject-func-descr-get
    title: "CPython Objects/funcobject.c: func_descr_get"
    url: https://github.com/python/cpython/blob/v3.14.7/Objects/funcobject.c
---

## Short answer

**Функції є non-data descriptors: їхній `__get__` при доступі через instance повертає `MethodType(func, obj)`, який і є bound method.**[^py314-howto-descriptor-functions-and-methods] Bound method зберігає пару `(__func__, __self__)`; при виклику `obj.method(x)` він автоматично підставляє `__self__` як перший аргумент перед `x`.[^py314-reference-datamodel] Таким чином implicit `self` – це не магія синтаксису, а результат роботи function descriptor protocol.

## Detailed explanation

Функція в класі – це об’єкт `function`, який визначає лише `__get__`, без `__set__` і `__delete__`. Отже, це non-data descriptor. При `obj.method` Python викликає `__get__` цієї функції з `obj` і класом, і функція повертає bound method. Логіка коротка: якщо `obj` є `None`, повернути саму функцію, інакше створити `MethodType(func, obj)`.[^py314-howto-descriptor-functions-and-methods][^cpython-funcobject-func-descr-get]

Bound method – це пара: `__func__` (функція з класу) і `__self__` (instance). Коли його викликають, `__self__` іде першим аргументом, тож `m(5)` означає те саме, що `Counter.incr(c, 5)`.[^py314-reference-datamodel] Сама функція `incr` не містить `c`: прив’язка відбувається в момент доступу через instance.

Приклад: доступ без виклику створює bound method, а `Counter.incr(c, 2)` – звичайний виклик функції з явним `self`. Коментарі показують результат запуску (CPython 3.14):

```python
class Counter:
    def __init__(self):
        self.n = 0

    def incr(self, step):
        self.n += step
        return self.n

c = Counter()
m = c.incr                           # no call yet: a bound method object is created
print(type(m).__name__)              # method
print(m.__self__ is c)               # True
print(m.__func__ is Counter.incr)    # True: the same function, found on the class
print(m(5))                          # 5: __self__ is passed as the first argument
print(Counter.incr(c, 2))            # 7: explicit self, the same function
print(c.incr is c.incr)              # False: a new bound method object on each access
print(c.incr == c.incr)              # True: equal, because __self__ and __func__ match
```

Кожен доступ `c.incr` створює новий bound method. Тому `c.incr is c.incr` дає `False`, а `c.incr == c.incr` дає `True`: рівність порівнює `__self__` і `__func__`. Оскільки функція є non-data descriptor, запис `c.incr = ...` в instance dictionary має пріоритет над класом, і `c.incr` поверне записане значення.[^py314-reference-datamodel-invoking-descriptors]

У виразі `c.incr(5)` CPython не створює проміжного bound method: у CPython 3.12+ байткод `LOAD_ATTR` з прапорцем method (раніше `LOAD_METHOD`) кладе на стек функцію і `self`, а `CALL` передає `self` першим аргументом.[^py314-library-dis-load-attr] Семантика та сама, тож обидві форми правильні; різниця є лише деталлю реалізації.

Bound method, збережений у змінній, містить `__self__`, тобто сам instance.[^py314-reference-datamodel] Через це змінна тримає посилання на instance, і поки вона жива, instance не звільняється.

**Типові помилки:**
- очікувати, що `c.incr` виконає метод: без дужок повертається bound method, а не результат;
- вважати `c.incr is c.incr` ознакою того, що метод один і той самий: кожен доступ дає новий об’єкт;
- зберігати bound method як callback, не враховуючи, що він утримує instance.
