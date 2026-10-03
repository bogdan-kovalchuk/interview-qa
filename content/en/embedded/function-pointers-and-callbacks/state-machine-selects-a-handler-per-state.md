---
id: emb-fnptr-0044
title: "What is a state machine built on function pointers?"
description: "A table of state handlers or transition handlers where the current state selects the function to handle an event."
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
  - source_id: cppreference-pointer
    title: "cppreference: Pointers"
    url: https://en.cppreference.com/w/cpp/language/pointer
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: "Describes function pointer types used in handler tables; choosing a state-machine model is an architectural decision."
---

## Short answer

**It is a table of state handlers or transition handlers** where the current state selects the function to handle an event.

For example: `state = handlers[state](ctx, event);`. This makes each state a separate function and removes a large nested `switch`. For embedded protocol stacks this is often more readable and testable per state handler.

Rule: the state enum must be bounds-checked before indexing into the handler table.[^cppreference-pointer]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
