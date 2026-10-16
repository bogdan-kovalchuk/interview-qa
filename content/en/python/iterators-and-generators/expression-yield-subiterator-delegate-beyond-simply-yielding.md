---
id: py-itergen-0009
title: "What does the expression `yield from subiterator` delegate beyond simply re-yielding each value?"
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
  - source_id: pep-0380-yield-from
    title: "PEP 380: Syntax for Delegating to a Subgenerator"
    url: https://peps.python.org/pep-0380/
---

## Short answer

**`yield from` passes values sent with `send()` and exceptions thrown with `throw()` on to the subiterator, if it supports them.**[^py314-reference-expressions-yield-expressions] If the subiterator lacks the needed method, `send()` raises `AttributeError` or `TypeError`, and `throw()` raises the passed exception immediately.[^py314-reference-expressions-yield-expressions] When the subiterator finishes, its `StopIteration.value` becomes the result of the `yield from` expression itself.[^py314-reference-expressions-yield-expressions] `close()` on the delegating generator is also passed to the subiterator if it has that method.[^pep-0380-yield-from]

## Detailed explanation

`yield from` is not equivalent to `for v in sub: yield v`. The loop passes only values outward. `yield from` makes the delegating generator transparent: `send()` and `throw()` go directly to the subiterator, and its `return` value becomes the value of the expression itself.[^py314-reference-expressions-yield-expressions] The delegation protocol is specified in PEP 380, which also says that `close()` is passed to the subiterator if it has that method.[^pep-0380-yield-from]

Example: `outer()` delegates to `sub()`. A value sent with `send()` reaches `sub`, an exception thrown with `throw()` is caught by `sub`, and `return "done"` becomes the result of `yield from`. Next, an ordinary `for` loop over a new `sub()` call shows that `send()` does not reach it:

```python
def sub():
    try:
        received = yield "ready"       # send() value arrives here
        yield f"got {received}"
        return "done"                  # becomes the value of the yield from expression
    except ValueError as exc:          # throw() reaches the subiterator
        yield f"sub caught {exc}"

def outer():
    result = yield from sub()
    print("yield from returned:", result)
    yield "outer finished"

g = outer()
print(next(g))                         # ready
print(g.send("A"))                     # got A
print(next(g))                         # yield from returned: done, then outer finished

h = outer()
print(next(h))                         # ready
print(h.throw(ValueError("boom")))     # sub caught boom

def plain_loop():
    for value in sub():                # the for loop calls next(), never send()
        yield value

k = plain_loop()
print(next(k))                         # ready
print(k.send("B"))                     # got None: "B" is not forwarded
```

If the subiterator is an ordinary iterator without `send()`, such as a `list_iterator`, then `send()` with a non-None value raises `AttributeError` or `TypeError`, and `throw()` raises the passed exception right at the `yield from` point.[^py314-reference-expressions-yield-expressions]

**Common mistakes:**
- replacing `yield from` with `for ... yield` and then expecting `send()` to reach the subiterator;
- thinking that a `return` in a subgenerator is yielded as an item; it is actually the result of `yield from`;
- sending a non-None value to a subiterator that has no `send()`, such as a `list_iterator`.
