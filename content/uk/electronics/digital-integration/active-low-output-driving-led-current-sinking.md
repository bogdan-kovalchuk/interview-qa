---
id: emb-elinteg-0006
title: "Чому світлодіод підключають анодом до живлення, а катодом до виходу дешифратора з активним низьким рівнем?"
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

Вихід із активним низьким рівнем переходить у нуль при спрацьовуванні, замикаючи коло на землю та вбираючи струм (sinking). Логічні мікросхеми серії TTL здатні вбирати значно більший вихідний струм <span class="formula">\(I_{OL}\)</span>, ніж віддавати у стані одиниці <span class="formula">\(I_{OH}\)</span>. Тому підключення катода світлодіода через резистор до виходу забезпечує яскраве світіння без перевантаження мікросхеми.[^udemy-electronics-course]

## Detailed explanation

TODO
