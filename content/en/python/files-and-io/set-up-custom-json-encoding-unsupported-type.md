---
id: py-fileio-0011
title: "How do you set up custom JSON encoding for an unsupported type without losing an explicit wire schema?"
description: "How do you set up custom JSON encoding for an unsupported type without losing an explicit wire schema?"
track: python
section: files-and-io
level: middle
type: practical
tags: []
status: published
updated: 2026-10-13
content_revision: 2
reconciled_with:
  uk: 2
anki:
  export: true
sources:
  - source_id: py314-library-io
    title: "Python 3.14: Library/io"
    url: https://docs.python.org/3.14/library/io.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-library-pathlib
    title: "Python 3.14: Library/pathlib"
    url: https://docs.python.org/3.14/library/pathlib.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-library-json
    title: "Python 3.14: Library/json"
    url: https://docs.python.org/3.14/library/json.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-library-pickle
    title: "Python 3.14: Library/pickle"
    url: https://docs.python.org/3.14/library/pickle.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-library-os-os-fsync
    title: "Python 3.14: Library/os"
    url: https://docs.python.org/3.14/library/os.html#os.fsync
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-library-os-os-replace
    title: "Python 3.14: Library/os"
    url: https://docs.python.org/3.14/library/os.html#os.replace
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-library-tempfile
    title: "Python 3.14: Library/tempfile"
    url: https://docs.python.org/3.14/library/tempfile.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-library-json-encoder-table
    title: "Python 3.14: Library/json (JSONEncoder)"
    url: https://docs.python.org/3.14/library/json.html#json.JSONEncoder
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation: the types JSONEncoder serializes by default."
  - source_id: py314-library-json-encoder-default
    title: "Python 3.14: Library/json (Encoders and Decoders)"
    url: https://docs.python.org/3.14/library/json.html#py-to-json-table
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation: the default parameter for unsupported types, TypeError without it, and a subclass with a default() method."
  - source_id: py314-library-json-decoder-object-hook
    title: "Python 3.14: Library/json (JSON-to-Python conversion table)"
    url: https://docs.python.org/3.14/library/json.html#json-to-py-table
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation: object_hook is called with the result of each decoded JSON object, and its return value replaces the dict."
  - source_id: py314-library-json-dump
    title: "Python 3.14: Library/json (dump)"
    url: https://docs.python.org/3.14/library/json.html#json.dump
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation: the cls parameter for a JSONEncoder subclass that overrides default()."
---

## Short answer

**Pass a `default` function for encoding and an `object_hook` for decoding.** `default` is called only for objects that `json` cannot serialize, and it should return a JSON-encodable version of the object or raise `TypeError`.[^py314-library-json-encoder-default] `object_hook` is called with every decoded JSON object, and its return value replaces the dict.[^py314-library-json-decoder-object-hook] The type is written as a dict with a marker key, for example `{"__complex__": true, "real": …, "imag": …}`, so the wire schema stays explicit.

## Detailed explanation

By default, the `json` encoder serializes only `dict`, `list`, `tuple`, `str`, `int`, `float`, `True`, `False`, and `None`.[^py314-library-json-encoder-table] Anything else, such as `complex` or `set`, raises `TypeError` unless a rule is supplied.[^py314-library-json-encoder-default] A custom type therefore needs two sides: an encoder that turns the value into a JSON-encodable form, and a decoder that recognises that form and rebuilds the object.

`default` is called only for values the encoder cannot serialize in the usual way. The function must either return a JSON-encodable version of the value or raise `TypeError` for an unknown type. Returning `None` or `str(obj)` silently changes the data: the value becomes a different JSON type, and the decoder can no longer restore the original type. The same mechanism is available through a subclass of `json.JSONEncoder` that overrides `default()` and is passed with `cls=`.[^py314-library-json-encoder-default][^py314-library-json-dump] On the decoding side, `object_hook` is called for each JSON object after it has been parsed.[^py314-library-json-decoder-object-hook] In CPython, nested objects are passed to the hook before the objects that contain them.

The marker key makes the wire format explicit: anyone who reads the JSON can see that the value describes a `complex`. The limit of this approach is that `object_hook` sees every JSON object. A plain dict with `"__complex__": 1` stays a dict, because the `is True` check rejects it, but a dict with `"__complex__": true` in any data will be restored as a `complex`. So the marker should be a rare name or a versioned prefix, and the decoder should also check the set of expected fields.

The example encodes `complex` and restores it during decoding; other values pass through unchanged.

```python
import json

def encode_special(obj):
    if isinstance(obj, complex):
        return {"__complex__": True, "real": obj.real, "imag": obj.imag}
    raise TypeError(f"Object of type {type(obj).__name__} is not JSON serializable")

def decode_special(d):
    if d.get("__complex__") is True:
        return complex(d["real"], d["imag"])
    return d

text = json.dumps({"z": 1 + 2j, "n": 3}, default=encode_special)
print(text)  # {"z": {"__complex__": true, "real": 1.0, "imag": 2.0}, "n": 3}
restored = json.loads(text, object_hook=decode_special)
print(restored)  # {'z': (1+2j), 'n': 3}
```

**Common mistakes:**
- mixing up the arguments: `default` is passed to `json.dumps`, and `object_hook` to `json.loads`;
- returning `None` or `str(obj)` for an unknown type instead of raising `TypeError`, which silently changes the data's type;
- choosing a generic marker such as `"type"` that can collide with real data.

## Environment

TODO

## Deliverable

TODO

## Acceptance criteria

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
