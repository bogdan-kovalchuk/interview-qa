---
id: emb-fnptr-0031
title: "Trap: why must `void *context` be cast back to the right type?"
description: "A cast from void * does not check the type; incorrect object access may cause undefined behaviour."
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
---

## Short answer

<span class="warn">A cast from `void *` does not check the type; undefined behaviour occurs if the result is used to access the object incorrectly.</span>

`void *` carries no runtime type information. If a callback expects `struct Uart *` but receives a pointer to `struct Spi`, dereferencing it as `struct Uart` may violate alignment or typed-object access rules.[^iso-c-n1570]

Protection: use a typed registration API where possible; verify the object type; use a wrapper for incompatible contexts.[^iso-c-n1570]

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
