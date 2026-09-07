---
id: emb-patterns-0034
title: "Trap: why is `reg |= (value << SHIFT)` without clearing the mask a bug?"
description: "OR only sets bits but does not clear old ones so the new value layers on top of the existing field"
track: embedded
section: common-code-patterns
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

<span class="warn">OR only sets bits but does not clear old ones</span> – if the field already had a value, the new one is layered on top.

For example, the old field is `0b110`, we write `0b001` via `|=` -> we get `0b111`, not `0b001`.

Defense: first `reg &= ~MASK;`, then `reg |= (value << SHIFT) & MASK;` – a full read-modify-write.[^embeddedinterviewlab]

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
