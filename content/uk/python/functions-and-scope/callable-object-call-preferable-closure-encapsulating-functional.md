---
id: py-funcs-0022
title: "Коли callable object із `__call__` доцільніший за closure для інкапсуляції стану функціонального компонента?"
description: "Callable-об’єкт із __call__ доцільніший, коли стан потрібно відкрито зберігати, тестувати, серіалізувати або розширювати додатковими методами."
track: python
section: functions-and-scope
level: senior
type: comparison
tags: [call]
status: published
updated: 2026-10-13
content_revision: 2
reconciled_with:
  en: 2
anki:
  export: true
sources:
  - source_id: py314-reference-datamodel-object-call
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html#object.__call__
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-reference-datamodel-function-closure
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html#function.__closure__
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14: атрибут __closure__ функції зберігає cells для вільних змінних."
  - source_id: py314-library-pickle-what-can-be-pickled
    title: "Python 3.14: Library/pickle"
    url: https://docs.python.org/3.14/library/pickle.html#what-can-be-pickled-and-unpickled
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14: які об’єкти можна pickle; функції й класи за іменем з верхнього рівня модуля, локальні функції й lambda не підтримуються."
---

## Short answer

**Callable-об’єкт із `__call__` доцільніший, коли стан потрібно відкрито зберігати, тестувати, серіалізувати або розширювати додатковими методами.**[^py314-reference-datamodel-object-call] Closure тримає стан у cell-змінних, які не є атрибутами й доступні ззовні хіба що через `__closure__`. Екземпляр класу, визначеного на верхньому рівні модуля, можна pickle, якщо його дані можна pickle, тоді як локальна closure ні.[^py314-library-pickle-what-can-be-pickled] Клас також дає іменовані методи, наприклад `reset()`, і звичайне успадкування.

## Detailed explanation

Обидва варіанти дають callable зі станом: closure – звичайну функцію, яка тримає змінні зовнішньої функції, а callable object – екземпляр класу з методом `__call__`. Коли Python виконує `obj(...)`, він викликає `type(obj).__call__(obj, ...)`.[^py314-reference-datamodel-object-call] Тому поведінка виклику однакова, а різниця лежить в інструментах навколо стану: доступ до нього, тестування, збереження і розширення.

Closure коротка і не потребує класу, але її стан не є частиною інтерфейсу. Лічильник з `nonlocal` зберігає `count` у cell, який видно через `function.__closure__`.[^py314-reference-datamodel-function-closure] Щоб додати `reset()`, доведеться писати другу функцію з `nonlocal` або повертати кілька замикань, кожне з яких тестується окремо.

```python
class Counter:
    def __init__(self, start=0):
        self.count = start

    def __call__(self):
        self.count += 1
        return self.count

    def reset(self, start=0):
        self.count = start

c = Counter()
print(c(), c())                       # 1 2
c.reset()
print(c(), c.count)                   # 1 1

def make_counter(start=0):
    count = start
    def counter():
        nonlocal count
        count += 1
        return count
    return counter

f = make_counter()
print(f(), f())                       # 1 2
print(f.__closure__[0].cell_contents) # 2, the state is read through the closure cell
```

Callable object дає стан як атрибут: тест перевіряє `c.count` напряму, а `reset()` є звичайним методом, який можна викликати з інших модулів і перевизначити в підкласі. Серіалізація розділяє ці варіанти ще різкіше. `pickle` зберігає функції й класи за іменем, тому вони мають бути доступні з верхнього рівня модуля, а екземпляр зберігає лише свої дані.[^py314-library-pickle-what-can-be-pickled] Локальна `counter` не має такого імені, і `pickle.dumps(f)` падає: `AttributeError` у 3.13, `PicklingError` у 3.14.

Closure доречна для короткого внутрішнього стану, який ніхто ззовні не має читати. Callable object доречний, коли стан треба інспектувати, тестувати, зберігати або розширювати набором методів.

**Типові помилки:**
- вважати closure повністю інкапсульованою: її стан видно через `__closure__`, тож це лише приховування від звичайного коду;
- писати клас із `__call__` без методів і атрибутів, який не дає жодної переваги перед функцією;
- тримати в атрибутах callable lambda або локальну функцію, після чого `pickle` падає, хоча сам клас визначено на верхньому рівні.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
