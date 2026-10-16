---
id: py-fileio-0013
title: "Why can't `pickle.loads()` be called on untrusted data, even after checking the expected object type?"
track: python
section: files-and-io
sources:
  - source_id: py314-library-io
    title: "Python 3.14: Library/io"
    url: https://docs.python.org/3.14/library/io.html
  - source_id: py314-library-pathlib
    title: "Python 3.14: Library/pathlib"
    url: https://docs.python.org/3.14/library/pathlib.html
  - source_id: py314-library-json
    title: "Python 3.14: Library/json"
    url: https://docs.python.org/3.14/library/json.html
  - source_id: py314-library-pickle
    title: "Python 3.14: Library/pickle"
    url: https://docs.python.org/3.14/library/pickle.html
  - source_id: py314-library-os-os-fsync
    title: "Python 3.14: Library/os"
    url: https://docs.python.org/3.14/library/os.html#os.fsync
  - source_id: py314-library-os-os-replace
    title: "Python 3.14: Library/os"
    url: https://docs.python.org/3.14/library/os.html#os.replace
  - source_id: py314-library-tempfile
    title: "Python 3.14: Library/tempfile"
    url: https://docs.python.org/3.14/library/tempfile.html
  - source_id: py314-library-pickle-restricting-globals
    title: "Python 3.14: Library/pickle (Restricting Globals)"
    url: https://docs.python.org/3.14/library/pickle.html#pickle-restrict
  - source_id: py314-library-pickle-object-reduce
    title: "Python 3.14: Library/pickle (object.__reduce__)"
    url: https://docs.python.org/3.14/library/pickle.html#object.__reduce__
  - source_id: py314-library-pickle-find-class
    title: "Python 3.14: Library/pickle (Unpickler.find_class)"
    url: https://docs.python.org/3.14/library/pickle.html#pickle.Unpickler.find_class
---

## Short answer

**`pickle.loads()` can run arbitrary code while it restores an object, so checking the type of the result comes too late.**[^py314-library-pickle] A pickle stream can import any function or class and call it with arguments, for example `os.system`, and a class can specify such a call itself through `__reduce__`.[^py314-library-pickle-restricting-globals][^py314-library-pickle-object-reduce] Restricting globals through `find_class` can only reduce the risk, and it does not make pickle safe for untrusted data.[^py314-library-pickle-find-class][^py314-library-pickle] For such data, use `json` or another format that does not execute code.[^py314-library-pickle]

## Detailed explanation

The unpickler does not only read data; it also executes the instructions in the pickle stream. The documentation warns plainly that pickle is not secure: a malicious stream can run arbitrary code during unpickling, so data from an untrusted source, or data that could have been tampered with, must not be unpickled.[^py314-library-pickle] By default, unpickling imports any class or function found in the data, which allows arbitrary code to be invoked.[^py314-library-pickle-restricting-globals] A class can specify such a call itself through `__reduce__`: the method returns a callable and a tuple of arguments, which the unpickler calls to create the object.[^py314-library-pickle-object-reduce]

The example is harmless because it calls `print` instead of `os.system`, but the mechanism is the same: the call happens inside `loads()`, and checking the result afterwards cannot undo it.

```python
import pickle

class Payload:
    def __reduce__(self):
        # loads() calls print(...) while it rebuilds the object
        return (print, ("side effect during pickle.loads",))

untrusted = pickle.dumps(Payload())

obj = pickle.loads(untrusted)  # the side effect happens here, before loads() returns
print(type(obj))               # <class 'NoneType'>
print(isinstance(obj, dict))   # False: a check like this rejects the value, too late
```

`Unpickler.find_class()` is called whenever a global class or function is requested, so it can be overridden to forbid globals or narrow the set of allowed names.[^py314-library-pickle-find-class] But an allowed function runs with all of its capabilities: if the allowed list includes anything that reads files or starts processes, the list will not stop it. Restricting globals reduces the attack surface, but it does not make unpickling safe for untrusted data.[^py314-library-pickle]

If data comes from outside, use a format that does not execute code, such as `json`, and validate the schema after parsing. If pickle must stay in use between your own services, authenticate the data before calling `loads()`: the documentation suggests signing data with `hmac` to make sure it has not been tampered with.[^py314-library-pickle] The signature check must happen before any call to `loads()`, otherwise a malicious stream would already have run.

**Common mistakes:**
- assuming that an `isinstance` check after `loads()` protects against code execution;
- assuming that an allow-list in `find_class` makes pickle safe for untrusted data;
- accepting pickle data from a shared cache, queue, or directory that another party can write to.
