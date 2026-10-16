---
id: emb-elinteg-0027
title: "Яку послідовність станів формує регістр зсуву з інвертованим зворотним зв'язком (лічильник Джонсона)?"
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

Якщо інверсний вихід останнього тригера регістра зсуву підключити до послідовного входу першого розряду, утворюється лічильник Джонсона. Для n-розрядного регістра довжина повного циклу становить <span class="formula">\(2n\)</span> тактових імпульсів. Регістр послідовно заповнюється n одиницями, після чого наступні n тактів послідовно очищають його нулями.[^udemy-electronics-course]

## Detailed explanation

TODO
