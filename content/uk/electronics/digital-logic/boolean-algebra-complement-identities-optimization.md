---
id: emb-eldig-0004
title: "Чому тотожності з комплементом X·/X = 0 та X + /X = 1 важливі для оптимізації логіки?"
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

Змінна та її інверсія завжди набувають протилежних значень 0 і 1. Оскільки AND із нулем завжди дає 0, добуток <span class="formula">\(X \cdot \overline{X} = 0\)</span>. Оскільки OR з одиницею дає 1, сума <span class="formula">\(X + \overline{X} = 1\)</span>. Це дозволяє усувати зайві змінні та логічні вентилі з цифрової схеми без зміни її поведінки.[^udemy-electronics-course]

## Detailed explanation

TODO
