---
id: emb-cppfound-0093
title: "What is printed?<br><pre class=\"code-block\"><code><span class=\"code-type\">int</span> arr[<span class=\"code-num\">4</span>]={<span class=\"code-num\">10</span>,<span class=\"code-num\">20</span>,<span class=\"code-num\">30</span>,<span class=\"code-num\">40</span>};<br><span class=\"code-fn\">printf</span>(\"%d %d\",*(arr+<span class=\"code-num\">3</span>), arr[<span class=\"code-num\">3</span>]);</code></pre>"
description: "Why array subscripting and pointer arithmetic are equivalent in C."
track: embedded
section: c-in-embedded
level: junior
type: mechanism
tags: []
status: published
updated: 2026-09-06
content_revision: 1
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

TODO

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
