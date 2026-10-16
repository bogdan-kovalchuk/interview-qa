---
id: py-oop-0017
title: "Why does zero-argument `super()` mean \"the next one in the MRO\" rather than simply \"the immediate parent class\"?"
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

**Zero-argument `super()` takes the enclosing class and the method's first argument (usually `self`), then searches the `__mro__` of the object's actual type for the next class, not the parent of the class where `super()` is written.**[^py314-builtins-functions-super] This matters in the diamond `D(B, C)` with `B(A)` and `C(A)`: when the object's type is `D`, `super()` in `B` passes control to `C`, not `A`. Writing `super()` does not fix a parent; the order is determined at run time.

## Detailed explanation

Zero-argument `super()` works only inside an ordinary method of a class. The compiler fills in two values: `type`, the class in which the method is written, and `obj`, the first argument of the function, usually `self`.[^py314-builtins-functions-super] Because of this, `super()` inside a nested function does not work as expected.[^py314-builtins-functions-super]

The key question is what "next" means. The documentation defines the order this way: `object_or_type` determines whose `__mro__` is searched, and the search starts from the class right after `type`. For the MRO `D, B, C, A, object` with `type` equal to `B`, the search continues through `C, A, object`.[^py314-builtins-functions-super] So the next class for `super()` in `B` depends on the object's actual type: it is `C` for `D()` and `A` for `B()`.

In the example, `B` calls `super().hello()`. For `D()` the next class is `C`, and for `B()` it is `A`:

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

This is how cooperative methods and mixins work: each class calls `super()` without knowing what comes next. If `super()` meant "the parent", then `D().hello()` would never call `C.hello`. So `super()` should be read as "the next class in the MRO of the object's actual type", not as "the base class".[^py314-builtins-functions-super]

**Common mistakes:**
- writing `A.hello(self)` instead of `super().hello()` in `B`: for `D()` that call skips `C`;
- assuming `super()` always calls the parent named in `class B(A)`;
- calling `super()` inside a nested function or generator expression and expecting it to know the method's class.[^py314-builtins-functions-super]
