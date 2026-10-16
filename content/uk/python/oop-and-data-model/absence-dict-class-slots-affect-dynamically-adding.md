---
id: py-oop-0008
title: "Як відсутність `__dict__` у класі з `__slots__` впливає на динамічне додавання атрибутів?"
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
  - source_id: py314-reference-datamodel-slots
    title: "Python 3.14: Reference/datamodel, __slots__"
    url: https://docs.python.org/3.14/reference/datamodel.html#slots
---

## Short answer

**Instance класу, у всьому ланцюгу успадкування якого кожен клас визначає `__slots__`, не має `__dict__`, тому спроба додати атрибут, не перелічений у `__slots__`, піднімає `AttributeError`.**[^py314-reference-datamodel-slots] Атрибути зберігаються в слотах (дескрипторах рівня класу), а не в словнику; це економить пам’ять на великих наборах instance, але обмежує гнучкість.[^py314-reference-datamodel-slots] <span class="warn">Якщо до `__slots__` додати `'__dict__'`, instance знову отримає словник і зможе приймати довільні атрибути.</span>[^py314-reference-datamodel-slots]

## Detailed explanation

За замовчуванням атрибути екземпляра зберігаються в його `__dict__`, тобто в окремому словнику для кожного instance. `__slots__` змінює це: клас оголошує фіксований набір імен, для кожного імені на рівні класу створюється descriptor, а `__dict__` і `__weakref__` автоматично не створюються, якщо їх не перелічено.[^py314-reference-datamodel-slots] Економія пам’яті може бути значною, а доступ до атрибутів – швидшим.[^py314-reference-datamodel-slots]

Наслідок для динамічного додавання видно на простому прикладі:

```python
class Point:
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(1, 2)
print(hasattr(p, '__dict__'))  # False: no per-instance dictionary
try:
    p.z = 3                    # 'z' is not in __slots__
except AttributeError as e:
    print(e)                   # 3.13+: 'Point' object has no attribute 'z' and no __dict__ for setting new attributes (3.12 and earlier: only "...has no attribute 'z'")
```

Умова «кожен клас ланцюга» важлива. Якщо один із базових класів не визначає `__slots__`, його `__dict__` успадковується, і дочірній клас приймає довільні атрибути, навіть коли сам має `__slots__`.[^py314-reference-datamodel-slots] Приклад:

```python
class Base:              # no __slots__: instances get __dict__
    pass

class Child(Base):
    __slots__ = ('x',)

c = Child()
c.extra = 1              # works: the inherited __dict__ accepts it
print(hasattr(c, '__dict__'))  # True
print(c.extra)                 # 1
```

Два правила ще важливі. Атрибут класу не може задавати значення за замовчуванням для слота, бо він перекрив би descriptor слота.[^py314-reference-datamodel-slots] У CPython такий клас не створюється (`ValueError`: `'x' in __slots__ conflicts with class variable`). Якщо потрібні і слоти, і довільні атрибути, до `__slots__` додають `'__dict__'`, але тоді instance знову має словник, і частина переваг слотів зникає.[^py314-reference-datamodel-slots]

**Типові помилки:**
- вважати, що будь-який клас зі `__slots__` забороняє нові атрибути: з базовим класом без `__slots__` словник є;
- записувати значення за замовчуванням як атрибут класу з тим самим іменем, що й слот;
- додавати `'__dict__'` до `__slots__` і очікувати, що всі переваги слотів збережуться.
