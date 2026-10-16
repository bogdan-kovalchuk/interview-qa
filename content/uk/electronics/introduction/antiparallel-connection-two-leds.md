---
id: emb-elintro-0294
title: "Що таке антипаралельне включення двох LED?"
track: electronics
section: introduction
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), картки курсу"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-direct-current
    title: "All About Circuits textbook, Volume I: DC"
    url: https://www.allaboutcircuits.com/textbook/direct-current/
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
  - source_id: kingbright-led-ratings
    title: "Kingbright: 2022–2023 Catalog, Technical Notes"
    url: https://www.kingbrightusa.com/webimages/2021/ecatalog/files/basic-html/page63.html
---

## Short answer

Антипаралельно з’єднані LED мають спільні два вузли, але протилежні напрямки. За кожної полярності прямий струм проходить через один LED, тоді як інший має зворотне зміщення; його допустиму зворотну напругу потрібно перевірити за datasheet.[^kingbright-led-ratings]

## Detailed explanation

Антипаралельне з’єднання – це два діоди між тими самими вузлами, але з протилежною орієнтацією анода й катода. За однієї полярності один LED зміщений прямо і може світитися, а другий – зворотно. Після зміни полярності ролі міняються. Таку пару можна використати для індикації обох напрямків струму, наприклад за змінної полярності керування.[^kingbright-led-ratings]

Схема сама по собі не обмежує струм: потрібен відповідний обмежувач, зазвичай резистор послідовно з парою. Через один LED протікає робочий прямий струм, а інший бачить приблизно його пряме падіння у зворотному напрямку. Чи безпечно це для другого LED, визначає його максимальна зворотна напруга. Каталог Kingbright наводить граничне значення 5 V для певних типів, але параметр залежить від конкретної моделі.[^kingbright-led-ratings]

**Типова помилка:** вважати, що кожен LED гарантовано захищає інший. Пара може обмежити зворотну напругу приблизно прямим падінням провідного LED лише за допустимого струму й відповідних характеристик обох компонентів. Для конкретного виробу звіряйте datasheet; за потреби застосовуйте окремий захисний діод.

Приклад: за позитивної напруги на першому вузлі LED, анод якого з’єднаний із ним, може бути прямозміщений і проводити струм; зустрічний LED буде зворотно зміщений. За негативної полярності провідним стане зустрічний LED. Полярність і граничну напругу перевіряють за документацією обраного компонента.[^kingbright-led-ratings]
