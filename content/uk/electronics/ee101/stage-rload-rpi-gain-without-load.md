---
id: emb-elee-0215
title: "Каскад CE: `R_C` = 4,7 кОм, `R_E` = 1 кОм, `R_load` = 10 кОм, β = 100, `r_pi` ≈ 2,6 кОм. Яке підсилення з навантаженням і без нього?"
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

Із навантаженням `A_v = -beta*R_C_ac/(r_pi + (beta+1)*R_E)`, де `R_C_ac = R_C || R_load` ≈ 3,20 кОм, маємо `A_v` ≈ -3,09; без навантаження `A_v` ≈ -4,54. Навантаження не можна ігнорувати: воно знижує підсилення майже на третину.[^fiore-common-emitter-amplifier]

## Detailed explanation

**Умови й модель.** Припускаємо, що `R_E` не зашунтовано, тобто за змінним струмом він повністю в колі, а генератор має нульовий внутрішній опір. Розділовий конденсатор на виході в середній смузі є коротким замиканням, а шина живлення є AC-землею, тому змінний опір колектора – це паралель `R_C` і `R_load`: `R_C_ac = 4,7 кОм || 10 кОм = 47/14,7 ≈ 3,20 кОм`.[^fiore-common-emitter-amplifier]

**Вираз для підсилення.** З `i_C = β·i_B` і `r'_e = 26 мВ / I_C` випливає `r_pi = β·r'_e`.[^fiore-bjt-ac-model] Напруга бази `v_b = i_b*(r_pi + (β+1)*R_E)`, бо емітерний струм `(β+1)*i_b` тече через `R_E`, а колекторний струм `β*i_b` тече через `R_C_ac`. Звідси `A_v = -β*R_C_ac/(r_pi + (β+1)*R_E)`. При β = 100 і `r_pi = 2,6 кОм` маємо `r'_e = 26 Ом`, тобто `I_C = 1 мА`. Fiore записує той самий каскад як `-r_C/(r'_e + r_E)` з наближенням `I_E ≈ I_C`.[^fiore-common-emitter-amplifier] Для `r_E = 1 кОм` це `-3197/1026 ≈ -3,12`, тобто на 1 % більше за точне значення -3,09.

**Числа.** Без навантаження `A_v = -100*4,7/(2,6 + 101*1) ≈ -4,54`. З навантаженням `A_v = -100*3,20/103,6 ≈ -3,09`. Підсилення пропорційне `R_C_ac`, а знаменник від навантаження не залежить, тож навантаження зменшує модуль підсилення в тій самій пропорції: 3,20/4,70 ≈ 0,68, тобто на 32 %. Оскільки `(β+1)*R_E = 101 кОм` значно більше за `r_pi = 2,6 кОм`, можна записати `A_v ≈ -R_C_ac/R_E`, тобто -3,20 і -4,70; для цього каскаду похибка такого наближення близько 4 %.

**Межі.** Формула справедлива для малих сигналів у середній смузі частот. Скінченний вихідний опір транзистора (ефект Ерлі) тут не враховано: колекторний струм трохи зростає з `V_CE`,[^fiore-bjt-collector-curves] а Fiore оцінює `r'_C` порядку 100 кОм.[^fiore-common-emitter-amplifier] Паралель `4,7 кОм || 100 кОм ≈ 4,49 кОм` знизила б модуль підсилення приблизно на 4,5 %, що не змінює висновку про вплив навантаження.

**Типові помилки:**

- Брати `R_load` замість `R_C || R_load` для змінного сигналу.
- Вважати, що `R_E` не впливає на підсилення, забувши про множник `(β+1)` у знаменнику.
- Забути про знак: каскад зі спільним емітером інвертує фазу, тому `A_v` від’ємне.[^fiore-bjt-ac-model]
