---
id: emb-dtypes-0113
title: "What are little-endian and big-endian, and where do they matter in embedded systems?"
track: embedded
section: memory-alignment-and-endianness
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: python-struct-byte-order
    title: "Python 3 struct module: byte order, size, and alignment"
    url: https://docs.python.org/3/library/struct.html#byte-order-size-and-alignment
---

## Short answer

**Endianness** defines the byte order of a multibyte value in memory: little-endian places the least significant byte at the lowest address, big-endian – the most significant. In embedded systems, this matters in binary protocols, peripheral FIFOs, network byte order, flash images, and debug memory view.[^python-struct-byte-order] Bit order within an SPI/I2C frame is a separate property and does not equal CPU endianness.[^iso-c-n1570]

## Detailed explanation

TODO
