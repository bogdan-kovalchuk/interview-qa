---
id: emb-fnptr-0055
title: "Trap: why should function pointer addresses not be serialised or stored in a Flash config?"
description: "Function addresses are not a stable external ABI."
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
    applicability: "Describes C pointer conversion rules; the standard does not define a serialization format for function pointers or guarantee address stability across builds."
---

## Short answer

<span class="warn">A function pointer value is not a portable, stable identifier.</span>

After a rebuild, link-time optimisation, linker script change or firmware update an address may change. On an MCU with bootloader and application layout it may depend on the slot. A stale value may be invalid or designate different code; C does not define a long-term external storage format for function pointers.[^c11-function-pointers]

Defence: serialise a symbolic ID or opcode, not a function address, and after boot select the handler through the current dispatch table.[^c11-function-pointers]

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
