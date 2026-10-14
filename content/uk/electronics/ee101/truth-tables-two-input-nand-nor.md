---
id: emb-elee-0239
title: "Яка таблиця істинності двовхідних AND, NAND, OR і NOR?"
description: "Яка таблиця істинності двовхідних AND, NAND, OR і NOR?"
track: electronics
section: ee101
level: junior
type: concept
tags: []
status: published
updated: 2026-10-14
content_revision: 2
reconciled_with:
  en: 2
anki:
  export: true
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), картки курсу"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
    accessed: 2026-09-27
    kind: community
    version: null
    applicability: "Походження питання: лекція 77, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-14; курс не є доказом цих тверджень."
  - source_id: aac-alternating-current
    title: "All About Circuits textbook, Volume II: AC"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: AC-кола, реактивний опір, фазори, імпеданс, фільтри й трансформатори; конкретні номінали й схеми курсу можуть відрізнятися."
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: діоди, стабілітрони, біполярні й польові транзистори та джерела живлення; конкретні номінали й схеми курсу можуть відрізнятися."
  - source_id: ti-hc00
    title: "TI SN74HC00 quadruple NAND gates datasheet"
    url: https://www.ti.com/lit/ds/symlink/sn74hc00.pdf
    accessed: 2026-10-14
    kind: official
    version: "SCLS181H"
    applicability: "Таблиця 8-1 (Function Table): NAND дає L лише при H і H; розділ 8.4: стандартні CMOS-входи не можна залишати плаваючими. Лише 74HC00."
  - source_id: ti-hc08
    title: "TI SN74HC08 quadruple 2-input AND gates datasheet"
    url: https://www.ti.com/lit/ds/symlink/sn74hc08.pdf
    accessed: 2026-10-14
    kind: official
    version: "SCLS081J"
    applicability: "Таблиця 7-1 (Function Table): AND дає H лише при H і H; Boolean-функція Y = A AND B. Лише 74HC08."
  - source_id: ti-hc32
    title: "TI SN74HC32 quadruple 2-input OR gates datasheet"
    url: https://www.ti.com/lit/ds/symlink/sn74hc32.pdf
    accessed: 2026-10-14
    kind: official
    version: "SCLS200F"
    applicability: "Таблиця 8-1 (Function Table): OR дає L лише при L і L; Boolean-функція Y = A OR B. Лише 74HC32."
  - source_id: ti-hc02
    title: "TI SN74HC02 quadruple 2-input NOR gates datasheet"
    url: https://www.ti.com/lit/ds/symlink/sn74hc02.pdf
    accessed: 2026-10-14
    kind: official
    version: "SCLS076G"
    applicability: "Таблиця 8-1 (Function Table): NOR дає H лише при L і L; вихід інвертований відносно OR. Лише 74HC02."
  - source_id: ti-hc04
    title: "TI SN74HC04 hex inverters datasheet"
    url: https://www.ti.com/lit/ds/symlink/sn74hc04.pdf
    accessed: 2026-10-14
    kind: official
    version: "SCLS078H"
    applicability: "Таблиця 8-1 (Function Table): вхід L дає вихід H, вхід H дає вихід L. Лише 74HC04."
---

## Short answer

AND дає 1 лише при 11[^ti-hc08], а NAND дає 0 лише при 11.[^ti-hc00] OR дає 0 лише при 00[^ti-hc32], а NOR дає 1 лише при 00.[^ti-hc02] Формули: `Y = A*B` (AND)[^ti-hc08], `Y = NOT(A*B)` (NAND)[^ti-hc00], `Y = A+B` (OR)[^ti-hc32], `Y = NOT(A+B)` (NOR)[^ti-hc02], `Y = NOT A` (NOT).[^ti-hc04]

## Detailed explanation

Таблиця істинності перелічує вихід для кожної комбінації входів. Для двох входів таких комбінацій `2^2 = 4` (00, 01, 10, 11), для трьох – `2^3 = 8`. Таблиця істинності однозначно визначає логічну функцію, але не сам вентиль: TTL і CMOS NAND мають одну таблицю, тому елементи з однаковою таблицею взаємозамінні за логікою, але не обов’язково за рівнями, навантаженням і швидкістю.

Для входів 00 AND і OR дають 0, а NAND і NOR – 1. Для 01 і 10 AND і NOR дають 0, а NAND і OR – 1. Для 11 AND і OR дають 1, а NAND і NOR – 0.[^ti-hc00][^ti-hc02][^ti-hc08][^ti-hc32]

NAND і NOR – це інверсії AND і OR у кожному рядку: `NAND = NOT(AND)`, `NOR = NOT(OR)`. Звідси випливає закон де Моргана `NOT(A*B) = NOT A + NOT B`, тобто NAND – це OR з інвертованими входами. Перевірка за рядками: для 01 обидві частини дають 1, для 11 – 0.

Таблиця описує ідеальні логічні рівні. Фізичний вхід розпізнається як 0 або 1 лише в межах `VIL` і `VIH`, а вихід має відповідати `VOL` і `VOH`. Для плаваючого входу таблиця не працює, бо стандартні CMOS-входи не можна залишати плаваючими.[^ti-hc00]

**Типові помилки:**

- Плутати NAND з AND: NAND дає 0 лише при 11, тобто це інвертований результат.
- Вважати, що NOR дає 1 при будь-якій одиниці на вході: він дає 1 лише при 00.
- Для трьох входів брати 4 рядки замість 8.

## Sources

<!-- generated from frontmatter -->
