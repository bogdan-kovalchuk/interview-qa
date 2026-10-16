---
id: emb-elee-0225
title: "Чому той самий `current sink` 10 мА від 9 В не працює з навантаженням 1 кОм?"
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
  - source_id: fiore-ohms-law
    title: "Engineering LibreTexts: DC Electrical Circuit Analysis – A Practical Approach (Fiore), 3.5 Ohm's Law"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/DC_Electrical_Circuit_Analysis_-_A_Practical_Approach_(Fiore)/03:_Series_Resistive_Circuits/3.05:_Ohm's_Law
  - source_id: fiore-bjt-dc-load-line
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 4.6 DC Load Lines"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/04:_Bipolar_Junction_Transistors_(BJTs)/4.6:_DC_Load_Lines
---

## Short answer

**Запасу напруги немає:** 10 мА на 1 кОм потребують `V = I*R = 10 V`, а все живлення лише 9 V.[^fiore-ohms-law] Коли заданий струм недосяжний, транзистор насичується, і `current sink` дає не більше 9 мА – максимум, який задає коло.[^fiore-bjt-dc-load-line]

## Detailed explanation

Якщо навантаження 1 кОм і `current sink` з’єднані послідовно між шиною 9 V і землею, сума падінь напруги на них не може перевищувати 9 V. Для 10 мА на 1 кОм потрібно `0.010 A * 1000 Ω = 10 V` лише на навантаженні. Це більше за все живлення, тож такий режим недосяжний за будь-якого транзистора й будь-якого резистора емітера. Обмеження випливає із закону Ома `V = I*R`, застосованого до резистора в колі.[^fiore-ohms-law]

Граничний струм задає коло: `V_CC/R = 9 V / 1 kΩ = 9 mA`. Коли заданий струм вищий, транзистор насичується і дає не більше 9 mA.[^fiore-bjt-dc-load-line] Навіть якщо знехтувати падінням на резисторі емітера й узяти `V_CE(sat)` близько 0,1 В, навантаження отримає не більше `(9 - 0.1)/1000 = 8.9 mA`. Ідеальна межа без жодних втрат – 9 mA, і вона вже менша за 10 mA.

`Current sink` тримає заданий струм лише за наявності запасу напруги. Тому мінімальне живлення для 10 mA на 1 kΩ становить 10 V плюс падіння на самому стоці. При 9 V навантаження має бути не більше 900 Ω (`9 V / 10 mA`), а з урахуванням падінь на стоці – менше.

**Типові помилки:**

- Вважати, що `current sink` видає задані 10 mA незалежно від навантаження: струм обмежує живлення.
- Перевіряти лише номінал резистора емітера, а не запас напруги на навантаженні.
- Не враховувати `V_CE(sat)` і падіння на резисторі емітера, коли шукають граничне навантаження.
