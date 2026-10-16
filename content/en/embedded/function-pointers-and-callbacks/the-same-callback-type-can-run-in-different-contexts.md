---
id: emb-fnptr-0050
title: "Why must a callback API document its execution context?"
track: embedded
section: function-pointers-and-callbacks
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: freertos-isr-api
    title: "Mastering the FreeRTOS Real Time Kernel: Using the FreeRTOS API from an ISR"
    url: https://www.freertos.org/media/2018/161204_Mastering_the_FreeRTOS_Real_Time_Kernel-A_Hands-On_Tutorial_Guide.pdf
---

## Short answer

**Because the same callback type can be invoked from ISR, task, main loop or driver lock context.**[^freertos-isr-api]

This determines whether the callback may block or call an API that can wait on a task or scheduler. For example, FreeRTOS provides separate ISR-safe API variants because an ordinary call may try to place a task into the Blocked state, which an ISR cannot do.[^freertos-isr-api]

Therefore, a callback contract should describe its execution context and permitted operations; it is also useful to state reentrancy, lifetime and ownership.

## Detailed explanation

TODO
