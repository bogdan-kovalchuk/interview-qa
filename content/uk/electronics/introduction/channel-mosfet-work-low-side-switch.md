---
id: emb-elintro-0253
title: "Як працює N-channel MOSFET як low-side switch?"
track: electronics
section: introduction
sources:
  - source_id: ti-mosfet-selection
    title: "Texas Instruments: Avoid Common Mistakes When Selecting and Designing with Power MOSFETs"
    url: https://www.ti.com/lit/an/slpa021/slpa021.pdf
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), картки курсу"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-direct-current
    title: "All About Circuits textbook, Volume I: DC"
    url: https://www.allaboutcircuits.com/textbook/direct-current/
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
---

## Short answer

Навантаження під’єднане між живленням і drain, а source – до спільного `GND`. Коли керування створює достатнє додатне `V_GS`, N-channel MOSFET проводить струм від навантаження до землі; `V_GS(th)` позначає лише початок провідності, а не гарантує малий `R_DS(on)`.[^ti-mosfet-selection]

## Detailed explanation

У схемі low-side switch N-channel MOSFET стоїть між навантаженням і землею: навантаження з’єднане з плюсом живлення, drain – з його нижнім виводом, а source – зі спільним `GND`. Керувальний сигнал задає напругу саме між gate і source. Коли `V_GS` достатньо додатне, канал утворює провідний шлях від drain до source, струм проходить через навантаження, а напруга на ньому приблизно дорівнює напрузі живлення за малих втрат ключа.[^ti-mosfet-selection]

Коли gate повертається до потенціалу source, канал вимикається й струм навантаження припиняється, окрім можливих шляхів через інші елементи схеми. Для індуктивного навантаження струм не може миттєво зникнути, тому потрібен належний шлях рециркуляції або обмеження напруги. Спільна земля між контролером і силовим колом потрібна для визначеного керувального `V_GS`; інакше напруга pin відносно землі може не бути напругою gate-source.[^ti-mosfet-selection]

Важлива межа – `V_GS(th)` не є рекомендованою напругою керування. Цей параметр задають за дуже малого струму, коли MOSFET лише починає проводити. Щоб ключ працював із низькими втратами, знайдіть у datasheet значення `R_DS(on)` при `V_GS`, яке реально може видати контролер. Наприклад, не можна автоматично вважати, що MOSFET з `V_GS(th) = 2 V` повністю відкритий від GPIO 3.3 V: потрібна специфікація опору за відповідної напруги gate.[^ti-mosfet-selection]

Практично перевіряють розсіювану потужність `P = I²*R_DS(on)`, нагрівання, допустимі `V_DS` та `V_GS`, а також перехідні процеси навантаження. Типова помилка – під’єднати MOSFET як ключ, але оцінити його лише за порогом `V_GS(th)` або за максимальним струмом із заголовка datasheet. Номінали треба оцінювати за умовами вимірювання, корпусом і реальним охолодженням.[^ti-mosfet-selection]
