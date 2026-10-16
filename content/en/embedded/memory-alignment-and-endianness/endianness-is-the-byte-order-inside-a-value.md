---
id: emb-align-0011
title: "What are little-endian and big-endian for the value `0x12345678`?"
track: embedded
section: memory-alignment-and-endianness
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: posix-byte-order
    title: "General Concepts: Data Types"
    url: https://pubs.opengroup.org/onlinepubs/009696699/basedefs/xbd_chap04.html
  - source_id: learncpp-object-sizes
    title: "Object sizes and the sizeof operator"
    url: https://www.learncpp.com/cpp-tutorial/object-sizes-and-the-sizeof-operator/
  - source_id: acode-cpp-next
    title: "C++ вивчено – що далі?"
    url: https://acode.com.ua/end-cpp-what-is-next/
---

## Short answer

**Byte order of a multi-byte value in memory.**

```text
Address: 00   01   02   03
LE:      78   56   34   12  (least-significant byte first)
BE:      12   34   56   78  (most-significant byte first)
```

LSB (least significant byte) is the least-significant eight bits; MSB (most significant byte) is the most-significant eight bits. Little-endian stores the LSB at the lowest address, while big-endian stores the MSB there. The exact byte order is a property of the target or data format, not of the integer itself.

Rule: endianness affects only multi-byte types; a `uint8_t` array is the same everywhere.[^embeddedinterviewlab]

## Detailed explanation

The integer value `0x12345678` is the same mathematical value in both cases. Endianness becomes observable when its multi-byte object representation is stored, inspected as bytes, or transferred to a format that specifies a byte order. The four component bytes are `0x12`, `0x34`, `0x56`, and `0x78`; only their address order changes.

In C, every object has a sequence of bytes called its object representation. Character types may inspect those bytes, so examining an integer through an `unsigned char *` is a valid way to observe the target's representation.[^iso-c-n1570] The language standard does not require ordinary integers to use either little-endian or big-endian order, so portable code must not assume one.

Endianness does not reverse a byte array. If a buffer contains the sequence `{ 0x12, 0x34, 0x56, 0x78 }`, its indices retain that sequence on every conforming target. The question is what numeric value code assigns when it interprets those bytes as one multi-byte integer.

External interfaces remove ambiguity by defining an order. POSIX network byte order places the most-significant octet first and supplies conversion functions for 16-bit and 32-bit values.[^posix-byte-order] For file formats, device registers, and non-IP protocols, follow that interface's own specification.

LearnCpp's discussion of object sizes provides useful background on how objects occupy bytes,[^learncpp-object-sizes] while the aCode roadmap is a supplementary path for continuing systems-oriented C and C++ study.[^acode-cpp-next]
