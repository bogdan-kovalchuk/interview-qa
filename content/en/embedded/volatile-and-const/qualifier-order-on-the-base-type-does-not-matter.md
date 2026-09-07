---
id: emb-volconst-0057
title: "Trap: are `const volatile uint32_t *` and `volatile const uint32_t *` the same?"
description: "Yes, for the pointed-to base type the order of const and volatile does not change the meaning."
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

**Yes, for the pointed-to base type the order of `const` and `volatile` does not change the meaning.**

Both types mean pointer to const volatile `uint32_t`. The data behind the pointer cannot be written through this lvalue, but reads must be volatile. The important thing is not to confuse this with `const volatile uint32_t * const`, where the extra `const` after `*` protects the pointer itself.

Rule: the order of cv-qualifiers at one type level does not matter; what matters is which level of the pointer chain they apply to.[^embeddedinterviewlab]

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
