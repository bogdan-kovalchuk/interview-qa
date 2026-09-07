---
id: emb-cppfound-0073
title: "Яке значення матиме `*(uint8_t*)(&val)` якщо `uint32_t val = 0x12345678` (little-endian)?"
description: "How a byte pointer exposes the least significant byte on little-endian systems."
track: embedded
section: c-in-embedded
level: junior
type: mechanism
tags: []
status: published
updated: 2026-09-07
content_revision: 2
reconciled_with:
  en: 3
anki:
  export: true
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Source question and answer; answer not independently verified."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Авторитетне джерело рівня секції для понять розділу c-in-embedded; деталі конкретних пристроїв і тулчейнів можуть відрізнятися."
---

## Short answer

**0x78**.

Cast `(uint8_t*)(&val)` – вказівник на перший байт `val` у пам'яті. На little-endian: LSB знаходиться за найменшою адресою -> `0x78`.

Розкладка у пам'яті: `[78][56][34][12]`; наступний байт: `*((uint8_t*)(&val) + 1) = 0x56`.

Доступ через byte pointer дозволений для character types (`unsigned char*`); На практиці `uint8_t` зазвичай є typedef до `unsigned char`.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
