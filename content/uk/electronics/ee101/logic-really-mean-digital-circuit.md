---
id: emb-elee-0233
title: "Що насправді означають логічні 0 і 1 у цифровій схемі?"
track: electronics
section: ee101
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), картки курсу"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-alternating-current
    title: "All About Circuits textbook, Volume II: AC"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
  - source_id: auburn-digital-voltages
    title: "Auburn University ELEC 3040/3050: Digital system voltages/currents and reading component data sheets (lab lecture notes)"
    url: https://www.eng.auburn.edu/~nelson/courses/elec3040_3050/LabLectures/DigitalElectricalQuantities_ARM.pdf
  - source_id: ti-hc00
    title: "TI SN74HC00 quadruple NAND gates datasheet"
    url: https://www.ti.com/lit/ds/symlink/sn74hc00.pdf
---

## Short answer

Логічні 0 і 1 – це діапазони напруг, а не точні числа: вхід сприймає низький рівень до `V_IL` (максимум), високий – від `V_IH` (мінімум), а між ними результат невизначений.[^auburn-digital-voltages] Половина живлення не є порогом: для 74HC при `V_CC = 4,5 В` вхідні межі 1,35 і 3,15 В, тож 2,25 В лежить між ними.[^ti-hc00]

## Detailed explanation

Логічне значення – це інтерпретація напруги на виводі, а не сама напруга. Пристрій зчитує вхідну напругу за порогами: `V_IL` – найбільша напруга, яку він сприймає як 0, `V_IH` – найменша, яку він сприймає як 1. Напруги між ними він не зчитує однозначно.[^auburn-digital-voltages] Вихід описують іншими межами: `V_OL` – найбільша напруга в стані 0, `V_OH` – найменша в стані 1.[^auburn-digital-voltages]

**Приклад:** для 74HC00 при `V_CC = 4,5 В` даташит дає `V_IL` (max) = 1,35 В і `V_IH` (min) = 3,15 В. Для виходу він дає `V_OL` (max) = 0,1 В і `V_OH` (min) = 4,4 В при струмі 20 мкА.[^ti-hc00] Напруга 2,25 В, тобто половина живлення, лежить усередині невизначеної зони, тому поріг не можна ставити на половині `V_CC`. Запас завадостійкості записують як `V_OH - V_IH` для високого рівня і `V_IL - V_OL` для низького.[^auburn-digital-voltages] Для 74HC при 4,5 В це `4,4 - 3,15 = 1,25 В` і `1,35 - 0,1 = 1,25 В`.[^ti-hc00]

Ці числа діють за заданих умов. Вихідні рівні залежать від струму навантаження: при 4 мА `V_OL` (max) уже 0,33 В у діапазоні від –40 до 85 °C.[^ti-hc00] Пороги залежать від родини: стандарт TTL має `V_IH` = 2,0 В і `V_IL` = 0,8 В, а значення між 0,8 і 2,0 В дають непередбачуваний результат.[^auburn-digital-voltages] Тому логічні рівні беруть з даташиту конкретної родини і напруги живлення.

**Типові помилки:**

- Вважати, що 0 – це рівно 0 В, а 1 – рівно `V_CC`: гарантують лише межі `V_IL`, `V_IH`, `V_OL`, `V_OH`.
- Ставити поріг на половині живлення: для 74HC при 4,5 В це 2,25 В, що лежить у зоні невизначеності.
- Залишати вхід плаваючим або подавати сигнал, що довго проходить через зону між порогами.
