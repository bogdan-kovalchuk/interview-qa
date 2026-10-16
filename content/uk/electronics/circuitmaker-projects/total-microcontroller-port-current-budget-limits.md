---
id: emb-elcmproj-0061
title: "Чому вибір резисторів світлодіодів розраховують за сумарним лімітом струму корпусу мікроконтролера?"
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

Окремий вивід GPIO витримує до <span class="formula">\(20\text{–}40\ \text{мА}\)</span>, але сумарний струм через виводи живлення обмежений лімітом <span class="formula">\(200\ \text{мА}\)</span>. Одночасне ввімкнення кількох світлодіодів загрожує перевантаженням шин і перегрівом кристала. Збільшення опору резисторів до 330–1000 Ом обмежує загальний струм до безпечних меж.[^udemy-electronics-course]

## Detailed explanation

TODO
