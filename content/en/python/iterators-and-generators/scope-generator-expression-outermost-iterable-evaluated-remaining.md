---
id: py-itergen-0017
title: "In what scope is a generator expression's outermost iterable evaluated, and when are its remaining clauses evaluated?"
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
  - source_id: py314-reference-expressions-generator-expressions
    title: "Python 3.14: Reference/expressions"
    url: https://docs.python.org/3.14/reference/expressions.html#generator-expressions
  - source_id: py314-reference-expressions-displays-for-lists-sets-and-dictionaries
    title: "Python 3.14: Reference/expressions"
    url: https://docs.python.org/3.14/reference/expressions.html#displays-for-lists-sets-and-dictionaries
  - source_id: py314-reference-executionmodel-resolution-of-names
    title: "Python 3.14: Reference/executionmodel"
    url: https://docs.python.org/3.14/reference/executionmodel.html#resolution-of-names
---

## Short answer

**The outermost iterable is evaluated immediately in the enclosing scope; all other expressions (the output expression and the following `for` and `if` clauses) are evaluated lazily in an implicitly nested scope.**[^py314-reference-expressions-generator-expressions] So a `NameError` or `TypeError` for the outermost iterable is raised when the generator expression is created, while errors in the inner expressions appear only during iteration. Target-list variables do not leak into the enclosing scope.[^py314-reference-expressions-displays-for-lists-sets-and-dictionaries]

## Detailed explanation

A generator expression has two moments: creation and execution. At creation, Python evaluates the outermost iterable in the enclosing scope and passes it as an argument to the implicitly nested scope. The remaining expressions, that is the output expression and the following `for` and `if` clauses, run later.[^py314-reference-expressions-displays-for-lists-sets-and-dictionaries] These expressions are evaluated lazily, as in an ordinary generator, meaning when the iterator is asked for a value.[^py314-reference-expressions-generator-expressions] So `(x for x in 5)` fails at once with a `TypeError`, while an error in the output expression appears only at the first `next()`.

The consequences are easiest to see in a class body, because there the scope of class-level names is limited. The outermost iterable sees the class-level names, but the output expression does not, because the scope of names defined in a class block does not extend to generator expressions.[^py314-reference-executionmodel-resolution-of-names] In the example below, `ok` works because `names` is evaluated in the class scope, while `gen` fails only during iteration:

```python
class Config:
    names = ['a', 'b']
    prefix = '>'
    ok = [n for n in names]              # outermost iterable: class scope, works
    gen = (prefix + n for n in names)    # prefix is looked up in the nested scope

g = Config.gen                           # no error yet: creation succeeded
# next(g)                                # NameError: name 'prefix' is not defined
# (x for x in 5)                         # TypeError at creation: 'int' object is not iterable
```

Names from the target list do not leak into the enclosing scope: after a generator expression, the name `x` does not exist in the outer scope.[^py314-reference-expressions-displays-for-lists-sets-and-dictionaries]

**Common mistakes:**
- assuming that an error in the output expression appears at once, when the generator expression is created;
- referring in a class body to a class-level name from the output expression and expecting it to be found: the NameError appears during iteration;
- looking for the target-list variable after a generator expression: it does not leak into the outer scope.
