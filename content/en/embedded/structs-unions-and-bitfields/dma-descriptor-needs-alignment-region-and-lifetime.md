---
id: emb-structs-0043
title: "Trap: why can a DMA descriptor struct not simply sit on the stack?"
description: "DMA may require specific alignment, memory region, and a lifetime longer than the stack frame."
track: embedded
section: structs-unions-and-bitfields
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
  - source_id: st-an4839
    title: "STMicroelectronics AN4839: Level 1 cache on STM32F7 Series and STM32H7 Series"
    url: https://www.st.com/resource/en/application_note/an4839-level-1-cache-on-stm32f7-series-and-stm32h7-series-stmicroelectronics.pdf
    accessed: 2026-10-04
    kind: official
    version: "Rev 2"
    applicability: "Describes cache coherency and maintenance for the listed STM32 devices with Cortex-M7; it does not define universal requirements for other MCUs or DMA."
---

## Short answer

<span class="warn">A DMA descriptor must meet the controller's alignment and accessible-memory requirements and remain valid for the entire transfer.</span>

A stack object can disappear after the function returns, be misaligned for the DMA engine, or reside in cacheable RAM without the required clean/invalidate operation. The descriptor layout must match the hardware manual; cache maintenance is platform-dependent.[^st-an4839]

Mitigation: use DMA-accessible memory, required alignment, and sufficient lifetime. Follow the MCU's cache-maintenance guidance; AN4839 applies to STM32F7/H7 with Cortex-M7.[^iso-c-n1570] [^st-an4839]

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
