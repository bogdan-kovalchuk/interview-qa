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
updated: 2026-10-04
content_revision: 3
reconciled_with:
  uk: 2
anki:
  export: true
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Origin of the question and the original answer (owner's deck). The short answer and the Ukrainian explanation were checked against cited technical sources on 2026-10-04; this source is not proof of the claims."
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

<span class="warn">A `union` does not store a tag indicating which member is currently intended.</span>

A `union` lets different variants share storage, but it does not store a discriminator. If the receiver does not know the payload type from a header or enum, reading another member is not a reliable way to identify the payload type or value.[^iso-c-n1570]

Defense: store the discriminator separately, for example in `struct Message { enum Type type; union Payload payload; };`, and check it before accessing the corresponding member.[^iso-c-n1570]

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
