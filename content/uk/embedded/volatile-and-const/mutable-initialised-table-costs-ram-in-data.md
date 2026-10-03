---
id: emb-volconst-0026
title: "В яку секцію зазвичай потрапить не-`const` таблиця?"
description: "У .data: initialized mutable global/static data."
track: embedded
section: volatile-and-const
level: junior
type: mechanism
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
  - source_id: avr-libc-program-space
    title: "AVR-LibC: Data in Program Space"
    url: https://avrdudes.github.io/avr-libc/avr-libc-user-manual/pgmspace.html
    accessed: 2026-10-04
    kind: official
    version: "current"
    applicability: "Приклад поведінки avr-gcc та AVR linker script: mutable static data може бути в .data, а const і розміщення у Flash залежать від архітектури та linker script."
---

## Question code

```c
uint16_t sine_lut[256] = { 0, 402, 804 };
```

## Short answer

У типовому embedded ELF toolchain це initialized mutable data у `.data`.

У типовій схемі linker залишає load image у Flash, а startup code копіює байти в RAM до `main()`. Таблиця займає місце в обох пам’ятях і потребує часу на копіювання; деталі залежать від toolchain і linker script.[^avr-libc-program-space]

Якщо таблиця незмінна, `const` дає змогу розмістити її в read-only секції, але не гарантує адресу у Flash.[^avr-libc-program-space]

## Detailed explanation

Змінна таблиця з ініціалізатором і static storage duration у типовій embedded збірці з writable data потрапляє до `.data`, бо програма має право змінювати її елементи. Назва секції є домовленістю об’єктного формату й toolchain, а не правилом мови C: стандарт визначає тривалість зберігання та допустимий доступ, але не назви `.data` чи фізичні адреси.[^iso-c-n1570] GNU toolchain зазвичай розділяє initialized writable data і read-only data на відповідні секції, після чого linker script визначає їх розміщення.[^avr-libc-program-space]

У поширеній MCU схемі оперативна пам’ять містить робочу копію writable об’єктів, а їхні початкові байти зберігаються у Flash image. Startup code переносить ці байти до RAM до виклику `main()`. Отже, таблиця коштує місця у двох пам’ятях: образ має містити початкові значення, а RAM має вмістити змінювану копію. Також зростає час стартової ініціалізації. Це типова реалізація, не вимога C; окремі MCU можуть мати інші карти пам’яті або спеціальний доступ до Flash.[^avr-libc-program-space]

Якщо таблиця незмінна, кваліфікатор `const` описує обмеження запису через її тип і дозволяє toolchain розмістити її у read-only секції. Але `const` саме по собі не обіцяє Flash: linker script, адресний простір і можливості архітектури визначають фактичне розміщення та спосіб читання. Наприклад, AVR має окремі правила доступу до program memory, а AVR-LibC радить перевіряти результат у map file.[^avr-libc-program-space]

Приклад: у наведеному `sine_lut` тип елементів не містить `const`, тож код може присвоїти нове значення, навіть якщо алгоритм цього ніколи не робить. Якщо це справді таблиця лише для читання, оголошення `const uint16_t sine_lut[256]` виражає цей контракт; після збірки перевіряють map file, щоб переконатися, що linker розмістив дані там, де очікує прошивка. Не слід робити висновок про використання RAM лише з назви `.data` у вихідному коді або про Flash лише з наявності `const`.[^iso-c-n1570] [^avr-libc-program-space]

## Sources

<!-- generated from frontmatter -->
