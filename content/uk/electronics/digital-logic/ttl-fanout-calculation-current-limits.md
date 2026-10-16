---
id: emb-eldig-0011
title: "Як обчислюється навантажувальна здатність (fanout) виходу мікросхеми TTL?"
track: electronics
section: digital-logic
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), картки курсу"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-digital
    title: "All About Circuits textbook, Volume IV: Digital"
    url: https://www.allaboutcircuits.com/textbook/digital/
---

## Short answer

Fanout обчислюють окремо для стану HIGH як <span class="formula">\(|I_{OH}| / I_{IH}\)</span> і для стану LOW як <span class="formula">\(I_{OL} / |I_{IL}|\)</span>. Підсумковим fanout вибирають менше з двох отриманих значень. Для мікросхеми 74LS04 за типових паспортних струмів це забезпечує коефіцієнт розгалуження 20 для обох станів.[^udemy-electronics-course]

## Detailed explanation

TODO
