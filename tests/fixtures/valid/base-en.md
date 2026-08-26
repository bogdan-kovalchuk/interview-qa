---
id: py-gil-9000
title: "Why does one blocking call stop the event loop?"
description: "A minimal valid English fixture."
track: python
section: concurrency-and-gil
level: middle
type: mechanism
tags: [event-loop, blocking]
status: published
updated: 2026-09-04
content_revision: 1
reconciled_with:
  uk: 1
anki:
  export: true
sources:
  - source_id: python-asyncio-docs
    title: "Python asyncio documentation"
    url: https://docs.python.org/3.14/library/asyncio.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "CPython 3.14 and compatible implementations with asyncio."
---

## Short answer

The event loop runs callbacks on one thread.[^python-asyncio-docs] A blocking call prevents that thread from advancing other callbacks.

## Detailed explanation

The event loop depends on tasks returning control while they wait.[^python-asyncio-docs]

## Evaluation guide

### Expected signals

- Connects blocking work to the event loop thread.

### Red flags

- Says every asynchronous operation creates a thread.

### Level-up follow-up

- Ask how to isolate blocking work.

## Sources

<!-- generated from frontmatter -->
