---
id: emb-structs-0042
title: "Що робить `alignas`/`_Alignas` або compiler-specific alignment attribute?"
description: "Встановлює або підсилює вимогу вирівнювання оголошеного об’єкта."
track: embedded
section: structs-unions-and-bitfields
level: junior
type: concept
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
  - source_id: cpp-draft-dcl-align
    title: "C++ working draft: Alignment specifier [dcl.align]"
    url: https://eel.is/c++draft/dcl.align
    accessed: 2026-10-04
    kind: spec
    version: "Current working draft"
    applicability: "Правила C++ для застосування alignas до variable, class data member і class declaration; не охоплює compiler-specific attributes."
---

## Short answer

**Встановлює або підсилює вимогу вирівнювання оголошеного об’єкта**; можливість застосувати це до самого типу залежить від мови або compiler-specific extension.

У embedded це потрібно для DMA buffers, cache line alignment, vector tables або периферійних вимог. Наприклад, DMA descriptor може вимагати 16-byte alignment; cache maintenance на Cortex-M7 часто працює по cache lines.

Правило: alignment – частина hardware contract. Перевіряй адресу runtime або compile-time і описуй вимогу в декларації, attribute чи linker script.[^iso-c-n1570] [^cpp-draft-dcl-align]

## Detailed explanation

Alignment – це обмеження на адресу, за якою розміщується об’єкт. Наприклад, вимога 16-byte alignment означає, що адреса об’єкта має бути кратною 16. Звичайні типи вже мають alignment вимоги, визначені реалізацією; `alignas` у C++ або `_Alignas` у C11 дають змогу задати вирівнювання для декларації, а C++ також дозволяє застосувати `alignas` до class declaration. Compiler-specific attributes можуть мати інші правила застосування.[^iso-c-n1570] [^cpp-draft-dcl-align]

Вирівнювання не змінює значення об’єкта і не гарантує, що периферія може його читати. Воно може змінити padding структури, її `sizeof` або вимоги до пам’яті, але не забезпечує потрібний linker section, доступність конкретному DMA engine чи cache coherency. Надмірне вирівнювання також може витрачати RAM, особливо для масивів: кожен елемент мусить зберігати alignment типу.[^iso-c-n1570] [^cpp-draft-dcl-align]

**Приклад:** драйвер може вимагати, щоб descriptor починався з адреси, кратної 16. Декларація з потрібним alignment допомагає компілятору розмістити об’єкт відповідно, але треба перевірити, що вимогу підтримує toolchain і що linker не переносить секцію у непридатну область. Для DMA конкретні обмеження задають reference manual і документація периферії; не існує універсальної 16-byte вимоги для всіх контролерів.[^iso-c-n1570]

**Типові помилки:**

- Вважати, що вирівнювання гарантує правильний layout для wire protocol.
- Застосовувати синтаксис одного compiler-specific attribute до іншого toolchain.
- Прирівнювати alignment адреси до cache maintenance або memory barrier.

Перевіряй адресу та розмір під конкретною ABI, а для апаратної вимоги звіряй документацію MCU і linker script. Alignment є лише однією частиною hardware contract.[^iso-c-n1570]

## Sources

<!-- generated from frontmatter -->
