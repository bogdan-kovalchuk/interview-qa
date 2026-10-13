---
id: emb-elee-0197
title: "Чи створює один великий резистор від живлення до бази стабільну напругу бази?"
description: "Чи створює один великий резистор від живлення до бази стабільну напругу бази?"
track: electronics
section: ee101
level: junior
type: pitfall
tags: []
status: published
updated: 2026-10-13
content_revision: 2
reconciled_with:
  en: 2
anki:
  export: true
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), картки курсу"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
    accessed: 2026-09-27
    kind: community
    version: null
    applicability: "Походження питання: лекція 68, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-13; курс не є доказом цих тверджень."
  - source_id: aac-alternating-current
    title: "All About Circuits textbook, Volume II: AC"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: AC-кола, реактивний опір, фазори, імпеданс, фільтри й трансформатори; конкретні номінали й схеми курсу можуть відрізнятися."
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: діоди, стабілітрони, біполярні й польові транзистори та джерела живлення; конкретні номінали й схеми курсу можуть відрізнятися."
  - source_id: fiore-bjt-ebers-moll
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 4.5 Ebers-Moll Model"
    url: "https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/04:_Bipolar_Junction_Transistors_(BJTs)/4.5:_Ebers-Moll_Model"
    accessed: 2026-10-13
    kind: book
    version: null
    applicability: "Підручник, розділ 4.5: приклад базового зміщення з резистором R_B, I_B = (V_BB - V_BE)/R_B; при β = 100 і 200 колекторний струм 4,65 мА і 9,3 мА; β змінюється між екземплярами, зі струмом і температурою. Загальна картина; числа стосуються лише цього кола."
  - source_id: fiore-bias-need
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 5.2 The Need For Biasing"
    url: "https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/05:_BJT_Biasing/5.2:_The_Need_For_Biasing"
    accessed: 2026-10-13
    kind: book
    version: null
    applicability: "Підручник, розділ 5.2: навіщо потрібне зміщення (V_BE ≈ 0,7 В; без постійного зміщення від’ємна півхвиля сигналу в кілька сотень мілівольт ігнорується); нестабільна Q-точка погіршує підсилення, спотворення й вихідну потужність. Загальна картина."
  - source_id: fiore-voltage-divider-bias
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 5.4 Voltage Divider Bias"
    url: "https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/05:_BJT_Biasing/5.4:_Voltage_Divider_Bias"
    accessed: 2026-10-13
    kind: book
    version: null
    applicability: "Підручник, розділ 5.4: подільник напруги з еквівалентом Тевеніна V_TH і R_TH; петля база–емітера; наближення I_E ≈ I_C і умова R_E значно більше за R_TH/β; подільник названо конфігурацією з високою стабільністю зміщення. Номінали прикладу підручника стосуються лише його кола."
---

## Short answer

Ні: резистор задає струм бази, а не її напругу. Напругу бази фіксує база–емітерний перехід, близько 0,7 В, а колекторний струм `I_C` = β*`I_B` змінюється разом із β, яка різниться між екземплярами й залежить від температури.[^fiore-bjt-ebers-moll]

## Detailed explanation

Резистор `R_B` між живленням `V_CC` і базою має падіння `V_CC` - `V_B`. При прямо зміщеному переході база–емітер і емітері на землі `V_B` ≈ `V_BE` ≈ 0,7 В для кремнію.[^fiore-bjt-ebers-moll] Отже падіння на резисторі майже фіксоване, і струм бази визначає сам резистор: `I_B` = (`V_CC` - `V_BE`) / `R_B`. Резистор задає струм бази, а не напругу бази, тому велике `R_B` не є способом задати напругу бази: воно лише зменшує `I_B`, а стабільність колекторного струму від цього не змінюється.

Колекторний струм далі визначає β, бо `I_C` = β*`I_B`. Підручник розглядає таке коло: база через `R_B` = 200 кОм від 10 В, колектор через 1 кОм від 15 В. При β = 100 виходить `I_B` = 46,5 мкА, `I_C` = 4,65 мА і `V_CE` = 10,35 В. При β = 200 той самий `I_B` дає вдвічі більший `I_C` = 9,3 мА і `V_CE` = 5,7 В.[^fiore-bjt-ebers-moll] Робоча точка зсувається разом із β, хоча база й далі тримається близько 0,7 В.

Підручник називає цю схему головною вадою базового зміщення і описує тепловий ефект: за сталого `I_B` вищий β дає більший `I_C`, більший `I_C` дає більше тепла, а тепло, своєю чергою, підвищує β. Цикл може повторюватися, тож для стабільності потрібна інша схема.[^fiore-bjt-ebers-moll]

Стабільну напругу бази дає подільник. Fiore називає подільник напруги конфігурацією з високою стабільністю зміщення і наближає `V_B` значенням еквівалентної напруги подільника `V_TH`, коли подільник слабо навантажений. Наближення працює, коли `R_E` значно більший за `R_TH`/β; тоді `I_C` майже не залежить від β.[^fiore-voltage-divider-bias]

**Типові помилки:**

- Вважати, що `R_B` задає `V_B`: напругу фіксує `V_BE`, а резистор визначає `I_B`.
- Вважати, що великий `R_B` робить схему стабільною: `I_C` = β*`I_B` лишається залежним від β.
- Ігнорувати тепловий додатний зворотний зв’язок: з ростом температури β зростає, і `I_C` теж.[^fiore-bjt-ebers-moll]

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
