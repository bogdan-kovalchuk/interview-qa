---
id: emb-tmplcx-0014
title: "Where does template code bloat come from?"
description: "Each unique instantiation produces a separate full copy of code in Flash."
track: embedded
section: templates-and-constexpr
level: junior
type: concept
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
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N4861"
    applicability: "Authoritative section-level reference for the C++ language rules involved; freestanding and vendor toolchains can differ."
---

## Short answer

<span class="warn">Each unique instantiation = a separate full copy of code in Flash.</span>

`CircularBuffer<uint8_t,64>`, `<uint16_t,64>`, `<uint32_t,64>` produce three full copies of all methods, even though the logic is identical.

Rule: watch the number of instantiations – on flash-constrained MCUs this quickly eats up ROM.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
