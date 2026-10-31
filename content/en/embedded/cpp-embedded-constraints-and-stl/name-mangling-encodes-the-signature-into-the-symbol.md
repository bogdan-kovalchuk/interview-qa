---
id: emb-cppstl-0017
title: "What is name mangling and why does it make `extern \"C\"` necessary?"
track: embedded
section: cpp-embedded-constraints-and-stl
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
  - source_id: itanium-cxx-abi
    title: "Itanium C++ ABI: External Names (Mangling)"
    url: https://itanium-cxx-abi.github.io/cxx-abi/abi.html#mangling
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

**C++ encodes the signature into the symbol (for overload resolution): `sensor_read(uint8_t)` -> `_Z10sensor_readh`; C does not mangle.**

Without `extern "C"` the linker looks for the mangled name and does not find the unmangled C symbol -> link error.

Rule: mangling is the reason a cross-language interface requires C linkage.[^embeddedinterviewlab]

## Detailed explanation

TODO
