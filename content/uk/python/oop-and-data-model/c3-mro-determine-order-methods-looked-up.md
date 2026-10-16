---
id: py-oop-0016
title: "Як C3 MRO визначає порядок пошуку methods для множинного успадкування і яку властивість порядку він зберігає?"
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
---

## Short answer

**C3 будує лінеаризацію `L[C] = C + merge(L[B₁], …, L[Bₙ], B₁, …, Bₙ)`, зберігаючи local precedence order (порядок bases у `class C(A, B)`) і monotonicity (порядок із MRO класу зберігається в MRO його нащадків).**[^py314-howto-mro] Merge на кожному кроці бере першу «good head»: голову першого зі списків, якої немає в хвостах жодного зі списків. Якщо good head немає, створення класу завершується `TypeError`.[^py314-howto-mro] Пошук атрибутів у базових класах іде цим порядком.[^py314-reference-datamodel]

## Detailed explanation

У множинному успадкуванні пошук атрибута проходить класи в порядку `__mro__`. Цей кортеж обчислюється під час створення класу: `type.mro()` викликається при створенні класу, а його результат зберігається в `__mro__`. Для звичайних класів саме C3 будує цей порядок.[^py314-reference-datamodel]

Лінеаризація описується рекурсивною формулою `L[C(B₁…Bₙ)] = C + merge(L[B₁], …, L[Bₙ], B₁, …, Bₙ)`. Merge бере голову першого списку, якщо вона не стоїть у хвості жодного іншого списку (good head). Інакше пробує голову наступного списку. Обраний клас додається до результату і видаляється з усіх списків. Якщо good head не знайдено, Python відмовляється створити клас.[^py314-howto-mro]

Приклад показує обидві властивості і конфлікт:

```python
class A:
    def who(self):
        return 'A'

class B:
    def who(self):
        return 'B'

class C(A, B):
    pass

print([k.__name__ for k in C.__mro__])  # ['C', 'A', 'B', 'object']
print(C().who())                        # A: the earlier base in the class statement wins

class D(C):
    pass

print([k.__name__ for k in D.__mro__])  # ['D', 'C', 'A', 'B', 'object']: A still precedes B

class X:
    pass

class Y:
    pass

class P(X, Y):
    pass

class Q(Y, X):
    pass

try:
    class R(P, Q):  # P needs X before Y, Q needs Y before X
        pass
except TypeError:
    print('class R cannot be created')  # the class statement fails
```

У `C(A, B)` порядок bases зберігається: `A` стоїть перед `B`, тож `C().who()` повертає `'A'`. Це local precedence ordering.[^py314-howto-mro] Для `D(C)` MRO – `D, C, A, B, object`, тобто пара «`A` перед `B`» переходить у MRO нащадка без змін. Це monotonicity: якщо X передує Y у MRO класу, то X передує Y і в MRO будь-якого його нащадка.[^py314-howto-mro]

Монотонність важлива, бо без неї створення нового підкласу могло б мовчки змінити, який метод знайде пошук. Конфлікт порядку видно вже під час визначення класу: `P(X, Y)` вимагає X перед Y, `Q(Y, X)` вимагає навпаки, а `R(P, Q)` не має узгодженого MRO, тому `class R` кидає `TypeError`.[^py314-howto-mro]

**Типові помилки:**
- плутати `__bases__` з `__mro__`: `__bases__` містить лише прямих батьків класу, а `__mro__` є повним порядком пошуку.[^py314-reference-datamodel]
- вважати, що `class C(A, B)` і `class C(B, A)` дають однаковий пошук: порядок bases є частиною правила, тож у другому варіанті методи спершу шукаються в `B`.
