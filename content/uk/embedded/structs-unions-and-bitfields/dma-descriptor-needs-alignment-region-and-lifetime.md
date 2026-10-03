---
id: emb-structs-0043
title: "Trap: чому DMA descriptor struct не можна просто довільно розмістити на stack?"
description: "DMA може вимагати конкретне alignment, memory region і lifetime довший за stack frame."
track: embedded
section: structs-unions-and-bitfields
level: junior
type: pitfall
tags: []
status: published
updated: 2026-10-04
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
    applicability: "Походження питання й первинної відповіді (власна колода). Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; це джерело не є доказом тверджень."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Авторитетне джерело рівня секції для згаданих правил мови C; конкретні пристрої й тулчейни можуть відрізнятися."
  - source_id: st-an4839
    title: "STMicroelectronics AN4839: Level 1 cache on STM32F7 Series and STM32H7 Series"
    url: https://www.st.com/resource/en/application_note/an4839-level-1-cache-on-stm32f7-series-and-stm32h7-series-stmicroelectronics.pdf
    accessed: 2026-10-04
    kind: official
    version: "Rev 2"
    applicability: "Пояснює cache coherency і cache maintenance для зазначених STM32 із Cortex-M7; не задає універсальні вимоги для інших MCU чи DMA."
---

## Short answer

<span class="warn">DMA descriptor має відповідати вимогам контролера щодо alignment і доступної memory region та залишатися чинним увесь час transfer.</span>

Stack object може зникнути після повернення функції, бути невирівняним для DMA engine або лежати в cacheable RAM без потрібного clean/invalidate. Структура descriptor-а має відповідати layout із hardware manual; cache maintenance потрібен лише там, де цього вимагає платформа.[^st-an4839]

Захист: розміщуй descriptor у доступній DMA memory region з потрібним alignment і достатнім lifetime. Для cacheable memory виконуй описаний виробником cache maintenance; AN4839 стосується STM32F7/H7 з Cortex-M7.[^iso-c-n1570] [^st-an4839]

## Detailed explanation

DMA descriptor – це структура в пам’яті, з якої DMA engine читає адресу, довжину, прапорці або посилання на наступний descriptor. Під час transfer контролер сам звертається до цієї пам’яті, паралельно з CPU. Тому об’єкт має існувати й бути доступним контролеру протягом усього transfer; локальний stack object перестає бути придатним після виходу з функції, яка його створила.[^iso-c-n1570]

Вимоги до адреси та memory region визначає конкретний DMA engine. Деякі контролери приймають лише певні діапазони RAM або мають обмеження alignment і формату полів. `alignas` може задовольнити вимогу до адреси, але не переносить об’єкт у доступний регіон і не фіксує hardware layout автоматично. Його треба звірити з reference manual і визначеннями регістрів саме цього MCU.[^iso-c-n1570]

Окрема проблема виникає, якщо CPU cacheable-ом працює з тією самою RAM, що й DMA: CPU може бачити нові дані у своєму cache, тоді як DMA читає стару версію з RAM. На STM32F7/H7 з Cortex-M7 ST описує cache clean перед передаванням даних від CPU до DMA та invalidate у відповідних сценаріях приймання; точна операція залежить від напрямку transfer і конфігурації пам’яті. Це платформна вимога, а не властивість самого C struct.[^st-an4839]

**Приклад:** функція готує descriptor на stack і запускає асинхронний DMA, а потім повертається. Контролер може прочитати адресу вже повторно використаної stack-пам’яті. Тривале зберігання, наприклад у `static` об’єкті, розв’язує проблему lifetime, але саме по собі не гарантує правильну адресу, region, layout або coherency.[^iso-c-n1570] [^st-an4839]

**Типові помилки:**

- Вважати, що `static` автоматично означає DMA-accessible.
- Припускати, що вирівнювання саме по собі очищує cache.
- Використовувати compiler padding як частину descriptor-а, не перевіривши layout.

Виділяй DMA objects у секції linker script, узгодженій із memory map, застосовуй потрібне alignment і перевіряй lifetime. Далі виконуй лише ті cache operations та barriers, які вимагає конкретний MCU та його документація.[^st-an4839]

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
