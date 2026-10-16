---
id: emb-elee-0199
title: "Як врахувати навантаження подільника зміщення базою транзистора?"
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
  - source_id: fiore-bjt-datasheet
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 4.4 BJT Data Sheet Interpretation"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/04:_Bipolar_Junction_Transistors_(BJTs)/4.4:_BJT_Data_Sheet_Interpretation
---

## Short answer

Подільник замінюють еквівалентом Тевеніна: `V_TH = V_CC*R2/(R1+R2)`, `R_TH = R1*R2/(R1+R2)`. Далі `I_B = (V_TH - V_BE)/(R_TH + (beta+1)*R_E)` і `V_B = V_TH - I_B*R_TH`, де `I_E` = (`beta`+1)*`I_B`.[^fiore-voltage-divider-bias][^fiore-bjt-basics]

## Detailed explanation

Ідеальний подільник дає `V_B` = `V_TH`, але база забирає струм `I_B` із точки з’єднання `R1` і `R2`. Цей струм тече через `R_TH` і створює падіння `I_B`*`R_TH`, тож `V_B` = `V_TH` - `I_B`*`R_TH`: навантаження базою зсуває напругу вниз. Fiore записує той самий еквівалент Тевеніна `V_TH` = `V_CC`*`R2`/(`R1`+`R2`) і `R_TH` = `R1`*`R2`/(`R1`+`R2`).[^fiore-voltage-divider-bias]

Петля база–емітер дає `V_TH` = `I_B`*`R_TH` + `V_BE` + `I_E`*`R_E`. Оскільки `I_E` = `I_C` + `I_B` і `I_C` = β*`I_B`, маємо `I_E` = (β+1)*`I_B`.[^fiore-bjt-basics] Підставивши, отримуємо `I_B` = (`V_TH` - `V_BE`)/(`R_TH` + (β+1)*`R_E`). Fiore використовує наближення `I_E` ≈ `I_C`, яке замінює (β+1) на β і дає `I_C` = (`V_TH` - `V_BE`)/(`R_E` + `R_TH`/β).[^fiore-voltage-divider-bias]

Приклад: `V_CC` = 12 В, `R1` = 47 кОм, `R2` = 10 кОм, `R_E` = 1 кОм, β = 100, `V_BE` = 0,7 В. Тоді `V_TH` = 12*10/57 ≈ 2,105 В і `R_TH` = 47*10/57 ≈ 8,25 кОм. Якщо ігнорувати навантаження базою, `I_E` = (2,105 - 0,7) / 1 кОм ≈ 1,405 мА. З навантаженням `I_B` = 1,405 / (8,25 + 101*1) мА ≈ 0,0129 мА, тобто 12,9 мкА, тоді `I_E` = 101*12,9 мкА ≈ 1,30 мА, а `V_B` = 2,105 - 0,0129*8,25 ≈ 2,00 В. Наївний розрахунок завищує `I_E` приблизно на 8 %: різниця дорівнює `R_TH`/((β+1)*`R_E`) ≈ 8,25 кОм / 101 кОм ≈ 8 %.

Це та сама умова, що в Fiore для наближеного струму: доданок `R_TH`/β можна відкинути, якщо `R_E` значно більший за `R_TH`/β.[^fiore-voltage-divider-bias] У прикладі `R_TH`/β ≈ 82 Ом проти `R_E` = 1 кОм, тому помилка близько 8 %. Навіть при струмі подільника в 16 разів більшому за `I_B` (`V_CC`/(`R1`+`R2`) ≈ 0,21 мА) похибка лишається ≈ 8 %. Щоб її зменшити, потрібно зменшити `R_TH` відносно (β+1)*`R_E`. Для β беруть значення з даташита за робочого струму, бо β залежить від струму й температури.[^fiore-bjt-datasheet]

**Типові помилки:**

- Брати `V_B` = `V_TH` без перевірки: навантаження базою зсуває його на `I_B`*`R_TH`.
- Вважати, що струму подільника в 10–20 разів більше за `I_B` достатньо без перевірки `R_TH` відносно (β+1)*`R_E`.
- Ставити `I_C` ≈ (`V_TH` - `V_BE`)/`R_E` при малому `R_E`, не перевіривши умову наближення.
