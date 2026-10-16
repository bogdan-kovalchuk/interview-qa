---
id: emb-elinteg-0022
title: "Як паразитні параметри аналогового ключа 74HC4051 впливають на пропускання високочастотних сигналів?"
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

Ключ має власний внутрішній опір у відкритому стані <span class="formula">\(R_{ON}\)</span> та паразитні ємності відносно підкладки й суміжних каналів. Ці параметри утворюють RC-фільтр низьких частот, що обмежує смугу пропускання та викликає завал фронтів імпульсних сигналів. На високих частотах (від одиниць мегагерців) прямокутні імпульси зазнають викидів і дзвону через паразитні індуктивності макетних з'єднань.[^udemy-electronics-course]

## Detailed explanation

TODO
