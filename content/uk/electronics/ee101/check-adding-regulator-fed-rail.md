---
id: emb-elee-0168
title: "Що перевірити, додаючи стабілізатор 3,3 В, який живиться від шини 5 В?"
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
  - source_id: ti-tps769
    title: "Texas Instruments TPS769: 100mA, 16V, Low-Dropout Linear Regulator (datasheet)"
    url: https://www.ti.com/lit/ds/symlink/tps769.pdf
  - source_id: ti-lm340
    title: "TI: LM340, LM340A, LM7805 family wide VIN 1.5-A fixed voltage regulators (datasheet)"
    url: https://www.ti.com/lit/ds/symlink/lm340.pdf
  - source_id: ti-slva079
    title: "Texas Instruments SLVA079: Understanding the Terms and Definitions of LDO Voltage Regulators"
    url: https://www.ti.com/lit/an/slva079/slva079.pdf
---

## Short answer

Перевіряють за datasheet саме обраної мікросхеми: що вхідний діапазон і dropout дозволяють роботу від 5 В, що її струм покриває навантаження 3,3 В, які конденсатори потрібні для стабільності, а також розведення виводів і орієнтацію корпусу (особливо SMD на перехіднику). Наприклад, TPS76933 розрахований на вхід 2,5–16 В або 2,7–10 В залежно від версії кристала, струм до 100 мА і корпус SOT-23 з 5 виводами.[^ti-tps769] Інший LDO може мати інші виводи, струмові межі й умови стабільності.

## Detailed explanation

Другий лінійний стабілізатор для живлення від шини 5 В – просто ще одне навантаження цієї шини, але придатність конкретної мікросхеми визначає її datasheet. Перше – запас за напругою. Dropout – різниця вхід–вихід, за якої стабілізація припиняється;[^ti-slva079] для TPS76933 за 100 мА він не перевищує 218 мВ.[^ti-tps769] Сама шина 5 В на 7805 може бути в межах 4,75–5,25 В,[^ti-lm340] отже запас у найгіршому разі `4,75 - 3,3 = 1,45 В`, що значно більше за dropout. Вхідний діапазон 2,5–16 В (new) або 2,7–10 В (legacy) 5 В також охоплює.[^ti-tps769]

Друге – струм. Для TPS769 рекомендований вихідний струм не перевищує 100 мА,[^ti-tps769] тож якщо шина 3,3 В бере 100 мА (як у qid:emb-elee-0169), мікросхема працює на самій межі, і для запасу обирають стабілізатор на більший струм. Цей струм іде з шини 5 В і додається до струму її власних навантажень (див. qid:emb-elee-0161). Тепло в новому стабілізаторі: `P = (5 - 3,3)*0,1 = 0,17 Вт`,[^ti-slva079] а за `RθJA = 178,6 °C/W` (new chip, SOT-23-5) це підвищення температури переходу на `0,17*178,6 ≈ 30 °C` над навколишньою.[^ti-tps769]

Третє – конденсатори. Datasheet TPS769 вимагає вихідний конденсатор не менш як 4,7 мкФ з ESR 0,2–10 Ом (legacy) або 2,2–200 мкФ з ESR 0–3 Ом (new) і вхідний 1 мкФ, причому номінали вважають зниженими вдвічі, а ефективна вихідна ємність має лишатися не меншою за 1 мкФ.[^ti-tps769] Без підходящого вихідного конденсатора LDO може бути нестабільним, а ємність керамічних конденсаторів зменшується під DC-зміщенням, тож номінал беруть із запасом.

Четверте – виводи. У SOT-23-5 TPS769 вивід 1 – IN, 2 – GND, 3 – EN, 4 – FB/NC, 5 – OUT, і EN вмикає стабілізатор низьким рівнем, тож його треба з’єднати із землею, а не лишати вільним чи підтягувати вгору.[^ti-tps769] У 7805 в корпусі TO-220 виводи 1–3 – це вхід, земля й вихід,[^ti-lm340] тоді як у SOT-23-5 вихід – вивід 5, а вивід 3 – EN, тож переносити розпіновку з однієї мікросхеми на іншу не можна. На перехіднику для SMD корпус особливо легко повернути неправильно.

**Типові помилки:**

- Вважати, що будь-який стабілізатор 3,3 В має ту саму розпіновку й вимоги до конденсаторів.
- Не звіряти максимальний струм мікросхеми зі струмом шини 3,3 В.
- Лишати вхід EN вільним, не з’ясувавши його активний рівень.
- Не враховувати, що струм шини 3,3 В протікає крізь стабілізатор 5 В.
