---
id: py-itergen-0012
title: "How do `throw()` and `close()` affect control flow inside a suspended generator?"
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
  - source_id: py314-reference-expressions-generator-iterator-methods
    title: "Python 3.14: Reference/expressions"
    url: https://docs.python.org/3.14/reference/expressions.html#generator-iterator-methods
---

## Short answer

**`throw()` raises the given exception at the point of the paused `yield`, and `close()` raises `GeneratorExit` there.**[^py314-reference-expressions-generator-iterator-methods] If the generator catches the exception in a `try/except` around the `yield`, it can continue and yield the next value, which `throw()` returns. If an exception passed to `throw()` is not handled, it propagates to the caller. <span class="warn">If the generator yields again after `GeneratorExit`, `close()` raises `RuntimeError`.</span>[^py314-reference-expressions-generator-iterator-methods]

## Detailed explanation

A paused generator stops at a `yield`. `next()` and `send()` resume it in the usual way, passing a value into that expression. `throw()` and `close()` resume it differently: they raise an exception at the `yield`, so a `try`, `except` or `finally` around that `yield` runs as if that expression itself had raised the exception.[^py314-reference-expressions-generator-iterator-methods]

The `throw()` example: the generator catches the exception, yields a new value, and `throw()` returns that value. The comments show the output on CPython 3.13 and 3.14:

```python
def catcher():
    try:
        yield 1                     # suspended here
    except ValueError as error:
        print('caught', repr(error))
        yield 'after catch'         # throw() returns this value
    yield 'end'

g = catcher()
print(next(g))                      # 1
print(g.throw(ValueError('boom')))  # caught ValueError('boom'), then after catch
print(next(g))                      # end
```

If the exception is not caught, `throw()` does not swallow it: the exception propagates to the caller, and the generator is finished afterwards. `close()` works differently: it raises `GeneratorExit`, which the generator may choose not to catch. A `finally` around the `yield` runs both for `close()` and for an uncaught `throw()`.[^py314-reference-expressions-generator-iterator-methods]

The `close()` example shows `finally`. In CPython, if the generator has not started yet, `close()` does not run its body:

```python
def resource():
    print('open')
    try:
        yield 1
    finally:
        print('cleanup')            # runs when the paused generator is closed

g = resource()
next(g)                             # open
g.close()                           # cleanup
g2 = resource()
g2.close()                          # prints nothing: the body never started
```

If the generator returns a value in response to `GeneratorExit`, then from Python 3.13 on `close()` returns that value. If the generator yields again after `GeneratorExit`, `close()` raises `RuntimeError`.[^py314-reference-expressions-generator-iterator-methods]

**Common mistakes:**
- thinking that `close()` only "closes" the generator: it raises `GeneratorExit` at the paused `yield`, so `finally` runs;
- yielding again after `GeneratorExit`: `close()` then raises `RuntimeError`;
- expecting `throw()` always to return a value: if the generator does not catch the exception or finishes without yielding again, the exception propagates or `StopIteration` is raised.
