---
id: emb-elintro-0068
title: "9V крона – зі скількох елементів вона складається всередині?"
description: "9V крона – зі скількох елементів вона складається всередині?"
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
    applicability: "Походження питання: лекція 8, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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
  - source_id: energizer-9v
    title: "Energizer 6LR61 Alkaline Power: Product Datasheet"
    url: https://data.energizer.com/pdfs/alk-power-9v.pdf
    accessed: 2026-10-04
    kind: official
    version: null
    applicability: "Підтверджує конкретну модель 6LR61 як лужну батарею формату 9 V; не описує внутрішню кількість окремих елементів."
  - source_id: energizer-522-datasheet
    title: "Energizer 522 9V alkaline battery datasheet"
    url: https://data.energizer.com/pdfs/522.pdf
    accessed: 2026-10-04
    kind: official
    version: "522GL1019"
    applicability: "Позначення IEC 6LR61/6LF22 і номінальна напруга 9.0 V лужної батареї Energizer 522."
  - source_id: battery-nomenclature
    title: "Wikipedia: Battery nomenclature (IEC 60086 designation system)"
    url: https://en.wikipedia.org/wiki/Battery_nomenclature
    accessed: 2026-10-04
    kind: community
    version: null
    applicability: "Система позначень IEC 60086: перша цифра коду вказує кількість послідовних елементів (приклад 6F22 – шість елементів)."
---

## Short answer

Лужна батарея 9 V має позначення IEC `6LR61` (або `6LF22`), а перша цифра такого коду означає кількість послідовно з’єднаних елементів – тобто шість елементів.[^energizer-522-datasheet] [^battery-nomenclature] Номінальні напруги послідовних елементів додаються: `6 × 1.5 V = 9 V`.[^aac-direct-current] Батареї формату 9 V з іншою хімією, наприклад літієві чи NiMH, можуть мати іншу кількість елементів.

## Detailed explanation

Батарея формату 9 V – це батарейний блок, а не обов’язково один електрохімічний елемент. У поширеній лужній конструкції всередині є шість елементів, з’єднаних послідовно. Кожен має номінальну напругу близько 1.5 V, тож сума номіналів дає 9 V.[^energizer-522-datasheet] [^battery-nomenclature]

Послідовне з’єднання означає, що позитивний вивід одного елемента сполучений із негативним виводом наступного. Через усі елементи проходить той самий струм, а їхні електрорушійні сили додаються. Наприклад, для шести однакових елементів `V_total = 6*1.5 V = 9 V` за номінальними значеннями.[^aac-direct-current]

Однак цифра 9 V на корпусі є номінальним позначенням, а не обіцянкою незмінної напруги. Напруга на клемах залежить від хімії, заряду, температури, навантаження та внутрішнього опору. Не всі батареї цього формату мають однакову внутрішню конструкцію: виробник може використати іншу хімію або розташування елементів. Тому відповідь «шість» стосується поширеного лужного варіанта, а не кожного можливого 9-вольтового блока.[^energizer-9v]

**Типова помилка:** вважати кількість елементів універсальною лише за позначкою напруги. Для конкретної моделі слід звірятися з її документацією, бо однакова номінальна напруга не гарантує однакової хімії чи внутрішньої будови.[^energizer-9v]

## Sources

<!-- generated from frontmatter -->
