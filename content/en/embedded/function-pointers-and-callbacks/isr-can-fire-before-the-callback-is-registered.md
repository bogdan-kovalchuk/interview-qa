---
id: emb-fnptr-0011
title: "Trap: what is wrong with this callback storage?"
description: "The callback may be unregistered or NULL, causing undefined behavior."
track: embedded
section: function-pointers-and-callbacks
level: junior
type: pitfall
tags: []
status: published
updated: 2026-10-04
content_revision: 4
reconciled_with:
  uk: 3
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

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
