---
id: emb-fnptr-0026
title: "Why must a callback invoked from an ISR be short?"
description: "The ISR callback runs in interrupt context where the system must not be blocked for long."
track: embedded
section: function-pointers-and-callbacks
level: junior
type: concept
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
  - source_id: arm-interrupt-latency
    title: "Arm: A Beginner’s Guide on Interrupt Latency"
    url: https://developer.arm.com/community/arm-community-blogs/b/architectures-and-processors-blog/posts/beginner-guide-on-interrupt-latency-and-interrupt-latency-of-the-arm-cortex-m-processors
    accessed: 2026-10-04
    kind: official
    version: null
    applicability: "Explains interrupt latency and interrupt handling on Cortex-M; priority and nesting details depend on the specific core and MCU."
  - source_id: freertos-isr-api
    title: "FreeRTOS Reference Manual V10.0.0: API Usage Restrictions"
    url: https://en.freertos.org/media/2018/FreeRTOS_Reference_Manual_V10.0.0.pdf
    accessed: 2026-10-04
    kind: official
    version: "V10.0.0"
    applicability: "Supports FreeRTOS ISR API restrictions and FromISR calls; it does not define rules for other RTOSes or MCUs."
---

## Short answer

**The ISR callback runs in interrupt context**, so its work must be short and obey the platform's ISR rules.

Long processing delays the return to interrupted code and can increase the waiting time for other interrupts. For example, FreeRTOS forbids calling API functions without the `FromISR` suffix from an ISR; the callback contract should state its calling context.

Rule: an ISR callback should quickly record the event or notify a task through an ISR-safe method, then leave lengthy work to thread or main context.[^embeddedinterviewlab] [^arm-interrupt-latency] [^freertos-isr-api]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
