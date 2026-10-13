---
id: emb-elee-0203
title: "Що таке диференційний емітерний опір `r_e` і як його оцінити?"
description: "Що таке диференційний емітерний опір `r_e` і як його оцінити?"
track: electronics
section: ee101
level: junior
type: concept
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
    applicability: "Походження питання: лекція 70, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-13; курс не є доказом цих тверджень."
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
  - source_id: fiore-bjt-ac-model
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 7.2 Simplified AC Model of the BJT"
    url: "https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/07:_BJT_Small_Signal_Amplifiers/7.2:_Simplified_AC_Model_of_the_BJT"
    accessed: 2026-10-13
    kind: book
    version: null
    applicability: "Підручник, розділ 7.2: експоненційна модель переходу (q/kT ≈ 38,6 при 300 K, тобто V_T ≈ 25,9 мВ); динамічний опір r'_e = 26 мВ / I_C без об’ємного опору; залежить від температури; малосигнальна модель для низьких і середніх частот."
  - source_id: fiore-bjt-basics
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 4.2 The Bipolar Junction Transistor"
    url: "https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/04:_Bipolar_Junction_Transistors_(BJTs)/4.2:_The_Bipolar_Junction_Transistor"
    accessed: 2026-10-13
    kind: book
    version: null
    applicability: "Підручник, розділ 4.2: I_E = I_C + I_B, I_C = β·I_B; при значно більшому I_C, ніж I_B, I_E ≈ I_C; V_BE ≈ 0,7 В для кремнію. Загальна картина, не для конкретного транзистора."
---

## Short answer

`r_e` – малосигнальний (диференційний) опір емітерного переходу в робочій точці: обернений нахил експоненційної характеристики база–емітер, `r_e` = dV_BE/dI_E ≈ 26 мВ / `I_E` при 300 K. Для `I_E` = 1 мА це ≈ 26 Ом.[^fiore-bjt-ac-model]

## Detailed explanation

Перехід база–емітер є діодом, тож струм експоненційно залежить від напруги: `I_C` = `I_S` × exp(`V_BE` / `V_T`), де `V_T` = kT/q. При 300 K величина q/kT ≈ 38,6 1/В, тобто `V_T` ≈ 25,9 мВ.[^fiore-bjt-ac-model] Малий змінний сигнал коливається навколо робочої точки, а ділянку характеристики біля неї можна вважати прямою. Її нахил визначає опір: динамічний опір є оберненим нахилом, тобто `r_e` = dV_BE/dI_E ≈ `V_T` / `I_E`.[^fiore-bjt-ac-model]

Числа. При `I_E` = 1 мА маємо `r_e` ≈ 25,9 мВ / 1 мА ≈ 26 Ом; при 0,1 мА – ≈ 260 Ом; при 5 мА – ≈ 5,2 Ом. Підручник записує формулу через `I_C`, але `I_E` = `I_C` + `I_B` і `I_B` = `I_C` / β, тож при великому β різниця між `I_E` і `I_C` мала.[^fiore-bjt-ac-model][^fiore-bjt-basics]

Межі застосування. Значення 26 мВ / `I_C` справедливе, поки змінна складова струму лишається малою, у підручнику – кілька відсотків від струму спокою. Воно трохи занижене, бо не включає об’ємного (bulk) опору. При сталому `I_E` значення `r_e` = `kT` / (`q` × `I_E`) зростає з температурою приблизно на 0,33 % на кельвін (1/300 К ≈ 0,33 %/К). Зменшення `r_e` з ростом температури було б лише при сталому `V_BE`, коли зростає струм, бо `I_S` залежить від температури.[^fiore-bjt-ac-model]

**Типові помилки:**
- Брати відношення `V_BE` / `I_E` (статичний опір: 0,7 В / 1 мА = 700 Ом) замість нахилу: динамічний опір у тій самій точці приблизно в 27 разів менший.[^fiore-bjt-ac-model]
- Вважати, що `r_e` – окремий резистор, який можна виміряти омметром у схемі: омметр дає статичний опір, а не малосигнальний.
- Ігнорувати об’ємний опір і температуру, коли потрібна точність.

## Sources

<!-- generated from frontmatter -->
