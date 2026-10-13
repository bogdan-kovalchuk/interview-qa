---
id: emb-elee-0212
title: "Чому перед поданням сигналу на підсилювач треба виміряти DC-напруги, і що робити при обрізанні синуса?"
description: "Чому перед поданням сигналу на підсилювач треба виміряти DC-напруги, і що робити при обрізанні синуса?"
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
  - source_id: mit-6071-bjt-notes
    title: "MIT OCW 6.071/22.071 (Spring 2006): Transistors: Bipolar Junction Transistors (BJT), lecture notes"
    url: "https://ocw.mit.edu/courses/6-071j-introduction-to-electronics-signals-and-measurement-spring-2006/b30aa58fb0c9915da21e5a5855384818_19_bjt_1.pdf"
    accessed: 2026-10-13
    kind: book
    version: "Spring 2006"
    applicability: "Лекційні нотатки університетського курсу: відсічення (I_C = 0, V_o = V_CC), насичення (V_CE(sat) типово близько 0,2 В; I_C(sat) = (V_CC - V_CE(sat))/R_C), I_C = β·I_B; для β = 100 α = 0,99 і I_C ≈ I_E. Малосигнальних параметрів нотатки не описують."
---

## Short answer

Без правильної робочої точки каскад може бути у відсіченні або насиченні ще до сигналу, тож спочатку вимірюють `V_B`, `V_E`, `V_C` без сигналу.[^mit-6071-bjt-notes] Якщо синус обрізається, перевіряють робочу точку: за правильного зсуву зменшують амплітуду вхідного сигналу, а за неправильного виправляють резистори зсуву.[^fiore-bjt-dc-load-line]

## Detailed explanation

Змінний сигнал накладається на постійну робочу точку, тому спершу треба переконатися, що вона правильна.[^fiore-bjt-ac-model] Для кремнієвого транзистора `V_BE` ≈ 0,7 В, тож `V_E` = `V_B` - 0,7 В.[^fiore-bjt-basics] Якщо виміряні `V_B` і `V_E` не сходяться з цим співвідношенням, зсув неправильний ще до того, як на вхід подано сигнал. Подавати сигнал у такому стані не варто: він покаже симптом, але не причину.

Два крайні стани видно з постійних напруг. Відсічення: `I_C` = 0, на `R_C` немає падіння, тож `V_C` ≈ `V_CC`.[^mit-6071-bjt-notes] Насичення: `V_CE` ≈ 0,2 В, тож `V_C` ≈ `V_E` + 0,2 В.[^mit-6071-bjt-notes] Якщо `V_C` стоїть біля `V_CC` або біля `V_E`, каскад уже на краю, і синус обрізається навіть при малій амплітуді.

Навантажувальна пряма показує, які значення може набувати вихідна напруга. Її кінці: насичення при `I_C(sat)` = `V_CC`/`R_C` і відсічення при `V_CE` = `V_CC`.[^fiore-bjt-dc-load-line] Робоча точка між цими кінцями дає місце для розмаху в обидва боки. Якщо піковий розмах перевищує цей запас, синус обрізається, навіть коли зсув правильний; тоді правильним рішенням є менша амплітуда вхідного сигналу.

У CE-каскаді вихід береться з колектора, а сигнал інвертується.[^fiore-bjt-ac-model] Тому обрізання верхнього піку вихідної напруги означає, що колектор упирається в `V_CC`, тобто відсічення, а обрізання нижнього піку означає, що він упирається в `V_E` + 0,2 В, тобто насичення.[^mit-6071-bjt-notes]

**Типові помилки:**

- Подавати сигнал, не перевіривши постійні напруги: обрізання може мати причину в зсуві, а не в амплітуді.
- Вважати, що обрізання завжди лікується меншою амплітудою: якщо робоча точка біля кінця навантажувальної прямої, малий сигнал обрізається з одного боку.[^fiore-bjt-dc-load-line]

## Sources

<!-- generated from frontmatter -->
