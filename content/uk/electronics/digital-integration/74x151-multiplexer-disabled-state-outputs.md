---
id: emb-elinteg-0017
title: "Які рівні встановлюються на виходах мультиплексора 74x151 при деактивованому вході дозволу?"
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

Коли вхід дозволу <span class="formula">\(\overline{E}\)</span> встановлено у стан 1 (заборона), мікросхема 74x151 не переводить виходи у високоімпедансний стан Hi-Z. Натомість прямий вихід Y примусово фіксується в логічний 0, а інверсний вихід <span class="formula">\(\overline{Y}\)</span> – у логічну 1 незалежно від вхідних сигналів. Для отримання Hi-Z на спільній шині потрібні мікросхеми з трьома станами виходу.[^udemy-electronics-course]

## Detailed explanation

TODO
