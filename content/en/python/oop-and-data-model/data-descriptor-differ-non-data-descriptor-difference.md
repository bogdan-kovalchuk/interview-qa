---
id: py-oop-0009
title: "How does a data descriptor differ from a non-data descriptor, and how does that difference change precedence during attribute lookup?"
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
  - source_id: py314-reference-datamodel-invoking-descriptors
    title: "Python 3.14: Reference/datamodel, Invoking Descriptors"
    url: https://docs.python.org/3.14/reference/datamodel.html#invoking-descriptors
  - source_id: py314-reference-datamodel-implementing-descriptors
    title: "Python 3.14: Reference/datamodel, Implementing Descriptors"
    url: https://docs.python.org/3.14/reference/datamodel.html#implementing-descriptors
---

## Short answer

**A data descriptor defines `__set__` and/or `__delete__` (together with `__get__` it overrides the instance `__dict__` on read); a non-data descriptor defines only `__get__` and yields to the instance `__dict__`.**[^py314-reference-datamodel-invoking-descriptors] A descriptor with only `__set__` and no `__get__` does not override the dictionary on read. An example of a data descriptor is `property`; an example of a non-data descriptor is an ordinary method. So `obj.method = 42` overwrites the method for that instance, while `obj.prop = 42` calls the property setter (without a setter it raises `AttributeError`).

## Detailed explanation

A descriptor is an object that defines at least one of the methods `__get__`, `__set__`, `__delete__`. It becomes a data descriptor if it defines `__set__` or `__delete__`; if it defines only `__get__`, it is a non-data descriptor.[^py314-reference-datamodel-invoking-descriptors] The word "data" refers to the presence of these methods, not to whether the object stores data. A descriptor takes effect only when it is in the dictionary of the class or of one of its base classes, so a descriptor written into an instance's `__dict__` is not called.[^py314-reference-datamodel-implementing-descriptors]

During `obj.x`, Python finds `x` in the class. If the object found defines `__get__` and `__set__` or `__delete__` (a data descriptor), its `__get__` is called, and the instance dictionary is not read. Otherwise the instance dictionary is checked: if it contains `x`, that value is returned. Only if the dictionary has no `x` is the `__get__` of a non-data descriptor called.[^py314-reference-datamodel-invoking-descriptors] So the instance dictionary overrides a non-data descriptor, but not a data descriptor.

An example with two descriptors and the same value in the instance dictionary:

```python
class DataDesc:
    def __get__(self, obj, objtype=None):
        return 'data __get__'
    def __set__(self, obj, value):
        print('data __set__ called')

class NonDataDesc:
    def __get__(self, obj, objtype=None):
        return 'non-data __get__'

class C:
    d = DataDesc()
    n = NonDataDesc()

c = C()
vars(c)['d'] = 'in dict'
vars(c)['n'] = 'in dict'
print(c.d)      # data __get__: the data descriptor wins over the instance dict
print(c.n)      # in dict: the instance dict wins over the non-data descriptor
c.d = 1         # data __set__ called: assignment goes to __set__, not to the dict
print(vars(c))  # {'d': 'in dict', 'n': 'in dict'}
```

An ordinary method is a non-data descriptor, so it can be overridden for a single instance:

```python
class Greeter:
    def hello(self):
        return 'method'

g = Greeter()
g.hello = lambda: 'instance'     # a function is a non-data descriptor, so the dict entry wins
print(g.hello())                 # instance
print(Greeter().hello())         # method
```

**Common mistakes:**
- thinking that "data" means "stores data": the name is determined by the presence of `__set__` or `__delete__`;
- expecting `obj.prop = 42` to always work: for a property without a setter, assignment raises `AttributeError`;
- storing a descriptor as an instance attribute (`obj.d = Desc()`) instead of in the class: Python will not call it.
