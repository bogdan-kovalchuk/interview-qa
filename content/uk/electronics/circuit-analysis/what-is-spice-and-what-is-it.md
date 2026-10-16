---
id: emb-elcirc-0037
title: "Що таке SPICE і яке його призначення?"
track: electronics
section: circuit-analysis
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), картки курсу"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-direct-current
    title: "All About Circuits textbook, Volume I: DC"
    url: https://www.allaboutcircuits.com/textbook/direct-current/
  - source_id: berkeley-spice-report-1973
    title: "UC Berkeley EECS Technical Report UCB/ERL M382: SPICE"
    url: https://www2.eecs.berkeley.edu/Pubs/TechRpts/1973/22871.html
  - source_id: ngspice-manual
    title: "ngspice User's Manual"
    url: https://ngspice.sourceforge.io/docs/ngspice-manual.pdf
---

## Short answer

SPICE розшифровується як **Simulation Program with Integrated Circuit Emphasis** – симулятор електричних кіл, започаткований в UC Berkeley у 1973 році.[^berkeley-spice-report-1973] Він обчислює поведінку заданої моделі кола, зокрема DC-режим, перехідні процеси та малосигнальну AC-відповідь, без фізичного прототипу.[^ngspice-manual]

## Detailed explanation

SPICE – це програмне моделювання електричного кола за його описом у netlist, де перелічено компоненти, їхні вузли та моделі.[^ngspice-manual]

Назва походить від Simulation Program with Integrated Circuit Emphasis. Початкову програму розробили в UC Berkeley; технічний звіт 1973 року описує nodal analysis і нелінійний DC-, малосигнальний та перехідний аналіз. Сьогодні назву SPICE використовують для родини сумісних симуляторів, тому команди, моделі та підтримувані функції треба звіряти з документацією конкретного інструмента.[^berkeley-spice-report-1973]

Симулятор перетворює netlist на математичну модель. Для лінійної резистивної схеми він застосовує закони Кірхгофа й параметри елементів; для нелінійних компонентів, наприклад діодів і транзисторів, розв’язувач знаходить робочий стан чисельними методами. У transient аналізі він повторно розв’язує модель у часових кроках, а в AC аналізі лінеаризує нелінійні компоненти біля DC operating point і досліджує малосигнальну відповідь.[^ngspice-manual]

Результат залежить від якості моделі та припущень. Реальний резистор має допуск, транзистор має конкретні параметри, а parasitics і температура можуть змінити поведінку; відсутню фізику netlist не вгадає. Тому SPICE корисний для перевірки очікуваної роботи, порівняння варіантів і пошуку помилок до складання, але не замінює перевірку чутливості до параметрів і вимірювання готової плати.[^ngspice-manual]

**Типова помилка:** сприймати симуляцію як доказ того, що плата працюватиме саме так. Переконайтеся, що моделі відповідають деталям і робочим умовам, а висновок обмежений тими ефектами, які симулятор справді моделює.[^ngspice-manual]
