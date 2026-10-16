---
id: emb-elinteg-0042
title: "Чому тактову частоту системи слід обмежувати з урахуванням затримки комбінаційного компаратора?"
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

Компаратор є чисто комбінаційною схемою, вихід якої стабілізується лише після проходження сигналу через кілька рівнів логіки. Затримка поширення <span class="formula">\(t_{pd}\)</span> для мікросхем серії HC становить близько 15–20 нс на каскад. Якщо зчитати результат порівняння до завершення цього часу встановлення, схема зафіксує невірні проміжні перехідні стани.[^udemy-electronics-course]

## Detailed explanation

TODO
