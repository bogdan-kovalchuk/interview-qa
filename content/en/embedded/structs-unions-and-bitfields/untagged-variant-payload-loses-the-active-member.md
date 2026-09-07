---
id: emb-structs-0019
title: "What is wrong with this variant payload?"
description: "There is no tag indicating which field is valid."
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
union Payload {
    uint16_t temperature;
    uint32_t pressure;
};

union Payload p;
```

## Short answer

<span class="warn">There is no tag indicating which field is valid.</span>

A union saves memory but loses information about the active variant. If the receiver does not know the payload type from a header or enum, it can misinterpret the same bytes.

Defense: use `struct Message { enum Type type; union Payload payload; };` or obtain the discriminator from the protocol header and check it before access.[^embeddedinterviewlab]

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
