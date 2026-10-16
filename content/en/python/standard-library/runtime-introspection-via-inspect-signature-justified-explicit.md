---
id: py-stdlib-0017
title: "When is runtime introspection via `inspect.signature()` justified, and when does an explicit protocol reduce coupling to implementation details?"
track: python
section: standard-library
sources:
  - source_id: py314-library-functools
    title: "Python 3.14: Library/functools"
    url: https://docs.python.org/3.14/library/functools.html
  - source_id: py314-library-inspect-inspect-signature
    title: "Python 3.14: Library/inspect"
    url: https://docs.python.org/3.14/library/inspect.html#inspect.signature
  - source_id: py314-library-typing-protocol
    title: "Python 3.14: Library/typing (typing.Protocol)"
    url: https://docs.python.org/3.14/library/typing.html#typing.Protocol
---

## Short answer

**`inspect.signature()` is justified in generic tools (DI containers, decorators, wrappers) that must accept arbitrary callables without a known interface in advance.**[^py314-library-inspect-inspect-signature] When a component needs only a specific behaviour, an explicit `Protocol` states it in code, and a type checker verifies the implementations, so the dependency is on the contract rather than on the parameter names of one particular class.[^py314-library-typing-protocol] `signature()` reads the signature that the implementation declares, and raises `ValueError` when no signature can be provided.[^py314-library-inspect-inspect-signature]

## Detailed explanation

`inspect.signature(callable)` returns a `Signature` object with the parameter names, their default values and their annotations.[^py314-library-inspect-inspect-signature] This is introspection at run time: the code learns the signature while the program is already running. Such an approach fits code that cannot know the callable in advance. A DI container, for example, builds constructor arguments by name.

The price of this is a dependency on the implementation. The container below matches registry keys to parameter names. If a required parameter is renamed, the call fails with `TypeError`, but only when the program runs. If a parameter with a default is renamed, there is no error: the container silently passes the default, and the result is wrong (`('db', 8080)` instead of `('db', 5432)`). No static check sees this, because the registry is an ordinary `dict`.

```python
import inspect

class Server:
    def __init__(self, host: str, port: int = 8080):
        self.address = (host, port)

def build(factory, registry):
    # Runtime introspection: the container reads parameter names.
    params = inspect.signature(factory).parameters
    kwargs = {name: registry[name] for name in params if name in registry}
    return factory(**kwargs)

print(build(Server, {"host": "db", "port": 5432}).address)  # ('db', 5432)

class RenamedHost:  # required parameter renamed: the call fails
    def __init__(self, hostname: str, port: int = 8080):
        self.address = (hostname, port)

try:
    build(RenamedHost, {"host": "db", "port": 5432})
except TypeError as error:
    print(error)  # RenamedHost.__init__() missing 1 required positional argument: 'hostname'

class RenamedPort:  # defaulted parameter renamed: no error, the default is used silently
    def __init__(self, host: str, portnum: int = 8080):
        self.address = (host, portnum)

print(build(RenamedPort, {"host": "db", "port": 5432}).address)  # ('db', 8080)
```

An explicit protocol reduces this dependency. The consumer describes the behaviour it needs, and `typing.Protocol` lets a type checker verify that a class provides it, without explicit inheritance.[^py314-library-typing-protocol] The implementation can then change its internal details, and the consumer never reads its signature at run time. For application code where the interface is known in advance, this is usually the better boundary.

Introspection has limits of its own. `signature()` raises `ValueError` when no signature can be provided, and `TypeError` when the type of the object is not supported.[^py314-library-inspect-inspect-signature] As observed on CPython 3.13 and 3.14, `inspect.signature(dict)` and `inspect.signature(int)` raise `ValueError`: these builtin types have no signature. By default `signature()` follows the `__wrapped__` attribute, which `functools.wraps` adds,[^py314-library-functools] so a wrapper shows the signature of the original function. With `follow_wrapped=False` it shows the wrapper's own signature, `(*args, **kwargs)`.[^py314-library-inspect-inspect-signature]

The working rule: use introspection at a boundary where the type is truly unknown, and handle its errors. Where the interface is known in advance, an explicit Protocol or an ordinary annotated parameter makes the dependency visible and checked before the program runs.

**Common mistakes:**
- treating `signature()` as a contract rather than a snapshot of the current code: renaming a parameter changes the result without a warning;
- using `signature()` where the interface is known in advance, which adds a dependency on parameter names for no benefit;
- not handling `ValueError` and `TypeError` in a container that accepts arbitrary callables;
- wrapping a function without `functools.wraps`, which hides its real signature from introspection.
