---
id: emb-cppfound-0067
title: "What is a pointer past the end, and when may it be formed?"
description: "How the one-past-the-end pointer is formed and used safely."
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

**One-past-the-end pointer** – a pointer to the element immediately after the last one in an array: `arr + N` for an array of N elements. Per the C standard: forming it is **allowed**, but <span class="warn">dereferencing it is UB</span>. Usage – the standard end idiom: `int *end = arr + N; for(int *p=arr; p!=end; p++)`. Pointers further (arr+N+1 etc.) – UB already when formed; therefore: <span class="warn">only one element "past the end"</span>.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
