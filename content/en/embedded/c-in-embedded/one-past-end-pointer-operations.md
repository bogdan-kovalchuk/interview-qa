---
id: emb-cppfound-0087
title: "What is a one-past-the-end pointer and which operations are allowed?"
description: "Which operations are valid for a pointer one element past an array."
track: embedded
section: c-in-embedded
level: junior
type: concept
tags: []
status: published
updated: 2026-09-07
content_revision: 2
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
    applicability: "Origin of the question and answer; answer not independently verified."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Authoritative section-level reference for c in embedded concepts; details of specific devices and toolchains can differ."
---

## Short answer

**One-past-the-end** is a pointer to the element immediately after the array: `int *end = arr + N`. It is legal under the C standard.

Allowed:
- **Forming** it (the address is valid);
- **Comparing**: `p != end`, `p <= end`;
- **Subtracting** from another pointer within the array.

Forbidden:
- <span class="warn">Dereferencing</span>: `*end` -> UB;
- <span class="warn">Incrementing further</span>: `end+1` -> UB.

Standard idiom: `for(int *p=arr; p!=arr+N; p++)`[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
