---
id: emb-elinteg-0069
title: "Чому використання D-тригерів спрощує отримання функцій збудження автомата з карт Карно?"
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

Для D-тригера значення, записане в наступному такті, строго дорівнює логічному рівню на вході: <span class="formula">\(Q(t+1) = D\)</span>. Завдяки цій характеристичній тотожності карта Карно для функції наступного стану біта безпосередньо є картою збудження входу D відповідного тригера. Для інших тригерів (JK, T, SR) довелося б проводити додаткове перетворення через характеристичні таблиці переходів.[^udemy-electronics-course]

## Detailed explanation

TODO
