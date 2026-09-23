---
id: py-oop-0025
title: "Коли abstract base class доречніша за неформальну duck typing перевірку?"
description: "ABC доречні, коли потрібна гарантія інтерфейсу на етапі створення instance, підтримка isinstance/issubclass перевірок, або реєстрація virtual subclasses для структурної сумісності."
track: python
section: oop-and-data-model
level: middle
type: comparison
tags: []
status: published
updated: 2026-09-04
content_revision: 1
reconciled_with:
  en: 1
anki:
  export: true
sources:
  - source_id: py314-reference-datamodel
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-howto-descriptor
    title: "Python 3.14: Howto/descriptor"
    url: https://docs.python.org/3.14/howto/descriptor.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-howto-mro
    title: "Python 3.14: Howto/mro"
    url: https://docs.python.org/3.14/howto/mro.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-dataclasses
    title: "Python 3.14: Library/dataclasses"
    url: https://docs.python.org/3.14/library/dataclasses.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
---

## Short answer

**ABC доречні, коли потрібна гарантія інтерфейсу на етапі створення instance, підтримка `isinstance`/`issubclass` перевірок, або реєстрація virtual subclasses для структурної сумісності.**[^py314-reference-datamodel] Duck typing підходить для простих сценаріїв, де гнучкість важливіша за формальні гарантії. ABC дає чіткий контракт: якщо клас не реалізує всі abstract methods, instantiation викличе `TypeError`, що запобігає помилкам пізніше.

## Detailed explanation

TODO

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
