---
id: emb-align-0020
title: "Trap: why can you not `memcpy` a raw struct between different MCUs?"
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
  - source_id: learncpp-struct-miscellany
    title: "Struct miscellany"
    url: https://www.learncpp.com/cpp-tutorial/struct-miscellany/
  - source_id: acode-cpp-next
    title: "C++ вивчено – що далі?"
    url: https://acode.com.ua/end-cpp-what-is-next/
---

## Short answer

<span class="warn">The in-memory representation of a C structure is an ABI detail, not a portable wire format.</span>

Two endpoints may happen to match, but different ABIs can choose different member offsets, tail padding, type widths, alignment, and byte order. Raw `memcpy` transfers all those implementation choices, including padding bytes.

Fix: always define an explicit wire format and serialize field by field with explicit byte order.[^embeddedinterviewlab]

## Detailed explanation

For a structure, C preserves member declaration order but permits unnamed padding between members and after the last member. The amount is implementation-defined, and even the representation of scalar members is not a portable serialization contract.[^iso-c-n1570] Additional hazards include:

- `int`, `long`, enums, pointers, and floating-point types can have different sizes or representations;
- integer byte order can differ;
- bit-field allocation order and packing are implementation-defined;
- padding bytes may hold unspecified data and can leak stale memory if transmitted;
- compiler options such as packing change the ABI without defining a protocol.

`memcpy` itself performs exactly the requested byte copy. The defect is using it on an object whose bytes were never specified as an interoperable message. Packing can reduce padding, but it does not normalize endianness, scalar representation, or versioning.

Define a wire format independently: exact field widths, byte offsets, signedness, byte order, reserved bytes, and version rules. Encode each field into a byte buffer and decode it into aligned native objects. POSIX network order is one example of such an explicit contract for selected integer widths.[^posix-byte-order] Test with golden byte vectors rather than only round trips between identical builds.

Raw structure copying is acceptable only inside a deliberately constrained ABI boundary where both sides are guaranteed to use the same type definition, compiler ABI, options, alignment, representation, and version. State and verify that constraint; do not infer it merely because both devices are called MCU.

LearnCpp's structure discussion illustrates how padding enters a layout,[^learncpp-struct-miscellany] while the aCode roadmap is supplementary guidance for continuing C and C++ study.[^acode-cpp-next]
