---
id: emb-elinteg-0046
title: "Як каскадувати 4-бітні суматори 74LS83 для додавання багаторозрядних чисел?"
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

Для побудови 8-бітного суматора використовують дві мікросхеми 74LS83: вихід перенесення C4 молодшого ступеня підключають до входу перенесення C0 старшого. На вхід C0 молодшого ступеня подають нуль (GND) при звичайному додаванні. Підсумкова 8-бітна сума формується розрядами <span class="formula">\(\Sigma_1\)</span>–<span class="formula">\(\Sigma_4\)</span> обох мікросхем, а вихід C4 старшої позначає переповнення.[^udemy-electronics-course]

## Detailed explanation

TODO
