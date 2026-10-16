---
id: emb-volconst-0045
title: "Why are peripheral register struct fields declared `volatile`?"
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

## Short answer

**Because each field of the struct overlay represents a hardware register, not an ordinary RAM field.**

When code accesses a field declared volatile, the implementation must preserve the corresponding volatile access under the C rules. However, the exact definition of an access is implementation-defined; `volatile` alone does not guarantee atomicity, bus transaction width, or the required ordering of hardware operations.[^iso-c-n1570]

Rule: qualify memory-mapped register accesses as `volatile`, and check the address, field layout, access width, and side effects against the MCU documentation.[^iso-c-n1570]

## Detailed explanation

TODO
