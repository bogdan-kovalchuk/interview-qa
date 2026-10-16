---
id: py-fileio-0014
title: "When should you choose `StringIO`, and when `BytesIO`, for an in-memory stream?"
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
  - source_id: py314-library-io-stringio
    title: "Python 3.14: Library/io (StringIO)"
    url: https://docs.python.org/3.14/library/io.html#io.StringIO
  - source_id: py314-library-io-bytesio
    title: "Python 3.14: Library/io (BytesIO)"
    url: https://docs.python.org/3.14/library/io.html#io.BytesIO
  - source_id: py314-library-io-binary-io
    title: "Python 3.14: Library/io (Binary I/O)"
    url: https://docs.python.org/3.14/library/io.html#binary-io
  - source_id: py314-library-io-bytesio-getbuffer
    title: "Python 3.14: Library/io (BytesIO.getbuffer)"
    url: https://docs.python.org/3.14/library/io.html#io.BytesIO.getbuffer
  - source_id: py314-library-io-textiowrapper
    title: "Python 3.14: Library/io (TextIOWrapper)"
    url: https://docs.python.org/3.14/library/io.html#io.TextIOWrapper
---

## Short answer

**Use `StringIO` for text (`str`) and `BytesIO` for binary data (`bytes` or `bytearray`).** `StringIO` inherits from `io.TextIOBase` and accepts a `newline` parameter that controls newline translation.[^py314-library-io-stringio] `BytesIO` inherits from `io.BufferedIOBase` and performs no encoding or decoding.[^py314-library-io-bytesio][^py314-library-io-binary-io] `getbuffer()` returns a view of the buffer without copying it, and changes made through the view are immediately visible in the `BytesIO`.[^py314-library-io-bytesio-getbuffer] If the API expects a text stream, use `StringIO`; if it expects binary data (images, serialized data, network packets), use `BytesIO`.

## Detailed explanation

`StringIO` is a text stream in memory, and `BytesIO` is a binary stream in memory.[^py314-library-io-stringio][^py314-library-io-bytesio] The difference lies in the unit of data: `write()` on a `StringIO` accepts only `str`, while on a `BytesIO` it accepts only bytes-like objects, and `getvalue()` returns the matching type. So the choice depends on what the code that reads or writes the stream works with: text or bytes.

The example shows the data types, the errors when they are mixed, and writing text into a binary buffer through explicit encoding.

```python
import io

text = io.StringIO()
text.write("hello")
print(text.getvalue())                 # hello

raw = io.BytesIO()
raw.write(b"\x89PNG")
print(raw.getvalue())                  # b'\x89PNG'

try:
    raw.write("hello")                 # str is not bytes-like
except TypeError as error:
    print(error)                       # a bytes-like object is required, not 'str'

try:
    text.write(b"x")                   # bytes is not str
except TypeError as error:
    print(error)                       # string argument expected, got 'bytes'

buf = io.BytesIO()
wrapper = io.TextIOWrapper(buf, encoding="utf-8", write_through=True)
wrapper.write("héllo")
print(buf.getvalue())                  # b'h\xc3\xa9llo'
```

If text must be written to a binary buffer, wrap the `BytesIO` in an `io.TextIOWrapper` with an explicit `encoding`: the encoding is then visible where the stream is created, not in a manual `.encode()` call somewhere else in the code.[^py314-library-io-textiowrapper] The `write_through=True` parameter, as in the example, passes data to the buffer immediately, without waiting for `flush()`.[^py314-library-io-textiowrapper]

`getbuffer()` returns a view without copying the data; in CPython the view is a `memoryview`. While the view exists, the `BytesIO` cannot be resized or closed, so the view should be released after use.[^py314-library-io-bytesio-getbuffer]

**Common mistakes:**
- writing `str` into a `BytesIO`, or bytes into a `StringIO`: both raise `TypeError`;
- choosing `StringIO` for a binary format (images, packets): it does not accept bytes, so you would have to invent an encoding that the format does not define;
- encoding text with `.encode()` in one place and decoding it with a different encoding somewhere else.
