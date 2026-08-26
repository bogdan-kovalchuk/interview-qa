---
id: py-gil-9000
title: "Чому один блокувальний виклик зупиняє event loop?"
description: "Мінімальна валідна українська fixture."
track: python
section: concurrency-and-gil
level: middle
type: mechanism
tags: [event-loop, blocking]
status: published
updated: 2026-09-04
content_revision: 1
reconciled_with:
  en: 1
anki:
  export: true
sources:
  - source_id: python-asyncio-docs
    title: "Python asyncio documentation"
    url: https://docs.python.org/3.14/library/asyncio.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "CPython 3.14 і сумісні реалізації з asyncio."
---

## Short answer

Event loop виконує callbacks в одному потоці.[^python-asyncio-docs] Блокувальний виклик не дає цьому потоку просувати інші callbacks.

## Detailed explanation

Event loop залежить від того, що tasks повертають керування під час очікування.[^python-asyncio-docs]

## Evaluation guide

### Expected signals

- Пов'язує блокувальну роботу з потоком event loop.

### Red flags

- Каже, що кожна асинхронна операція створює потік.

### Level-up follow-up

- Запитати, як ізолювати блокувальну роботу.

## Sources

<!-- generated from frontmatter -->
