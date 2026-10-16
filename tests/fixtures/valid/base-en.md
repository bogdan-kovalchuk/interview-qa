---
id: py-gil-9000
title: "Why does one blocking call stop the event loop?"
track: python
section: concurrency-and-gil
sources:
  - source_id: python-asyncio-docs
    title: "Python asyncio documentation"
    url: https://docs.python.org/3.14/library/asyncio.html
---

## Short answer

The event loop runs callbacks on one thread.[^python-asyncio-docs] A blocking call prevents that thread from advancing other callbacks.

## Detailed explanation

The event loop depends on tasks returning control while they wait.[^python-asyncio-docs]
