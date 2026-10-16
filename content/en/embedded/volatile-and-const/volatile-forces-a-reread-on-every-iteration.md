---
id: emb-volconst-0006
title: "What changes once `volatile` is added?"
track: embedded
section: volatile-and-const
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Question code

```c
volatile uint8_t rx_done = 0;

while (rx_done == 0) { }
```

## Short answer

Each evaluation of volatile `rx_done` is an access under the abstract-machine rules; the C implementation defines what counts as such an access.[^iso-c-n1570]

This can let the main loop observe ISR changes in a supported toolchain; DMA also needs platform-specific memory and cache coordination. Without `volatile`, the compiler may reuse a value because the loop does not write `rx_done`.[^iso-c-n1570]

For a simple `uint8_t` flag, it may suffice for separate accesses on a particular implementation, but `volatile` does not ensure atomicity or safe read-modify-write operations.[^iso-c-n1570]

## Detailed explanation

TODO
