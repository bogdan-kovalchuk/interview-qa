---
id: emb-dtypes-0105
title: "Чим DRAM відрізняється від SRAM і які наслідки це має для latency, refresh, controller і startup?"
description: "SRAM не потребує refresh і коштує дорожче за bit; DRAM щільніша, але потребує controller та refresh, а її latency залежить від системи й pattern доступу."
track: embedded
section: data-types-and-memory-layout
level: senior
type: concept
tags: []
status: published
updated: 2026-10-04
content_revision: 3
reconciled_with:
  en: 3
anki:
  export: true
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
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
    applicability: "Авторитетне джерело рівня секції для понять розділу data-types-and-memory-layout; деталі конкретних пристроїв і тулчейнів можуть відрізнятися."
  - source_id: microchip-mpu-memory
    title: "Microchip Developer Help: Differences Between MCU and MPU Development"
    url: https://developerhelp.microchip.com/xwiki/bin/view/products/mcu-mpu/32bit-mpu/differences-between-mcu-and-mpu-development/
    accessed: 2026-10-04
    kind: official
    version: null
    applicability: "Порівнює типове застосування SRAM та DRAM, щільність, вартість і роль memory controller в описаних Microchip MPU-системах; не задає універсальні latency."
  - source_id: uboot-memory-startup
    title: "U-Boot documentation: Memory Management"
    url: https://docs.u-boot.org/en/latest/develop/memory.html
    accessed: 2026-10-04
    kind: official
    version: "latest"
    applicability: "Показує приклад boot flow, де до ініціалізації DRAM рання пам’ять може бути SRAM, а стек переноситься після налаштування DRAM; точний порядок залежить від плати."
---

## Short answer

**SRAM** не потребує refresh і зазвичай має нижчу access latency, але її cost per bit вищий. **DRAM** дає більшу щільність і місткість, проте потребує memory controller та періодичного refresh; access latency залежить від memory technology й pattern доступу.[^microchip-mpu-memory] На платі із зовнішньою DRAM early boot може спершу виконуватися з SRAM, доки boot code не налаштує controller і DRAM.[^uboot-memory-startup]

## Detailed explanation

SRAM зберігає кожен bit у latch-схемі, тому після запису не потребує періодичного refresh, поки живлення збережене. Типові SRAM мають простий інтерфейс і малу access latency, але кожен bit займає більше транзисторної площі. Унаслідок цього обсяг вбудованої SRAM обмежений, а велика зовнішня SRAM дорожча за bit. DRAM зберігає bit як заряд у комірці; заряд витікає, тож масив треба періодично refresh-ити. Компактніша комірка забезпечує вищу щільність і нижчу вартість за bit, а також дає змогу встановити значно більшу пам’ять у системі.[^microchip-mpu-memory]

Не порівнюй latency лише за назвами типів: фактичний час доступу залежить від конкретної мікросхеми, controller, тактування, кількості outstanding запитів, cache, арбітражу та pattern звернень. DRAM організована в banks і rows, а переходи між рядками й refresh можуть додавати затримку; водночас controller приховує частину витрат чергуванням запитів. Порівнювати треба повний шлях CPU-to-memory за потрібним навантаженням, не лише номінальний час комірки. DRAM refresh керується controller або самою пам’яттю в self-refresh mode; це не обов’язково робота firmware для кожного циклу.[^microchip-mpu-memory]

Вбудована SRAM часто доступна відразу після reset, але зовнішня DRAM ще потребує налаштування controller, параметрів сигналу й, для окремих поколінь або швидкісних режимів, calibration/training. Тому ранній код може працювати з ROM, Flash чи SRAM, ініціалізувати тактування й DRAM controller, перевірити результат, а тоді перенести stack, data або наступний boot stage у DRAM. U-Boot описує саме такий загальний шаблон: ранні stack і allocator розміщені у доступній пам’яті, часто SRAM, до завершення DRAM setup.[^uboot-memory-startup] Це поширений сценарій, а не універсальна послідовність: деякі MCU мають лише внутрішню SRAM, а деякі системи вже отримують DRAM initialized від попереднього boot stage.

Вибір пам’яті є компромісом системного рівня. SRAM вигідна для малих deterministic working sets, latency-sensitive buffers та коду, який потрібен до доступності зовнішньої пам’яті. DRAM доречна, коли потрібна велика ємність для ОС, network buffers чи framebuffers, і проєкт може оплатити controller, routing, startup time та refresh overhead.[^microchip-mpu-memory]

**Типові помилки:**

- Називати DRAM завжди «повільною»: порівняння залежить від controller, cache та навантаження.
- Стверджувати, що SRAM узагалі не має latency або є завжди on-chip; зовнішні SRAM також мають bus і timing.
- Вважати, що кожна плата мусить виконувати training однаково або запускатися з SRAM; це визначає SoC, boot ROM і конкретна board configuration.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
