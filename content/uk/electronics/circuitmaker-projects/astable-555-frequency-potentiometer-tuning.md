---
id: emb-elcmproj-0012
title: "Як потенціометри регулюють частоту імпульсів у автоколивальному генераторі на таймері 555?"
track: electronics
section: circuitmaker-projects
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), картки курсу"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: circuitmaker-docs
    title: "CircuitMaker documentation"
    url: https://www.altium.com/documentation/altium-circuitmaker
---

## Short answer

Частота генератора задається формулою часу заряду й розряду конденсатора: <span class="formula">\(f \approx 1{,}44 / ((R_A + 2R_B)\,C)\)</span>. Послідовне ввімкнення підлаштовних потенціометрів змінює еквівалентний опір плечей подільника. Це дозволяє плавно підлаштовувати темп спалахів світлодіодів від часток герца до сотень герц.[^udemy-electronics-course]

## Detailed explanation

TODO
