---
id: emb-elpcb-0018
title: "Чому виробничі файли Gerber небезпечно перевіряти лише вбудованим переглядачем CAD?"
track: electronics
section: pcb-design
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), картки курсу"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: circuitmaker-docs
    title: "CircuitMaker documentation"
    url: https://www.altium.com/documentation/altium-circuitmaker
---

## Short answer

Вбудований переглядач САПР часто бере графічні дані з внутрішньої бази проєкту, маскуючи реальні помилки експорту. Сторонній автономний Gerber-переглядач відображає вихідні вектори так, як їх прочитає фотоплотер на заводі. Це дозволяє вчасно виявити зміщення шарів, дзеркальне відображення, пропущені файли свердління, пошкоджені апертури чи інвертовані полігони до оплати виробничої партії.[^udemy-electronics-course]

## Detailed explanation

TODO
