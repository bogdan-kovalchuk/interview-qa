---
id: emb-elintro-0293
title: "Чому у схемі з батареєю 9 V, резистором 220 Ω і LED струм не дорівнює точно `9/220`?"
track: electronics
section: introduction
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), картки курсу"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-direct-current
    title: "All About Circuits textbook, Volume I: DC"
    url: https://www.allaboutcircuits.com/textbook/direct-current/
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
  - source_id: ti-led-resistor
    title: "Texas Instruments: AN-1293 Driving RGB LED Using LP3936"
    url: https://www.ti.com/jp/lit/pdf/snva071
---

## Short answer

LED має пряме падіння напруги `V_f`, тому на резисторі залишається приблизно `9 V - V_f`, а струм дорівнює цьому падінню, поділеному на 220 Ω.[^ti-led-resistor] За `V_f = 2 V` оцінка становить близько 31.8 mA, а не `9/220`.

## Detailed explanation

У послідовному колі батарея, резистор і LED мають однаковий струм, але напруга батареї розподіляється між компонентами. Коли LED увімкнений у прямому напрямку, на ньому є пряме падіння `V_f`; на резисторі залишається різниця між напругою живлення й напругою LED. Тому оцінка струму: `I = (V_supply - V_f)/R`.[^ti-led-resistor]

Припустімо, що батарея дорівнює 9 V, резистор – рівно 220 Ω, а `V_f` у робочій точці становить 2 V. На резисторі буде 7 V, а струм – приблизно 31.8 mA. Це оцінка, не гарантовано точне значення: напруга батареї змінюється під навантаженням, допуск резистора ненульовий, а `V_f` залежить від типу LED, струму й температури.[^ti-led-resistor]

Вольт-амперна характеристика діода нелінійна. Не можна вважати LED резистором із фіксованим опором; при зміні струму змінюється його падіння напруги. Резистор встановлює робочу точку й обмежує струм, а точний проєкт враховує крайні значення живлення, `V_f`, допуск резистора та допустимий струм LED.[^ti-led-resistor]

**Типова помилка:** ділити всі 9 V на 220 Ω, ніби вся напруга припадає на резистор. Це ігнорує LED. Також не слід вважати 2 V універсальним значенням: виробник задає `V_f` для конкретних умов.

У наведеній оцінці резистор розсіює приблизно `P = 7 V * 31.8 mA ≈ 0.223 W`, тож резистор 0.25 W має малий запас. Реальний вибір потужності залежить від допусків і температурних умов.[^ti-led-resistor]
