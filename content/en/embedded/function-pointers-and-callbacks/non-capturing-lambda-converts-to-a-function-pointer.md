---
id: emb-fnptr-0037
title: "Can a C++ non-capturing lambda be passed to a C-style callback?"
description: "Yes, if the lambda has no captures and the signature is compatible."
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
  - source_id: cpp-lambda-closure
    title: "C++ working draft: Closure types"
    url: https://eel.is/c++draft/expr.prim.lambda.closure
    accessed: 2026-10-04
    kind: spec
    version: "current working draft"
    applicability: "Rules for conversion of non-capturing lambdas and closure types; it does not specify particular ABIs or C HAL requirements."
---

## Short answer

**Yes, if the lambda has no captures and the signature is compatible.**

A non-generic lambda with no captures has a conversion function to a function pointer with compatible parameter and return types. A capturing lambda has no such conversion; pass state separately through a context pointer or use a C++ callback abstraction.[^cpp-lambda-closure]

For a C HAL callback, also check the exact signature and calling convention required by the API.[^cpp-lambda-closure]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
