---
id: emb-elintro-0291
title: "Яка температура плавлення евтектичного припою 63/37 SnPb?"
description: "Яка температура плавлення евтектичного припою 63/37 SnPb?"
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
    applicability: "Походження питання: лекція 25, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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
  - source_id: lucas-milhaupt-sn63pb37
    title: "Lucas-Milhaupt: 63Sn/37Pb solder alloy"
    url: https://www.lucasmilhaupt.com/EN/Products/63Sn37Pb.htm
    accessed: 2026-10-04
    kind: official
    version: null
    applicability: "Виробник вказує склад 63/37 і однакові solidus та liquidus 183 °C."
---

## Short answer

Евтектичний 63/37 SnPb плавиться при 183 °C: виробник указує однакові значення solidus і liquidus. На відміну від сплаву з інтервалом плавлення, він не проходить через широкий пастоподібний стан.[^lucas-milhaupt-sn63pb37]

## Detailed explanation

Евтектичний припій Sn63/Pb37 має solidus і liquidus 183 °C, тому плавиться при одній температурі, без інтервалу пастоподібного стану, характерного для неевтектичних складів.[^lucas-milhaupt-sn63pb37] Це температура самого сплаву, а не рекомендована температура жала паяльника.

Евтектика – склад, за якого рідка фаза переходить у тверду при найнижчій температурі для відповідної системи сплаву. У точці плавлення рідка й тверда фази можуть співіснувати, але сплав не має широкого двофазного інтервалу. З’єднання швидко переходить між твердим і рідким станом; якість пайки водночас залежить від змочування, флюсу, чистоти поверхонь і теплового режиму.[^lucas-milhaupt-sn63pb37]

Позначення 63/37 означає номінально 63 % олова та 37 % свинцю. Інший склад SnPb може мати інтервал плавлення, тому не можна переносити 183 °C на будь-який припій із цими металами.[^lucas-milhaupt-sn63pb37]

**Типова помилка:** називати 183 °C температурою паяльника. Це температура плавлення сплаву; жало налаштовують вище, щоб компенсувати тепловідвід і прогріти з’єднання, а точне значення залежить від процесу й компонентів.

Приклад: якщо температура всередині з’єднання досягає 183 °C, цей сплав плавиться. Виробник указує однакові 183 °C для solidus і liquidus, що підтверджує відсутність інтервалу між початком і завершенням плавлення.[^lucas-milhaupt-sn63pb37]

## Sources

<!-- generated from frontmatter -->
