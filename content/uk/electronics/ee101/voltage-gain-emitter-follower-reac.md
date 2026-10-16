---
id: emb-elee-0204
title: "Яке підсилення за напругою емітерного повторювача при `I_E` = 1 мА і `R_E,ac` = 1 кОм?"
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
  - source_id: fiore-common-collector
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 7.4 Common Collector Amplifier"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/07:_BJT_Small_Signal_Amplifiers/7.4:_Common_Collector_Amplifier
  - source_id: fiore-bjt-ac-model
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 7.2 Simplified AC Model of the BJT"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/07:_BJT_Small_Signal_Amplifiers/7.2:_Simplified_AC_Model_of_the_BJT
---

## Short answer

`A_v` ≈ `R_E,ac` / (`r_e` + `R_E,ac`) = 1000 / (26 + 1000) ≈ 0,975, де `R_E,ac` = `R_E` ∥ `R_load`, а `r_e` ≈ 26 мВ / `I_E` = 26 Ом.[^fiore-common-collector][^fiore-bjt-ac-model] Вихід синфазний входу, інверсії немає.[^fiore-common-collector]

## Detailed explanation

Формула виходить із малосигнальної схеми. Струм емітера `i_e` проходить через `r_e` і `R_E,ac`, тож напруга бази `v_B` = `i_e` × (`r_e` + `R_E,ac`), а напруга емітера `v_E` = `i_e` × `R_E,ac`. Ділення дає `A_v` = `v_E` / `v_B` = `R_E,ac` / (`r_e` + `R_E,ac`).[^fiore-common-collector] При `I_E` = 1 мА маємо `r_e` ≈ 26 мВ / 1 мА = 26 Ом, тож `A_v` = 1000 / 1026 ≈ 0,975.[^fiore-bjt-ac-model] Отже, близько 2,5 % вхідної напруги падає на самому переході.

Залежність від `R_E,ac` показує, наскільки ця формула чутлива. Якщо до `R_E` = 1 кОм паралельно підключити навантаження 1 кОм, то `R_E,ac` = 500 Ом і `A_v` = 500 / 526 ≈ 0,95. При `R_E,ac` = 100 Ом підсилення падає до 100 / 126 ≈ 0,79. Чим менший `R_E,ac` порівняно з `r_e`, тим більша втрата.

Межі формули. Це відношення `v_E` / `v_B`, тобто від бази, а не від джерела сигналу. Джерело з великим внутрішнім опором і вхідний опір каскаду з подільником бази зменшують сигнал, що доходить до бази. У прикладі підручника з іншими номіналами підсилення від бази становить 0,944, а з урахуванням джерела 1 кОм – близько 0,85.[^fiore-common-collector] Крім того, `r_e` залежить від струму й температури, тож значення 0,975 відповідає 1 мА і 300 K; при інших умовах `r_e` і підсилення змінюються.[^fiore-bjt-ac-model]

**Типові помилки:**
- Брати `R_E` замість `R_E,ac` у навантаженому повторювачі: при паралельному навантаженні 1 кОм `A_v` ≈ 0,95, а не 0,975.
- Вважати підсилення точно 1: `r_e` > 0, тому `A_v` завжди менше 1.
- Приймати 0,975 за підсилення всього каскаду з джерелом: джерело і подільник бази дають менше.
