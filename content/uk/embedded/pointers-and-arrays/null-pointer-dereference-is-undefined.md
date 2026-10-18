---
id: emb-cppfound-0019
title: "Що таке NULL pointer і що відбувається при його розіменуванні?"
track: embedded
section: pointers-and-arrays
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

**NULL pointer** – гарантовано невалідна адреса (null pointer constant): у C визначений як `0` або `(void*)0`, у C++ – `nullptr`.

Розіменування NULL -> <span class="warn">undefined behavior</span>. На Cortex-M: адреса `0x00000000` – початок Flash (Vector Table), тож запис туди -> HardFault або пошкодження Vector Table.

Захист: завжди перевіряй перед розіменуванням: `if(p != NULL) *p = val;`; Ініціалізуй: `int *p = NULL;`[^embeddedinterviewlab]

## Detailed explanation

TODO
