---
id: emb-elee-0229
title: "Аудіокаскад: `R_C` = 4,7 кОм, `R_E` = 1 кОм, `I_E` ≈ 1 мА, навантаження 10 кОм. Яке підсилення і вихід для 20 мВ peak на базі?"
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
  - source_id: fiore-bjt-basics
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 4.2 The Bipolar Junction Transistor"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/04:_Bipolar_Junction_Transistors_(BJTs)/4.2:_The_Bipolar_Junction_Transistor
---

## Short answer

`A_v = -(R_C||R_load)/(r'_e + R_E) = -3197/1026 ≈ -3.1`, де `r'_e = 26 mV/1 mA = 26 Ω`. Вихід ≈ 62 мВ peak з інверсією фази, якщо 20 мВ peak є саме на базі.[^fiore-common-emitter-amplifier][^fiore-bjt-ac-model]

## Detailed explanation

Це підсилювач зі спільним емітером із нешунтованим `R_E`. На змінному сигналі конденсатори зв’язку є короткими замиканнями, тож колекторний опір для змінного сигналу – це паралель `R_C` і навантаження: `r_C = R_C||R_load = 4700*10000/(4700+10000) ≈ 3197 Ω`. Конденсатора в емітері немає, тож у знаменнику стоїть сам `R_E = 1 kΩ`. Підсилення має вигляд `A_v = -r_C/(r'_e + R_E)`.[^fiore-common-emitter-amplifier]

Опір `r'_e` визначає струм колектора: `r'_e = 26 mV / I_C`. Для `I_E = 1 mA` і `I_C ≈ I_E` дістаємо `r'_e = 26 Ω`.[^fiore-bjt-basics] Число 26 мВ – округлене значення 25,9 мВ при 300 K, і `r'_e` змінюється з температурою.[^fiore-bjt-ac-model] Отже `r'_e + R_E = 26 + 1000 = 1026 Ω`.

Підсилення: `A_v = -3197/1026 ≈ -3.116`, тобто модуль близько 3,1, або `20*log10(3.116) ≈ 9.9 dB`. Знак мінус означає інверсію сигналу на 180°.[^fiore-common-emitter-amplifier] Вихід: `3.116*20 mV ≈ 62.3 mV peak`, тобто `-62.3 mV peak` відносно базового сигналу. Без навантаження знаменник той самий, а `r_C = 4700 Ω`, тож підсилення було б `-4700/1026 ≈ -4.6`; навантаження 10 kΩ знижує його приблизно на третину.

Межі. Формула дає підсилення від бази до виходу, тому 20 mV беремо саме на базі. Якщо ж вони задані на генераторі з внутрішнім опором, сигнал на базі слабший через дільник із вхідним опором каскаду. За Fiore `Z_in(base) = β(r'_e + R_E)`; при β = 100 це `100*1026 ≈ 103 kΩ`, але β в умові не задано, а в паралелі з базовими резисторами вхідний опір буде меншим, тому вплив дільника без цих даних не оцінюється.[^fiore-common-emitter-amplifier]

**Типові помилки:**

- Брати `r_C = R_C`, не додаючи навантаження паралельно.
- Ігнорувати `R_E` у знаменнику: `-3197/26 ≈ -123` замість `-3.1` – це вже схема з повним шунтом.
- Вважати, що 20 mV на виході генератора – те саме, що 20 mV на базі, і не врахувати дільник.
