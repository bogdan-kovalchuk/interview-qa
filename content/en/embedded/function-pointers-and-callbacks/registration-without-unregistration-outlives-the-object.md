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
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Authoritative section-level reference for the C language rules involved; specific devices and toolchains can differ."
---

## Short answer

<span class="warn">The driver can invoke the callback after the module or object has been destroyed.</span>

Especially in C++ embedded: the object destructor may have finished, but the C HAL still holds `ctx = this`. The next interrupt calls the thunk with a dangling `this` pointer.

Defence: in the destructor or shutdown path, unregister the callback and disable interrupts or events before destroying state. Define ownership in the API.[^embeddedinterviewlab]

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
