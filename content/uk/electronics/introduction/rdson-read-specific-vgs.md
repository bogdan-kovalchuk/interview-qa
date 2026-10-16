---
id: emb-elintro-0257
title: "Чому `R_DS(on)` треба дивитися при конкретній `V_GS`?"
track: electronics
section: introduction
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), картки курсу"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-direct-current
    title: "All About Circuits textbook, Volume I: DC"
    url: https://www.allaboutcircuits.com/textbook/direct-current/
  - source_id: infineon-optimos
    title: "Infineon OptiMOS Power MOSFET Datasheet Explanation"
    url: https://www.infineon.com/assets/row/public/documents/24/42/infineon-mosfet-optimos-datasheet-explanation-applicationnotes-en.pdf
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
---

## Short answer

`R_DS(on)` залежить від `V_GS`, струму та температури, тому треба використовувати гарантоване значення datasheet при умовах, близьких до реального драйвера й навантаження.[^infineon-optimos] Порогова `V_GS(th)` означає лише початок провідності за малого тестового струму, а не повне відкривання.[^infineon-optimos]

## Detailed explanation

On-resistance MOSFET не є сталою незалежно від керування величиною: `R_DS(on)` вимірюють за заданих `V_GS`, drain current і температури. Вища напруга gate-source зазвичай сильніше формує канал і зменшує опір у дозволеному діапазоні, але допустиму напругу gate теж обмежує datasheet. Для вибору беруть гарантовану межу, а не типове значення графіка, якщо конструкція має працювати за найгірших умов.[^infineon-optimos]

У таблиці шукайте рядки `R_DS(on)` з умовою тесту. Якщо MOSFET керується GPIO 3.3 V, число, гарантоване лише при 10 V, не доводить, що транзистор матиме такий самий опір при 3.3 V. Перевірте, чи є гарантоване значення при доступній напрузі; графік типових характеристик може допомогти оцінці, але не є виробничою гарантією. За малих `V_GS` опір також змінюється з температурою та струмом.[^infineon-optimos]

Не плутайте `V_GS(th)` з напругою повного відкривання. Порогове значення задають за малим тестовим drain current, отже воно показує, коли канал тільки починає проводити. Воно не гарантує низького падіння напруги чи малого нагрівання у навантаженні. Для оцінки втрат у простому повністю ввімкненому режимі використовуйте `P = I²*R_DS(on)`, із опором за робочої напруги керування та з поправкою на гарячий кристал.[^infineon-optimos]

**Типові помилки:**

- Порівнювати опори при різних `V_GS` так, ніби умови однакові.
- Обрати logic-level MOSFET лише за низьким `V_GS(th)`, не перевіривши `R_DS(on)`.
- Вважати типове значення достатнім доказом для worst-case розрахунку.
