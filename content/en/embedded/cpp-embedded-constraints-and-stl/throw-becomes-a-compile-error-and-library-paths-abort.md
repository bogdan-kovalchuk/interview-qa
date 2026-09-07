---
id: emb-cppstl-0002
title: "Trap: what happens to `throw` and `try`/`catch` under `-fno-exceptions`?"
description: "Under -fno-exceptions, throw and try/catch become compile errors and library throws become abort"
track: embedded
section: cpp-embedded-constraints-and-stl
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
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N4861"
    applicability: "Authoritative section-level reference for the C++ language rules involved; freestanding and vendor toolchains can differ."
---

## Short answer

<span class="warn">In your own code `throw`/`try`/`catch` usually become compile errors; library paths that would have thrown an exception often end in `abort()`.</span>

This is not "magic error removal": a path through `vector::at()` out-of-range may crash the system instead of raising a handled exception.

Defence: audit throwing API (application programming interface) in the standard library and replace them with explicit checks/statuses.[^embeddedinterviewlab]

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
