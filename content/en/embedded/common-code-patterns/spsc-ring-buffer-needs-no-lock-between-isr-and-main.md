---
id: emb-patterns-0007
title: "What is an SPSC ring buffer, and when can it operate without a lock?"
track: embedded
section: common-code-patterns
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: linux-circular-buffers
    title: "Linux kernel documentation: Circular Buffers"
    url: https://docs.kernel.org/core-api/circular-buffers.html
---

## Short answer

**An SPSC (single-producer / single-consumer) ring buffer** can avoid a mutex when indices are atomic and the platform provides the required ordering for publishing data. A single writer per index is not enough.[^linux-circular-buffers]

One typical arrangement has an ISR (interrupt service routine), such as UART RX (universal asynchronous receiver-transmitter receive), as producer and the main loop as consumer. `head` and `tail` have separate owners, but atomic access and ordering depend on the platform.[^linux-circular-buffers]

It suits streaming data with defined full/empty behaviour; check platform guarantees before using it.[^linux-circular-buffers]

## Detailed explanation

TODO
