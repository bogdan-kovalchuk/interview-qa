---
id: emb-eldig-0033
title: "Чому з'єднання виходу 5 В TTL із входом 5 В CMOS потребує підтягувального резистора?"
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

Стандартний вихід TTL гарантує рівень одиниці лише <span class="formula">\(V_{OH} \ge 2{,}4\text{ В}\)</span>, тоді як вхід CMOS вимагає поріг не менше <span class="formula">\(V_{IH} = 3{,}5\text{ В}\)</span>. Під навантаженням напруга TTL не досягає порогу спрацьовування CMOS, спричиняючи збої логіки. Підтягувальний резистор опором 1–10 кОм до шини +5 В підтягує вихідний рівень до напруги живлення.[^udemy-electronics-course]

## Detailed explanation

TODO
