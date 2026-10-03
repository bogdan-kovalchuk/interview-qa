---
id: emb-fnptr-0050
title: "Why must a callback API document its execution context?"
description: "The same callback type can be invoked from ISR, task, main loop or driver lock context."
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
  - source_id: freertos-isr-api
    title: "Mastering the FreeRTOS Real Time Kernel: Using the FreeRTOS API from an ISR"
    url: https://www.freertos.org/media/2018/161204_Mastering_the_FreeRTOS_Real_Time_Kernel-A_Hands-On_Tutorial_Guide.pdf
    accessed: 2026-10-04
    kind: official
    version: "V10.0.0 tutorial"
    applicability: "Explains that an ISR cannot block a task and requires specifically permitted ISR-safe APIs; exact restrictions depend on the platform."
---

## Short answer

**Because the same callback type can be invoked from ISR, task, main loop or driver lock context.**[^freertos-isr-api]

This determines whether the callback may block or call an API that can wait on a task or scheduler. For example, FreeRTOS provides separate ISR-safe API variants because an ordinary call may try to place a task into the Blocked state, which an ISR cannot do.[^freertos-isr-api]

Therefore, a callback contract should describe its execution context and permitted operations; it is also useful to state reentrancy, lifetime and ownership.

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
