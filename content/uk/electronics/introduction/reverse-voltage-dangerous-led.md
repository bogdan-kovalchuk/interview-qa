---
id: emb-elintro-0123
title: "Чому зворотна напруга небезпечна для LED?"
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
  - source_id: kingbright-wp154a4
    title: "Kingbright WP154A4SEJ3VBDZGC/CA datasheet"
    url: https://www.kingbrightusa.com/images/catalog/SPEC/WP154A4SEJ3VBDZGC-CA.pdf
---

## Short answer

LED зазвичай має невеликий граничний `V_R`, але конкретне значення потрібно перевіряти в datasheet. Для Kingbright WP154A4SEJ3VBDZGC/CA вказано 5 V.[^kingbright-wp154a4] За перевищення рейтингу можливий зворотний пробій і пошкодження, тож не варто вважати всі LED однаково стійкими до зворотної напруги.[^kingbright-wp154a4]

## Detailed explanation

У прямому напрямку LED проводить струм і випромінює світло, а за зворотної полярності його p-n-перехід блокує струм, окрім малого витоку. Зворотна напруга не є необмежено безпечною: виробник задає максимальне `V_R`, перевищення якого може спричинити пробій, деградацію або відмову компонента.[^aac-semiconductors]

Універсального рейтингу для всіх LED немає. Наприклад, datasheet Kingbright WP154A4SEJ3VBDZGC/CA вказує `V_R = 5 V`. Це параметр конкретної серії, а не загальне правило; для проєкту слід дивитися абсолютні максимальні рейтинги власної деталі.[^kingbright-wp154a4]

Зворотна напруга може виникати в колах зі змінною полярністю або під час перемикання індуктивного навантаження. Її обмежують відповідною схемою захисту, наприклад діодом, включеним зустрічно-паралельно, а не покладаються на пробій LED.[^aac-semiconductors]

**Типова помилка:** сприймати малий зворотний витік як захист. Він описує поведінку нижче рейтингу; після його перевищення струм не гарантовано залишиться малим, а допустима напруга залежить від деталі.[^aac-semiconductors]

Також слід розрізняти максимальну зворотну напругу та зворотний струм, зазначений за тестової напруги: таблиця струму не означає, що перехід може безпечно витримати будь-який рівень. У Kingbright datasheet `V_R = 5 V` наведено як абсолютний рейтинг, тоді як струм витоку подано окремим параметром для тестування при цій напрузі. Рейтинг не є робочою ціллю, і в реальному колі бажано лишати запас на перехідні процеси.[^kingbright-wp154a4]
