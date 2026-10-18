---
id: emb-cppfound-0073
title: "Яке значення матиме `*(uint8_t*)(&val)` якщо `uint32_t val = 0x12345678` (little-endian)?"
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

**0x78**.

Cast `(uint8_t*)(&val)` – вказівник на перший байт `val` у пам'яті. На little-endian: LSB знаходиться за найменшою адресою -> `0x78`.

Розкладка у пам'яті: `[78][56][34][12]`; наступний байт: `*((uint8_t*)(&val) + 1) = 0x56`.

Доступ через byte pointer дозволений для character types (`unsigned char*`); На практиці `uint8_t` зазвичай є typedef до `unsigned char`.[^embeddedinterviewlab]

## Detailed explanation

TODO
