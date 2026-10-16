---
id: emb-volconst-0054
title: "Which type is better for an ISR flag: `volatile bool` or `bool`?"
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

For a flag changed by an ISR and checked by the main loop, `volatile` is often required by the specific compiler and MCU rules, for example `static volatile bool button_pressed;`.[^iso-c-n1570]

Without the relevant guarantee, the compiler may not repeat the access. `volatile` does not guarantee atomicity: the MCU and compiler must specify that the type can be read and written atomically. C does not guarantee this universally.[^iso-c-n1570]

Rule: use the platform-defined volatile access for an ISR flag and verify its atomicity; complex state needs a synchronization protocol.[^iso-c-n1570]

## Detailed explanation

TODO
