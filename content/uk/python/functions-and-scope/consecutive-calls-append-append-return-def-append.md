---
id: py-funcs-0006
title: "Що повернуть два послідовні виклики `append(1)` і `append(2)` для `def append(x, items=[]): items.append(x); return items`, і чому?"
track: python
section: functions-and-scope
sources:
  - source_id: py314-reference-compound-stmts-function-definitions
    title: "Python 3.14: Reference/compound Stmts"
    url: https://docs.python.org/3.14/reference/compound_stmts.html#function-definitions
  - source_id: py314-faq-programming-why-are-default-values-shared-between
    title: "Python 3.14: Faq/programming"
    url: https://docs.python.org/3.14/faq/programming.html#why-are-default-values-shared-between-objects
---

## Short answer

**`append(1)` повертає `[1]`, `append(2)` повертає `[1, 2]` – обидва виклики працюють з одним і тим самим списком.**[^py314-faq-programming-why-are-default-values-shared-between] Default-об’єкт `[]` створюється один раз під час виконання `def`, а не при кожному виклику.[^py314-reference-compound-stmts-function-definitions] Параметр `items` вказує на цей єдиний об’єкт, тому `.append()` накопичує елементи між викликами. <span class="warn">Це класична пастка mutable default.</span> Правильний патерн – використовувати `items=None` і створювати новий список усередині функції.[^py314-faq-programming-why-are-default-values-shared-between]

## Detailed explanation

Значення за замовчуванням обчислюються зліва направо під час виконання інструкції `def`, а не при кожному виклику функції. Вираз `[]` у сигнатурі виконується один раз: отриманий список зберігається разом із функцією і використовується в кожному виклику, де `items` не передано.[^py314-reference-compound-stmts-function-definitions] Тому два виклики без `items` працюють з одним і тим самим списком, а не з двома порожніми.

Наступний приклад показує, що саме спільне. Перші два результати – це той самий об’єкт, який функція змінює на кожному виклику:

```python
def append(x, items=[]):
    items.append(x)
    return items

print(append(1))              # [1]
print(append(2))              # [1, 2]: the same list object, not a new one
print(append.__defaults__)    # ([1, 2],): the default object itself was changed

first = append(3)
second = append(4)
print(first is second)        # True: both names refer to one list
print(first)                  # [1, 2, 3, 4]: the earlier result changed too
```

Повернене значення – не знімок стану, а посилання на спільний список. Якщо зберегти результат першого виклику, він покаже `[1, 2, 3, 4]` після наступних викликів. Розв’язання – `items=None` і створення списку всередині функції, коли `items is None`: тоді кожен виклик без аргументу отримує новий об’єкт.[^py314-faq-programming-why-are-default-values-shared-between]

Пастка стосується лише змінюваних значень за замовчуванням. Числа, рядки і `None` не можна змінити на місці, тому їхнє спільне використання безпечне.[^py314-faq-programming-why-are-default-values-shared-between]

**Типові помилки:**
- вважати, що кожен виклик без `items` отримує новий порожній список;
- зберегти результат першого виклику і очікувати, що він не зміниться після другого;
- писати `items=[]` або `items={}` у функції, яка змінює цей аргумент.
