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

<span class="warn">Without a cast you cannot; with a cast you can hide a design error.</span>

A function with a `uint8_t *` parameter has the right to write to the buffer, so passing a `const uint8_t *` violates that contract. If the buffer lives in Flash/`.rodata`, an accidental write can end in a fault or undefined behavior.

Defense: separate the API: input buffer as `const uint8_t *`, output buffer as `uint8_t *`. Do not strip qualifiers with a cast for convenience.[^embeddedinterviewlab]

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
