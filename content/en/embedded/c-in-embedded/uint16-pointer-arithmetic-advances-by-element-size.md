---
id: emb-cppfound-0022
title: "What address will `p` have after: `uint16_t arr[4]; uint16_t *p = arr; p += 2;`?"
description: "Pointer arithmetic scales by sizeof the pointed-to type, so p += 2 on uint16t advances by 4 bytes to arr[2]."
track: embedded
section: c-in-embedded
level: junior
type: mechanism
tags: []
status: published
updated: 2026-09-07
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
    applicability: "Source question and answer; answer not independently verified."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Authoritative section-level reference for c in embedded concepts; details of specific devices and toolchains can differ."
---

## Short answer

If `arr` is at address `0x2000` -> `p = 0x2000 + 2 * sizeof(uint16_t) = 0x2000 + 4 = 0x2004`.

The pointer arithmetic step for `uint16_t*` is 2 bytes. `p += 2` -> offset of 2 elements × 2 bytes = 4 bytes.

Now `p` points to `arr[2]`. Note: steps are always in "type elements", not bytes.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
