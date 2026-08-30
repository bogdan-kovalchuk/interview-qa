---
id: emb-dtypes-0100
title: "Trap: легально у C чи C++? `union { float f; uint32_t u; } pun; pun.f = 1.0f; uint32_t r = pun.u;`"
description: "У C це поширений union type punning, а формально у C++ читання неактивного члена union - undefined behavior."
track: embedded
section: data-types-and-memory-layout
level: middle
type: pitfall
tags: []
status: published
updated: 2026-09-06
content_revision: 1
reconciled_with:
  en: 1
anki:
  export: true
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Джерело питання і відповіді; відповідь не перевірена незалежно."
---

## Short answer

У **C**: це поширений union type punning. Він не є strict-aliasing порушенням, але отримане значення залежить від IEEE 754 representation, endianness і реалізації. Для максимально переносимого коду краще `memcpy(&r, &pun.f, sizeof r)`.

У **C++**: формально - <span class="warn">undefined behavior</span> (active member rule: активним є `f`, читання `u` - UB). GCC/Clang підтримують як extension, але стандарт не гарантує.

Безпечна альтернатива для C++ (C++20): `std::bit_cast<uint32_t>(1.0f)`.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
