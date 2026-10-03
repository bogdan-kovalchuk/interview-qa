---
id: emb-dtypes-0104
title: "Як забезпечити atomic register update, якщо один регістр змінюють main code і ISR?"
description: "Для атомарної зміни бітів використовуй периферійний set/clear регістр, якщо він передбачений; інакше захисти всю critical section від відповідного ISR."
track: embedded
section: data-types-and-memory-layout
level: senior
type: pitfall
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
  - source_id: stm32g0-gpio-bsrr
    title: "STMicroelectronics STM32G0x0 Reference Manual, GPIO bit set/reset register"
    url: https://www.st.com/resource/en/reference_manual/dm00463896-stm32g0x0-advanced-armbased-32bit-mcus-stmicroelectronics.pdf
    accessed: 2026-10-04
    kind: official
    version: "RM0454 Rev 5"
    applicability: "Пояснює атомарне бітове керування GPIO через BSRR саме на STM32G0x0; інші периферії й MCU можуть мати інші правила."
---

## Short answer

Переважно використовуй передбачений периферією set/clear register, якщо документація гарантує, що запис змінює лише вибрані біти: наприклад, STM32G0 `GPIOx_BSRR` атомарно змінює відповідні біти `GPIOx_ODR`.[^stm32g0-gpio-bsrr] Інакше на однопроцесорній системі захисти read-modify-write critical section-ом, який тимчасово маскує саме той interrupt, що конкурує за регістр. <span class="warn">`volatile` і звичайний atomic primitive не роблять довільний peripheral read-modify-write безпечним.</span>[^iso-c-n1570]

## Detailed explanation

Симптом гонки – біт, який main code або ISR щойно встановив, іноді повертається до старого значення. Наприклад, main читає `REG`, готує значення зі зміненим bit 0, ISR встановлює bit 1, а main потім записує свою копію зі старим bit 1 і стирає оновлення ISR. Читання та запис кожне окремо можуть бути атомарними на шині, але пара read-modify-write не обов’язково є однією атомарною операцією.

Перший вибір – peripheral API, яке змінює біти без повторного читання всього регістра. Наприклад, STM32G0 має `GPIOx_BSRR`: записи в set/reset поля змінюють відповідні біти `GPIOx_ODR` одною операцією, без вимкнення interrupts. Це властивість конкретного регістра STM32G0, а не загальна обіцянка для кожного register із назвою set/clear; звіряй atomicity, маски й побічні ефекти в reference manual.[^stm32g0-gpio-bsrr]

Якщо такого механізму немає і єдиний конкурент – ISR на одному ядрі, коротку critical section можна захистити тимчасовим маскуванням відповідного interrupt навколо всього read-modify-write. Зберігай і відновлюй попередній стан mask, а не безумовно вмикай interrupts на виході: код міг бути викликаний із уже активної critical section. Маскування має покривати всі ISR, що змінюють той самий регістр, і бути мінімальним за тривалістю. Воно не зупиняє інше ядро, DMA або peripheral hardware; для цих учасників потрібен механізм синхронізації чи регістровий протокол, який справді охоплює їх.

Поняття atomic operation з C/C++ теж не можна автоматично переносити на MMIO. Атомарна операція над RAM об’єктом має мовні гарантії для цього об’єкта, тоді як peripheral register може мати спеціальну семантику читання/запису, підтримувати лише певну ширину або не підтримувати read-modify-write зовсім. `volatile` вимагає видимих доступів компілятора, але не забезпечує atomicity чи захист від переривання.[^iso-c-n1570]

**Типові помилки:**

- Виконувати `REG |= mask` і вважати це одним апаратним записом: компілятор зазвичай реалізує вираз окремими читанням і записом.
- Маскувати лише один interrupt, хоча той самий регістр також змінює інший ISR або ядро.
- Використовувати toggle alias для операції set/clear без перевірки семантики: повторний toggle повертає біт у протилежний стан.
- Маскувати interrupts і вважати, що це зупиняє DMA або зміну регістра самим peripheral.

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
