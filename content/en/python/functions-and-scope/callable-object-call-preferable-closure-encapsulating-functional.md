---
id: py-funcs-0022
title: "When is a callable object with `__call__` preferable to a closure for encapsulating a functional component's state?"
track: python
section: functions-and-scope
sources:
  - source_id: py314-reference-datamodel-object-call
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html#object.__call__
  - source_id: py314-reference-datamodel-function-closure
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html#function.__closure__
  - source_id: py314-library-pickle-what-can-be-pickled
    title: "Python 3.14: Library/pickle"
    url: https://docs.python.org/3.14/library/pickle.html#what-can-be-pickled-and-unpickled
---

## Short answer

**A callable object with `__call__` is preferable when its state must be stored openly, tested, serialized, or extended with additional methods.**[^py314-reference-datamodel-object-call] A closure keeps its state in cell variables, which are not attributes and are reachable from outside only through `__closure__`. An instance of a class defined at module top level can be pickled if its data can be pickled, whereas a local closure cannot.[^py314-library-pickle-what-can-be-pickled] The class also provides named methods, such as `reset()`, and ordinary inheritance.

## Detailed explanation

Both options give a callable with state: a closure is an ordinary function that holds the variables of the enclosing function, and a callable object is an instance of a class with a `__call__` method. When Python runs `obj(...)`, it calls `type(obj).__call__(obj, ...)`.[^py314-reference-datamodel-object-call] So the call behaves the same way, and the difference lies in the tooling around the state: access to it, testing, storage and extension.

A closure is short and needs no class, but its state is not part of its interface. A counter with `nonlocal` keeps `count` in a cell, which is visible through `function.__closure__`.[^py314-reference-datamodel-function-closure] To add `reset()`, you would have to write a second function with `nonlocal` or return several closures, each of which is tested separately.

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

A callable object exposes its state as an attribute: a test checks `c.count` directly, and `reset()` is an ordinary method that other modules can call and a subclass can override. Serialization separates the two even more sharply. `pickle` stores functions and classes by name, so they must be reachable from the module top level, while an instance stores only its own data.[^py314-library-pickle-what-can-be-pickled] The local `counter` has no such name, and `pickle.dumps(f)` fails: with `AttributeError` in 3.13 and `PicklingError` in 3.14.

A closure suits short internal state that nobody outside should read. A callable object suits state that must be inspected, tested, stored or extended with a set of methods.

**Common mistakes:**
- treating a closure as fully encapsulated: its state is visible through `__closure__`, so this only hides it from ordinary code;
- writing a class with `__call__` but no methods or attributes, which gives no advantage over a function;
- keeping a lambda or a local function in an attribute and then failing to pickle, even though the class itself is defined at module top level.
