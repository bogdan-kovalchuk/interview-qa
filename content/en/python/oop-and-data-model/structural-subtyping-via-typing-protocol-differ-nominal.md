---
id: py-oop-0026
title: "How does structural subtyping via `typing.Protocol` differ from nominal inheritance via an ABC?"
description: "A Protocol checks structure: a class qualifies if it has the required methods, without inheritance; an ABC declares membership explicitly through inheritance, register() or __subclasshook__."
track: python
section: oop-and-data-model
level: middle
type: comparison
tags: [typing-protocol]
status: published
updated: 2026-10-13
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
  - source_id: py314-howto-descriptor
    title: "Python 3.14: Howto/descriptor"
    url: https://docs.python.org/3.14/howto/descriptor.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-howto-mro
    title: "Python 3.14: Howto/mro"
    url: https://docs.python.org/3.14/howto/mro.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-library-dataclasses
    title: "Python 3.14: Library/dataclasses"
    url: https://docs.python.org/3.14/library/dataclasses.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-library-typing-nominal-vs-structural-subtyping
    title: "Python 3.14: Library/typing (Nominal vs structural subtyping)"
    url: https://docs.python.org/3.14/library/typing.html#nominal-vs-structural-subtyping
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation: definitions of nominal and structural subtyping for static type checkers. Does not describe runtime isinstance behaviour."
  - source_id: py314-library-typing-protocol
    title: "Python 3.14: Library/typing (typing.Protocol)"
    url: https://docs.python.org/3.14/library/typing.html#typing.Protocol
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation: the Protocol class and the requirement of @runtime_checkable for isinstance and issubclass."
  - source_id: py314-library-typing-runtime-checkable
    title: "Python 3.14: Library/typing (typing.runtime_checkable)"
    url: https://docs.python.org/3.14/library/typing.html#typing.runtime_checkable
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation: @runtime_checkable checks only the presence of attributes, not signatures or types; isinstance with such a protocol can be slow."
  - source_id: py314-library-abc-abcmeta-register
    title: "Python 3.14: Library/abc (ABCMeta.register)"
    url: https://docs.python.org/3.14/library/abc.html#abc.ABCMeta.register
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation: register() makes a class a virtual subclass of an ABC; the ABC does not appear in its MRO and its methods are not callable via super()."
  - source_id: py314-library-abc-abcmeta-subclasshook
    title: "Python 3.14: Library/abc (ABCMeta.__subclasshook__)"
    url: https://docs.python.org/3.14/library/abc.html#abc.ABCMeta.__subclasshook__
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation: __subclasshook__ as a way for an ABC to decide subclass membership without register()."
---

## Short answer

**`Protocol` uses structural subtyping: a class matches it if it has methods with compatible signatures, without explicit inheritance.**[^py314-library-typing-nominal-vs-structural-subtyping] `isinstance` accepts a `Protocol` only when it is decorated with `@runtime_checkable`[^py314-library-typing-protocol] and then checks only that the attributes are present, not their types.[^py314-library-typing-runtime-checkable] An ABC is nominal by default: the ABC itself decides membership through explicit inheritance or `register()`.[^py314-library-abc-abcmeta-register] But an ABC with `__subclasshook__`, such as `collections.abc.Iterable`, checks structure at run time.[^py314-library-abc-abcmeta-subclasshook]

## Detailed explanation

The difference lies in who decides that a class belongs to a type. By default the ABC itself declares membership: the class must explicitly inherit from it or be registered. Structural subtyping, on which `Protocol` is built, requires no link between the classes: a static type checker verifies that the class has methods with compatible signatures, and the class itself declares nothing.[^py314-library-typing-nominal-vs-structural-subtyping]

At run time the behaviour is different. `isinstance()` accepts a `Protocol` only when it is marked `@runtime_checkable`; without the decorator such a check raises `TypeError`.[^py314-library-typing-protocol] The decorator makes the check coarse: it sees only that attributes and methods exist and ignores their signatures.[^py314-library-typing-runtime-checkable] The next example shows that a class whose `close` has a different signature still passes the check:

```python
from typing import Protocol, runtime_checkable


@runtime_checkable
class Closable(Protocol):
    def close(self) -> None: ...


class LogFile:  # no base class: only the method matters
    def close(self) -> None:
        pass


class Socket:
    def close(self, force: bool) -> None:  # different signature
        pass


print(isinstance(LogFile(), Closable))  # True
print(isinstance(Socket(), Closable))   # True: the runtime check ignores signatures
```

Registration with `register()` works differently: the class is recorded as a virtual subclass of the ABC, with no structural check. After that `isinstance()` and `issubclass()` treat it as a subclass, but the ABC does not appear in that class's MRO, and its methods are not callable even via `super()`.[^py314-library-abc-abcmeta-register] The `__subclasshook__` method offers another way: the ABC itself decides whether to treat a class as a subclass, for example by looking for a method in the class's `__dict__`.[^py314-library-abc-abcmeta-subclasshook]

In practice `Protocol` is convenient when you describe the expected behaviour of foreign objects and a static check is enough. An ABC fits when the shared implementation lives in a base class, or when membership must be explicit, as in plugins that register themselves.

**Common mistakes:**
- assuming that `isinstance()` with a `@runtime_checkable` Protocol checks signatures or types, not only that attributes exist;
- assuming that `register()` adds the ABC to the MRO or copies its methods into the class;
- calling `isinstance()` with a `Protocol` that is not marked `@runtime_checkable`: this raises `TypeError`.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
