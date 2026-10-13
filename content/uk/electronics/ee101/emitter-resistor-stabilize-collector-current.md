---
id: emb-elee-0193
title: "Як емітерний резистор стабілізує колекторний струм?"
description: "Як емітерний резистор стабілізує колекторний струм?"
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
  - source_id: fiore-emitter-bias
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 5.3 Two-Supply Emitter Bias"
    url: "https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/05:_BJT_Biasing/5.3:_Two-Supply_Emitter_Bias"
    accessed: 2026-10-13
    kind: book
    version: null
    applicability: "Підручник, розділ 5.3: емітерний зсув від двох джерел, I_C = (|V_EE| - V_BE)/(R_E + R_B/β); якщо R_E значно більший за R_B/β, β майже не впливає на I_C; V_C = V_CC - I_C*R_C. Число прикладу (подвоєння β дає зміну I_C близько 1 %) стосується лише цих номіналів."
  - source_id: libretexts-fiore-diode-models
    title: "Fiore: Semiconductor Devices, 2.4 Diode Circuit Models (Engineering LibreTexts)"
    url: "https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/02:_PN_Junctions_and_Diodes/2.4:_Diode_Circuit_Models"
    accessed: 2026-10-13
    kind: book
    version: null
    applicability: "Розділ 2.4: колінна напруга 0,7 В для кремнію як поведінкова модель діода, а не джерело напруги. Не описує конкретний прилад."
  - source_id: mit-6071-bjt-notes
    title: "MIT OCW 6.071/22.071 (Spring 2006): Transistors: Bipolar Junction Transistors (BJT), lecture notes"
    url: "https://ocw.mit.edu/courses/6-071j-introduction-to-electronics-signals-and-measurement-spring-2006/b30aa58fb0c9915da21e5a5855384818_19_bjt_1.pdf"
    accessed: 2026-10-13
    kind: book
    version: "Spring 2006"
    applicability: "Лекційні нотатки MIT OCW: I_E = (1+β)·I_B, I_C = β/(1+β)·I_E; для β = 100 α = 0.99. Університетська лекція, не документ виробника; конкретні транзистори можуть відрізнятися."
  - source_id: fiore-pn-junction
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 2.2 The PN Junction"
    url: "https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/02:_PN_Junctions_and_Diodes/2.2:_The_PN_Junction"
    accessed: 2026-10-13
    kind: book
    version: null
    applicability: "Підручник, розділ 2.2: рівняння Шоклі для p-n переходу, струм експоненційно залежить від напруги; струм насичення зростає з температурою, і при нагріванні крива зсувається ліворуч (за тієї самої напруги струм більший). Описує діод, а не транзистор."
  - source_id: fiore-ebers-moll
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 4.5 Ebers-Moll Model"
    url: "https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/04:_Bipolar_Junction_Transistors_(BJTs)/4.5:_Ebers-Moll_Model"
    accessed: 2026-10-13
    kind: book
    version: null
    applicability: "Підручник, розділ 4.5: спрощена модель Еберса–Молла; β залежить від приладу, температури, I_C і V_CE. У базовому зсуві з фіксованим I_B подвоєння β подвоює I_C. Даних конкретного приладу не наводить."
---

## Short answer

Якщо `V_B` стала, то приблизно `V_E = V_B - V_BE`, і `R_E` перетворює цю напругу на струм `I_E = (V_B - V_BE)/R_E`.[^fiore-emitter-bias] Зростання струму підвищує `V_E` і зменшує `V_BE` – локальний від’ємний зворотний зв’язок.[^fiore-pn-junction]

## Detailed explanation

Нехай база отримує стабільну напругу `V_B` від джерела з малим вихідним опором. Коли перехід база–емітер відкритий, напруга на ньому близька до 0.7 В для кремнію, тож потенціал емітера `V_E = V_B - V_BE`.[^libretexts-fiore-diode-models] Струм емітера визначає резистор: `I_E = V_E/R_E = (V_B - V_BE)/R_E`. У цьому наближенні β майже не входить у вираз, бо струм задається напругою на базі й опором в емітері.[^fiore-emitter-bias]

Колекторний струм `I_C = α*I_E`, де `α = β/(β+1)`. При β = 100 маємо α = 0.99, тож `I_C` відрізняється від `I_E` лише на 1 %.[^mit-6071-bjt-notes]

Тепер припустімо, що щось підняло `I_C`, наприклад β або температура. Тоді зростає й `I_E`, а з ним і падіння напруги `V_E = I_E*R_E`. Оскільки `V_B` стала, `V_BE = V_B - V_E` зменшується. Струм через перехід експоненційно залежить від `V_BE`, тож він спадає і тягне `I_C` назад.[^fiore-pn-junction] Вихідний струм зменшує напругу, яка його викликала, і це і є від’ємний зворотний зв’язок.

Приклад: `V_B` = 2.0 В, `V_BE` = 0.7 В, `R_E` = 1 кОм дають `I_E` = 1.30 мА. При β = 100 `I_C` = 0.990 × 1.30 ≈ 1.287 мА, а при β = 200 `I_C` = 0.995 × 1.30 ≈ 1.294 мА. Подвоєння β змінює струм менш ніж на 0.5 %. Для порівняння, у базовому зсуві з фіксованим `I_B` подвоєння β подвоює `I_C`.[^fiore-ebers-moll]

Стабілізація має межі. Якщо `V_B` дає дільник з еквівалентним опором `R_B`, струм бази `I_B` зсуває `V_B` на `I_B*R_B`. Наближено `I_C = (V_B - V_BE)/R_E` працює, коли `R_E` значно більший за `R_B/β`.[^fiore-emitter-bias] Друге обмеження – сама `V_BE`: при `V_E` ≈ 0.2 В і `R_E` = 1 кОм струм `I_E` ≈ 0.2 мА, а похибка 0.1 В у `V_BE` змінює його на 0.1 мА, тобто на 50 %. Тому малий `V_E` струм не стабілізує.

**Типові помилки:**

- Вважати, що `R_E` стабілізує струм за будь-якої схеми бази: дільник з великим опором `R_B` зсуває напругу бази струмом `I_B`.
- Вважати 0.7 В точною величиною: похибка `V_BE` переходить у струм як `ΔV_BE/R_E`.
- Брати малий `V_E`: тоді невелика зміна `V_BE` дає великий розкид струму.

## Sources

<!-- generated from frontmatter -->
