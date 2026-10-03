---
id: emb-fnptr-0042
title: "Why is `std::function` not always suitable for an embedded callback API?"
description: "std::function is convenient but can carry overhead and potential allocations."
track: embedded
section: function-pointers-and-callbacks
level: junior
type: concept
tags: []
status: published
updated: 2026-10-04
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
    applicability: "Origin of the question and the original answer (owner's deck). The short answer and the Ukrainian explanation were checked against cited technical sources on 2026-10-04; this source is not proof of the claims."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Authoritative section-level reference for the C language rules involved; specific devices and toolchains can differ."
  - source_id: cppreference-function
    title: "cppreference: std::function constructor"
    url: https://en.cppreference.com/w/cpp/utility/functional/function
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: "Describes type erasure and the small-object optimization guarantee for function pointers and reference_wrapper; other allocation details are implementation-dependent."
---

## Short answer

**`std::function` is convenient but can carry overhead and potential allocations.**

It type-erases the callable and can store lambdas and functors, but this increases code size, may pull in exceptions and RTTI depending on the toolchain, and sometimes uses the heap when the callable does not fit in the small buffer optimization.

Embedded rule: in low-level drivers, `function pointer + void *ctx` is used more often; in the application layer, `std::function` is acceptable if project policy allows it.[^cppreference-function]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
