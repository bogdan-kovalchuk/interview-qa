---
id: emb-elcmproj-0072
title: "Чому перший зразок виготовленої плати збирають і запускають поетапно, блок за блоком?"
track: electronics
section: circuitmaker-projects
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), картки курсу"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: circuitmaker-docs
    title: "CircuitMaker documentation"
    url: https://www.altium.com/documentation/altium-circuitmaker
---

## Short answer

Монтаж починають виключно з блоку живлення, щоб переконатися у відповідності напруг і захистити мікросхеми від пробою. Потім монтують процесор із тактовим генератором, і лише після перевірки зв’язку встановлюють іншу периферію. Поетапний запуск локалізує помилки монтажу й короткі замикання без ризику вигорання схеми.[^udemy-electronics-course]

## Detailed explanation

TODO
