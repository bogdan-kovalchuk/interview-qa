---
id: emb-elee-0217
title: "Чому виміряне підсилення від генератора може бути меншим за розраховане від бази?"
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
  - source_id: fiore-common-emitter-amplifier
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 7.3 Common Emitter Amplifier"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/07:_BJT_Small_Signal_Amplifiers/7.3:_Common_Emitter_Amplifier
  - source_id: fiore-bjt-ac-model
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 7.2 Simplified AC Model of the BJT"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/07:_BJT_Small_Signal_Amplifiers/7.2:_Simplified_AC_Model_of_the_BJT
  - source_id: fiore-bjt-collector-curves
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 4.3 BJT Collector Curves"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/04:_Bipolar_Junction_Transistors_(BJTs)/4.3:_BJT_Collector_Curves
---

## Short answer

Вихідний опір генератора утворює подільник із вхідним опором каскаду, тому до бази доходить менший сигнал: `A_v(gen) = A_v(base)*Z_in/(Z_in + R_gen)`.[^fiore-common-emitter-amplifier] Формула для бази також не враховує ефект Ерлі і високочастотні ємності, тож навіть без дільника вона може відрізнятися від виміряного.[^fiore-bjt-collector-curves][^fiore-bjt-ac-model]

## Detailed explanation

**Два різні підсилення.** Розрахункове підсилення `A_v(base) = v_out/v_b` відносить вихід до напруги на базі. Вимірюють же `A_v(gen) = v_out/v_g`, де `v_g` – напруга генератора з внутрішнім опором `R_gen`. Вхідний опір каскаду `Z_in = R_B || β(r'_e + r_E)` разом із `R_gen` утворює дільник:[^fiore-common-emitter-amplifier] `v_b = v_g*Z_in/(Z_in + R_gen)`. Отже `A_v(gen) = A_v(base)*Z_in/(Z_in + R_gen)`, і при ненульовому `R_gen` модуль виміряного підсилення менший за розрахований від бази.

**Приклад.** Припустімо, для ілюстрації, що `R_gen = 1 кОм` і `Z_in = 5 кОм`. Дільник дає `5/(5 + 1) ≈ 0,833`. Для каскаду з попереднього питання без навантаження `A_v(base) ≈ -4,54` (див. qid:emb-elee-0215), тож `A_v(gen) ≈ -3,78`, тобто на 17 % менше. Вхідний опір зростає з β і з `R_E`, якщо `R_E` не зашунтовано,[^fiore-common-emitter-amplifier] тож більший `R_E` послаблює цей ефект.

**Чому формула від бази неточна.** Розрахунок від бази з `r_C = R_C || R_load` опускає скінченний вихідний опір транзистора `r'_C`, який за Fiore має порядок 100 кОм.[^fiore-common-emitter-amplifier] Для `R_C = 4,7 кОм` паралель з `r'_C` дає 4,49 кОм, тобто модуль підсилення менший приблизно на 4,5 %. Це наслідок ефекту Ерлі: колекторний струм трохи зростає зі `V_CE`, а продовження ділянки постійного струму перетинає вісь у точці, що визначає напругу Ерлі `V_A`.[^fiore-bjt-collector-curves] Крім того, модель малого сигналу в Fiore не містить ємностей переходів і призначена для низьких і середніх частот, тож на високих частотах розрахунок від бази теж неточний.[^fiore-bjt-ac-model]

**Типові помилки:**

- Вважати, що генератор віддає всю свою напругу на вхід каскаду: з `R_gen` і `Z_in` завжди є дільник.
- Вважати опір генератора 1 кОм «малим»: при вхідному опорі 5 кОм він забирає майже 17 % сигналу.
- Порівнювати виміряне підсилення з розрахунком від бази, не перераховуючи його через `Z_in` і `R_gen`.
