---
id: emb-elintro-0294
title: "Що таке антипаралельне включення двох LED?"
description: "Що таке антипаралельне включення двох LED?"
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
  - source_id: kingbright-led-ratings
    title: "Kingbright: 2022–2023 Catalog, Technical Notes"
    url: https://www.kingbrightusa.com/webimages/2021/ecatalog/files/basic-html/page63.html
    accessed: 2026-10-04
    kind: official
    version: "2022–2023 catalog"
    applicability: "Вказує зворотну напругу 5 V для окремих моделей; не універсальний рейтинг LED."
---
## Short answer

Антипаралельно з’єднані LED мають спільні два вузли, але протилежні напрямки. За кожної полярності прямий струм проходить через один LED, тоді як інший має зворотне зміщення; його допустиму зворотну напругу потрібно перевірити за datasheet.[^kingbright-led-ratings]

## Detailed explanation

Антипаралельне з’єднання – це два діоди між тими самими вузлами, але з протилежною орієнтацією анода й катода. За однієї полярності один LED зміщений прямо і може світитися, а другий – зворотно. Після зміни полярності ролі міняються. Таку пару можна використати для індикації обох напрямків струму, наприклад за змінної полярності керування.[^kingbright-led-ratings]

Схема сама по собі не обмежує струм: потрібен відповідний обмежувач, зазвичай резистор послідовно з парою. Через один LED протікає робочий прямий струм, а інший бачить приблизно його пряме падіння у зворотному напрямку. Чи безпечно це для другого LED, визначає його максимальна зворотна напруга. Каталог Kingbright наводить граничне значення 5 V для певних типів, але параметр залежить від конкретної моделі.[^kingbright-led-ratings]

**Типова помилка:** вважати, що кожен LED гарантовано захищає інший. Пара може обмежити зворотну напругу приблизно прямим падінням провідного LED лише за допустимого струму й відповідних характеристик обох компонентів. Для конкретного виробу звіряйте datasheet; за потреби застосовуйте окремий захисний діод.

Приклад: за позитивної напруги на першому вузлі LED, анод якого з’єднаний із ним, може бути прямозміщений і проводити струм; зустрічний LED буде зворотно зміщений. За негативної полярності провідним стане зустрічний LED. Полярність і граничну напругу перевіряють за документацією обраного компонента.[^kingbright-led-ratings]

## Sources

<!-- generated from frontmatter -->
