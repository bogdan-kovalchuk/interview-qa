---
id: emb-elinteg-0021
title: "Чому один і той самий вивід мікросхеми 4051 у схемних бібліотеках може позначатися як INH або як /E?"
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

Позначення відображають різний погляд на логічну полярність керування одним і тим самим вузлом. Назва INH (inhibit) вказує на заборону високим рівнем (HIGH вимикає всі ключі), а позначення <span class="formula">\(\overline{E}\)</span> вказує на дозвіл низьким рівнем (LOW вмикає вибраний ключ). При розробці завжди слід перевіряти активний рівень у технічному описі, а не орієнтуватися лише на текст мітки.[^udemy-electronics-course]

## Detailed explanation

TODO
