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
  - source_id: c11-function-pointers
    title: "ISO/IEC 9899:2011 Committee Draft N1570, 6.3.2.3"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-10-04
    kind: spec
    version: "N1570"
    applicability: "Describes C call and pointer rules; dispatch-table corruption risk depends on the architecture and platform protections."
---

## Short answer

<span class="warn">It moves the control-flow decision into data.</span>

If a function pointer is corrupted by memory corruption, an out-of-bounds access or a stack bug, an indirect call may target a function other than the expected one. The impact depends on the architecture, memory and system protections.[^c11-function-pointers]

Defence: keep immutable tables in read-only memory, validate indices and input values, and use MPU or stack protection when the platform supports them.[^c11-function-pointers]

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
