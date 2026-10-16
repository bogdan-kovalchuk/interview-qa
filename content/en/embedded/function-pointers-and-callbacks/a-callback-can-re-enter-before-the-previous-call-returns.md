---
id: emb-fnptr-0051
title: "Trap: why can a callback be a reentrancy problem?"
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

<span class="warn">A callback can be called again before the previous invocation has finished.</span>[^freertos-isr-api]

This can happen if a nested interrupt permits another call before the first ISR returns, or if the callback synchronously calls an API that invokes it again. If both invocations modify the same static buffer, their data can overwrite each other.

To prevent this, document reentrancy, isolate each invocation's state or explicitly serialize events; if nested calls are unsupported, forbid them in the contract and implementation.

## Detailed explanation

TODO
