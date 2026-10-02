---
id: emb-dtypes-0002
title: "В яку секцію пам'яті потрапить? `const uint32_t FIRMWARE_VERSION = 0x0102;`"
description: "Типове компонування може розмістити const-об'єкт у .rodata, але фактичне розташування визначають compiler і linker script."
track: embedded
section: data-types-and-memory-layout
level: middle
type: mechanism
tags: []
status: published
updated: 2026-10-04
content_revision: 3
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
    applicability: "Авторитетне джерело рівня секції для понять розділу data-types-and-memory-layout; деталі конкретних пристроїв і тулчейнів можуть відрізнятися."
  - source_id: embedded-ld-layout
    title: "GNU ld documentation: linker scripts and output section LMA"
    url: https://sourceware.org/binutils/docs/ld/Output-Section-LMA.html
    accessed: 2026-10-04
    kind: official
    version: "Binutils 2.47"
    applicability: "Документація GNU ld показує, як linker script зіставляє секції з адресами виконання та завантаження; фактичне розміщення залежить від target і конкретного скрипту."
---

## Short answer

Для `const uint32_t FIRMWARE_VERSION = 0x0102;` типове компонування розміщує об'єкт у read-only області, часто `.rodata` у Flash. Але `const` у C забороняє зміну через це lvalue, а не наказує linker вибрати `.rodata` чи гарантує відсутність RAM-витрат. Фактичне розміщення залежить від compiler, використання об'єкта й linker script.[^embedded-ld-layout]

## Detailed explanation

У C кваліфікатор `const` є частиною типу. Він обмежує модифікацію об'єкта через lvalue відповідного типу, але стандарт мови не визначає секцій `.rodata` і `.data` та не пов'язує `const` із Flash.[^iso-c-n1570]

У типовому bare-metal проєкті compiler створює input section для констант, а linker script зіставляє її з output section на кшталт `.rodata` та областю ROM. Інші скрипти можуть розмістити дані інакше; оптимізатор також може прибрати невикористаний об'єкт або вбудувати його значення, тож окремого символу в образі не буде.[^embedded-ld-layout]

Якщо об'єкт потрібен під час виконання, але target читає його лише з Flash, таке компонування може зекономити RAM. Перевіряйте map-файл і linker script, а не виводьте розташування з одного `const`. Для значення, яке змінюється після старту, потрібна змінна RAM; початкове значення такої змінної може зберігатися в образі й копіюватися startup code.[^embedded-ld-layout]

У linker script важливо розрізняти адресу виконання й адресу завантаження. Незмінний об'єкт часто має обидві адреси у Flash, тоді як змінні з початковими значеннями можуть мати адресу виконання в RAM і копію-джерело у Flash. Отже, навіть ненульове значення саме собою не визначає секцію: впливають mutability, атрибути секцій, оптимізація та схема пам'яті плати.[^embedded-ld-layout]

Якщо адреса об'єкта спостерігається зовнішнім кодом або потрібен гарантований доступ з периферії, перевірте, що compiler не оптимізував його і що секція не потрапила до недоступного регіону. Для конкретної збірки map-файл є практичною відповіддю, а linker script пояснює, чому адреса саме така.

**Типові помилки:**
- Вважати, що `const` у C тотожне зберіганню в ROM.
- Приписувати кожному глобальному `const` окремі байти Flash, навіть коли compiler усунув об'єкт.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
