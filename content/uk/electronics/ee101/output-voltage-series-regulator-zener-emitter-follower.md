---
id: emb-elee-0202
title: "Яку вихідну напругу дасть послідовний стабілізатор зі стабілітроном 5,6 В на базі емітерного повторювача?"
description: "Яку вихідну напругу дасть послідовний стабілізатор зі стабілітроном 5,6 В на базі емітерного повторювача?"
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
    applicability: "Походження питання: лекція 69, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-13; курс не є доказом цих тверджень."
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
  - source_id: fiore-zener-follower
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 4.7 BJT Switching and Driver Applications"
    url: "https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/04:_Bipolar_Junction_Transistors_(BJTs)/4.7:_BJT_Switching_and_Driver_Applications"
    accessed: 2026-10-13
    kind: book
    version: null
    applicability: "Підручник, розділ 4.7.3 (Zener Follower): стабілітрон зворотно зміщений через резистор, вихід знімають з емітера; вихідна напруга V_Z − V_BE. Розділ не розглядає залежність V_BE від струму й температури та мінімальний струм стабілітрона."
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
  - source_id: nexperia-an90031
    title: "Nexperia AN90031: Zener diodes – physical basics, parameters and application examples"
    url: https://assets.nexperia.com/documents/application-note/AN90031.pdf
    accessed: 2026-10-13
    kind: official
    version: "Rev. 3.0, 7 June 2023"
    applicability: "Application note: резистор R1 має пропускати мінімальний струм стабілітрона плюс максимальний струм навантаження; струм вимірювання V_Z у даташиті (близько 5 мА до 17 В) названо доброю величиною; температурний коефіцієнт S_Z залежить від робочого струму, сильніше при нижчих напругах. Дані Nexperia; інші виробники можуть мати інші числа."
---

## Short answer

Вихід знімають з емітера: `V_out` ≈ `V_Z` − `V_BE` ≈ 5,6 − 0,7 = 4,9 В, а `V_BE` змінюється зі струмом навантаження й температурою.[^fiore-zener-follower][^fiore-bjt-ac-model] Струм резистора має бути не менший за мінімальний струм стабілітрона плюс `I_B`, щоб стабілітрон працював на крутій ділянці зворотної характеристики.[^nexperia-an90031]

## Detailed explanation

Стабілітрон включений зворотно між базою і землею, а вхідна напруга подається на базу через резистор `R`. Стабілітрон фіксує напругу бази на рівні `V_Z` = 5,6 В, тож емітер, а разом з ним і вихід, має напругу `V_Z` − `V_BE` ≈ 4,9 В. Так підручник описує стабілітронний повторювач (Zener follower): вихід задає стабілітрон, а струм навантаження йде через транзистор.[^fiore-zener-follower]

Для кремнію `V_BE` типово дорівнює 0,7 В, тож 4,9 В є номінальним значенням.[^fiore-bjt-basics] Але `V_BE` не сталий: за експоненційною моделлю він зростає приблизно на 26 мВ при збільшенні струму емітера в e разів. Якщо струм навантаження зростає з 1 мА до 10 мА, тобто в 10 разів, `V_BE` зростає приблизно на 25,9 мВ × ln 10 ≈ 60 мВ, і вихід стає нижчим приблизно на 60 мВ.[^fiore-bjt-ac-model]

Струм через `R` дорівнює `I_Z` + `I_B`, а `I_B` = `I_E` / (β + 1), бо `I_E` = (β + 1) × `I_B`.[^fiore-bjt-basics] Припустімо: `V_in` = 9 В, навантаження до 10 мА, β = 100, а стабілітрон потребує 5 мА; близько такого струму даташит зазвичай вимірює `V_Z`.[^nexperia-an90031] Тоді `I_B` ≈ 10 мА / 101 ≈ 0,1 мА, а `R` ≤ (9 − 5,6) В / (5 + 0,1) мА ≈ 3,4 В / 5,1 мА ≈ 667 Ом. Якщо взяти більший `R`, при максимальному навантаженні стабілітрон отримає менше за мінімум, потрібний для крутої ділянки, і стабілізація погіршиться.[^nexperia-an90031]

Межі схеми. Температурний коефіцієнт стабілітрона залежить від робочого струму, і для нижчих напруг цей вплив суттєвий, тож 4,9 В – це номінал для заданих струму й температури, а не гарантія.[^nexperia-an90031] Навантаження живиться через колектор, а через `R` іде лише `I_B`: якщо `I_E` перевищить ≈ (β + 1) × (`I_R` − `I_Z,min`), де `I_R` – струм резистора `R`, стабілітрон втратить мінімальний струм і `V_out` просяде.[^fiore-zener-follower][^fiore-bjt-basics] Обмеження струму немає, тож коротке замикання виходу може перегріти транзистор.

**Типові помилки:**
- Вважати вихід рівним `V_Z` = 5,6 В і не віднімати `V_BE`.
- Вважати вихід незалежним від навантаження: `V_BE` зростає зі струмом.
- Перевіряти `R` лише для холостого ходу: при максимальному навантаженні стабілітрон отримує найменший струм.

## Sources

<!-- generated from frontmatter -->
