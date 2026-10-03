---
id: emb-fnptr-0043
title: "Trap: what is wrong with registering a callback and never unregistering it?"
description: "The driver can invoke the callback after the module or object has been destroyed."
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
  - source_id: cppreference-pointer
    title: "cppreference: Pointers"
    url: https://en.cppreference.com/w/cpp/language/pointer
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: "Supports the danger of using an invalid pointer; unregister synchronization is API-specific."
  - source_id: cppcoreguidelines-lifetime
    title: "C++ Core Guidelines: Lifetime safety"
    url: "https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines"
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: "General guidance for avoiding dangling pointers; it does not prescribe a particular driver shutdown protocol."
---

## Short answer

<span class="warn">The driver can invoke the callback after the module or object has been destroyed.</span>

Especially in C++ embedded: the object destructor may have finished, but the C HAL still holds `ctx = this`. The next interrupt calls the thunk with a dangling `this` pointer.

Defence: in the destructor or shutdown path, unregister the callback and disable interrupts or events before destroying state. Define ownership in the API.[^cppcoreguidelines-lifetime]

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
