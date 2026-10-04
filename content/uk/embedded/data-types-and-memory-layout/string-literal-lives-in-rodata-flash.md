---
id: emb-dtypes-0035
title: "Де буде рядковий літерал `\"Hello, World!\"` у пам'яті embedded програми?"
description: "Рядкові літерали часто лежать у read-only секції на кшталт .rodata у Flash, але розміщення залежить від toolchain і linker script."
track: embedded
section: data-types-and-memory-layout
level: junior
type: mechanism
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
---

## Short answer

У типовій embedded-збірці рядковий літерал часто розміщений у read-only секції на кшталт `.rodata`, відображеній у Flash, але це залежить від toolchain і linker script, а не гарантується C.

Однаковий рядок використовується лише один раз (deduplication залежить від компілятора).

<span class="warn">Окремий об’єкт</span>: `char arr[] = "hello";` створює змінний масив із копією символів; автоматичний локальний масив зазвичай розміщений у stack, а static-масив – у writable static storage. Перевіряйте map-файл цільової збірки.[^iso-c-n1570]

## Detailed explanation

Рядковий літерал у C задає масив символів зі static storage duration, що містить символи та завершальний нуль. Мова гарантує тривалість існування цього масиву, але не конкретну секцію `.rodata` чи розташування у Flash.[^iso-c-n1570]

У типовій embedded-збірці linker розміщує літерали в read-only секції на Flash, щоб вони не займали RAM. Це домовленість toolchain, а не гарантія C: linker script задає відображення секцій у фізичну пам’ять, а архітектура може мати окремий адресний простір програмної пам’яті. Перевіряйте linker script і map-файл для конкретної цілі.

Не плутайте літерал із масивом, який ним ініціалізують. У `char arr[] = "hello";` створюється окремий змінний масив із копією символів. Локальний автоматичний `arr` зазвичай займає стек, а об’єкт зі static storage duration – writable static storage, часто `.data`; його байти потребують RAM під час роботи. Вказівник `const char *p = "hello";` зазвичай посилається на літерал, але спроба змінити сам літерал має undefined behavior у C.[^iso-c-n1570]

**Типові помилки:**

- Стверджувати, що всі літерали гарантовано перебувають у Flash без перевірки linker-конфігурації.
- Вважати, що `char arr[]` є лише іншим записом вказівника на літерал.

Для оцінки RAM відрізняйте місце літерала від об’єктів, які копіюють його вміст, і враховуйте можливі копії, створені бібліотеками.

## Sources

<!-- generated from frontmatter -->
