---
id: emb-volconst-0028
title: "Trap: what is wrong with this API?"
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
void uart_send(uint8_t *data, size_t len);
const uint8_t msg[] = { 0x55, 0xAA };
uart_send(msg, 2);
```

## Short answer

<span class="warn">The API loses const-correctness.</span>

If `uart_send` only reads the buffer, declare its parameter as `const uint8_t *data`. Otherwise passing a `const` buffer causes a pointer type incompatibility; explicitly casting away `const` does not make a write valid and can hide a bug.

Declare read-only input parameters as `const T *` so the signature matches the function's behavior.[^iso-c-n1570]

## Detailed explanation

TODO
