---
id: emb-align-0037
title: "Why enable `UNALIGN_TRP` on an M3/M4 during development?"
description: "To make some processor-supported misaligned accesses raise UsageFault during debugging."
track: embedded
section: memory-alignment-and-endianness
level: junior
type: concept
tags: []
status: published
updated: 2026-10-04
content_revision: 4
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
  - source_id: arm-cortex-m3-trm
    title: "Arm Cortex-M3 Technical Reference Manual"
    url: https://documentation-service.arm.com/static/6036810d5319e554d4ba108e
    accessed: 2026-10-04
    kind: official
    version: "DDI 0337E"
    applicability: "Describes unaligned access support and the UNALIGN_TRP bit on Cortex-M3; instructions have different rules."
  - source_id: arm-cortex-m4-guide
    title: "Cortex-M4 Devices Generic User Guide"
    url: https://documentation-service.arm.com/static/5f2ac76d60a93e65927bbdc5
    accessed: 2026-10-04
    kind: official
    version: "DUI 0553B"
    applicability: "Describes Cortex-M4 unaligned load/store instructions and recommends UNALIGN_TRP; this is not a universal guarantee for all accesses."
---

## Short answer

**To make some misaligned accesses raise an explicit UsageFault during debugging.**

M3/M4 support unaligned accesses only for some load/store instructions; other instructions already fault. `UNALIGN_TRP` in `SCB->CCR` makes supported unaligned accesses raise UsageFault, but it does not diagnose every alignment violation in C code.[^arm-cortex-m3-trm] [^arm-cortex-m4-guide] [^iso-c-n1570]

Use this mode as an additional check on the specific core, while keeping the language and platform alignment requirements in the code.[^arm-cortex-m4-guide] [^iso-c-n1570]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
