---
id: emb-align-0026
title: "Що робить `_Alignas` / `alignas` і навіщо?"
description: "Задає підвищену вимогу вирівнювання для змінної."
track: embedded
section: memory-alignment-and-endianness
level: junior
type: concept
tags: []
status: published
updated: 2026-10-04
content_revision: 2
reconciled_with:
  en: 4
anki:
  export: true
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Походження питання й первинної відповіді (власна колода). Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; це джерело не є доказом тверджень."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Авторитетне джерело рівня секції для згаданих правил мови C; конкретні пристрої й тулчейни можуть відрізнятися."
  - source_id: stm32-an4839
    title: "STMicroelectronics AN4839: Level 1 cache on STM32F7 and STM32H7 Series"
    url: https://www.st.com/resource/en/application_note/an4839-level-1-cache-on-stm32f7-series-and-stm32h7-series-stmicroelectronics.pdf
    accessed: 2026-10-04
    kind: official
    version: "Rev 2"
    applicability: "Cache і DMA узгодженість на STM32F7/H7 з Cortex-M7; вимоги інших MCU можуть відрізнятися."
---

## Question code

```c
_Alignas(32) uint8_t dma_buf[256];
```

## Short answer

**Задає вимогу вирівнювання для оголошеного об’єкта.**

Застосовуйте, коли ABI або апаратний контракт вимагає певної адреси. Підтримка конкретного значення залежить від реалізації; саме вирівнювання не забезпечує узгодженість DMA-кешу.

Правило: для DMA враховуйте вимоги пристрою, доступну пам’ять і процедуру cache maintenance окремо від `_Alignas`.[^iso-c-n1570]

## Detailed explanation

`_Alignas` у C задає мінімальну вимогу вирівнювання об’єкта; він може посилити звичайну вимогу типу, але не визначає розташування даних у протоколі чи поведінку DMA.[^iso-c-n1570]

У прикладі `_Alignas(32)` просить компілятор розмістити масив `dma_buf` за адресою, кратною 32 байтам. Це має сенс лише якщо реалізація підтримує таке extended alignment і лінкер може його зберегти для обраної секції. C не вимагає, щоб кожна реалізація підтримувала будь-яке довільне значення вирівнювання.[^iso-c-n1570]

Для реального DMA також потрібно перевірити, що контролер бачить область пам’яті, де розташований буфер, і що адреса та розмір відповідають вимогам контролера. Якщо CPU має D-cache, програмі можуть бути потрібні clean перед передачею даних DMA та invalidate перед читанням даних, записаних DMA; точний порядок залежить від напрямку передачі й платформи.[^stm32-an4839]

Приклад:

```c
_Alignas(32) uint8_t dma_buf[256];
```

**Типові помилки:**

- Вважати, що `_Alignas` автоматично робить пам’ять DMA-сумісною.
- Плутати вирівнювання адреси з cache maintenance.

Перевіряйте фактичну адресу в linker map або під час налагодження та звіряйте її з документацією MCU і DMA.

## Sources

<!-- generated from frontmatter -->
