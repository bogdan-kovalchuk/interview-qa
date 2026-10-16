---
id: emb-elinteg-0073
title: "Як безпечно об'єднати тактовий генератор і кнопку ручного тактування для керування лічильником?"
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

Виходи генератора імпульсів і кнопки з підтяжкою не можна з'єднувати паралельно через виникнення струмового конфлікту шини при незбігу рівнів. Їх підключають через двовходовий логічний елемент OR, вихід якого надходить на тактовий вхід лічильника. Під час ручного тактування генератор необхідно зупинити або перевести в стан логічного 0, інакше постійна одиниця на вході OR заблокує сигнали від кнопки.[^udemy-electronics-course]

## Detailed explanation

TODO
