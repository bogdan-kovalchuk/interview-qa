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

<span class="warn">Function addresses are not a stable external ABI.</span>

After a rebuild, link-time optimisation, linker script change or firmware update the addresses will change. On an MCU with bootloader and application layout the address can depend on the slot. Calling a stale stored address can jump into the wrong code.

Defence: serialise a symbolic ID or opcode, not a function address, and after boot select the handler through the current dispatch table.[^embeddedinterviewlab]

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
