---
id: py-framew-0001
title: "How does Pydantic runtime validation differ from static type checking?"
track: python
section: frameworks
sources:
  - source_id: py314-library-typing
    title: "Python 3.14: typing - Support for type hints"
    url: https://docs.python.org/3.14/library/typing.html#typing-support-for-type-hints
  - source_id: pep-0484
    title: "PEP 484: Type Hints"
    url: https://peps.python.org/pep-0484/
  - source_id: pydantic-models
    title: "Pydantic documentation: Models"
    url: https://pydantic.dev/docs/validation/latest/concepts/models/
  - source_id: pydantic-strict-mode
    title: "Pydantic documentation: Strict Mode"
    url: https://pydantic.dev/docs/validation/latest/concepts/strict_mode/
---

## Short answer

**A static type checker analyzes annotations offline, without running the program.**[^pep-0484] The Python runtime does not enforce function and variable annotations.[^py314-library-typing] Pydantic reads annotations when it validates untrusted input and returns a model whose fields conform to the declared types, or raises `ValidationError`.[^pydantic-models] In Pydantic v2, by default it coerces compatible values (`"42"` becomes `42`), and strict mode rejects that coercion.[^pydantic-strict-mode] Static checking finds inconsistencies before the program runs, while Pydantic validates data at runtime; neither replaces the other.

## Detailed explanation

A static type checker (for example mypy or pyright) reads the annotations in the source code and checks them offline, without running the program. PEP 484 describes annotations as data available at runtime through `__annotations__`, but with no type checking during execution: a separate off-line type checker does the checking.[^pep-0484] Python itself does not apply the annotations of functions and variables as type checks.[^py314-library-typing] So a function annotated `n: int` accepts a string without an error at run time:

```python
def double(n: int) -> int:
    return n * 2


print(double("ab"))  # prints abab; mypy reports the call as an error
```

Pydantic reads the same annotations at runtime. A model is a class that inherits from `BaseModel` and describes its fields as annotated attributes. During validation it returns an instance whose fields conform to the declared types, or it raises `ValidationError`.[^pydantic-models] The documentation clarifies the boundary: the guarantee covers the types of the result, not the input data. Untrusted data is passed into the model, and after validation its fields conform to the types.[^pydantic-models]

```python
from pydantic import BaseModel, ValidationError


class User(BaseModel):
    id: int
    name: str


print(User(id="42", name="Ann"))  # id=42 name='Ann'
try:
    User(id="abc", name="Ann")
except ValidationError:
    print("rejected")  # rejected
```

The limits depend on the mode. In Pydantic v2, by default it tries to convert a value to the required type when it can: `"42"` becomes `42`.[^pydantic-strict-mode] Strict mode rejects that conversion and raises an error if the data has the wrong type.[^pydantic-strict-mode] A static checker reports an error for `User(id="42", name="Ann")` written in the code (`str` instead of `int`), although lax mode in Pydantic v2 would accept the same input at runtime. So the checker evaluates the program text, while Pydantic evaluates the concrete value during execution.

Static checking and Pydantic complement each other. The checker finds inconsistencies in the code before the program runs. Pydantic stands at the boundary where data arrives from outside, for example from JSON, an HTTP request, or environment variables, and checks it at runtime. Neither replaces the other: the checker cannot see that external JSON contains `"abc"`, and Pydantic does not find a mistake in an internal call that never creates a model.

**Common mistakes:**
- assuming that `def f(x: int)` checks the type of the argument at call time;
- assuming that a Pydantic model checks all the internal code; it checks the data that enters the model;
- expecting `"42"` for an `int` field to be rejected without strict mode; in Pydantic v2 by default it becomes `42`.
