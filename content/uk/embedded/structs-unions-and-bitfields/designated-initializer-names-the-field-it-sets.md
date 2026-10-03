---
id: emb-structs-0029
title: "Що таке designated initializer і чому він корисний для структур?"
description: "Designated initializer явно вказує, яке поле ініціалізується: .baud = 115200."
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
---

## Short answer

**Designated initializer** явно вказує, яке поле ініціалізується: `.baud = 115200`.

Це робить код стійкішим до зміни порядку полів і читабельнішим для configuration structs. Незаповнені поля отримують zero initialization, якщо initializer є aggregate initializer.

Embedded-правило: для driver config краще `UART_Config cfg = { .baud = 115200, .parity = PARITY_NONE };`, ніж positional initializer із довгим списком чисел.[^iso-c-n1570]

## Detailed explanation

Designated initializer у C називає поле або елемент масиву, який отримує задане значення, наприклад `.baud = 115200`. Такий запис є частиною синтаксису aggregate initializer, визначеного стандартом C починаючи з C99.[^iso-c-n1570]

Звичайний positional initializer прив’язує значення до порядку полів у декларації. Із designated initializer зв’язок видно безпосередньо: читач бачить, що `115200` є baud rate, а не, наприклад, кодом parity. Це також спрощує перегляд змін у структурі: додавання іншого поля не змінює значення, призначені явно названим полям. Саме тому такий стиль зручний для конфігурацій периферійних драйверів.[^iso-c-n1570]

Позначення поля не є перевіркою правильності його значення. Наприклад, `.baud = 115200` синтаксично однозначне, але прошивка все одно має перевірити, чи підтримують таку швидкість конкретний UART і його clock. Так само пропущені поля aggregate initializer отримують нульове значення, а не автоматично обраний безпечний режим; це важливо для полів, де нуль означає вимкнення або невалідну конфігурацію.[^iso-c-n1570]

Приклад: у `struct UartConfig { uint32_t baud; uint8_t parity; uint8_t stop_bits; };` запис `{ .baud = 115200, .parity = 0, .stop_bits = 1 }` показує призначення кожного числа. Коли конфігурація змінюється, назви полів допомагають помітити помилку під час рев’ю, хоча не замінюють перевірки допустимих діапазонів.

**Типова помилка:** вважати designated initializer гарантією коректної конфігурації. Він усуває неоднозначність позиційного зіставлення, але значення та поведінку периферії все одно треба перевіряти за документацією пристрою.[^iso-c-n1570]

## Sources

<!-- generated from frontmatter -->
