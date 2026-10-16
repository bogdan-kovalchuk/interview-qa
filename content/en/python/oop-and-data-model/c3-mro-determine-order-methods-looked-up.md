---
id: py-oop-0016
title: "How does C3 MRO determine the order in which methods are looked up under multiple inheritance, and what ordering property does it preserve?"
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

**C3 builds the linearization `L[C] = C + merge(L[B₁], …, L[Bₙ], B₁, …, Bₙ)`, preserving local precedence order (the order of bases in `class C(A, B)`) and monotonicity (the order in a class's MRO is kept in the MRO of each of its subclasses).**[^py314-howto-mro] At each step, merge takes the first good head: scanning the lists left to right, the first head that appears in no list's tail. If there is no good head, class creation fails with `TypeError`.[^py314-howto-mro] Attribute lookup through the base classes follows this order.[^py314-reference-datamodel]

## Detailed explanation

In multiple inheritance, attribute lookup visits the classes in the order given by `__mro__`. This tuple is computed when the class is created: `type.mro()` is called at class creation, and its result is stored in `__mro__`. For ordinary classes, C3 is what builds this order.[^py314-reference-datamodel]

The linearization is defined recursively as `L[C(B₁…Bₙ)] = C + merge(L[B₁], …, L[Bₙ], B₁, …, Bₙ)`. Merge takes the head of the first list if it does not appear in the tail of any other list (a good head). Otherwise it tries the head of the next list. The chosen class is added to the result and removed from all lists. If no good head can be found, Python refuses to create the class.[^py314-howto-mro]

The example below shows both properties and a conflict:

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

In `C(A, B)` the order of bases is kept: `A` comes before `B`, so `C().who()` returns `'A'`. This is local precedence ordering.[^py314-howto-mro] For `D(C)` the MRO is `D, C, A, B, object`, so the pair "`A` before `B`" carries over unchanged into the subclass's MRO. This is monotonicity: if X precedes Y in a class's MRO, then X precedes Y in the MRO of every subclass.[^py314-howto-mro]

Monotonicity matters because without it, creating a new subclass could silently change which method the lookup finds. Order conflicts show up when the class is defined: `P(X, Y)` requires X before Y, `Q(Y, X)` requires the reverse, and `R(P, Q)` has no consistent MRO, so `class R` raises `TypeError`.[^py314-howto-mro]

**Common mistakes:**
- confusing `__bases__` with `__mro__`: `__bases__` holds only the direct bases of a class, while `__mro__` is the full lookup order.[^py314-reference-datamodel]
- assuming `class C(A, B)` and `class C(B, A)` give the same method lookup: the order of bases is part of the rule, so in the second version methods are looked up in `B` first.
