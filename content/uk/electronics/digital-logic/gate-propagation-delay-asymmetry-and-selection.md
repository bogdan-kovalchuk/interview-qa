---
id: emb-eldig-0009
title: "Чому затримки t_PLH і t_PHL вентиля бувають різними і як це впливає на вибір логіки?"
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

Переходи з низького рівня у високий (t_PLH) та з високого в низький (t_PHL) визначаються різними внутрішніми транзисторами й паразитними ємностями. У серії 74LS вентиль 74LS32 (OR) зазвичай має меншу затримку поширення, ніж 74LS08 (AND). Якщо критичний шлях схеми не вкладається в часовий бюджет, перетворення логіки на швидші вентилі прискорює обчислення.[^udemy-electronics-course]

## Detailed explanation

TODO
