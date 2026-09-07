---
id: emb-fnptr-0057
title: "Trap: why can an indirect call through a function pointer be a problem in safety-critical firmware?"
description: "An indirect call moves the control-flow decision into data."
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

<span class="warn">It moves the control-flow decision into data.</span>

If a function pointer is overwritten through memory corruption, an out-of-bounds access or a stack bug, the program can jump into unexpected code. For safety and security this is a serious risk, especially when the tables are mutable in RAM.

Defence: make dispatch tables `const` in Flash, check indices, do not accept function addresses from external input, enable MPU or stack protection where available.[^embeddedinterviewlab]

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
