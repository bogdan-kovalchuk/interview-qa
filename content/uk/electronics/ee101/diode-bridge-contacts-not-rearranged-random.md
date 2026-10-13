---
id: emb-elee-0181
title: "Чому не можна переставляти контакти діодного моста навмання?"
description: "Чому не можна переставляти контакти діодного моста навмання?"
track: electronics
section: ee101
level: junior
type: pitfall
tags: []
status: published
updated: 2026-10-13
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
    applicability: "Походження питання: лекція 65, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-13; курс не є доказом цих тверджень."
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
  - source_id: libretexts-fiore-rectification
    title: "Fiore: Semiconductor Devices, 3.2 Rectification (Engineering LibreTexts)"
    url: "https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/03:_Diode_Applications/3.2:_Rectification"
    accessed: 2026-10-13
    kind: book
    version: null
    applicability: "Мостовий випрямляч: у кожному півперіоді проводять два діоди, струм через навантаження має один напрямок в обидва півперіоди, а напруга на навантаженні дорівнює напрузі вторинної обмотки мінус два падіння на діодах. Це рівень підручника, а не datasheet конкретного моста."
  - source_id: fiore-capacitors
    title: "Engineering LibreTexts: DC Electrical Circuit Analysis – A Practical Approach (Fiore), 8.2 Capacitance and Capacitors"
    url: "https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/DC_Electrical_Circuit_Analysis_-_A_Practical_Approach_(Fiore)/08:_Capacitors/8.2:_Capacitance_and_Capacitors"
    accessed: 2026-10-13
    kind: book
    version: null
    applicability: "Електролітичні конденсатори поляризовані: вставлені навпаки, вони можуть вийти з ладу катастрофічно. Розділ також дає i = C*dv/dt; ESR, пульсації та випрямлячі він не розглядає."
---

## Short answer

Два AC-виводи моста взаємозамінні: полярність виходу не залежить від того, який із них позитивний.[^libretexts-fiore-rectification] Фіксованими є лише «+» і «−», тож якщо вторинну обмотку підключити напряму до них, два діоди моста у зворотний півперіод замикають обмотку накоротко. Якщо ж обидва виводи обмотки опиняються на одному вузлі, обмотка закорочена безпосередньо.

## Detailed explanation

Міст із чотирьох діодів має два змінні входи та два вихідні виводи, «+» і «−». У кожному півперіоді проводять два діоди, і струм через навантаження тече в одному напрямку, тому вихід позитивний незалежно від того, який змінний вхід був позитивним.[^libretexts-fiore-rectification] Отже, два AC-виводи можна поміняти місцями без шкоди, а «+» і «−» – ні, бо від них залежить, з якою полярністю працюватимуть конденсатор і стабілізатор.

Розглянемо обмотку, підключену напряму до «+» і «−» (AC-виводи моста при цьому нікуди не приєднані). У півперіод, коли «+» позитивніший, конденсатор заряджається прямо від обмотки, без падіння на діоді. У протилежний півперіод два послідовні діоди моста, що ведуть від «−» до «+», відкриваються, обмотка фактично закорочена через них, а напруга на конденсаторі затискається приблизно на −1,4 В. Струм обмежує переважно опір обмотки. Небезпека: перегрів діодів, трансформатора й запобіжника.

Полярний конденсатор не розрахований на зворотну напругу: електролітичний конденсатор, вставлений навпаки, може вийти з ладу катастрофічно.[^fiore-capacitors] Тут на ньому з’являється зворотна напруга близько −1,4 В, тож він працює поза своїм призначенням.

**Приклад:** вторинна обмотка 12 В RMS має пік близько 17 В. У протилежний півперіод на обмотці ті самі 17 В, а діоди затискають конденсатор на −1,4 В, тож на опорі обмотки падає 17 − 1,4 ≈ 15,6 В. Припустімо опір обмотки 0,5 Ом (це припущення, а не дані конкретного трансформатора): струм близько 15,6 / 0,5 ≈ 31 А, а при 1 Ом – близько 16 А. Оцінка лише за опором, без урахування індуктивності обмотки; обидва значення – коротке замикання, а не робочий режим.

**Типові помилки:**

- Вважати, що AC-виводи і «+» з «−» можна міняти навмання: AC-виводи взаємозамінні, DC-виводи ні.
- Підключати вторинну обмотку напряму до «+» і «−», минаючи міст, щоб спростити монтаж.
- Ставити полярний конденсатор на вихід моста, не перевіривши полярність.

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
