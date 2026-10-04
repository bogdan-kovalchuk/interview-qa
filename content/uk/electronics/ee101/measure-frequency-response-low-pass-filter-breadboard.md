---
id: emb-elee-0104
title: "Як виміряти АЧХ RC-ФНЧ на макеті?"
description: "Як виміряти АЧХ RC-ФНЧ на макеті?"
track: electronics
section: ee101
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
    applicability: "Походження питання: лекція 50, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
  - source_id: aac-alternating-current
    title: "All About Circuits textbook, Volume II: AC"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: AC-кола, реактивний опір, фазори, імпеданс, фільтри й трансформатори; конкретні номінали й схеми курсу можуть відрізнятися."
  - source_id: tek-scope-frequency-response
    title: "Tektronix: Measuring Impedance and Capacitance with an Oscilloscope and Function Generator"
    url: https://download.tek.com/document/48W-29165-0%20Using%20an%20oscillocope%20and%20function%20generator%20to%20measure%20capacitor%204-24-2013%20DP.pdf
    accessed: 2026-10-04
    kind: official
    version: null
    applicability: "Підтримує практику вимірювання двох вузлів осцилографом і перевірку фактичних амплітуд; приклад Tektronix для вимірювання компонента, не спеціальний протокол атестації RC-ФНЧ."
  - source_id: tek-generator-load
    title: "Tektronix: Function generator amplitude and load impedance FAQ"
    url: https://www.tek.com/en/support/faqs/if-i-set-my-amplitude-my-afg3000-series-generator-actual-amplitude-measured-my-scope-or
    accessed: 2026-10-04
    kind: official
    version: null
    applicability: "Пояснює для AFG3000 розбіжність між налаштуванням амплітуди для навантаження 50 Ω і фактичним виміром на високоомному вході; поведінка залежить від моделі генератора."
  - source_id: aac-low-pass
    title: "All About Circuits: Low-pass Filters"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-8/low-pass-filters/
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: "Підтримує інтерпретацію точки −3 dB та вплив навантаження на характеристику простого RC-ФНЧ."
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: діоди, стабілітрони, біполярні й польові транзистори та джерела живлення; конкретні номінали й схеми курсу можуть відрізнятися."
---

## Short answer

Подайте синусоїду без DC-зміщення, вимірюючи CH1 на вході фільтра й CH2 на виході. На кожній частоті використайте фактичні `V_in` і `V_out`, обчисліть `A = V_out/V_in` та `G_dB = 20*log10(A)`, і перевірте налаштування навантаження генератора.[^tek-scope-frequency-response] [^tek-generator-load]

## Detailed explanation

Вимірювання частотної характеристики показує, як змінюється передавання сигналу зі зміною частоти. Для RC-ФНЧ зберіть схему з короткими з’єднаннями на макеті та спільною землею. Подайте синусоїдальний сигнал із нульовим DC-зміщенням, якщо схема не потребує окремого зміщення, і під’єднайте канал 1 осцилографа до входу, а канал 2 – до виходу. Така пара вимірювань дає фактичні напруги на обох вузлах, а не лише номінальне налаштування генератора.[^tek-scope-frequency-response]

Почніть із частоти значно нижче очікуваного зрізу, потім виміряйте поблизу нього і вище. На кожному кроці дочекайтеся стабільної синусоїди та запишіть частоту й амплітуди обох каналів в однаковому форматі – наприклад, RMS або peak-to-peak. Коефіцієнт амплітуди обчислюють як `A = V_out/V_in`, а відносний рівень – як `G_dB = 20*log10(A)`. Якщо амплітуда входу змінюється з частотою, це нормалізоване відношення допомагає порівнювати власне фільтр.[^tek-scope-frequency-response]

Приклад процедури: для кожної частоти запишіть `f`, `V_in`, `V_out`, `A` та `G_dB`, а потім побудуйте таблицю або графік `G_dB` від логарифма частоти. Для ідеального першого порядку RC-ФНЧ точка, де рівень приблизно на 3 dB нижчий за низькочастотний рівень, близька до частоти зрізу. На практиці номінали компонентів, навантаження виходу і вхідний опір вимірювального приладу можуть змінити криву.[^aac-low-pass]

Перед інтерпретацією перевірте, як генератор визначає амплітуду. Наприклад, деякі Tektronix AFG показують значення, розраховане для навантаження 50 Ω; із високоомним входом осцилографа виміряне значення може бути майже вдвічі більшим. Точна поведінка залежить від моделі, тож звірте режим load у меню або керівництві приладу та покладайтеся на вимір CH1 як на фактичний вхід фільтра.[^tek-generator-load]

**Типова помилка:** будувати характеристику за заданою генератором амплітудою і вихідним виміром, не перевіривши дійсний вхід. Розбіжність між режимами 50 Ω і High Z тоді помилково виглядає як підсилення чи ослаблення фільтра. Вимірюйте обидва вузли одночасно, використовуйте однакову метрику амплітуди й переконайтеся, що затискачі землі пробників під’єднані до землі схеми.[^tek-scope-frequency-response] [^tek-generator-load]

## Sources

<!-- generated from frontmatter -->
