---
id: emb-elee-0228
title: "Яку роль у практичному аудіопідсилювачі зі спільним емітером виконують вхідний і вихідний конденсатори та нешунтований `R_E`?"
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
---

## Short answer

Вхідний конденсатор блокує постійну напругу бази від джерела, а вихідний – постійну напругу колектора від навантаження; обидва пропускають змінний сигнал.[^fiore-common-emitter-amplifier] Нешунтований `R_E` зменшує підсилення, але також зменшує залежність підсилення від `r'_e` і спотворення.[^fiore-common-emitter-amplifier]

## Detailed explanation

Підсилювач зі спільним емітером підсилює змінний сигнал поверх постійного зміщення, яке задають резистори. Щоб сигнал не порушував це зміщення, на вході й виході ставлять конденсатори зв’язку. Для постійного струму вони є розривами, тож вхідне джерело не змінює зміщення і не зсуває робочу точку; для змінного сигналу їхній реактанс має бути малим порівняно з навколишніми резисторами на частоті сигналу, тому сигнал проходить.[^fiore-common-emitter-amplifier] Вихідний конденсатор робить те саме з навантаженням: постійна колекторна напруга не потрапляє в навантаження чи наступний каскад.

Нешунтований `R_E` – це резистор у емітері (emitter degeneration), що дає від’ємний зворотний зв’язок. Якщо `C_E` шунтує його, на змінному сигналі емітер заземлений, і `A_v = -r_C/r'_e`: підсилення максимальне, але залежить від `r'_e`, а отже від струму колектора й температури. Без шунта `A_v = -r_C/(r'_e + R_E)`, де `r_C` – паралель колекторного резистора й навантаження.[^fiore-common-emitter-amplifier][^fiore-bjt-ac-model]

Наслідок у цифрах. Без навантаження, при `R_C = 4.7 kΩ`, `R_E = 1 kΩ` і `r'_e = 26 Ω` (струм близько 1 mA) маємо `A_v = -4700/1026 ≈ -4.6` без шунта та `-4700/26 ≈ -181` з повним шунтом. Тобто `R_E` зменшує підсилення приблизно в `1026/26 ≈ 39` разів. Зате знаменник `r'_e + R_E` чутливий до `r'_e` значно менше: якщо `r'_e` зросте на 10% (з 26 до 28.6 Ω), знаменник без шунта зросте лише на 0.25% (з 1026 до 1028.6), а з повним шунтом – на 10%.[^fiore-common-emitter-amplifier]

Ємності мають бути такими, щоб їхній реактанс на частоті сигналу був малим порівняно з навколишніми резисторами; інакше на низьких частотах сигнал слабшає. Тому вхідний і вихідний конденсатори вибирають разом з опорами, які вони бачать, а не ізольовано.[^fiore-common-emitter-amplifier] Нешунтований `R_E` цього не змінює, але зменшує підсилення, бо додає опір у знаменник.

**Типові помилки:**

- Вважати, що вихідний конденсатор пропускає постійну напругу колектора до навантаження.
- Очікувати від нешунтованого `R_E` такого самого підсилення, як при шунті: різниця приблизно в 39 разів.
- Брати `A_v = -R_C/r'_e` без `R_E`, коли `C_E` відсутній.
