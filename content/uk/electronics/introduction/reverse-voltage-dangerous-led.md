---
id: emb-elintro-0123
title: "Чому зворотна напруга небезпечна для LED?"
description: "Чому зворотна напруга небезпечна для LED?"
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
    applicability: "Походження питання: лекція 12, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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
  - source_id: kingbright-wp154a4
    title: "Kingbright WP154A4SEJ3VBDZGC/CA datasheet"
    url: https://www.kingbrightusa.com/images/catalog/SPEC/WP154A4SEJ3VBDZGC-CA.pdf
    accessed: 2026-10-04
    kind: official
    version: null
    applicability: "Datasheet LED Kingbright WP154A4SEJ3VBDZGC/CA: V_R = 5 V, температурний коефіцієнт V_F −2.0 mV/°C (Hyper Red) за I_F = 20 mA."
---

## Short answer

LED зазвичай має невеликий граничний `V_R`, але конкретне значення потрібно перевіряти в datasheet. Для Kingbright WP154A4SEJ3VBDZGC/CA вказано 5 V.[^kingbright-wp154a4] За перевищення рейтингу можливий зворотний пробій і пошкодження, тож не варто вважати всі LED однаково стійкими до зворотної напруги.[^kingbright-wp154a4]

## Detailed explanation

У прямому напрямку LED проводить струм і випромінює світло, а за зворотної полярності його p-n-перехід блокує струм, окрім малого витоку. Зворотна напруга не є необмежено безпечною: виробник задає максимальне `V_R`, перевищення якого може спричинити пробій, деградацію або відмову компонента.[^aac-semiconductors]

Універсального рейтингу для всіх LED немає. Наприклад, datasheet Kingbright WP154A4SEJ3VBDZGC/CA вказує `V_R = 5 V`. Це параметр конкретної серії, а не загальне правило; для проєкту слід дивитися абсолютні максимальні рейтинги власної деталі.[^kingbright-wp154a4]

Зворотна напруга може виникати в колах зі змінною полярністю або під час перемикання індуктивного навантаження. Її обмежують відповідною схемою захисту, наприклад діодом, включеним зустрічно-паралельно, а не покладаються на пробій LED.[^aac-semiconductors]

**Типова помилка:** сприймати малий зворотний витік як захист. Він описує поведінку нижче рейтингу; після його перевищення струм не гарантовано залишиться малим, а допустима напруга залежить від деталі.[^aac-semiconductors]

Також слід розрізняти максимальну зворотну напругу та зворотний струм, зазначений за тестової напруги: таблиця струму не означає, що перехід може безпечно витримати будь-який рівень. У Kingbright datasheet `V_R = 5 V` наведено як абсолютний рейтинг, тоді як струм витоку подано окремим параметром для тестування при цій напрузі. Рейтинг не є робочою ціллю, і в реальному колі бажано лишати запас на перехідні процеси.[^kingbright-wp154a4]

## Sources

<!-- generated from frontmatter -->
