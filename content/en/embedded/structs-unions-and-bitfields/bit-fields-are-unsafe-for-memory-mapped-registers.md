---
id: emb-structs-0024
title: "Trap: why are bit-fields dangerous for memory-mapped registers?"
track: embedded
section: structs-unions-and-bitfields
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: stm32-w1c-manual
    title: "SR5E1x 32-bit Arm Cortex-M7 architecture microcontroller reference manual"
    url: https://www.st.com/resource/en/reference_manual/rm0483-sr5e1x-32bit-arm-cortexm7-architecture-microcontroller-for-electrical-vehicle-applications-stmicroelectronics.pdf
---

## Short answer

<span class="warn">Bit-field layout is implementation-defined, and access often generates a read-modify-write.</span>

Bit ordering within a storage unit, signedness of plain `int` bit-fields, and padding between them all depend on the compiler/ABI. Moreover, writing one bit-field may read the entire register and write it back, which is dangerous for write-one-to-clear or read-to-clear bits.

Defence: for hardware registers it is often better to use masks/shifts and atomic set/clear registers. If bit-fields are allowed, pin to a specific compiler ABI and test the generated code.[^iso-c-n1570]

## Detailed explanation

TODO
