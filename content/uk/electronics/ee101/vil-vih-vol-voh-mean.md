---
id: emb-elee-0234
title: "Що означають `V_IL`, `V_IH`, `V_OL` і `V_OH`?"
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

`V_IL` – найбільша вхідна напруга, яку пристрій сприймає як 0, а `V_IH` – найменша, яку він сприймає як 1. `V_OL` – найбільша вихідна напруга в стані 0, а `V_OH` – найменша вихідна напруга в стані 1.[^auburn-digital-voltages] Це межі, які задає даташит, а не номінальні рівні.[^ti-hc00]

## Detailed explanation

Ці чотири величини – межі, у яких логічна родина читає сигнали. Для входу важливі `V_IL` і `V_IH`: напруга нижче `V_IL` читається як 0, вище `V_IH` – як 1, а між ними результат не визначений.[^auburn-digital-voltages] Для виходу важливі `V_OL` і `V_OH`: вихід у стані 0 має видавати не більше `V_OL`, а в стані 1 – не менше `V_OH`.[^auburn-digital-voltages]

Вихід гарантує рівень, який вхід ще сприйме правильно, а різниця між ними є запасом завадостійкості. Для високого рівня його записують як `V_OH = V_IH + V_noise`: шум може зсунути рівень на `V_noise`, не змінивши прочитаного значення.[^auburn-digital-voltages] Для TTL `V_OH` = 2,4 В, `V_IH` = 2,0 В, `V_IL` = 0,8 В, `V_OL` = 0,4 В, тож запас з обох боків становить 0,4 В.[^auburn-digital-voltages]

Ці значення залежать від родини й напруги живлення. Для 74HC при 4,5 В `V_OH` (min) = 4,4 В і `V_IH` (min) = 3,15 В дають запас 1,25 В, тобто більший, ніж у TTL.[^ti-hc00] Позначення однакові, а числа в даташиті різні, тому їх треба брати з конкретного приладу.

Межі виходу залежать і від струму навантаження. Для 74HC при 20 мкА `V_OL` (max) = 0,1 В, а при 4 мА – до 0,33 В у діапазоні від –40 до 85 °C.[^ti-hc00] Запас, порахований за одним рядком таблиці, може не відповідати реальному навантаженню.

**Типові помилки:**

- Плутати `V_IL` (max) з `V_OL` (max): перший належить входу, другий – виходу, а запас визначає їх різниця.
- Вважати, що вихід видає рівно 0 В або `V_CC`: даташит дає лише межі.
- Брати пороги TTL (2,0 В і 0,8 В) для родини HC при 4,5 В, де `V_IH` (min) = 3,15 В.
