---
id: emb-structs-0028
title: "Trap: is the in-memory order of bit-fields portable?"
description: "No, the allocation order of bit-fields within a storage unit is implementation-defined."
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

## Short answer

<span class="warn">No: the allocation order of bit-fields within a storage unit is implementation-defined.</span>

One compiler may place the first field in the least significant bits; another compiler or a different ABI may behave differently. Endianness also does not give a simple portable rule for bit-field layout within bytes.

Defence: do not use bit-fields as a wire format between different compilers/targets. For protocol bits use masks/shifts over an integer obtained from explicitly parsed bytes.[^embeddedinterviewlab]

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
