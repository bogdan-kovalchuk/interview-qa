---
id: emb-elintro-0232
title: "Як правильно орієнтувати flyback-діод на моторі з NPN low-side ключем?"
description: "Як правильно орієнтувати flyback-діод на моторі з NPN low-side ключем?"
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
    applicability: "Походження питання: лекція 21, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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
  - source_id: ti-inductive-load-clamping
    title: "TI: Switching Inductive Loads with DRV89xx-Q1 Devices"
    url: https://www.ti.com/document-viewer/lit/html/slvaf04
    accessed: 2026-10-04
    kind: official
    version: null
    applicability: "Пояснює перехідну напругу на low-side ключі й роботу вільнохідного шляху; орієнтація діода тут відповідає типовому NPN low-side колу."
---

## Short answer

У типовому колі з NPN low-side ключем катод flyback-діода під’єднують до позитивного вузла живлення котушки, а анод – до вузла між котушкою та колектором. Так діод закритий під час живлення мотора й проводить після вимкнення ключа, коли котушка змінює полярність і підтримує струм.[^ti-inductive-load-clamping]

## Detailed explanation

У low-side схемі один кінець мотора або реле з’єднаний із плюсом живлення, а другий – із колектором NPN-транзистора; емітер зазвичай під’єднаний до землі. Під час увімкнення транзистор стягує колекторний вузол до землі, тому обидва кінці котушки мають майже однаковий потенціал, якщо діод стоїть у правильному напрямку. Катод діода під’єднаний до плюса, анод – до колекторного вузла, отже діод у цьому режимі зворотно зміщений.[^ti-inductive-load-clamping]

Коли транзистор вимикається, струм обмотки не може миттєво змінитися. Котушка піднімає потенціал колекторного вузла вище плюса живлення, доки діод не стане прямо зміщеним. Після цього струм циркулює через котушку й діод у локальному контурі, а колекторна напруга обмежується; це зменшує напругове навантаження на транзистор. У застосуваннях, де важлива швидкість відпускання реле чи спад струму мотора, враховуйте, що низький clamp звичайного діода сповільнює цей процес.[^ti-inductive-load-clamping]

**Типова помилка:** орієнтувати діод за позначкою смуги без зіставлення її з вузлами схеми. Смуга на корпусі зазвичай позначає катод, тому її під’єднують саме до плюсового боку котушки. Перевірте, що діод не проводить, коли ключ увімкнений, і що його номінальний струм достатній для струму котушки перед вимкненням. Для іншого типу драйвера, наприклад мостового, полярність та місце clamp можуть відрізнятися – не переносіть це правило без аналізу схеми.[^ti-inductive-load-clamping]

## Sources

<!-- generated from frontmatter -->
