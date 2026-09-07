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
updated: 2026-09-07
content_revision: 2
reconciled_with:
  uk: 1
anki:
  export: true
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Source question and answer; answer not independently verified."
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

If the ISR calls `rx_cb` before registration, it is undefined behavior and on an MCU very likely a HardFault. In interrupt context this is even worse: the fault can occur asynchronously and is hard to reproduce.

Defense: initialize the callback with a no-op function or check `if (rx_cb != NULL)`. Perform registration before enabling the interrupt.[^embeddedinterviewlab]

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
