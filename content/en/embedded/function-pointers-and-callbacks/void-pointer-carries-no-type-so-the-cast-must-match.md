---
id: emb-fnptr-0031
title: "Trap: why must `void *context` be cast back to the right type?"
description: "An incorrect cast of the context pointer gives undefined behavior when accessing the object."
track: embedded
section: function-pointers-and-callbacks
level: junior
type: pitfall
tags: []
status: published
updated: 2026-09-07
content_revision: 2
reconciled_with:
  uk: 1
anki:
  export: true
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Source question and answer; answer not independently verified."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Authoritative section-level reference for the C language rules involved; specific devices and toolchains can differ."
---

## Short answer

<span class="warn">An incorrect cast of the context pointer gives undefined behavior when accessing the object.</span>

`void *` carries no runtime type information. If the callback expects `struct Uart *` but the driver passed `struct Spi *`, the compiler will not protect you. Field accesses then interpret the wrong layout as the wrong type.

Protection: make the registration API typed where possible; add magic or version fields for debugging; do not reuse one callback signature for incompatible context objects without a wrapper.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
