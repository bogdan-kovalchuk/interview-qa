---
id: py-prac-0003
title: "Що надрукує `a = [[1]]; b = a.copy(); b[0].append(2); print(a)` і як shallow copy створює цей aliasing bug?"
track: python
section: practical-coding
sources:
  - source_id: py314-tutorial
    title: "Python 3.14: Tutorial"
    url: https://docs.python.org/3.14/tutorial/
  - source_id: py314-reference
    title: "Python 3.14: Reference"
    url: https://docs.python.org/3.14/reference/
  - source_id: py314-library-copy
    title: "Python 3.14: Library/copy"
    url: https://docs.python.org/3.14/library/copy.html
---

## Short answer

**Надрукує `[[1, 2]]` – `a` теж бачить зміну.** `list.copy()` створює shallow copy: новий зовнішній список, який містить ті самі елементи, тобто вкладений список копіюється лише за посиланням.[^py314-library-copy] Тому `b[0]` і `a[0]` – це один і той самий `list`, і `append(2)` через `b` змінює його для обох. <span class="warn">Для копії, яка не ділить вкладені об’єкти, використовують `copy.deepcopy()`.[^py314-library-copy]</span>

## Detailed explanation

Присвоєння `b = a` не копіює список: воно лише додає ще одне ім’я для того самого об’єкта.[^py314-library-copy] Метод `a.copy()` створює інший зовнішній список, але не копіює його елементи. Це і є shallow copy: новий контейнер, у якому посилання на елементи вказують на ті самі об’єкти, що й в оригіналі.[^py314-library-copy]

Рядок `b[0] is a[0]` показує спільний об’єкт. Мутація через `b[0]` видна через `a`, бо змінюється сам внутрішній список, а не посилання в зовнішньому:

```python
a = [[1]]
b = a.copy()
print(b[0] is a[0])  # True: both lists share the same inner object
b[0].append(2)
print(a)  # [[1, 2]]
b.append(3)
print(a)  # [[1, 2]]: the outer list is independent
```

Аліасинг тут має один рівень. Додавання елемента до зовнішнього `b` не змінює `a`, бо зовнішні списки різні. Тому баг легко пропустити: тест, який змінює лише верхній рівень, пройде, а зміна вкладеного елемента зламає оригінал.

Якщо вкладені об’єкти мають бути незалежними, використовують `copy.deepcopy()`. Він рекурсивно копіює вкладені об’єкти й зберігає memo-словник уже скопійованих, тому зациклені структури не призводять до нескінченного рекурсивного обходу.[^py314-library-copy] Приклад:

```python
import copy

a = [[1]]
c = copy.deepcopy(a)
c[0].append(2)
print(a)  # [[1]]
print(c)  # [[1, 2]]
```

Глибока копія теж не завжди правильна: вона може скопіювати й дані, які мали лишитися спільними між копіями.[^py314-library-copy]

**Типові помилки:**
- вважати, що `list.copy()` робить повну копію вкладених структур;
- змінити вкладений елемент однієї копії і очікувати, що інша не зміниться;
- використовувати `copy.deepcopy()` завжди, навіть коли дані мали бути спільними.
