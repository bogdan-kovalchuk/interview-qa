---
id: py-gil-9000
title: "Чому один блокувальний виклик зупиняє event loop?"
track: python
section: concurrency-and-gil
sources:
  - source_id: python-asyncio-docs
    title: "Python asyncio documentation"
    url: https://docs.python.org/3.14/library/asyncio.html
---

## Short answer

Event loop виконує callbacks в одному потоці.[^python-asyncio-docs] Блокувальний виклик не дає цьому потоку просувати інші callbacks.

## Detailed explanation

Event loop залежить від того, що tasks повертають керування під час очікування.[^python-asyncio-docs]
