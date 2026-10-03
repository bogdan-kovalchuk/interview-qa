---
id: emb-elintro-0257
title: "Чому `R_DS(on)` треба дивитися при конкретній `V_GS`?"
description: "Чому on-resistance MOSFET залежить від напруги gate-source?"
track: electronics
section: introduction
level: junior
type: concept
tags: []
status: published
updated: 2026-10-04
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
    applicability: "Походження питання: лекція 23, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
  - source_id: aac-direct-current
    title: "All About Circuits textbook, Volume I: DC"
    url: https://www.allaboutcircuits.com/textbook/direct-current/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: DC-кола, закон Ома, закони Кірхгофа, джерела й вимірювання; конкретні номінали й схеми курсу можуть відрізнятися."
  - source_id: infineon-optimos
    title: "Infineon OptiMOS Power MOSFET Datasheet Explanation"
    url: https://www.infineon.com/assets/row/public/documents/24/42/infineon-mosfet-optimos-datasheet-explanation-applicationnotes-en.pdf
    accessed: 2026-10-04
    kind: official
    version: "AN 2012-03 V1.1"
    applicability: "Пояснює залежність R_DS(on) від V_GS та тестування V_GS(th); приклади не є параметрами кожної деталі."
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: діоди, стабілітрони, біполярні й польові транзистори та джерела живлення; конкретні номінали й схеми курсу можуть відрізнятися."
---

## Short answer

`R_DS(on)` залежить від `V_GS`, струму та температури, тому треба використовувати гарантоване значення datasheet при умовах, близьких до реального драйвера й навантаження.[^infineon-optimos] Порогова `V_GS(th)` означає лише початок провідності за малого тестового струму, а не повне відкривання.[^infineon-optimos]

## Detailed explanation

On-resistance MOSFET не є сталою незалежно від керування величиною: `R_DS(on)` вимірюють за заданих `V_GS`, drain current і температури. Вища напруга gate-source зазвичай сильніше формує канал і зменшує опір у дозволеному діапазоні, але допустиму напругу gate теж обмежує datasheet. Для вибору беруть гарантовану межу, а не типове значення графіка, якщо конструкція має працювати за найгірших умов.[^infineon-optimos]

У таблиці шукайте рядки `R_DS(on)` з умовою тесту. Якщо MOSFET керується GPIO 3.3 V, число, гарантоване лише при 10 V, не доводить, що транзистор матиме такий самий опір при 3.3 V. Перевірте, чи є гарантоване значення при доступній напрузі; графік типових характеристик може допомогти оцінці, але не є виробничою гарантією. За малих `V_GS` опір також змінюється з температурою та струмом.[^infineon-optimos]

Не плутайте `V_GS(th)` з напругою повного відкривання. Порогове значення задають за малим тестовим drain current, отже воно показує, коли канал тільки починає проводити. Воно не гарантує низького падіння напруги чи малого нагрівання у навантаженні. Для оцінки втрат у простому повністю ввімкненому режимі використовуйте `P = I²*R_DS(on)`, із опором за робочої напруги керування та з поправкою на гарячий кристал.[^infineon-optimos]

**Типові помилки:**

- Порівнювати опори при різних `V_GS` так, ніби умови однакові.
- Обрати logic-level MOSFET лише за низьким `V_GS(th)`, не перевіривши `R_DS(on)`.
- Вважати типове значення достатнім доказом для worst-case розрахунку.

## Sources

<!-- generated from frontmatter -->
