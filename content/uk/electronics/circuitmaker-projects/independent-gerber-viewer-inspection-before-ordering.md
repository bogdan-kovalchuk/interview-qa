---
id: emb-elcmproj-0070
title: "Чому файли Gerber перед замовленням на виробництві обов’язково перевіряють у незалежному переглядачі?"
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

Вбудований переглядач САПР показує внутрішню базу даних проєкту, маскуючи реальні дефекти файлового експорту. Автономний переглядач (наприклад, Gerbv або ViewMate) відображає саме ті вектори, які отримає виробничий станок. Це дозволяє вчасно виявити розбіжність шарів, пошкодження апертур або зникнення полігонів.[^udemy-electronics-course]

## Detailed explanation

TODO
