---
id: emb-align-0030
title: "Що робить `__attribute__((aligned(N)))` для змінної?"
description: "Для підтримуваної цілі просить GCC задати змінній alignment щонайменше N байтів."
track: embedded
section: memory-alignment-and-endianness
level: junior
type: mechanism
tags: []
status: published
updated: 2026-10-04
content_revision: 2
reconciled_with:
  en: 4
anki:
  export: true
sources:
  - source_id: gcc-variable-attributes
    title: "GCC 12.5: Common Variable Attributes"
    url: https://gcc.gnu.org/onlinedocs/gcc-12.5.0/gcc/Common-Variable-Attributes.html
    accessed: 2026-10-04
    kind: official
    version: "12.5"
    applicability: "Описує GNU aligned attribute, power-of-two аргумент і обмеження linker; не гарантує поведінку інших компіляторів або target."
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
---

## Question code

```c
uint8_t buf[64] __attribute__((aligned(32)));
```

## Short answer

**Для підтримуваної цілі просить GCC забезпечити змінній alignment щонайменше N байтів.**[^gcc-variable-attributes]

Атрибут застосовують для DMA або cache-line буферів, коли потрібна вирівняна адреса. Це GNU compiler extension; стандарт C має `_Alignas`, але допустимість і підтримка значення залежать від реалізації та target.[^gcc-variable-attributes] [^iso-c-n1570]

`aligned` змінює вимогу до alignment, але сам собою не обирає memory region, не налаштовує DMA й не визначає wire format. `packed` – окремий атрибут зі своїми наслідками.[^gcc-variable-attributes]

## Detailed explanation

`__attribute__((aligned(N)))` – GNU attribute, який задає мінімальне alignment змінної або поля структури в байтах. Для прикладу з `aligned(32)` GCC намагається розмістити `buf` на межі, кратній 32, якщо target підтримує це значення.[^gcc-variable-attributes]

Такий запит може знадобитися периферії або інструкціям, що мають вимогу до адреси. Проте вирівнювання – лише одна з передумов роботи DMA: атрибут не переносить об’єкт у потрібний memory region, не забезпечує доступність цієї RAM контролеру й не виконує cache maintenance. Ці умови задають MCU, linker script і правила драйвера.[^gcc-variable-attributes]

У GCC значення мусить бути цілою константою-степенем двійки. Документація попереджає, що для static objects обмеження linker або object-file format можуть зменшити фактично досяжне alignment. Отже, сама декларація не доводить, що розміщена адреса відповідає потрібній умові на зібраному firmware.[^gcc-variable-attributes]

Стандартний C надає `_Alignas`, але це інший синтаксис із правилами стандарту та implementation-defined підтримкою сильнішого alignment. Для переносимого коду перевіряй стандартну версію й компілятор; у embedded-збірці додатково перевір map-файл або адресу в debugger.[^iso-c-n1570]

**Типові помилки:**
- Сприймати GNU attribute як portable C або однаково підтримуваний на кожному target.
- Вважати, що aligned buffer автоматично доступний DMA.
- Плутати адресу buffer із byte order даних у ньому.

Наприклад, `aligned(32)` може виконати вимогу адреси для DMA, але firmware все ще має переконатися, що буфер лежить у DMA-accessible RAM і що кеш очищено або інвалідовано відповідно до правил конкретного MCU.[^gcc-variable-attributes]

## Sources

<!-- generated from frontmatter -->
