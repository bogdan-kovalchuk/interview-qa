---
id: emb-elinteg-0029
title: "Як організовані послідовні входи в мікросхемі 74HC164 і як їх використовують для стробування даних?"
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

Мікросхема 74HC164 має два послідовні входи DSA і DSB, які всередині об'єднані двовходовим логічним елементом AND. Це дозволяє використовувати один із входів як інформаційний канал, а другий – як лінію дозволу (стробування). Якщо на керуючий вхід подано 0, надходження даних блокується і в регістр зсуваються виключно нулі.[^udemy-electronics-course]

## Detailed explanation

TODO
