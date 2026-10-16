---
id: emb-elee-0211
title: "Подільник 47 кОм / 10 кОм від 10 В дає 1,75 В. Чи буде база транзистора точно на 1,75 В?"
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
  - source_id: fiore-voltage-divider-bias
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 5.4 Voltage Divider Bias"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/05:_BJT_Biasing/5.4:_Voltage_Divider_Bias
---

## Short answer

Ні. 1,75 В – напруга ненавантаженого подільника; струм бази створює падіння на його еквівалентному опорі `R_TH`, тому `V_B` = `V_TH` - `I_B`·`R_TH` і нижча за 1,75 В.[^fiore-voltage-divider-bias]

## Detailed explanation

Подільник із `R_1` = 47 кОм (зверху, до 10 В) і `R_2` = 10 кОм (знизу) без навантаження дає `V_TH` = `V_CC`·`R_2`/(`R_1` + `R_2`) = 10·10/57 ≈ 1,754 В. Еквівалентний опір подільника – `R_TH` = `R_1` || `R_2` = 47·10/57 ≈ 8,25 кОм.[^fiore-voltage-divider-bias] Значення 1,75 В – це напруга, коли від подільника нічого не відбирають. Підключення бази змінює цей випадок.

База відбирає струм `I_B` із середньої точки подільника. Цей струм тече через `R_TH`, тому напруга в точці підключення падає на `I_B`·`R_TH`. У Fiore рівняння петлі база–емітер записано як `V_TH` = `I_B`·`R_TH` + `V_BE` + `I_E`·`R_E`, отже `V_B` = `V_BE` + `I_E`·`R_E` = `V_TH` - `I_B`·`R_TH`.[^fiore-voltage-divider-bias] Наприклад, за `I_B` = 10 мкА падіння становить 8,25 кОм · 10 мкА ≈ 82 мВ, і `V_B` ≈ 1,754 - 0,082 ≈ 1,67 В.

Точне значення `V_B` залежить від `I_B`, а той, у свою чергу, від `I_C` і `β` саме цього транзистора (`I_B` = `I_C`/`β`).[^fiore-voltage-divider-bias] Тому «точно 1,75 В» не очікують. До цього додаються допуски резисторів: ±5 % у кожному з двох резисторів змінюють `V_TH` більш ніж на 0,1 В. Правильна перевірка – розрахувати `I_B` із робочої точки, відняти `I_B`·`R_TH` і порівняти з виміряною напругою.

**Типові помилки:**

- Вважати напругу подільника напругою на базі, не віднімаючи `I_B`·`R_TH`.[^fiore-voltage-divider-bias]
- Брати `R_TH` як один із резисторів, а не як `R_1` || `R_2`.[^fiore-voltage-divider-bias]
- Очікувати точного значення при допусках резисторів: ±5 % змінюють `V_TH` більш ніж на 0,1 В.
