---
id: emb-fnptr-0025
title: "Trap: why can you not cast any address to a function pointer and call it?"
description: "The address may not be a valid entry point for a function with the required ABI signature."
track: embedded
section: function-pointers-and-callbacks
level: junior
type: pitfall
tags: []
status: published
updated: 2026-10-04
content_revision: 4
reconciled_with:
  uk: 3
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

<span class="warn">Converting an arbitrary integer to a function pointer does not make the address a valid function.</span>

In C, converting an integer to a pointer has an implementation-defined result: the address may be misaligned, may not point to an object or function of the referenced type, or may be a trap representation. Calling through a function pointer with an incompatible type also has undefined behavior.[^iso-c-n1570]

Protection: call only a known entry point with a compatible signature and the platform ABI rules; use the MCU's documented procedure when transferring to another image.[^embeddedinterviewlab] [^iso-c-n1570]

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
