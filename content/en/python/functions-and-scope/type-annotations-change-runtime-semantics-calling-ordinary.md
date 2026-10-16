---
id: py-funcs-0023
title: "Do type annotations change the runtime semantics of calling an ordinary Python function, and does the interpreter check argument types automatically?"
track: python
section: functions-and-scope
sources:
  - source_id: py314-reference-compound-stmts-annotations
    title: "Python 3.14: Reference/compound Stmts"
    url: https://docs.python.org/3.14/reference/compound_stmts.html#annotations
  - source_id: py314-library-typing
    title: "Python 3.14: Library/typing"
    url: https://docs.python.org/3.14/library/typing.html
---

## Short answer

**No: by themselves, type annotations do not change the runtime semantics of a call, and the interpreter does not check argument types automatically.**[^py314-reference-compound-stmts-annotations] Annotations are metadata stored on the function and visible through `__annotations__`; they do not affect argument passing or checking at call time. Static checking is done by external tools such as mypy or pyright.[^py314-library-typing] Runtime checking is done by separate libraries or custom code. <span class="warn">Common mistake:</span> expecting automatic type checking as in statically typed languages; Python has none.

## Detailed explanation

The first part of the answer concerns what Python itself does. The language documentation says that annotations are conventionally used for type hints, but the language does not enforce them. Their presence does not change the runtime semantics of the code, except where some mechanism reads the annotations itself, such as dataclasses or `functools.singledispatch`.[^py314-reference-compound-stmts-annotations] So `a: int` is an entry in metadata, not a check on the value actually passed.

The symptom is easy to see in a short example:

```python
def add(a: int, b: int) -> int:
    return a + b

def scale(value: int, factor: float) -> int:
    return value * factor

print(add("1", "2"))                 # 12, two str values pass without TypeError
print(scale(3, 1.5))                 # 4.5, the int return annotation is not checked
print(add.__annotations__)           # {'a': <class 'int'>, 'b': <class 'int'>, 'return': <class 'int'>}
```

The function applies `+` to whatever it receives. `+` is defined for strings (concatenation), so no error occurs. The interpreter does not compare values with annotations: `scale` returns a `float` although the annotation promises `int`. These results are the same in Python 3.13 and 3.14; only the moment at which the annotations themselves are computed changes.

Checking is done by other tools. A type checker reads the annotations without running the program and can flag such a call before execution.[^py314-library-typing] Runtime checking is written explicitly, for example with `isinstance`, or taken from a separate library, but either way it is custom code rather than a language feature.

**Common mistakes:**
- expecting `a: int` to reject a string at call time: without a type checker the error appears only where the operation itself fails;
- assuming `-> int` guarantees the result type: `scale(3, 1.5)` returns `4.5`;
- building protection against wrong types on annotations alone: the check must be written explicitly or taken from a library.
