---
id: py-objtypes-0020
title: "Does a type annotation change an object's actual runtime type, or automatically forbid assigning a value of a different type?"
description: "Does a type annotation change an object's actual runtime type, or automatically forbid assigning a value of a different type?"
track: python
section: objects-and-types
level: middle
type: pitfall
tags: []
status: published
updated: 2026-09-27
content_revision: 2
reconciled_with:
  uk: 2
anki:
  export: true
sources:
  - source_id: py314-reference-datamodel
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-library-stdtypes
    title: "Python 3.14: Library/stdtypes"
    url: https://docs.python.org/3.14/library/stdtypes.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-library-copy
    title: "Python 3.14: Library/copy"
    url: https://docs.python.org/3.14/library/copy.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-library-typing
    title: "Python 3.14: Library/typing"
    url: https://docs.python.org/3.14/library/typing.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
---

## Short answer

**No, a type annotation does not change an object's actual runtime type and does not prevent assigning a value of a different type – the Python runtime ignores annotations during execution.**[^py314-reference-datamodel] Annotations are stored in `__annotations__` and inspected via `typing.get_type_hints()`, but the interpreter performs no enforcement. Type checking is delegated entirely to external tools: static type checkers (mypy, pyright), IDEs, and linters. <span class="warn">Writing `x: int = 'hello'` is completely valid Python code that executes without runtime errors.</span>

## Detailed explanation

Type annotations in Python are purely syntactic metadata that have zero runtime impact on variable binding, object types, or execution flow.[^py314-reference-datamodel]

Python remains a dynamically typed language by design. When CPython compiles source code into bytecode, it emits no instructions for type validation or type coercion. Variable annotations in local scopes (inside functions) are discarded entirely after bytecode generation, while annotations on modules, classes, and function signatures are merely stored as metadata in `__annotations__` dictionaries (or evaluated lazily in Python 3.14 via PEP 649 / PEP 749). Consequently, an annotation neither converts a value to the target type nor raises an exception when an incompatible value is assigned.[^py314-library-typing]

The responsibility for type checking is delegated entirely to a static analysis phase performed before runtime by external tools such as `mypy` or `pyright`. At runtime, Python relies exclusively on dynamic typing and duck typing: objects define their own types (`type(obj)`), and operations succeed as long as the object supports the requested attribute or method at that moment. Runtime type enforcement only occurs if explicitly implemented in application code (such as via `isinstance()` checks) or through libraries that inspect annotations dynamically, such as Pydantic, Beartype, or Typeguard.

Example of runtime annotation ignorance by the Python interpreter:

```python
import typing

# Runtime ignores mismatched annotations completely
number: int = "not an integer"
print(type(number))  # <class 'str'>
print(number.upper())  # NOT AN INTEGER

def add_numbers(a: int, b: int) -> int:
    return a + b

# Dynamic dispatch works according to actual argument types at runtime
result = add_numbers("hello ", "world")
print(result)  # hello world
print(type(result))  # <class 'str'>

# Annotations are stored purely as metadata on functions
hints = typing.get_type_hints(add_numbers)
print(hints)  # {'a': <class 'int'>, 'b': <class 'int'>, 'return': <class 'int'>}
```

**Common pitfalls and misconceptions regarding type annotations:**
- expecting automatic type casting: assuming `age: int = "25"` coerces the string into integer `25`, whereas the variable remains a `str`;
- false sense of security without CI: writing type hints without enforcing a static type checker (`mypy`, `pyright`) in CI/CD leaves production code unprotected against type mismatches;
- validating external inputs: assuming standard annotations validate incoming JSON or HTTP request payloads without dedicated libraries (such as Pydantic or attrs);
- absence of local annotations in metadata: annotations on local variables inside function bodies are completely discarded after bytecode generation and do not exist in `__annotations__`.

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
