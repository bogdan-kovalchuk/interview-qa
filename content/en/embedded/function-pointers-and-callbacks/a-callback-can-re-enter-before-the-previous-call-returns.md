---
id: emb-fnptr-0051
title: "Trap: why can a callback be a reentrancy problem?"
description: "A callback can be called again before the previous invocation has finished."
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
  - source_id: freertos-isr-api
    title: "Mastering the FreeRTOS Real Time Kernel: Using the FreeRTOS API from an ISR"
    url: https://www.freertos.org/media/2018/161204_Mastering_the_FreeRTOS_Real_Time_Kernel-A_Hands-On_Tutorial_Guide.pdf
    accessed: 2026-10-04
    kind: official
    version: "V10.0.0 tutorial"
    applicability: "Explains ISR restrictions and ISR/task API differences in FreeRTOS; re-entry depends on system design and interrupt configuration."
---

## Short answer

<span class="warn">A callback can be called again before the previous invocation has finished.</span>[^freertos-isr-api]

This can happen if a nested interrupt permits another call before the first ISR returns, or if the callback synchronously calls an API that invokes it again. If both invocations modify the same static buffer, their data can overwrite each other.

To prevent this, document reentrancy, isolate each invocation's state or explicitly serialize events; if nested calls are unsupported, forbid them in the contract and implementation.

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
