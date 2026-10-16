---
id: emb-align-0013
title: "Trap: why can you not say \"endianness does not matter on ARM, it is always little-endian\"?"
track: embedded
section: memory-alignment-and-endianness
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: arm-library-endianness
    title: "Selection of Arm C and C++ library variants based on build options"
    url: https://developer.arm.com/documentation/dui0475/latest/the-arm-c-and-c---libraries/c-and-c---runtime-libraries/selection-of-arm-c-and-c---library-variants-based-on-build-options
  - source_id: posix-byte-order
    title: "General Concepts: Data Types"
    url: https://pubs.opengroup.org/onlinepubs/009696699/basedefs/xbd_chap04.html
  - source_id: learncpp-bitwise
    title: "Bitwise operators"
    url: https://www.learncpp.com/cpp-tutorial/bitwise-operators/
  - source_id: acode-cpp-next
    title: "C++ вивчено – що далі?"
    url: https://acode.com.ua/end-cpp-what-is-next/
---

## Short answer

<span class="warn">The Arm ecosystem includes little-endian and big-endian configurations, and an external data format can use an order different from the processor.</span>

A concrete microcontroller, however, has a specific implemented and configured byte order. Internet network byte order is big-endian, but field-bus payloads and file formats follow their own specifications; CAN payload bytes, for example, do not acquire one universal integer byte order from the CAN transport itself.

Fix: name both sides of the boundary – the target's host order and the external format's specified order – then convert only where required.[^embeddedinterviewlab]

## Detailed explanation

"Arm" names an architecture family, not one fixed board configuration. Toolchains and runtime libraries have distinct little-endian and big-endian variants,[^arm-library-endianness] while the selected MCU, reset configuration, ABI, and toolchain determine what a particular firmware image actually uses. Therefore, neither "Arm is always little-endian" nor "every Arm chip can switch at runtime" is a safe claim.

Byte order at an interface is an independent contract. POSIX defines network byte order with the most-significant octet first and provides host/network conversions.[^posix-byte-order] That supports statements about IP networking APIs, not a blanket statement that every protocol is big-endian. A peripheral register map, CAN application payload, Modbus register sequence, binary file, or custom packet can specify another ordering or define order separately for bytes, words, and bits.

Conversion is needed only for multibyte fields whose external order differs from the host representation. Single-byte fields need no byte-order conversion. Explicit shifts and masks are one portable decoding technique; the LearnCpp bitwise material covers those operations.[^learncpp-bitwise]

### Symptom

Firmware works on the developer's little-endian board but reads swapped lengths, timestamps, or register values when data comes from another implementation or interface.

### Why it happens

The code treats a local object representation as though it were the protocol representation. It also replaces the concrete device and protocol specifications with broad labels such as "Arm" or "network".

### How to avoid

Document byte order per multibyte field, use named encode/decode helpers at the boundary, and test them with fixed byte vectors. Use `htonl`/`ntohl` only where POSIX network order is the relevant contract; otherwise implement the format named by the device or protocol specification. The aCode roadmap is useful supplementary guidance for continuing the wider C and C++ learning path.[^acode-cpp-next]
