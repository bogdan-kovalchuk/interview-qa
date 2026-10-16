---
id: emb-elinteg-0008
title: "Чим відрізняються семисегментні індикатори зі спільним анодом та спільним катодом?"
track: electronics
section: digital-integration
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), картки курсу"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-digital
    title: "All About Circuits textbook, Volume IV: Digital"
    url: https://www.allaboutcircuits.com/textbook/digital/
---

## Short answer

В індикаторі зі спільним анодом аноди всіх сегментів з'єднані разом і підключаються до позитивної шини VCC, а окремі сегменти вмикаються подачею низького рівня (LOW) на катоди. В індикаторі зі спільним катодом усі катоди заземлені, а сегменти запалюються високим рівнем (HIGH) на анодах. Відповідно, для спільного анода використовують драйвер 74LS47, а для спільного катода – 74LS48.[^udemy-electronics-course]

## Detailed explanation

TODO
