---
id: emb-elee-0200
title: "`V_CC` = 5 В, подільник 33 кОм / 22 кОм, `R_E` = 1 кОм, β = 100. Які `V_B` і `I_E` з урахуванням струму бази?"
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
  - source_id: fiore-bjt-basics
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 4.2 The Bipolar Junction Transistor"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/04:_Bipolar_Junction_Transistors_(BJTs)/4.2:_The_Bipolar_Junction_Transistor
  - source_id: fiore-bjt-ac-model
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 7.2 Simplified AC Model of the BJT"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/07:_BJT_Small_Signal_Amplifiers/7.2:_Simplified_AC_Model_of_the_BJT
---

## Short answer

Подільник 33 кОм зверху до `V_CC` і 22 кОм до землі дає `V_TH` = 2 В і `R_TH` = 13,2 кОм. З урахуванням бази (`V_BE` ≈ 0,7 В, β = 100): `I_B` ≈ 11,4 мкА, `V_B` ≈ 1,85 В, `V_E` ≈ 1,15 В, `I_E` ≈ 1,15 мА – помітно менше за 1,3 мА, які дає наближення без струму бази.[^fiore-voltage-divider-bias]

## Detailed explanation

Подільник з 33 кОм до `V_CC` і 22 кОм до землі за теоремою Тевенена еквівалентний джерелу `V_TH` = 5 В × 22 кОм / 55 кОм = 2 В з внутрішнім опором `R_TH` = 33 кОм ∥ 22 кОм = 13,2 кОм.[^fiore-voltage-divider-bias] Без струму бази напруга на базі дорівнювала б 2 В. Але база споживає струм, який проходить через `R_TH`, тож напруга на базі падає нижче `V_TH` на `I_B` × `R_TH`. Саме цей ефект і треба врахувати.

Контур база–емітер дає `V_TH` = `I_B` × `R_TH` + `V_BE` + `I_E` × `R_E`. Оскільки `I_E` = (β + 1) × `I_B`, маємо `I_B` = (`V_TH` − `V_BE`) / (`R_TH` + (β + 1) × `R_E`) = 1,3 В / (13 200 Ом + 101 000 Ом) ≈ 11,4 мкА.[^fiore-bjt-basics] Далі `V_B` = 2 В − 11,4 мкА × 13,2 кОм ≈ 2 В − 0,15 В = 1,85 В, `V_E` = `V_B` − 0,7 В ≈ 1,15 В, а `I_E` = 1,15 В / 1 кОм ≈ 1,15 мА. Перевірка: `I_E` / `I_B` ≈ 1,15 мА / 11,4 мкА ≈ 101, як і має бути.

Ідеалізована відповідь без струму бази дає `I_E` = (`V_TH` − `V_BE`) / `R_E` = 1,3 мА. Точне значення 1,15 мА, тож ідеалізоване завищене приблизно на 13 %. Наближення `I_E` ≈ (`V_TH` − `V_BE`) / `R_E` справедливе, коли `R_E` значно більший за `R_TH` / β.[^fiore-voltage-divider-bias] Тут `R_TH` / β = 132 Ом проти 1 кОм, тому похибка саме така, і нехтувати нею не можна. Точна форма `I_E` = (`V_TH` − `V_BE`) / (`R_E` + `R_TH` / (β + 1)) дає ті самі 1,15 мА.

Залежність від β теж є: доданок `R_TH` / (β + 1) дорівнює 131 Ом при β = 100, 259 Ом при β = 50 і 66 Ом при β = 200, тому `I_E` ≈ 1,15 мА, 1,03 мА і 1,22 мА відповідно. Залежність від `V_BE` теж помітна: похибка 0,1 В дає ≈ 0,09 мА в `I_E`. До того ж `V_BE` змінюється зі струмом і температурою: за експоненційною моделлю він зростає приблизно на 26 мВ при збільшенні струму в e разів.[^fiore-bjt-ac-model]

**Типові помилки:**
- Вважати `V_B` = `V_TH` і брати `I_E` = (`V_TH` − `V_BE`) / `R_E` без перевірки струму бази: тут це завищує `I_E` приблизно на 13 %.
- Поставити 22 кОм зверху: тоді `V_TH` = 5 В × 33 / 55 = 3 В, а не 2 В.
- Вважати `V_BE` = 0,7 В сталим: це лише наближення для кремнію при певному струмі.
