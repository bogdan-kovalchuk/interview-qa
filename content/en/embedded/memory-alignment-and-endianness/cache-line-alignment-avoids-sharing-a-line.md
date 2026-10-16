---
id: emb-align-0027
title: "Why align a buffer to a cache line?"
track: embedded
section: memory-alignment-and-endianness
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: stm32-an4839
    title: "STMicroelectronics AN4839: Level 1 cache on STM32F7 and STM32H7 Series"
    url: https://www.st.com/resource/en/application_note/an4839-level-1-cache-on-stm32f7-series-and-stm32h7-series-stmicroelectronics.pdf
  - source_id: linux-false-sharing
    title: "Linux kernel documentation: False Sharing"
    url: https://docs.kernel.org/kernel-hacking/false-sharing.html
---

## Short answer

**To control data placement relative to a cache line when a use case requires it.**

False sharing occurs when independent data accessed concurrently by cores occupy one cache line. DMA using cached memory needs coherency through cache maintenance or a non-cacheable region; alignment alone does not provide it.[^stm32-an4839]

Check the cache-line size and required isolation for the specific platform; clean/invalidate operations depend on DMA direction.[^stm32-an4839]

## Detailed explanation

TODO
