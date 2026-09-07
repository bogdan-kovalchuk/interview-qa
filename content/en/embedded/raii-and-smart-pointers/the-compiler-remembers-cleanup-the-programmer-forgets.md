---
id: emb-raii-0020
title: "How is RAII better than manual init/deinit?"
description: "RAII gives cleanup guarantee, safe early return, one destructor instead of repetition, automatic destruction order and zero runtime after inlining."
track: embedded
section: raii-and-smart-pointers
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

- **Cleanup guarantee:** the compiler calls the dtor vs the programmer must remember;
- **Error path:** early return is safe vs every exit is a chance for a bug;
- **Duplication:** the dtor is written once vs repeated at every exit;
- **Order:** automatic reverse destruction vs manual calls in reverse order;
- **Runtime:** often zero after inlining, but this must be verified with release flags.

Rule: RAII adds no capabilities, it removes an entire class of human errors.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
