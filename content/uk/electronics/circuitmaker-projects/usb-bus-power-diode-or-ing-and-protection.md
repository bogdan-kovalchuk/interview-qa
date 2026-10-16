---
id: emb-elcmproj-0059
title: "Як схема на діодах Шотткі захищає пристрій при одночасному живленні від USB і зовнішньої батареї?"
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

Діоди вмикають за схемою «Монтажне АБО» у ланцюги живлення від порту USB та акумуляторної батареї. Струм автоматично споживається від лінії з вищим потенціалом, блокуючи друге джерело зворотним зміщенням. Мале падіння на діодах Шотткі захищає комп’ютерний порт USB від зустрічного струму батареї.[^udemy-electronics-course]

## Detailed explanation

TODO
