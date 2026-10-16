---
id: emb-elintro-0232
title: "Як правильно орієнтувати flyback-діод на моторі з NPN low-side ключем?"
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
  - source_id: ti-inductive-load-clamping
    title: "TI: Switching Inductive Loads with DRV89xx-Q1 Devices"
    url: https://www.ti.com/document-viewer/lit/html/slvaf04
---

## Short answer

У типовому колі з NPN low-side ключем катод flyback-діода під’єднують до позитивного вузла живлення котушки, а анод – до вузла між котушкою та колектором. Так діод закритий під час живлення мотора й проводить після вимкнення ключа, коли котушка змінює полярність і підтримує струм.[^ti-inductive-load-clamping]

## Detailed explanation

У low-side схемі один кінець мотора або реле з’єднаний із плюсом живлення, а другий – із колектором NPN-транзистора; емітер зазвичай під’єднаний до землі. Під час увімкнення транзистор стягує колекторний вузол до землі, тому обидва кінці котушки мають майже однаковий потенціал, якщо діод стоїть у правильному напрямку. Катод діода під’єднаний до плюса, анод – до колекторного вузла, отже діод у цьому режимі зворотно зміщений.[^ti-inductive-load-clamping]

Коли транзистор вимикається, струм обмотки не може миттєво змінитися. Котушка піднімає потенціал колекторного вузла вище плюса живлення, доки діод не стане прямо зміщеним. Після цього струм циркулює через котушку й діод у локальному контурі, а колекторна напруга обмежується; це зменшує напругове навантаження на транзистор. У застосуваннях, де важлива швидкість відпускання реле чи спад струму мотора, враховуйте, що низький clamp звичайного діода сповільнює цей процес.[^ti-inductive-load-clamping]

**Типова помилка:** орієнтувати діод за позначкою смуги без зіставлення її з вузлами схеми. Смуга на корпусі зазвичай позначає катод, тому її під’єднують саме до плюсового боку котушки. Перевірте, що діод не проводить, коли ключ увімкнений, і що його номінальний струм достатній для струму котушки перед вимкненням. Для іншого типу драйвера, наприклад мостового, полярність та місце clamp можуть відрізнятися – не переносіть це правило без аналізу схеми.[^ti-inductive-load-clamping]
