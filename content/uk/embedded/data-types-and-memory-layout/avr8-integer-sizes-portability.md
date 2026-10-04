---
id: emb-dtypes-0102
title: "Які розміри integer-типів на AVR8 і чому не можна переносити припущення з 32-bit MCU?"
description: "На типовому AVR8 int має 16 біт, на 32-bit MCU зазвичай 32, тому для portable firmware слід використовувати fixed-width типи."
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
  - source_id: avr-libc-faq-types
    title: "AVR-LibC User Manual: Frequently Asked Questions"
    url: https://avrdudes.github.io/avr-libc/avr-libc-user-manual-2.1.0/FAQ.html
    accessed: 2026-10-04
    kind: official
    version: "2.1.0"
    applicability: "Типові розміри типів конкретно для avr-gcc/AVR-LibC; розмір pointers залежить від адресного простору й target."
---

## Short answer

Для звичайного avr-gcc на AVR8 `char` має 8 біт, `int` 16 біт, а `long` 32 біти; це властивість цього toolchain/target, не всіх 8-bit MCU.[^avr-libc-faq-types] На типових 32-bit MCU `int` часто 32-бітний, але точний розмір задає ABI, тому діапазон арифметики та layout структур можуть відрізнятися. <span class="warn">Для полів із вимогою точної ширини використовуй `uint8_t`, `uint16_t` або `uint32_t` із `stdint.h`; для `printf` узгоджуй формат із типом.</span>[^iso-c-n1570]

## Detailed explanation

Розмір типу C визначає ABI конкретної реалізації, а не назва архітектури сама по собі. У типовій конфігурації avr-gcc для AVR8 `char` має 8 біт, `int` – 16, `long` – 32, а `long long` – 64. У багатьох 32-bit MCU `int` має 32 біти, проте код має спиратися на документацію компілятора й target, а не на ярлик «32-bit».[^avr-libc-faq-types]

Різниця проявляється не лише в максимальному числі. Вирази з `int` обчислюються з діапазоном цього типу, а signed overflow у C має undefined behavior; unsigned арифметика натомість виконується за модулем `2^N`. Отже, код, що накопичує лічильник або множить значення в `int`, може мати інший результат на AVR і на MCU з ширшим `int`. Формат `printf` теж має відповідати фактичному типу аргументу: невідповідність специфікатора й типу є помилкою, а однакова кількість бітів не робить усі типи форматно взаємозамінними.[^iso-c-n1570]

Фіксовані типи з `<stdint.h>` доречні для протоколів, регістрів і полів, де ширина є частиною контракту. `uint32_t` гарантує рівно 32 біти, якщо реалізація надає цей optional exact-width type; натомість `uint_least32_t` гарантує щонайменше 32 біти. Це не гарантує однаковий padding або binary layout усієї `struct` між ABI: для зовнішнього формату серіалізуйте поля явно, а не передавайте пам’ять структури напряму.[^iso-c-n1570]

Покажчик – окреме питання: avr-libc описує звичайні data pointers як 16-бітні для типового AVR, але function pointers та адресування program memory мають свої правила, а підтримувані AVR варіанти відрізняються. Тому не переносіть і pointer width, і `sizeof(int)` з одного target на інший; перевіряйте конкретний MCU, compiler flags і memory model.[^avr-libc-faq-types]

**Як уникнути помилки:**

- Перевірте `CHAR_BIT`, `INT_MAX` та `sizeof` у build для кожної цільової конфігурації.
- Використовуйте exact-width типи там, де ширина є частиною протоколу; для лічильників використовуйте тип із достатнім діапазоном.
- Вибирайте `printf` macros з `<inttypes.h>` для типів `stdint.h`, а не вгадуйте `%d` чи `%ld`.

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
