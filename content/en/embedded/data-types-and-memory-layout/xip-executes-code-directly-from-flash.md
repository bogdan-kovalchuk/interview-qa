---
id: emb-dtypes-0064
title: "What is XIP (Execute in Place) in embedded systems?"
track: embedded
section: data-types-and-memory-layout
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: arm-cortex-m3
    title: "Arm Cortex-M3 Technical Reference Manual"
    url: https://documentation-service.arm.com/static/6036810d5319e554d4ba108e
---

## Short answer

**XIP** (Execute in Place) is a mode where the processor executes code directly from the memory holding the image, without first copying that code into RAM.[^arm-cortex-m3] The memory and controller must provide an executable address space; support and placement depend on the MCU.[^arm-cortex-m3]

XIP reduces the RAM needed for code, but does not by itself guarantee faster startup or execution. Flash wait states, prefetch, and cache can affect fetch time, so critical routines are sometimes placed in RAM through the linker script and startup code.[^arm-cortex-m3]

## Detailed explanation

TODO
