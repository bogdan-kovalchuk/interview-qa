---
id: emb-elintro-0295
title: "Чому антипаралельним LED все одно потрібен резистор?"
description: "Чому антипаралельним LED все одно потрібен резистор?"
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
    applicability: "Походження питання: лекція 26, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
  - source_id: aac-direct-current
    title: "All About Circuits textbook, Volume I: DC"
    url: https://www.allaboutcircuits.com/textbook/direct-current/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: DC-кола, закон Ома, закони Кірхгофа, джерела й вимірювання; конкретні номінали й схеми курсу можуть відрізнятися."
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: діоди, стабілітрони, біполярні й польові транзистори та джерела живлення; конкретні номінали й схеми курсу можуть відрізнятися."
  - source_id: ti-led-resistor
    title: "Texas Instruments: AN-1293 Driving RGB LED Using LP3936"
    url: https://www.ti.com/jp/lit/pdf/snva071
    accessed: 2026-10-04
    kind: official
    version: "SNVA071A, revised April 2013"
    applicability: "Формула обмежувального резистора; приклади стосуються LP3936."
  - source_id: kingbright-led-ratings
    title: "Kingbright: 2022–2023 Catalog, Technical Notes"
    url: https://www.kingbrightusa.com/webimages/2021/ecatalog/files/basic-html/page63.html
    accessed: 2026-10-04
    kind: official
    version: "2022–2023 catalog"
    applicability: "Вказує зворотну напругу 5 V для окремих моделей; не універсальний рейтинг LED."
---
## Short answer

Антипаралельне з’єднання визначає, який LED проводить за кожної полярності, але не обмежує струм. Послідовний резистор задає його приблизно як `(V_supply - V_f)/R` і захищає провідний LED від надмірного струму.[^ti-led-resistor]

## Detailed explanation

В антипаралельній парі за однієї полярності один LED проводить у прямому напрямку, а за протилежної – другий. Проте LED має нелінійну вольт-амперну характеристику: невелике зростання напруги понад його пряме падіння може спричинити значний приріст струму. Сам факт, що пара змінює провідний LED, струм не обмежує.[^ti-led-resistor]

Резистор, увімкнений послідовно з парою, працює в обох напрямках. Для заданої полярності оцінюють струм як `I = (V_supply - V_f)/R`, де `V_f` – пряме падіння того LED, який проводить. Для протилежної полярності слід підставити пряме падіння другого LED. Оскільки їхні `V_f` можуть відрізнятися, струми також можуть бути різними.[^ti-led-resistor]

Приклад: за джерела 5 V, `V_f = 2 V` і резистора 330 Ω отримаємо приблизно 9.1 mA. Це припускає стабільне джерело й номінальний резистор; під час проєктування перевіряють крайні значення живлення, допуск резистора, прямі напруги обох LED та їхні граничні струми.[^ti-led-resistor]

**Типова помилка:** підключити антипаралельну пару до джерела без обмеження струму. Провідний LED може вийти за допустимий режим. Перевіряйте також зворотну напругу непровідного LED за його datasheet; резистор обмежує струм кола, але сам не гарантує безпечної зворотної напруги.[^kingbright-led-ratings]

Отже, резистор потрібен для обох напрямків струму, а номінал добирають за джерелом, характеристиками компонентів і бажаною яскравістю. Для змінного сигналу потрібно також перевірити потужність резистора та режим перемикання.

## Sources

<!-- generated from frontmatter -->
