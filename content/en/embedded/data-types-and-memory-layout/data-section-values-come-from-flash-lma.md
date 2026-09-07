---
id: emb-dtypes-0083
title: "What does the `.data` section hold, and where do its startup values come from?"
description: ".data holds initialized globals whose startup values startup code copies from Flash (the LMA) into RAM."
track: embedded
section: data-types-and-memory-layout
level: middle
type: mechanism
tags: []
status: published
updated: 2026-09-07
content_revision: 2
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
    applicability: "Origin of the question and answer; the answer is not independently verified."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Authoritative section-level reference for data types and memory layout concepts; details of specific devices and toolchains can differ."
---

## Short answer

`.data` holds **initialized global and static variables** with non-zero values.

In the `.elf`: initial values are in Flash (LMA). At boot, startup code performs:
`memcpy(&_sdata, &_sidata, &_edata - &_sdata);`
where `_sidata` is the start of data in Flash, `_sdata`/`_edata` are the boundaries in RAM.

Then: `memset(&_sbss, 0, &_ebss - &_sbss);`
Then `main()`. Controlled by the linker script.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
