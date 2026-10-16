---
id: emb-elee-0190
title: "Чому не можна проєктувати транзисторну схему під одне типове значення β?"
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
  - source_id: fiore-bjt-datasheet
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 4.4 BJT Data Sheet Interpretation"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/04:_Bipolar_Junction_Transistors_(BJTs)/4.4:_BJT_Data_Sheet_Interpretation
  - source_id: fiore-ebers-moll
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 4.5 Ebers-Moll Model"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/04:_Bipolar_Junction_Transistors_(BJTs)/4.5:_Ebers-Moll_Model
  - source_id: fiore-pn-junction
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 2.2 The PN Junction"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/02:_PN_Junctions_and_Diodes/2.2:_The_PN_Junction
  - source_id: fiore-biasing-need
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 5.2 The Need For Biasing"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/05:_BJT_Biasing/5.2:_The_Need_For_Biasing
  - source_id: fiore-emitter-bias
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 5.3 Two-Supply Emitter Bias"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/05:_BJT_Biasing/5.3:_Two-Supply_Emitter_Bias
---

## Short answer

β змінюється між екземплярами[^fiore-ebers-moll] і зі струмом та температурою,[^fiore-bjt-datasheet] а `V_BE` також не стала.[^fiore-pn-junction] Надійна схема задає робочу точку резисторами і зворотним зв’язком, щоб струм колектора не залежав від β.[^fiore-biasing-need]

## Detailed explanation

Коефіцієнт β не є сталою властивістю типу транзистора: він різний для кожного приладу. Для 2N3904 даташит за умов близько 10 мА дає діапазон від 100 до 300, тобто трикратний розкид.[^fiore-bjt-datasheet] Крім того, β падає при дуже малих і дуже великих струмах колектора та зростає з температурою.[^fiore-bjt-datasheet] Він залежить і від напруги `V_CE`, тож одне «типове» значення не описує прилад за всіх умов.[^fiore-ebers-moll]

Наслідок видно на схемі з фіксованим струмом бази. Джерело `V_BB` = 10 В через `R_B` = 200 кОм задає `I_B = (V_BB - V_BE)/R_B` ≈ 46.5 мкА, а `I_C = β*I_B`. При `V_CC` = 15 В і `R_C` = 1 кОм для β = 100 маємо `I_C` = 4.65 мА і `V_CE` = 10.35 В. Для β = 300, верхньої межі з діапазону, `I_C` = 13.95 мА і `V_CE` = 1.05 В: транзистор близько до насичення. Подвоєння β тут подвоює струм колектора.[^fiore-ebers-moll]

`V_BE` теж залежить від стану: зі зростанням температури струм насичення переходу зростає, і при тому самому струмі напруга на переході зменшується.[^fiore-pn-junction] У базовому зсуві з фіксованим `I_B` головна причина теплової петлі – зростання β з температурою: більший струм нагріває прилад, β зростає, струм стає ще більшим. Це тепловий додатний зворотний зв’язок, і без обмеження прилад може перегрітися й вийти з ладу.[^fiore-ebers-moll]

Надійна схема задає струм так, щоб він залежав від стабільних величин, а не від β. В емітерному зсуві від двох джерел, якщо `R_E` значно більший за `R_B/β`, β майже не впливає на `I_C`. У прикладі підручника (`R_E` = 2.7 кОм, `R_B` = 5.1 кОм) подвоєння β змінює `I_C` приблизно на 1 %.[^fiore-emitter-bias] Проєктувати слід так, щоб схема працювала на всьому діапазоні β з даташиту і при робочих температурах, тобто перевіряти межі, а не одне типове значення.

**Типові помилки:**

- Вважати β сталою величиною типу транзистора і брати одне значення з таблиці.
- Розраховувати `I_C = β*I_B` для схеми з фіксованим `I_B` без перевірки діапазону β, `V_CE` і насичення.
- Не враховувати, що `V_BE` і β залежать від температури.
