---
id: emb-elee-0249
title: "З чого складається кварцовий генератор Пірса?"
description: "З чого складається кварцовий генератор Пірса?"
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
    applicability: "Походження питання: лекція 79, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-14; курс не є доказом цих тверджень."
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
  - source_id: ti-sn74lvc1gx04-oscillator
    title: "Texas Instruments: datasheet SN74LVC1GX04 (SCES581D), розділ 9 Application and Implementation"
    url: https://www.ti.com/lit/ds/symlink/sn74lvc1gx04.pdf
    accessed: 2026-10-14
    kind: official
    version: "SCES581D, October 2015"
    applicability: "Розділ 9 datasheet: приклад генератора Пірса з кварцом і інверторами, рекомендоване навантаження 16 пФ, роль R_F і R_s. Стосується цього пристрою й наведених у ньому значень; не доводить загальних властивостей кварцових модулів."
---

## Short answer

Підсилювальний інвертор (у прикладі TI небуферизований), кварцовий резонатор, два навантажувальні конденсатори C1 і C2 та резистор зворотного зв’язку R_F, який зміщує інвертор у лінійну область.[^ti-sn74lvc1gx04-oscillator] У прикладі TI вихід формує буферизований інвертор, що дає сигнал повного розмаху.[^ti-sn74lvc1gx04-oscillator]

## Detailed explanation

Пірсовий генератор – це петля, у якій інвертор працює як підсилювач, а кварц задає частоту. У прикладі TI SN74LVC1GX04 є два інвертори: небуферизований є підсилювачем генератора. У прикладі TI вихід формує буферизований інвертор, що дає сигнал повного розмаху.[^ti-sn74lvc1gx04-oscillator] Резистор R_F, зазвичай від 1 МОм до 10 МОм, зміщує небуферизований інвертор у лінійну область роботи, тобто туди, де він підсилює, а не перемикає як цифровий елемент.[^ti-sn74lvc1gx04-oscillator]

Кварцовий резонатор з’єднує вхід і вихід інвертора, а конденсатори C1 і C2 – кожен свій вузол із землею. TI пише, що значення C1 і C2 обирають так, щоб із них обчислити навантаження C_L, а рекомендоване C_L для кварца в прикладі дорівнює 16 пФ.[^ti-sn74lvc1gx04-oscillator] Для рівних C1 = C2 = C виходить `C_L = C/2 + C_stray`, де `C_stray` – паразитна ємність плати й виводів. Приклад: при C1 = C2 = 26 пФ і `C_stray = 3 пФ` (припущення для ілюстрації) маємо `C_L = 26*26/(26+26) + 3 = 13 + 3 = 16 пФ`, тобто збіг із прикладом TI.

Послідовний резистор R_s обмежує струм через кварц. TI пише, що його значення залежить від максимальної потужності розсіювання кварца, і що зменшення R_s підвищує підсилення замкненого контуру, якщо потужність лишається в межах.[^ti-sn74lvc1gx04-oscillator] Перевірку починають із того, що без кварца схема не має коливатися; для такого тесту кварц замінюють еквівалентним паралельним резистивним опором.[^ti-sn74lvc1gx04-oscillator]

Підсилення небуферизованого інвертора падає разом із напругою живлення, а це зменшує підсилення замкненого контуру. Тому TI радить перевіряти, що схема коливається на потрібній частоті при найнижчій і найвищій напрузі живлення.[^ti-sn74lvc1gx04-oscillator]

**Типові помилки:**

- Брати R_F і R_s довільно: R_F зміщує інвертор у лінійну область, а R_s обмежує струм через кварц.[^ti-sn74lvc1gx04-oscillator]
- Вважати, що C_L дорівнює C1 або C2: при рівних C1 і C2 навантаження дорівнює C/2 плюс паразитна ємність.
- Перевіряти генератор лише при номінальній напрузі живлення, хоча підсилення падає разом із VCC.[^ti-sn74lvc1gx04-oscillator]

## Sources

<!-- generated from frontmatter -->
