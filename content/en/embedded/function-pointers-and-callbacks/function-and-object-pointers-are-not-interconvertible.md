---
id: emb-fnptr-0049
title: "Trap: why should function pointers and `void *` not be mixed?"
description: "C does not guarantee portable conversion between a function pointer and the object pointer void ."
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

<span class="warn">C does not guarantee portable conversion between a function pointer and the object pointer `void *`.</span>

On some platforms, code and data have different address spaces or different pointer sizes. POSIX has its own requirements for `dlsym`, but this is not a general ISO C rule and not an embedded guarantee.

Defence: keep function pointers in function pointer types and data pointers in `void *`. Do not put a callback address into a generic data pointer field.[^embeddedinterviewlab]

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
