---
id: emb-align-0033
title: "Why is `memcpy` safer than a typed-pointer cast for multi-byte access?"
track: embedded
section: memory-alignment-and-endianness
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

`memcpy` copies bytes without reading a value through a misaligned typed pointer or violating strict aliasing.[^iso-c-n1570] The destination must hold `n` bytes, and later reading it as `T` requires a properly aligned `T` object; copying does not convert byte order.[^iso-c-n1570] Optimization depends on the compiler and target, so C guarantees neither particular instructions nor a speed advantage.[^iso-c-n1570]

## Detailed explanation

TODO
