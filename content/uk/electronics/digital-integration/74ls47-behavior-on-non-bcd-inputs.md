---
id: emb-elinteg-0010
title: "Як поводиться дешифратор 74LS47 при подачі на входи двійкових кодів від 10 до 15?"
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

Мікросхема 74LS47 спроєктована для двійково-десяткового коду BCD (цифри 0–9), а не для повноцінних шістнадцяткових символів A–F. При кодах від 10 до 14 на індикаторі відображаються псевдовипадкові спеціальні символи або кути, а код 15 повністю гасить усі сегменти. Справжні літери A–F потребують спеціалізованих шістнадцяткових дешифраторів або програмованої логіки.[^udemy-electronics-course]

## Detailed explanation

TODO
