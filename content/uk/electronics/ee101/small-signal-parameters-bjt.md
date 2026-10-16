---
id: emb-elee-0214
title: "Які малосигнальні параметри BJT при `I_C` ≈ 1 мА і β = 100?"
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
  - source_id: fiore-bjt-ac-model
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 7.2 Simplified AC Model of the BJT"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/07:_BJT_Small_Signal_Amplifiers/7.2:_Simplified_AC_Model_of_the_BJT
  - source_id: fiore-common-emitter-amplifier
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 7.3 Common Emitter Amplifier"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/07:_BJT_Small_Signal_Amplifiers/7.3:_Common_Emitter_Amplifier
---

## Short answer

`g_m` = `I_C`/`V_T` ≈ 1 мА / 26 мВ ≈ 38,5 мСм, а `r'_e` = 26 мВ / `I_C` ≈ 26 Ом. Вхідний опір бази без опору в емітері дорівнює `r_pi` = β/`g_m` = β·`r'_e` ≈ 2,6 кОм.[^fiore-bjt-ac-model][^fiore-common-emitter-amplifier]

## Detailed explanation

Малосигнальну модель BJT на низьких і середніх частотах складають із динамічного опору переходу база–емітер. Цей опір визначає постійний колекторний струм: `r'_e` = 26 мВ / `I_C`. За `I_C` = 1 мА він дорівнює 26 Ом.[^fiore-bjt-ac-model] Число 26 мВ – наближення `V_T` = kT/q при 300 K ≈ 25,9 мВ, тож значення наближене. Обернена величина опору – крутизна `g_m` = `I_C`/`V_T`, яку Fiore називає transconductance; за 25,9 мВ вона дорівнює 38,6 мСм, за 26 мВ – 38,5 мСм.

Вхідний опір бази залежить від β. Коли в емітері немає опору (`r_E` = 0), база бачить опір β·`r'_e` = 100·26 Ом = 2,6 кОм. Це та сама величина, що β/`g_m`, бо `g_m` = 1/`r'_e`.[^fiore-bjt-ac-model][^fiore-common-emitter-amplifier] Якщо в емітері є `R_E`, опір стає β(`r'_e` + `R_E`), тобто значно більшим.[^fiore-common-emitter-amplifier]

**Приклад:** при `I_C` = 2 мА маємо `g_m` ≈ 77 мСм, `r'_e` ≈ 13 Ом і вхідний опір бази без `R_E` ≈ 1,3 кОм за β = 100. Подвоєння струму подвоює `g_m` і вдвічі зменшує `r'_e`. Зміна β при фіксованому `I_C` `g_m` не змінює, бо `g_m` = `I_C`/`V_T` від β не залежить.[^fiore-bjt-ac-model]

Модель не враховує ємності переходів і індуктивності виводів, тож придатна лише для низьких і середніх частот.[^fiore-bjt-ac-model] Опір об’ємного матеріалу в `r'_e` не входить, тому значення трохи занижене. Крім того, струм насичення `I_S` залежить від температури, а разом із ним змінюється і `r'_e`.[^fiore-bjt-ac-model]

**Типові помилки:**

- Вважати `g_m` залежним від β: `g_m` = `I_C`/`V_T` від β не залежить.[^fiore-bjt-ac-model]
- Брати 26 мВ/`I_C` за точне значення: модель наближена, об’ємний опір не входить, а `r'_e` змінюється з температурою.[^fiore-bjt-ac-model]
- Забувати `R_E` у вхідному опорі бази: з `R_E` він дорівнює β(`r'_e` + `R_E`).[^fiore-common-emitter-amplifier]
