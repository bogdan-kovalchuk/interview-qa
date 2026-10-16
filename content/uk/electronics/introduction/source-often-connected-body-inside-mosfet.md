---
id: emb-elintro-0246
title: "Чому source часто з’єднаний із body всередині MOSFET?"
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
  - source_id: infineon-power-mosfet-body-diode
    title: "Infineon: Designing with power MOSFETs – How to avoid common issues and failure modes"
    url: https://www.infineon.com/dgdl/Infineon-Designing_with_power_MOSFETs-ApplicationNotes-v01_02-EN.pdf?fileId=8ac78c8c7ddc01d7017e6c619a490f47
---

## Short answer

Body у силовому MOSFET формує частину напівпровідникової структури, а її з’єднання із source запобігає небажаному body effect.[^infineon-power-mosfet-body-diode] Це дає змогу вивести назовні три основні виводи.[^infineon-power-mosfet-body-diode]

## Detailed explanation

У типовому дискретному силовому MOSFET body – це область напівпровідника під gate, у якій формується керований канал. Якби її потенціал залишався незалежним від source, різниця `V_SB` впливала б на напругу, потрібну для утворення каналу. Виробник зазвичай з’єднує body із source усередині корпусу, фіксуючи цю різницю приблизно на нулі та спрощуючи компонент до трьох зовнішніх виводів: gate, drain і source.[^infineon-power-mosfet-body-diode]

Таке з’єднання не прибирає всі внутрішні p-n переходи. Перехід між body і drain залишається, тому між drain та source виникає intrinsic body diode. Для звичайного N-channel MOSFET її напрямок проводить струм від source до drain, коли вона прямо зміщена; для протилежного струму в off-state цей діод блокує лише в межах його допустимих параметрів. Отже, вимкнений MOSFET не є двонапрямним ідеальним розімкненим контактом.[^infineon-power-mosfet-body-diode]

Це важливо при виборі полярності підключення й у силових схемах. Наприклад, у half-bridge body diode одного ключа може тимчасово проводити індуктивний струм, а її reverse recovery впливає на втрати під час подальшого перемикання. У корпусах із окремим доступом до body або у спеціалізованих інтегральних структурах з’єднання може відрізнятися, тому остаточно звіряйтеся зі схемою та datasheet конкретного компонента.[^infineon-power-mosfet-body-diode]

**Типова помилка:** трактувати MOSFET як симетричний перемикач і вважати, що drain та source можна міняти місцями без наслідків. Перевіряйте напрямок body diode та шлях струму в обох станах ключа.

Приклад: якщо стандартний N-channel ключ вимкнений, але source має вищий потенціал за drain приблизно настільки, щоб прямо змістити body diode, струм може протікати через діод навіть без керувального сигналу на gate. Це окремий шлях від каналу, і його струм та нагрів потрібно перевірити за datasheet.[^infineon-power-mosfet-body-diode]
