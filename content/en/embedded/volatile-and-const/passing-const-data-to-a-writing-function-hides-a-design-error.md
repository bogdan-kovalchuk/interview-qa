---
id: emb-volconst-0050
title: "Trap: can you pass a `const uint8_t *` to a function expecting `uint8_t *`?"
description: "Without a cast it is not allowed; with a cast you can hide a design error."
track: embedded
section: volatile-and-const
level: junior
type: pitfall
tags: []
status: published
updated: 2026-10-04
content_revision: 4
reconciled_with:
  uk: 3
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

<span class="warn">Without a compiler diagnostic this is not allowed; a cast does not make writes legal for an actually const object.</span>

A `const uint8_t *` argument passed where `uint8_t *` is required violates C's type constraint and requires a diagnostic. Casting away the qualifier and writing has undefined behavior if the original object was actually defined `const`; otherwise the write may be permitted, but the API hides intent.[^iso-c-n1570]

Separate the API: input buffer as `const uint8_t *`, output buffer as `uint8_t *`. Do not strip the qualifier without checking whether the original object is modifiable.[^iso-c-n1570]

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
