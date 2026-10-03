---
id: emb-structs-0023
title: "Why can you not take the address of a bit-field?"
description: "A bit-field has no addressable byte object like a regular field."
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

## Short answer

<span class="warn">In C, the address-of operator `&` cannot be applied to a bit-field.</span>

A bit-field may be part of an addressable storage unit, but the C standard explicitly prohibits applying `&` to the bit-field itself. Thus `&s.flag` violates a language constraint and requires a compiler diagnostic.[^iso-c-n1570]

Such a field cannot be passed to a function as a pointer to it. If an API needs an address, copy the value into an ordinary variable or pass the containing structure/value another way.[^iso-c-n1570]

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
