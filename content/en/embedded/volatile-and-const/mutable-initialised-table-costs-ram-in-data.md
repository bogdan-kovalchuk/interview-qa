---
id: emb-volconst-0026
title: "Which section does a mutable lookup table land in?"
track: embedded
section: volatile-and-const
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: avr-libc-program-space
    title: "AVR-LibC: Data in Program Space"
    url: https://avrdudes.github.io/avr-libc/avr-libc-user-manual/pgmspace.html
---

## Question code

```c
uint16_t sine_lut[256] = { 0, 402, 804 };
```

## Short answer

In a typical embedded ELF toolchain, initialized mutable data goes into `.data`.

In a common arrangement, the linker keeps the load image in Flash and startup code copies the bytes to RAM before `main()`. The table occupies space in both memories and takes time to copy; details depend on the toolchain and linker script.[^avr-libc-program-space]

If the table is immutable, `const` allows placement in a read-only section, but does not guarantee a Flash address.[^avr-libc-program-space]

## Detailed explanation

TODO
