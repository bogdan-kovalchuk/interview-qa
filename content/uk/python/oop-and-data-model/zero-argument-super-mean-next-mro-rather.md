---
id: py-oop-0017
title: "Чому zero-argument `super()` означає «наступний у MRO», а не просто «безпосередній parent class»?"
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
  - source_id: py314-builtins-functions-super
    title: "Python 3.14: Built-in Functions/super"
    url: https://docs.python.org/3.14/builtins/functions.html#super
---

## Short answer

**`super()` без аргументів бере клас, у якому написано метод, і перший аргумент методу (зазвичай `self`), а далі шукає наступний клас у `__mro__` фактичного типу об’єкта, а не батька класу, де `super()` написано.**[^py314-builtins-functions-super] У ромбі `D(B, C)`, де `B(A)` і `C(A)`, виклик `super()` у `B` передає керування `C`, а не `A`, якщо фактичний тип об’єкта – `D` з MRO `D, B, C, A, object`. Порядок визначається під час виконання, а не текстом `super()`.

## Detailed explanation

Zero-argument форма `super()` працює лише всередині звичайного методу класу. Компілятор сам підставляє два значення: `type`, тобто клас, у якому написано метод, і `obj`, тобто перший аргумент функції, зазвичай `self`.[^py314-builtins-functions-super] Через це `super()` у вкладеній функції не працює так, як очікується.[^py314-builtins-functions-super]

Ключове питання – що означає «наступний». Документація визначає порядок так: `object_or_type` визначає, чий `__mro__` шукати, а пошук починається з класу, що йде одразу після `type`. Для MRO `D, B, C, A, object` і `type`, рівного `B`, пошук іде далі через `C, A, object`.[^py314-builtins-functions-super] Тому наступний клас для `super()` у `B` визначається фактичним типом об’єкта: це `C` для `D()` і `A` для `B()`.

У прикладі `B` викликає `super().hello()`. Для `D()` наступним буде `C`, а для `B()` – `A`:

```python
class A:
    def hello(self):
        print('A.hello')

class B(A):
    def hello(self):
        print('B.hello')
        super().hello()          # the next class after B in type(self).__mro__

class C(A):
    def hello(self):
        print('C.hello')
        super().hello()

class D(B, C):
    pass

print([k.__name__ for k in D.__mro__])  # ['D', 'B', 'C', 'A', 'object']
D().hello()
# B.hello
# C.hello   <- super() in B goes to C, not to A
# A.hello
B().hello()
# B.hello
# A.hello   <- without C in the MRO, the next class is A
```

Так працюють cooperative methods і mixins: кожен клас викликає `super()` і не знає, хто стоїть далі. Якби `super()` означав «батько», то `D().hello()` ніколи не викликав би `C.hello`. Тож `super()` варто читати як «наступний у MRO фактичного типу об’єкта», а не як «базовий клас».[^py314-builtins-functions-super]

**Типові помилки:**
- писати `A.hello(self)` замість `super().hello()` у `B`: для `D()` такий виклик обходить `C`;
- вважати, що `super()` завжди викликає батька, записаного в `class B(A)`;
- викликати `super()` у вкладеній функції або generator expression і очікувати, що вона знає клас методу.[^py314-builtins-functions-super]
