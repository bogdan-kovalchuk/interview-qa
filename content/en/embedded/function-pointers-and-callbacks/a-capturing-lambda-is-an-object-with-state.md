---
id: emb-fnptr-0038
title: "Trap: why can't a capturing lambda be passed as an ordinary C function-pointer callback?"
description: "A capturing lambda has no standard conversion to an ordinary function pointer because its closure object carries state."
track: embedded
section: function-pointers-and-callbacks
level: junior
type: pitfall
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
    applicability: "Rules for closure types and lambda conversion functions; it does not specify particular ABIs or C callback API requirements."
---

## Short answer

<span class="warn">A capturing lambda has no standard conversion to an ordinary function pointer: its closure object carries captured state.</span> [^cpp-lambda-closure]

Invocation goes through the closure object's `operator()`, while a function pointer does not store an instance of that object. Also, `void (*)(void)` specifically requires a function with no parameters and a `void` result; the target signature must match.

For a C callback, pass state separately through `void *ctx`; otherwise use a C++ callback abstraction that stores the closure object.[^cpp-lambda-closure]

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
