---
id: emb-fnptr-0027
title: "Trap: what is unsafe about calling `printf` from an ISR callback?"
track: embedded
section: function-pointers-and-callbacks
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: newlib-stdio
    title: "The Red Hat newlib C Library: Standard C library I/O and reentrancy"
    url: https://www.sourceware.org/newlib/libc.html
  - source_id: arm-interrupt-latency
    title: "Arm: A Beginner’s Guide on Interrupt Latency"
    url: https://developer.arm.com/community/arm-community-blogs/b/architectures-and-processors-blog/posts/beginner-guide-on-interrupt-latency-and-interrupt-latency-of-the-arm-cortex-m-processors
---

## Short answer

<span class="warn">Do not assume `printf` is ISR-safe without a guarantee from the specific libc and output backend.</span>

Depending on the libc and backend, `printf` may use stream state or a lock, or wait for UART transmission to finish. Re-entry while main code or a task is printing can corrupt or interleave output and keep the ISR busy.

Protection: in the ISR callback save a compact record to a buffer or set a flag, then print in task or main context; use a dedicated backend only if its ISR safety is documented.[^embeddedinterviewlab] [^newlib-stdio]

## Detailed explanation

TODO
