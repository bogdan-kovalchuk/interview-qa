---
id: emb-fnptr-0026
title: "Why must a callback invoked from an ISR be short?"
track: embedded
section: function-pointers-and-callbacks
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: arm-interrupt-latency
    title: "Arm: A Beginner’s Guide on Interrupt Latency"
    url: https://developer.arm.com/community/arm-community-blogs/b/architectures-and-processors-blog/posts/beginner-guide-on-interrupt-latency-and-interrupt-latency-of-the-arm-cortex-m-processors
  - source_id: freertos-isr-api
    title: "FreeRTOS Reference Manual V10.0.0: API Usage Restrictions"
    url: https://en.freertos.org/media/2018/FreeRTOS_Reference_Manual_V10.0.0.pdf
---

## Short answer

**The ISR callback runs in interrupt context**, so its work must be short and obey the platform's ISR rules.

Long processing delays the return to interrupted code and can increase the waiting time for other interrupts. For example, FreeRTOS forbids calling API functions without the `FromISR` suffix from an ISR; the callback contract should state its calling context.

Rule: an ISR callback should quickly record the event or notify a task through an ISR-safe method, then leave lengthy work to thread or main context.[^embeddedinterviewlab] [^arm-interrupt-latency] [^freertos-isr-api]

## Detailed explanation

TODO
