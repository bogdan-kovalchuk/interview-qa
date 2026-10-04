---
id: emb-dtypes-0081
title: "Що не так на 8-bit AVR MCU? `if(!(PORTA & (1<<8)))`"
description: "1<<8 = 256 не вміщається у 8-бітний PORTA, тож маска завжди дає 0 і умова завжди true."
track: embedded
section: data-types-and-memory-layout
level: middle
type: pitfall
tags: []
status: published
updated: 2026-10-04
content_revision: 4
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
    applicability: "Авторитетне джерело рівня секції для понять розділу data-types-and-memory-layout; деталі конкретних пристроїв і тулчейнів можуть відрізнятися."
  - source_id: avr-libc-faq-types
    title: "AVR-LibC 2.1.0 FAQ: Data types"
    url: https://avrdudes.github.io/avr-libc/avr-libc-user-manual-2.1.0/FAQ.html
    accessed: 2026-10-04
    kind: official
    version: "2.1.0"
    applicability: "Підтверджує розміри типів у типовій конфігурації avr-gcc; опція -mint8 змінює їх і не підтримується avr-libc."
---

## Short answer

Для звичайного avr-gcc `int` має 16 біт, тому `1 << 8` коректно обчислюється як `0x0100`; сам результат не переповнюється. Для 8-бітного регістра `PORTA` маска не відповідає жодному біту порту.

Після integer promotions байтове значення `PORTA` перетворюється на `int`, і його старший байт дорівнює нулю; отже, `PORTA & 0x0100` дорівнює нулю.

Умова <span class="warn">завжди true</span> незалежно від стану PORTA.

Для перевірки старшого біта порту використовуй `if (!(PORTA & (1u << 7)))`; конкретний регістр і доступні біти залежать від моделі MCU.[^avr-libc-faq-types] [^iso-c-n1570]

## Detailed explanation

Проблема тут не в тому, що `1 << 8` обов’язково переповнюється. У типовому avr-gcc `1` має тип `int`, а `int` є 16-бітним, тому зсув на 8 позицій дає значення 256 (`0x0100`). У C зсув визначений, коли правий операнд невід’ємний і менший за ширину типу після integer promotions; тут умова виконується. Варіант avr-gcc з `-mint8` змінює розміри типів, але AVR-LibC його не підтримує, тож висновок треба прив’язувати до конфігурації компілятора.[^avr-libc-faq-types] [^iso-c-n1570]

Регістр вводу-виводу, оголошений як 8-бітне значення, під час бітової операції просувається до `int`. Це не додає в нього фізичних бітів: числове значення лишається в діапазоні 0–255, а біт 8 залишається нульовим. Тому AND з `0x0100` дає нуль за будь-якого стану `PORTA`, а логічне заперечення нуля робить умову істинною. Зауваж, що назви й ширина регістрів залежать від конкретного AVR; у деяких моделей може не бути `PORTA` взагалі.[^avr-libc-faq-types] [^iso-c-n1570]

Для перевірки біта використовуй саме його номер, перевірений за документацією MCU. Якщо тестуєш один із восьми бітів 8-бітного регістра, допустимі номери від 0 до 7. Суфікс `u` робить намір із беззнаковою маскою явним, хоча в цьому прикладі 16-бітний `int` AVR також може подати результат. Якщо значення регістра використовується в ISR і змінюється апаратурою, окремо потрібен належний volatile-доступ; маска сама по собі цього не забезпечує.[^iso-c-n1570]

**Типові помилки:**

- Називати цей вираз undefined behavior через переповнення: на звичайному AVR-GCC зсув допустимий і результат вміщується в 16-бітний `int`.[^iso-c-n1570]
- Вважати, що ширина CPU автоматично визначає ширину кожного C-типу або кожного периферійного регістра. Звіряйся з ABI компілятора і datasheet саме свого MCU.[^avr-libc-faq-types]
- Використовувати `1 << 8` для біта 8-бітного порту: індекс 8 поза діапазоном бітів 0–7.

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
