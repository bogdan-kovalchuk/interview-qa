---
id: emb-elee-0210
title: "Каскад CE: `V_CC` = 10 В, `I_E` ≈ 1 мА, `R_E` = 1 кОм, `R_C` = 4,7 кОм. Які робоча точка і підсилення?"
description: "Каскад CE: `V_CC` = 10 В, `I_E` ≈ 1 мА, `R_E` = 1 кОм, `R_C` = 4,7 кОм. Які робоча точка і підсилення?"
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
    applicability: "Походження питання: лекція 71, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-13; курс не є доказом цих тверджень."
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
  - source_id: fiore-bjt-basics
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 4.2 The Bipolar Junction Transistor"
    url: "https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/04:_Bipolar_Junction_Transistors_(BJTs)/4.2:_The_Bipolar_Junction_Transistor"
    accessed: 2026-10-13
    kind: book
    version: null
    applicability: "Підручник, розділ 4.2: I_E = I_C + I_B; при I_C ≫ I_B маємо I_E ≈ I_C; V_BE ≈ 0,7 В для кремнію. Загальна картина, не для конкретного транзистора."
  - source_id: fiore-bjt-dc-load-line
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 4.6 DC Load Lines"
    url: "https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/04:_Bipolar_Junction_Transistors_(BJTs)/4.6:_DC_Load_Lines"
    accessed: 2026-10-13
    kind: book
    version: null
    applicability: "Підручник, розділ 4.6: навантажувальна пряма; I_C(sat) = V_CC/R_C – максимум колекторного струму в насиченні, V_CE(cutoff) = V_CC при I_C = 0; розрахунковий струм вище I_C(sat) дає I_C(sat). Формула V_CC/R_C не враховує V_CE(sat)."
  - source_id: fiore-bjt-ac-model
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 7.2 Simplified AC Model of the BJT"
    url: "https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/07:_BJT_Small_Signal_Amplifiers/7.2:_Simplified_AC_Model_of_the_BJT"
    accessed: 2026-10-13
    kind: book
    version: null
    applicability: "Підручник, розділ 7.2: r'_e = 26 мВ / I_C як динамічний опір переходу база–емітер (V_T ≈ 25,9 мВ при 300 K); опір об’ємного матеріалу не включено; залежить від I_C і температури; g_m – transconductance; модель для низьких і середніх частот, без ємностей переходів."
  - source_id: fiore-common-emitter-amplifier
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 7.3 Common Emitter Amplifier"
    url: "https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/07:_BJT_Small_Signal_Amplifiers/7.3:_Common_Emitter_Amplifier"
    accessed: 2026-10-13
    kind: book
    version: null
    applicability: "Підручник, розділ 7.3: AC-еквівалент за принципом суперпозиції, конденсатори замінюють короткими замиканнями, постійні джерела – ідеальним внутрішнім опором (AC-земля); A_v = -r_C/(r'_e + r_E); Z_in(base) = β(r'_e + r_E); Z_out ≈ R_C; нешунтований R_E зменшує підсилення й спотворення. Числові приклади стосуються лише цих схем."
  - source_id: mit-6071-bjt-notes
    title: "MIT OCW 6.071/22.071 (Spring 2006): Transistors: Bipolar Junction Transistors (BJT), lecture notes"
    url: "https://ocw.mit.edu/courses/6-071j-introduction-to-electronics-signals-and-measurement-spring-2006/b30aa58fb0c9915da21e5a5855384818_19_bjt_1.pdf"
    accessed: 2026-10-13
    kind: book
    version: "Spring 2006"
    applicability: "Лекційні нотатки університетського курсу: відсічення (I_C = 0, V_o = V_CC), насичення (V_CE(sat) типово близько 0,2 В; I_C(sat) = (V_CC - V_CE(sat))/R_C), I_C = β·I_B; для β = 100 α = 0,99 і I_C ≈ I_E. Малосигнальних параметрів нотатки не описують."
---

## Short answer

`V_E` ≈ 1 В, `V_B` ≈ 1,7 В, `V_C` ≈ 10 - 4,7 = 5,3 В, тож `V_CE` ≈ 4,3 В: є запас і до шини, і до насичення.[^fiore-bjt-basics][^mit-6071-bjt-notes] Якщо `R_E` не зашунтовано, `A_v` = `-R_C/(r'_e + R_E)`, де `r'_e` ≈ 26 Ом, тобто ≈ -4,6 (без навантаження й без вихідного опору транзистора).[^fiore-bjt-ac-model][^fiore-common-emitter-amplifier]

## Detailed explanation

Операційну точку знаходять із постійних напруг і струмів, і лише після цього розглядають змінний сигнал. Емітерний струм тут задано: `I_E` ≈ 1 мА. Для β = 100 маємо `I_C` ≈ `I_E`,[^mit-6071-bjt-notes] тож колекторний струм створює на `R_C` падіння 1 мА · 4,7 кОм = 4,7 В, і `V_C` = 10 - 4,7 = 5,3 В. На `R_E` падає `V_E` = 1 мА · 1 кОм = 1 В. Перехід база–емітер прямо зміщений, для кремнію `V_BE` ≈ 0,7 В, тож `V_B` ≈ 1,7 В.[^fiore-bjt-basics]

Межі роботи задає навантажувальна пряма. У відсіченні `I_C` = 0, і колектор підтягнуто до `V_CC`, тобто `V_C` = 10 В.[^mit-6071-bjt-notes] У насиченні `V_CE` спадає приблизно до 0,2 В.[^mit-6071-bjt-notes] Навантажувальна пряма тут проходить через `R_C` + `R_E`, бо `R_E` не зашунтовано: `I_C(sat)` ≈ (`V_CC` - `V_CE(sat)`)/(`R_C` + `R_E`) ≈ 9,8/5,7 ≈ 1,7 мА.[^fiore-bjt-dc-load-line] Тоді `V_E` ≈ 1,7 В, а `V_C` ≈ `V_E` + 0,2 В ≈ 1,9 В. Отже, колектор може піти вниз приблизно на 3,4 В (до `V_C` ≈ 1,9 В) і вгору на 4,7 В до відсічення. Тому каскад стоїть в активній області з великим запасом в обидва боки.

Змінне підсилення визначає опір у колі емітера. Динамічний опір переходу `r'_e` = 26 мВ / `I_C` = 26 Ом; його виводять з експоненційної моделі переходу, і він залежить від `I_C` і температури.[^fiore-bjt-ac-model] Якщо `R_E` не зашунтовано конденсатором, його опір повністю входить у змінне коло, і `A_v` = `-R_C`/(`r'_e` + `R_E`) = -4700/(26 + 1000) ≈ -4,6. Знак мінус означає інверсію фази на 180°, а вихідний опір каскаду наближено дорівнює `R_C`.[^fiore-common-emitter-amplifier] Вихідний опір самого транзистора, порядку 100 кОм за Fiore, тут не враховано, тож модуль підсилення трохи менший.[^fiore-common-emitter-amplifier]

**Приклад:** якщо `R_E` повністю зашунтувати конденсатором, у змінному колі `r_E` стає нулем, і `A_v` = `-R_C`/`r'_e` = -4700/26 ≈ -181. Підсилення зростає майже в 40 разів, але зростає й спотворення: неповне шунтування, тобто swamping, саме його зменшує.[^fiore-common-emitter-amplifier]

**Типові помилки:**

- Вважати `A_v` = `-R_C`/`R_E` точною формулою: це наближення, коли `R_E` значно більший за `r'_e`.[^fiore-common-emitter-amplifier]
- Розраховувати підсилення, не перевіривши, чи зашунтовано `R_E`: конденсатор змінює `A_v` у десятки разів.[^fiore-common-emitter-amplifier]
- Вважати `r'_e` сталим: він залежить від `I_C` і температури.[^fiore-bjt-ac-model]

## Sources

<!-- generated from frontmatter -->
