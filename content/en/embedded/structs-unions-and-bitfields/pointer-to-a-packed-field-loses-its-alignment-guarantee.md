---
id: emb-structs-0013
title: "Why can a pointer to a packed field be dangerous?"
description: "&pkt.value can be an unaligned address for a uint32t pointer."
track: embedded
section: structs-unions-and-bitfields
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

## Question code

```c
struct __attribute__((packed)) P {
    uint8_t tag;
    uint32_t value;
};

uint32_t *p = &pkt.value;
```

## Short answer

<span class="warn">`&pkt.value` can be an unaligned address for a `uint32_t *`.</span>

A plain `uint32_t *` carries the assumption that the address is sufficiently aligned for `uint32_t`. If the field is packed, this assumption can be false. Dereferencing such a pointer can be undefined behavior or a fault on an MCU.

Defense: do not take a pointer to packed multi-byte fields; use `memcpy(&tmp, &pkt.value, sizeof tmp)` or a byte parser.[^embeddedinterviewlab]

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
