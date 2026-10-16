---
id: emb-patterns-0021
title: "Trap: what is the danger of sentinel values for errors?"
track: embedded
section: common-code-patterns
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
uint16_t adc_read(uint8_t ch) {
  if (ch >= NUM_CH) return UINT16_MAX; // "invalid"
  // ...
}
```

## Short answer

<span class="warn">It works only if the sentinel value is never valid data.</span>

If `UINT16_MAX` is a legitimate ADC (analog-to-digital converter) reading, the caller cannot distinguish an error from a real maximum. When the exact type `uint16_t` exists, the C standard defines `UINT16_MAX` as its maximum value; it does not reserve it for errors.[^iso-c-n1570]

Defense: use a sentinel when the special value is physically impossible; otherwise use a return code plus an output pointer.[^embeddedinterviewlab]

## Detailed explanation

TODO
