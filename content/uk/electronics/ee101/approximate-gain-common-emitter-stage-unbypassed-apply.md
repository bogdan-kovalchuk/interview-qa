---
id: emb-elee-0209
title: "Яке наближене підсилення каскаду зі спільним емітером з нешунтованим `R_E` і коли воно придатне?"
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
  - source_id: fiore-common-collector-amplifier
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 7.4 Common Collector Amplifier"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/07:_BJT_Small_Signal_Amplifiers/7.4:_Common_Collector_Amplifier
  - source_id: fiore-emitter-bias
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 5.3 Two-Supply Emitter Bias"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/05:_BJT_Biasing/5.3:_Two-Supply_Emitter_Bias
---

## Short answer

За нешунтованого `R_E` при `R_E ≫ r_e` і навантаженні `R_L ≫ R_C` підсилення наближено дорівнює `A_v ≈ -R_C/R_E`; мінус означає інверсію. Нешунтований `R_E` зменшує підсилення, зате робить його стабільнішим (менша залежність від `r_e` і β) і зменшує спотворення; стабільність робочої точки забезпечує `R_E` за постійним струмом і при шунтуванні.[^fiore-common-emitter-amplifier][^fiore-emitter-bias]

## Detailed explanation

Точний вираз для каскаду з нешунтованим `R_E` такий: `A_v = -r_C/(r_e + R_E)`, де `r_C = R_C || R_L`. Його виводять так: напруга на базі дорівнює падінню змінного струму емітера на `r_e + R_E`, а колекторний змінний струм майже дорівнює струму емітера, бо β велике. Джерело при цьому має малий опір порівняно з вхідним опором каскаду, тож майже вся напруга сигналу потрапляє на базу.[^fiore-common-emitter-amplifier][^fiore-common-collector-amplifier] Якщо `R_E ≫ r_e` і `R_L ≫ R_C`, член `r_e` можна знехтувати, і виходить `A_v ≈ -R_C/R_E`. У цьому виразі β немає, тому підсилення не залежить від розкиду β; це наближення справедливе за великого β, коли `I_E ≈ I_C`.

Приклад: `R_C = 4,7 кОм`, `R_E = 470 Ом`, `I_E ≈ I_C = 1 мА`, отже `r_e = 26 мВ / 1 мА = 26 Ом`. Точний вираз дає `-4700/(470 + 26)` ≈ -9,5, а наближений `-4700/470 = -10`. Похибка близько 5 %, бо `R_E/r_e` ≈ 18. Якщо взяти `R_E = 47 Ом`, точне значення `-4700/73` ≈ -64, а наближене -100: похибка понад 50 %, бо `R_E/r_e` ≈ 1,8. Отже наближення тим точніше, чим більше `R_E` відносно `r_e`, а межу варто вибирати за допустимою похибкою.

Нешунтований `R_E` стабілізує постійний режим. За умови `R_E ≫ R_B/β` струм `I_C` майже не залежить від β, тобто робоча точка стабільна.[^fiore-emitter-bias] Конденсатор, який шунтує `R_E`, для постійного струму розімкнений, тож стабілізація зберігається. Для змінного сигналу шунтування замикає `R_E`: `r_E = 0`, і підсилення стає `-r_C/r_e`, що може бути в десятки разів більше. Тоді воно залежить від `r_e`, тобто від струму й температури, і зростають спотворення.[^fiore-common-emitter-amplifier]

**Типові помилки:**

- Застосовувати `A_v = -R_C/R_E` без перевірки, що `R_E ≫ r_e`.
- Ігнорувати `R_L`, підключений паралельно до `R_C`.
- Вважати, що шунтований `R_E` не змінює стабільність постійного режиму: він змінює лише змінний сигнал.
