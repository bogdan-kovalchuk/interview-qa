---
id: py-perf-0015
title: "How can batching reduce per-call I/O overhead while increasing latency and memory use?"
track: python
section: performance
sources:
  - source_id: py314-library-io-performance
    title: "Python 3.14: Library/io (Performance)"
    url: https://docs.python.org/3.14/library/io.html#performance
  - source_id: py314-library-functions-open
    title: "Python 3.14: Built-in Functions (open)"
    url: https://docs.python.org/3.14/library/functions.html#open
  - source_id: py314-library-profile
    title: "Python 3.14: Library/profile"
    url: https://docs.python.org/3.14/library/profile.html
  - source_id: py314-library-timeit
    title: "Python 3.14: Library/timeit"
    url: https://docs.python.org/3.14/library/timeit.html
  - source_id: py314-faq-programming-performance
    title: "Python 3.14: Faq/programming"
    url: https://docs.python.org/3.14/faq/programming.html#performance
---

## Short answer

**Batching combines many small I/O operations into one call.** The same principle underlies the standard library's buffered I/O, which reads and writes large chunks and hides the inefficiency of OS calls for each small operation.[^py314-library-io-performance] The cost is memory and delay: the whole batch must be collected before it is sent, and the first item waits until the batch fills or a timeout fires. <span class="warn">An overly large batch can exhaust memory or exceed request size limits set by the server or protocol.</span>

## Detailed explanation

Batching means collecting many small operations (writes, queries, messages) and executing them in one call once the batch is full or a timeout fires. The simplest standard-library example is buffered I/O. The documentation explains that it reads and writes large chunks of data even when the program asks for a single byte, and so hides the inefficiency of calling the operating system's lower-level I/O routines.[^py314-library-io-performance] For binary files without a `buffering` argument, `open()` also uses a buffer of a fixed size.[^py314-library-functions-open]

The gain depends on the OS and the kind of I/O: on some modern systems, such as Linux, unbuffered disk I/O can be as fast as buffered I/O.[^py314-library-io-performance] Buffered I/O offers predictable performance regardless of platform and backing device, so it is almost always preferable to unbuffered I/O for binary data.[^py314-library-io-performance] So the benefit of batching should be measured, not assumed.

Here is the same pattern in plain Python, without any I/O library. The function `send` stands in for one I/O call, and the loop packs items into batches of three (illustrative example):

```python
BATCH_SIZE = 3
batch = []

def send(items):  # stand-in for one I/O call
    print(f"send {len(items)} item(s): {items}")

for item in range(7):
    batch.append(item)      # item 0 waits in memory until the batch is full
    if len(batch) == BATCH_SIZE:
        send(batch)         # 7 items use 3 calls here instead of 7
        batch = []
if batch:
    send(batch)             # the last, partial batch
# Output:
# send 3 item(s): [0, 1, 2]
# send 3 item(s): [3, 4, 5]
# send 1 item(s): [6]
```

The price of batching is memory and latency: items are held in memory until the batch is sent, so peak RAM use grows with the batch size, and the first item waits until the batch fills or a timeout fires. Batch size is chosen against both limits.

Compare variants with `timeit`, on the same data and sizes as in production. The documentation recommends repeating the timing a few times and taking the best result, because other programs running on the same machine can affect it.[^py314-library-timeit]

**Common mistakes:**
- assuming batching is always faster: when the per-call overhead is small or the data is already buffered, the gain may be zero;
- growing the batch without limit, without counting memory and the delay before the first item is sent;
- forgetting to send the last, partial batch.
