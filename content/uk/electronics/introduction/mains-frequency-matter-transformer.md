---
id: emb-elintro-0086
title: "Чому частота мережі важлива для трансформатора?"
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
  - source_id: aac-transformer-saturation
    title: "All About Circuits: Practical Considerations - Transformers"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-9/practical-considerations-transformers/
---

## Short answer

За незмінних напруги й конструкції нижча частота збільшує максимальний магнітний потік в осерді та ризик насичення; тому трансформатор на `60 Гц` не обов’язково можна безпечно живити від `50 Гц`.[^aac-transformer-saturation] Перед підключенням звірте обидва параметри з паспортом конкретної моделі.

## Detailed explanation

Частота мережі визначає, як швидко змінюється магнітний потік в осерді трансформатора. За синусоїдальної напруги та незмінної кількості витків піковий потік приблизно обернено пропорційний частоті: нижча частота означає більший розмах потоку за цикл. Якщо осердя заходить у насичення, магнітний потік уже не зростає пропорційно струму намагнічування, а первинний струм може різко збільшитися; це спричиняє нагрівання й спотворення форми сигналу.[^aac-transformer-saturation]

Саме тому номінал трансформатора задає не просто напругу, а допустиме поєднання напруги та частоти. Модель із маркуванням `120 V, 60 Hz` не можна автоматично вважати придатною для `120 V, 50 Hz`: на нижчій частоті осердя може отримати надмірний потік. Зниження напруги пропорційно частоті зберігає приблизно той самий режим потоку, але вихідна напруга також зменшиться; для практичного застосування слід перевіряти паспорт виробу.[^aac-transformer-saturation]

На вищій частоті за тієї самої напруги потік менший, але це не робить будь-який мережевий трансформатор універсальним: втрати в осерді, паразитні параметри та нагрівання залежать від матеріалу й конструкції. Для високочастотних перетворювачів використовують інші осердя та розрахунок, ніж для трансформаторів мережевих `50/60 Hz`.[^aac-transformer-saturation]

**Типова помилка:** вважати, що напруги на первинній обмотці достатньо для оцінки сумісності. Потрібно зіставляти і напругу, і частоту з паспортними значеннями, а також ураховувати, чи є форма сигналу синусоїдальною.[^aac-transformer-saturation]
