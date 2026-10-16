---
id: py-oop-0023
title: "Чому comparison method має повертати `NotImplemented` для непідтримуваного operand замість негайного `False` або exception?"
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
  - source_id: py314-reference-datamodel-object-eq
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html#object.__eq__
  - source_id: py314-reference-datamodel-notimplemented
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html#notimplemented
  - source_id: py314-reference-expressions-value-comparisons
    title: "Python 3.14: Reference/expressions"
    url: https://docs.python.org/3.14/reference/expressions.html#value-comparisons
---

## Short answer

**Comparison method повертає `NotImplemented`, коли не підтримує другий operand, і тоді інтерпретатор пробує reflected method другого operand.**[^py314-reference-datamodel-object-eq] Якщо й він повертає `NotImplemented`, `==` і `!=` порівнюють ідентичність через `is` і `is not`.[^py314-reference-datamodel-object-eq] Порядкові оператори в такому випадку викликають `TypeError` (у CPython). Повернення `False` замість `NotImplemented` закриває шлях для другого operand.[^py314-reference-datamodel-object-eq]

## Detailed explanation

Для `a == b` зазвичай спершу викликається `type(a).__eq__(a, b)`. Якщо типи різні і тип правого operand є прямим або непрямим підкласом типу лівого, спершу викликається reflected method правого operand. `__eq__` є власним reflection, тому другий виклик – це `type(b).__eq__(b, a)`.[^py314-reference-datamodel-object-eq] Якщо жоден метод не повертає значення, відмінне від `NotImplemented`, `==` і `!=` переходять до `is` і `is not`.[^py314-reference-datamodel-object-eq]

Важлива відмінність – у значенні `False`. Це остаточна відповідь, і другий метод не викликається. `NotImplemented` означає «цей тип не знає про такий operand», і рішення переходить до іншого боку. Приклад показує обидві поведінки:

```python
class Strict:
    def __eq__(self, other):
        return False                  # final answer: the reflected method is never tried

class Lenient:
    def __eq__(self, other):
        return NotImplemented         # "not mine": the other operand decides

class Accepting:
    def __eq__(self, other):
        return True

print(Strict() == Accepting())        # False: Strict answered first
print(Lenient() == Accepting())       # True: Accepting.__eq__ is tried next
print(Lenient() == 1)                 # False: both sides gave NotImplemented, so == uses is
```

`Strict` відповідає одразу, тож `Accepting` ніхто не питає. `Lenient` повертає `NotImplemented`, і рішення передається `Accepting.__eq__`. Третій рядок показує fallback: якщо обидва operand відмовились, `==` порівнює ідентичність.

Виняток у `__eq__` гірший: `a == b` з будь-яким «чужим» об’єктом (також `in`, `list.index`) падає, і reflected method другого operand не отримує шансу.

Для порядкових операторів fallback до ідентичності немає. Документація каже, що стандартного порядкового оператора немає і спроба його використати дає `TypeError`.[^py314-reference-expressions-value-comparisons] У CPython, якщо обидва operand повертають `NotImplemented` для `<`, повідомлення містить назви обох типів, наприклад `'<' not supported between instances of 'A' and 'int'`.

`NotImplemented` не можна використовувати в булевому контексті. До Python 3.14 це було застаріло (DeprecationWarning з 3.9), а в 3.14 `bool(NotImplemented)` викликає `TypeError`.[^py314-reference-datamodel-notimplemented] Тому `if self.__eq__(other):` у 3.14 падає з `TypeError`, якщо метод повернув `NotImplemented`.

**Типові помилки:**
- повертати `None` або `False` замість `NotImplemented` для непідтримуваного типу: `__eq__`, що повертає `None`, дає `None` як результат `==`, а `False` закриває другий operand;
- очікувати від `==` з непідтримуваним типом `TypeError`: `==` дає `False`, а `TypeError` виникає для порядкових операторів;
- писати `if self.__eq__(other):` або `bool(NotImplemented)`: у 3.9–3.13 це DeprecationWarning, а в 3.14 – `TypeError`.
