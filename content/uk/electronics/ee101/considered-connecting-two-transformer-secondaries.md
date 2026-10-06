---
id: emb-elee-0176
title: "Що треба враховувати, з’єднуючи дві вторинні обмотки трансформатора?"
description: "Що треба враховувати, з’єднуючи дві вторинні обмотки трансформатора?"
track: electronics
section: ee101
level: junior
type: pitfall
tags: []
status: published
updated: 2026-10-06
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
    applicability: "Походження питання: лекція 64, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-06; курс не є доказом цих тверджень."
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
  - source_id: kuphaldt-phasing
    title: "Workforce LibreTexts: Lessons in Electric Circuits, Vol. II (Kuphaldt), 10.4 Phasing"
    url: "https://workforce.libretexts.org/Bookshelves/Electronics_Technology/Electric_Circuits_II_-_Alternating_Current_(Kuphaldt)/10:_Transformers/10.04:_Phasing"
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "Позначки dot convention на обмотках трансформатора вказують виводи однакової миттєвої полярності; збіг або розбіжність позначок визначає нульовий або 180-градусний зсув фази між обмотками. Розділ не розглядає послідовне чи паралельне з’єднання вторинних обмоток."
  - source_id: esp-transformers-part2
    title: "Elliott Sound Products: Beginners’ Guide to Transformers, Part 2 (section 8, Windings in Series and Parallel)"
    url: https://sound-au.com/xfmr2.htm
    accessed: 2026-10-06
    kind: book
    version: "page updated January 2023"
    applicability: "Послідовне й паралельне з’єднання вторинних обмоток: приклад 2 x 25 В / 5 А (250 VA) дає 50 В / 5 А послідовно або 25 В / 10 А паралельно; послідовно в фазі напруги додаються, у протифазі віднімаються й це не шкодить трансформатору; паралельно допустимо лише з однаковою напругою й у фазі, розрахунок циркулюючого струму для обмоток по 0,25 Ом, порада перевіряти напруги й користуватися запобіжником. Авторська навчальна стаття практика, а не стандарт чи datasheet; числа в прикладах ілюстративні."
  - source_id: hammond-266m20
    title: "Hammond Manufacturing: 266M20 power transformer, dual primary and secondary (datasheet)"
    url: https://www.hammfg.com/files/parts/pdf/266M20.pdf
    accessed: 2026-10-06
    kind: official
    version: null
    applicability: "Для моделі 266M20 (60 VA) виробник вказує вторинні обмотки: послідовно (з середньою точкою) 20 В / 3 А, паралельно 10 В / 6 А, і дозволяє використовувати їх з середньою точкою, паралельно або окремо. Значення стосуються лише цієї моделі; для інших трансформаторів схему з’єднання беруть з їхнього datasheet."
---

## Short answer

Спершу з’ясовують фазування за позначками (dots) на виводах і номінальні напруги обмоток.[^kuphaldt-phasing] Послідовне з’єднання в фазі складає напруги, а струм обмежує обмотка з меншим номіналом; у протифазі напруги віднімаються.[^esp-transformers-part2] Паралельно з’єднують лише обмотки з однаковою напругою, у фазі й тільки якщо це дозволяє виробник: у протифазі паралельне з’єднання майже коротко замикає обмотки.[^esp-transformers-part2]

## Detailed explanation

**Фазування.** Кожна обмотка має початок і кінець, а dot convention позначає виводи з однаковою миттєвою полярністю.[^kuphaldt-phasing] Дві обмотки, з’єднані послідовно в фазі, дають суму напруг, а в протифазі – різницю.[^esp-transformers-part2] Приклад: трансформатор із двома обмотками 25 В / 5 А (250 VA) у послідовному з’єднанні дає 50 В при 5 А, а в паралельному – 25 В при 10 А; потужність у VA та сама.[^esp-transformers-part2] Виробник вказує такі пари в datasheet: для Hammond 266M20 (60 VA) це 20 В / 3 А послідовно й 10 В / 6 А паралельно, а `20*3 = 10*6 = 60 VA`.[^hammond-266m20]

**Послідовне з’єднання.** Обмотки можна з’єднувати послідовно незалежно від напруги, а максимальний струм дорівнює номіналу обмотки з найменшим струмом.[^esp-transformers-part2] Помилка фазування тут не руйнівна: для двох однакових обмоток у протифазі вихід дорівнює нулю, і трансформатору це не шкодить.[^esp-transformers-part2] Тому таку помилку видно одразу за нульовою напругою.

**Паралельне з’єднання.** Воно допустиме лише для обмоток з однаковою напругою, з’єднаних у фазі: навіть різниця 1 В породжує циркулюючий струм, обмежений лише опором обмоток.[^esp-transformers-part2] Для двох обмоток по 0,25 Ом різниця 1 В дає `1/0.5 = 2 A` марних втрат і зайвий нагрів. Для двох обмоток по 25 В у протифазі напруга контуру дорівнює 50 В, і струм має порядок `50/0.5 = 100 A`, доки не спрацює запобіжник або не перегорить обмотка.[^esp-transformers-part2] Значення 0,25 Ом – приклад для обмотки на 5 А з тієї самої статті, а реальний струм залежить ще й від індуктивності розсіювання.

**Як діяти.** Паралельну схему використовують лише тоді, коли її дозволяє виробник: для 266M20 він прямо вказує, що вторинні обмотки можна використовувати з середньою точкою, паралельно або окремо.[^hammond-266m20] Якщо інформації немає, напруги обмоток вимірюють і не паралелять їх, коли вони відрізняються більш ніж на кілька сотень мілівольт; нове з’єднання перевіряють із запобіжником.[^esp-transformers-part2]

**Типові помилки:**

- Паралелити обмотки з різною напругою або невідомим фазуванням.
- Вважати, що паралельне з’єднання збільшує напругу, а послідовне – струм (насправді навпаки).
- У послідовному з’єднанні брати струм більший за номінал найслабшої обмотки.
- Перевіряти нове з’єднання без запобіжника.

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
