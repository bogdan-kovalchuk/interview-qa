---
id: emb-fnptr-0011
title: "Trap: what is wrong with this callback storage?"
track: embedded
section: function-pointers-and-callbacks
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
static void (*rx_cb)(uint8_t);

void uart_isr(void) {
    rx_cb(0x55);
}
```

## Short answer

<span class="warn">The callback may be unregistered or `NULL`.</span>

If the ISR calls a null or otherwise invalid `rx_cb`, the call has undefined behavior under C; the standard does not specify whether an MCU raises a HardFault, hangs, or has some other consequence. The defect can be difficult to reproduce when the interrupt arrives only in a narrow timing window.

Defense: install a no-op or check `if (rx_cb != NULL)`, and register the callback before enabling the relevant interrupt. Follow the platform's rules for ordering and synchronization.[^iso-c-n1570]

## Detailed explanation

TODO
