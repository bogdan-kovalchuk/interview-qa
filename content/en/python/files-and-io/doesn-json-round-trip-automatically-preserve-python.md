---
id: py-fileio-0012
title: "Why doesn't a JSON round trip automatically preserve every Python type and object identity?"
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
  - source_id: py314-library-json-encoder-table
    title: "Python 3.14: Library/json (JSONEncoder)"
    url: https://docs.python.org/3.14/library/json.html#json.JSONEncoder
  - source_id: py314-library-json-encoder-default
    title: "Python 3.14: Library/json (Encoders and Decoders)"
    url: https://docs.python.org/3.14/library/json.html#py-to-json-table
  - source_id: py314-library-json-decoder-table
    title: "Python 3.14: Library/json (JSONDecoder)"
    url: https://docs.python.org/3.14/library/json.html#json.JSONDecoder
  - source_id: py314-library-json-dump
    title: "Python 3.14: Library/json (dump)"
    url: https://docs.python.org/3.14/library/json.html#json.dump
---

## Short answer

**JSON has a limited set of types, so a round trip through `json.dumps` and `json.loads` does not preserve Python types or object identity.**[^py314-library-json-encoder-table] A tuple comes back as a list.[^py314-library-json-decoder-table] Keys of type `int`, `float`, `bool`, and `None` become the strings of their JSON spelling: the number 1 becomes `"1"`, `True` becomes `"true"`, and `None` becomes `"null"`.[^py314-library-json-dump] A `set` or a custom class without `default` raises `TypeError`.[^py314-library-json-encoder-default] In CPython, shared references become separate copies, and `json.dumps` rejects circular structures with `ValueError`.

## Detailed explanation

The `json` module maps Python values to JSON through a fixed table: `dict` becomes an object, `list` and `tuple` become arrays, `str` becomes a string, `int` and `float` become numbers, and `True`, `False`, and `None` become true, false, and null.[^py314-library-json-encoder-table] A value outside this table has no JSON form: without `default`, the encoder raises `TypeError`.[^py314-library-json-encoder-default] So `json.loads(json.dumps(x))` returns the nearest JSON-shaped equivalent of `x`, not `x` itself.

The conversion is not symmetric. A tuple is written as an array and read back as a `list`, so `(1, 2) == [1, 2]` is `False`, and equality is broken after the round trip.[^py314-library-json-decoder-table] Dict keys can be `str`, `int`, `float`, `bool`, or `None`, but in JSON every key is a string, so `{1: "x"}` comes back as `{'1': 'x'}`, and `{True: 1, None: 2}` comes back as `{'true': 1, 'null': 2}`.[^py314-library-json-dump] A tuple key is rejected with `TypeError` during encoding, because JSON has no such key type.[^py314-library-json-encoder-table]

Object identity is not preserved either. The serializer writes a shared list at every place where it appears, and the decoder creates a separate `list` for each occurrence. In CPython, `restored["a"] is restored["b"]` is `False` after the round trip, while the same expression on the original dict is `True`. Circular structures are rejected: with the default `check_circular=True`, the encoder checks containers for cycles to avoid infinite recursion, and with `check_circular=False` a `RecursionError` is expected instead.[^py314-library-json-encoder-default]

The example shows these differences; the output is the same on CPython 3.13 and 3.14.

```python
import json

print(json.loads(json.dumps((1, 2))))  # [1, 2], tuple comes back as list
print(json.loads(json.dumps({1: "x"})))  # {'1': 'x'}, int key becomes str

shared = [1, 2]
restored = json.loads(json.dumps({"a": shared, "b": shared}))
print(restored["a"] is restored["b"])  # False, one shared list became two

try:
    json.dumps({(2, 3): "tuple key"})
except TypeError as error:
    print(error)  # keys must be str, int, float, bool or None, not tuple

cyclic = []
cyclic.append(cyclic)
try:
    json.dumps(cyclic)
except ValueError as error:
    print(error)  # Circular reference detected
```

**Common mistakes:**
- expecting `json.loads(json.dumps(x)) == x` for any `x`: a tuple becomes a list, and equality breaks;
- using `default=str` for every unknown type: the value comes back as a string, and the original type cannot be restored;
- relying on the identity of shared objects after decoding: each occurrence becomes a separate object.
