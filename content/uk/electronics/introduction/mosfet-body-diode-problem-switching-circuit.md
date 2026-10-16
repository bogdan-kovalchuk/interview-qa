---
id: emb-elintro-0259
title: "Коли body diode MOSFET може бути проблемою в ключовій схемі?"
track: electronics
section: introduction
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), картки курсу"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-direct-current
    title: "All About Circuits textbook, Volume I: DC"
    url: https://www.allaboutcircuits.com/textbook/direct-current/
  - source_id: infineon-mosfet-layout
    title: "Infineon: Designing with power MOSFETs"
    url: https://www.infineon.com/assets/row/public/documents/24/42/infineon-designing-with-power-mosfets-applicationnotes-en.pdf?fileId=8ac78c8c7ddc01d7017e6c619a490f47
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
---

## Short answer

У силового MOSFET є внутрішній body diode, що може проводити при вимкненому каналі, якщо схема прикладає до нього пряме зміщення.[^infineon-mosfet-layout] У bridge-схемах важливі dead time та reverse recovery, а в захисті від зворотного струму одна деталь не завжди блокує струм в обох напрямках.[^infineon-mosfet-layout]

## Detailed explanation

Body diode – внутрішній PN junction між body та drain у звичайному power MOSFET; body зазвичай з’єднаний із source. Тому при вимкненому gate diode все одно створює напрямлений шлях струму, якщо її анод і катод отримують пряму напругу. У N-channel MOSFET типовий шлях body diode спрямований від source до drain, але для практичного підключення звіряйте символ і полярність конкретної деталі.[^infineon-mosfet-layout]

У напівмосту струм індуктивного навантаження не може миттєво зникнути. Під час dead time він може перейти у body diode нижнього або верхнього ключа. Коли протилежний MOSFET увімкнеться, diode має припинити провідність; накопичений заряд створює reverse-recovery current, додаткові втрати та напругові/струмові піки. Ризик залежить від струму, швидкості перемикання, dead time та параметрів `Q_rr` і `t_rr`, тому на практиці дивляться на форми сигналу й межі datasheet.[^infineon-mosfet-layout]

Ще один випадок – одноключовий захист або high-side перемикач. Коли MOSFET вимкнений, body diode може залишити шлях у небажаному напрямку, наприклад від навантаження назад до джерела. Якщо потрібно блокувати струм в обох напрямках, застосовують відповідну топологію, часто два MOSFET із протилежно зорієнтованими body diode; конкретну реалізацію визначають напруги, керування gate та очікуваний режим.[^infineon-mosfet-layout]

**Типові помилки:**

- Припускати, що `V_GS = 0` означає електричну ізоляцію між drain і source в обох напрямках.
- Забувати про коротку провідність body diode під час dead time і reverse recovery при комутації.
- Вважати, що body diode є безкоштовним ідеальним діодом: перевіряйте прямий спад, допустимий струм і recovery характеристики.
