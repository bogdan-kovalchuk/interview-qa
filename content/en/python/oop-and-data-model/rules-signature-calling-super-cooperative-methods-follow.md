---
id: py-oop-0019
title: "What rules for the signature and calling of `super()` must cooperative methods follow in a multiple-inheritance hierarchy?"
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

**Per the documentation, cooperative methods should share one calling signature, because the call order is determined at run time.**[^py314-builtins-functions-super] Each class takes its own arguments from `kwargs` and passes the rest via `super().method(*args, **kwargs)`. The root passes nothing further: in CPython `object.__init__` rejects extra arguments when the type overrides `__init__` or does not override `__new__`. A method without `super()` ends the chain.

## Detailed explanation

The documentation explains why the signature should be the same: in a cooperative hierarchy the call order is determined at run time, it adapts to changes in the hierarchy, and it can include sibling classes that are not known in advance. So a method does not know which class comes next, and it must accept what the previous class passes on.[^py314-builtins-functions-super]

The practical form is `*args, **kwargs` in every method. A class takes its own keyword with `pop` and passes the rest on. The root of the chain, here `Root`, checks that no unconsumed arguments remain. `Named` and `Colored` know nothing about each other: `Item(Colored, Named)` fixes the order at run time, so `Colored` takes its keyword first and `Named` sees only what is left. Example:

```python
class Root:
    # Last class before object: it forwards nothing, because object takes no arguments.
    def __init__(self, *args, **kwargs):
        if args or kwargs:
            raise TypeError(f'unused arguments: {args}, {kwargs}')

class Named(Root):
    def __init__(self, *args, **kwargs):
        self.name = kwargs.pop('name')        # takes its own argument
        super().__init__(*args, **kwargs)     # passes the rest on

class Colored(Root):
    def __init__(self, *args, **kwargs):
        self.color = kwargs.pop('color', 'none')
        super().__init__(*args, **kwargs)

class Item(Colored, Named):
    pass

item = Item(name='box', color='red')
print(item.name, item.color)                  # box red
print([k.__name__ for k in Item.__mro__])     # ['Item', 'Colored', 'Named', 'Root', 'object']
# Named does not know that Colored ran first: it receives only what is left.
try:
    Named(name='box', color='red')
except TypeError as e:
    print('TypeError:', e)                    # Root receives the unconsumed color
```

If the root calls `super().__init__(**kwargs)` with a non-empty `kwargs`, CPython raises `TypeError`, because `object.__init__()` accepts only `self`. So `super().__init__()` without arguments is safe, while passing arguments to it is not.

A method without `super()` ends the chain: the classes after it in the MRO do not run. The class then has to do all the work that the following classes would have done.

**Common mistakes:**
- passing arguments that nobody consumed into `object` or the root of the chain: in CPython this raises `TypeError`;
- adding a required positional argument to the `__init__` of one class without updating the calls elsewhere in the chain;
- leaving out `super()` in a class because "I am the last one here": other classes may still follow it in the MRO.
