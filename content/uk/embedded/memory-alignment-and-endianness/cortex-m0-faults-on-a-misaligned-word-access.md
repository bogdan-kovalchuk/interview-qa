---
id: emb-align-0007
title: "Trap: що станеться при misaligned 32-бітному доступі на Cortex-M0?"
description: "HardFault. Cortex-M0/M0+ (а також деякі RISC-V, ARM7TDMI) не підтримують misaligned access: будь-яке читання/запис uint16_t/uint32_t за невирівняною адресою -> fault."
track: embedded
section: memory-alignment-and-endianness
level: junior
type: pitfall
tags: []
status: published
updated: 2026-09-07
content_revision: 1
reconciled_with:
  en: 1
anki:
  export: true
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Походження питання і відповіді; відповідь незалежно не перевірена."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Авторитетне джерело рівня секції для згаданих правил мови C; конкретні пристрої й тулчейни можуть відрізнятися."
---

## Short answer

<span class="warn">HardFault.</span>

Cortex-M0/M0+ (а також деякі RISC-V, ARM7TDMI) <span class="warn">не підтримують misaligned access</span>: будь-яке читання/запис `uint16_t`/`uint32_t` за невирівняною адресою -> fault.

Захист: не приводь `uint8_t*` зі зсувом до `uint32_t*`; для невирівняних даних використовуй `memcpy` у вирівняну змінну.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
