---
id: emb-elcirc-0040
title: "Яка структура рядка компонента у нетлисті SPICE?"
description: "Яка структура рядка компонента у нетлисті SPICE?"
track: electronics
section: circuit-analysis
level: junior
type: concept
tags: []
status: published
updated: 2026-10-04
content_revision: 2
reconciled_with:
  en: 2
anki:
  export: true
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), картки курсу"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
    accessed: 2026-09-27
    kind: community
    version: null
    applicability: "Походження питання: лекція 31, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
  - source_id: aac-direct-current
    title: "All About Circuits textbook, Volume I: DC"
    url: https://www.allaboutcircuits.com/textbook/direct-current/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: DC-кола, закон Ома, закони Кірхгофа, джерела й вимірювання; конкретні номінали й схеми курсу можуть відрізнятися."
  - source_id: ngspice-netlist-manual
    title: "ngspice User's Manual"
    url: https://ngspice.sourceforge.io/docs/ngspice-manual.pdf
    accessed: 2026-10-04
    kind: official
    version: "current manual"
    applicability: "Документує netlist синтаксис і приклади компонентів саме ngspice; порядок полів залежить від типу елемента та може відрізнятися в інших симуляторах."
---

## Short answer

У ngspice рядок компонента зазвичай задає його ім’я, потрібні саме цьому типу елемента вузли, а потім значення чи параметри.[^ngspice-netlist-manual] Наприклад, `R1 1 2 1k` задає резистор, а `V1 1 0 DC 5` – DC-джерело між вузлом 1 та вузлом землі 0; формат решти полів залежить від типу компонента.[^ngspice-netlist-manual]

## Detailed explanation

У netlist SPICE кожен елемент описаний рядком, але універсальної кількості полів для всіх компонентів немає: їхня структура залежить від типу елемента.[^ngspice-netlist-manual]

У ngspice перша частина імені елемента визначає його клас: наприклад, `R` позначає resistor, `C` – capacitor, а `V` – voltage source. Далі вказують ім’я екземпляра, вузли, до яких приєднаний компонент, і його номінал або параметри. Повторення однакової назви вузла в різних рядках означає електричне з’єднання; вузол `0` є опорним ground.[^ngspice-netlist-manual]

Для простого резистора запис `R1 1 2 1k` читається як резистор R1 опором 1 kΩ між вузлами 1 і 2. Для незалежного джерела напруги `V1 1 0 DC 5` описує джерело 5 V між вузлами 1 та 0. Порядок вузлів важливий для полярності джерела, а складніші пристрої мають більше виводів і можуть посилатися на окрему модель через її ім’я.[^ngspice-netlist-manual]

Рядки, що починаються з крапки, зазвичай є керівними директивами або описами моделей, а не екземплярами компонентів. Для читабельності netlist дозволяє коментарі окремими рядками; у ngspice рядок, який починається з `*`, ігнорується як коментар. Довгі записи можна продовжувати, починаючи наступний рядок з `+` згідно з правилами парсера.[^ngspice-netlist-manual]

**Типова помилка:** трактувати схему `ім’я вузол вузол значення` як незмінний шаблон для будь-якого елемента. У резистора є два вузли й опір, у transistor або subcircuit – більше вузлів і модель; звіряйте порядок полів у формі саме потрібного компонента.[^ngspice-netlist-manual]

## Sources

<!-- generated from frontmatter -->
