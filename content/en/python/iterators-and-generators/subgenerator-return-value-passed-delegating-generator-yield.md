---
id: py-itergen-0010
title: "How is a subgenerator's `return` value passed to the delegating generator through `yield from`?"
track: python
section: iterators-and-generators
sources:
  - source_id: py314-library-stdtypes-iterator-types
    title: "Python 3.14: Library/stdtypes"
    url: https://docs.python.org/3.14/library/stdtypes.html#iterator-types
  - source_id: py314-reference-expressions-yield-expressions
    title: "Python 3.14: Reference/expressions"
    url: https://docs.python.org/3.14/reference/expressions.html#yield-expressions
  - source_id: py314-reference-datamodel-object-iter
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html#object.__iter__
  - source_id: py314-library-exceptions-stopiteration
    title: "Python 3.14: Library/exceptions"
    url: https://docs.python.org/3.14/library/exceptions.html#StopIteration
---

## Short answer

**A `return value` in a subgenerator sets `StopIteration.value`, and `yield from` takes that value as its own result.**[^py314-library-exceptions-stopiteration] When the subgenerator executes `return value`, it finishes and raises `StopIteration` with `value` equal to that value. The `yield from` expression takes this value and uses it as its own result, which can be assigned to a variable in the delegating generator.[^py314-reference-expressions-yield-expressions]

## Detailed explanation

The `yield from` expression delegates execution to a subgenerator: the values it yields with `yield` are passed on to the calling code unchanged. A value that the subgenerator returns with `return` is not passed on as an ordinary yielded value. When the body finishes, Python raises `StopIteration`, and the returned value is stored in its `value` attribute.[^py314-library-exceptions-stopiteration] Once the subiterator has finished, this value becomes the result of the `yield from` expression, so `result = yield from sub()` assigns to `result` exactly what `sub` returned with `return`.[^py314-reference-expressions-yield-expressions]

`sub` yields two values and returns `'done'`. `delegating` receives that value through `yield from` and returns its own value:

```python
def sub():
    yield 1
    yield 2
    return 'done'                   # becomes StopIteration.value

def delegating():
    result = yield from sub()       # result is 'done' after sub() finishes
    print('sub returned:', result)
    return result.upper()           # the value of delegating's own StopIteration

g = delegating()
print(next(g))                      # 1
print(next(g))                      # 2
try:
    next(g)                         # prints 'sub returned: done'
except StopIteration as stop:
    print('value:', stop.value)     # value: DONE
```

The first two `next()` calls return `1` and `2`. The third `next()` finishes `sub`: `yield from` receives `'done'`, `sub returned: done` is printed, and `delegating` finishes with its own `return`. Its `StopIteration.value` is `'DONE'`, because `delegating` returned that value, not `sub`.

The conditions matter. If the subgenerator has no `return`, or returns without a value, the result of `yield from` is `None`. The automatic transfer applies when the subiterator is a generator.[^py314-reference-expressions-yield-expressions] For an iterator that is not a generator, the value comes only from an explicitly set `StopIteration(value)`; otherwise `value` is `None`.[^py314-reference-expressions-yield-expressions][^py314-library-exceptions-stopiteration] So an iterator class that itself raises `StopIteration('explicit')` makes `yield from` evaluate to `'explicit'`.

**Common mistakes:**
- expecting a `return` to become an ordinary value for `next()` or a `for` loop: `return` is visible only as `StopIteration.value` or through `yield from`;
- assuming that `yield from` without a `return` gives a meaningful result: it is `None`;
- expecting a `value` from an iterator that is not a generator without an explicit `StopIteration(value)`.
