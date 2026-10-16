---
id: py-prac-0004
title: "In Python 3.14, what does `print(x)` print after a `match 1:` block with `case x: pass`, and how does the capture pattern affect the name's scope?"
track: python
section: practical-coding
sources:
  - source_id: py314-tutorial
    title: "Python 3.14: Tutorial"
    url: https://docs.python.org/3.14/tutorial/
  - source_id: py314-reference
    title: "Python 3.14: Reference"
    url: https://docs.python.org/3.14/reference/
  - source_id: py314-reference-compound-stmts
    title: "Python 3.14: Reference/compound Stmts"
    url: https://docs.python.org/3.14/reference/compound_stmts.html#the-match-statement
  - source_id: py314-reference-executionmodel
    title: "Python 3.14: Reference/executionmodel"
    url: https://docs.python.org/3.14/reference/executionmodel.html#naming-and-binding
---

## Short answer

**It prints `1`: a bare name in `case` is a capture pattern that binds the subject to the name `x`.**[^py314-reference-compound-stmts] Like `if` and `for`, `match` does not create a block with its own scope: `x` becomes an ordinary name in the current scope and stays bound after the `match`.[^py314-reference-executionmodel] <span class="warn">To compare against a named constant, use a dotted name such as `case Color.RED`; a bare name, other than `_`, is always a capture.[^py314-reference-compound-stmts]</span>

## Detailed explanation

`match` compares the subject with the `case` patterns in turn. A bare name is a capture pattern: it always matches and binds the subject to the name.[^py314-reference-compound-stmts] So in `match 1` with `case x:`, the name `x` gets the value `1`, even though no comparison takes place. The `pass` block does nothing, but the binding has already happened:

```python
match 1:
    case x:
        pass
print(x)  # 1: x is a module-level name, still bound after the match
```

A binding does not check existing values. If `LIMIT` already has a value, `case LIMIT:` rebinds it instead of comparing with it:

```python
LIMIT = 10
match 42:
    case LIMIT:  # capture pattern: always matches and rebinds LIMIT
        print("matched")  # matched
print(LIMIT)  # 42


class Color:
    RED = 1


match 2:
    case Color.RED:  # value pattern: compares 2 == Color.RED
        print("red")
    case _:
        print("other")  # other
```

To compare with a named value, use a dotted name (a value pattern): it matches when the value equals the subject using the `==` operator.[^py314-reference-compound-stmts] The single underscore `_` does not bind a name either, so it cannot be read after the `match`.[^py314-reference-compound-stmts]

`match` is not a block in the language's sense. The blocks are a module, a function body and a class definition, so `match` does not create a new scope.[^py314-reference-executionmodel] A name bound by a `case` inside a function becomes a local variable of the nearest enclosing function, unless a `global` or `nonlocal` statement applies.[^py314-reference-compound-stmts]

**Common mistakes:**
- writing `case RED:` for a constant `RED` and expecting a comparison instead of a binding;
- assuming that `case x:` does not change an `x` that already exists;
- assuming that `_` binds a value that can be read after the `match`.
