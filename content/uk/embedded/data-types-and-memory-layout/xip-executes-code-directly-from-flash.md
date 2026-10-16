---
id: emb-dtypes-0064
title: "Що таке XIP (Execute in Place) у embedded?"
track: embedded
section: data-types-and-memory-layout
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: arm-cortex-m3
    title: "Arm Cortex-M3 Technical Reference Manual"
    url: https://documentation-service.arm.com/static/6036810d5319e554d4ba108e
---

## Short answer

**XIP** (Execute in Place) – режим, у якому процесор виконує код безпосередньо з пам’яті, де зберігається образ, без попереднього копіювання цього коду в RAM.[^arm-cortex-m3] Для цього пам’ять і контролер мають надавати процесору придатний для виконання адресний простір; можливість і конкретне розташування залежать від MCU.[^arm-cortex-m3]

XIP зменшує потребу в RAM для коду, але саме по собі не гарантує швидшого запуску чи виконання. Очікування Flash, prefetch і кеш можуть впливати на час вибірки, тож критичні ділянки інколи розміщують у RAM відповідно до linker script і startup code.[^arm-cortex-m3]

## Detailed explanation

XIP розшифровується як Execute in Place: процесор виконує код із того місця пам’яті, де зберігається його образ, замість копіювання всього коду до RAM під час запуску. Пам’ять і контролер мають надати процесору придатний для виконання адресний простір; система може використовувати внутрішню Flash або memory-mapped зовнішню пам’ять.[^arm-cortex-m3]

Основна перевага – менша потреба в RAM для коду. XIP не означає автоматично швидший запуск чи виконання: startup усе ще має ініціалізувати дані, а швидкість вибірки залежить від параметрів пам’яті, wait states, prefetch і cache. Документація Cortex-M3 описує вплив wait states Flash на продуктивність ядра та способи частково приховати затримку prefetcher-ом.[^arm-cortex-m3]

Окремі функції іноді копіюють у RAM, щоб зменшити затримку або виконувати код під час операцій із Flash, які блокують читання. Для цього потрібні розміщення секції через linker script, копіювання у startup та підтримка атрибута компілятором; сама назва `.ramcode` нічого не гарантує. Перевіряйте map-файл і вимірюйте виконання на конкретному target.

**Типова помилка:** вважати, що кожен Cortex-M обов’язково виконує код із Flash у режимі XIP або що XIP усуває час старту. Це визначає конкретний MCU та його memory map, а не лише ядро.
