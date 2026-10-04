---
id: emb-align-0027
title: "Why align a buffer to a cache line?"
description: "To prevent false sharing and DMA incoherency by keeping data off shared cache lines."
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
  - source_id: stm32-an4839
    title: "STMicroelectronics AN4839: Level 1 cache on STM32F7 and STM32H7 Series"
    url: https://www.st.com/resource/en/application_note/an4839-level-1-cache-on-stm32f7-series-and-stm32h7-series-stmicroelectronics.pdf
    accessed: 2026-10-04
    kind: official
    version: "Rev 2"
    applicability: "Cache lines and DMA coherency on STM32F7/H7 with Cortex-M7; does not generalize to other MCUs."
  - source_id: linux-false-sharing
    title: "Linux kernel documentation: False Sharing"
    url: https://docs.kernel.org/kernel-hacking/false-sharing.html
    accessed: 2026-10-04
    kind: official
    version: null
    applicability: "False-sharing mechanism and performance impact on multicore systems; not an MCU requirement."
---

## Short answer

**To control data placement relative to a cache line when a use case requires it.**

False sharing occurs when independent data accessed concurrently by cores occupy one cache line. DMA using cached memory needs coherency through cache maintenance or a non-cacheable region; alignment alone does not provide it.[^stm32-an4839]

Check the cache-line size and required isolation for the specific platform; clean/invalidate operations depend on DMA direction.[^stm32-an4839]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
