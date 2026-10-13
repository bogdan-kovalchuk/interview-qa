---
id: emb-elee-0208
title: "Чому каскад зі спільним емітером інвертує сигнал?"
description: "Чому каскад зі спільним емітером інвертує сигнал?"
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
  - source_id: fiore-ac-model-bjt
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 7.2 Simplified AC Model of the BJT"
    url: "https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/07:_BJT_Small_Signal_Amplifiers/7.2:_Simplified_AC_Model_of_the_BJT"
    accessed: 2026-10-13
    kind: book
    version: null
    applicability: "Розділ 7.2: спрощена модель BJT для змінного сигналу; I_C = I_S*exp(38,6*V_BE) при 300 K; r'_e ≈ 26 мВ / I_C; у схемі зі спільним емітером фаза інвертується, у схемі зі спільним колектором – ні; модель для низьких і середніх частот."
  - source_id: fiore-common-emitter-amplifier
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 7.3 Common Emitter Amplifier"
    url: "https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/07:_BJT_Small_Signal_Amplifiers/7.3:_Common_Emitter_Amplifier"
    accessed: 2026-10-13
    kind: book
    version: null
    applicability: "Розділ 7.3: A_v = -r_C/(r'_e + r_E), знак мінус – інверсія на 180° у середній смузі; Z_in(base) = β(r'_e + r_E); Z_out ≈ R_C; нешунтований (swamping) R_E зменшує підсилення й спотворення і збільшує вхідний опір; числа прикладів стосуються лише цих схем."
  - source_id: fiore-bjt-dc-load-line
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 4.6 DC Load Lines"
    url: "https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/04:_Bipolar_Junction_Transistors_(BJTs)/4.6:_DC_Load_Lines"
    accessed: 2026-10-13
    kind: book
    version: null
    applicability: "Розділ 4.6: для постійного струму V_CE = V_CC − I_C*R_C; напруга на колекторі падає зі зростанням I_C."
  - source_id: fiore-ac-circuit-analysis
    title: "James M. Fiore: AC Electrical Circuit Analysis, A Practical Approach (sections 1.5 and 10.3)"
    url: https://www2.mvcc.edu/users/faculty/jfiore/Circuits2/ACElectricalCircuitAnalysis.pdf
    accessed: 2026-10-13
    kind: book
    version: null
    applicability: "Розділ 10.3 (діаграми Боде): RC-ланка з виходом на R і послідовним C; f_c = 1/(2*pi*R*C), де підсилення на зрізі на 3 дБ нижче середньосмугового; нижній злам спричинюють розділові й паразитні ємності; нижче f_c відповідь RC-ланки випередження спадає на 6 дБ на октаву."
---

## Short answer

Коли вхідний сигнал збільшує напругу база–емітер, зростає колекторний струм, а падіння на `R_C` стає більшим, тож `V_C = V_CC - I_C*R_C` зменшується.[^fiore-ac-model-bjt][^fiore-bjt-dc-load-line] Тому вихід у протифазі з входом, тобто зсунутий на 180° у середній смузі.[^fiore-common-emitter-amplifier]

## Detailed explanation

Каскад зі спільним емітером подає сигнал на базу, а вихід знімає з колектора. Колекторний струм визначає напругу на колекторі: для постійного струму `V_C = V_CC - I_C*R_C`, тож чим більший струм, тим нижча напруга на колекторі.[^fiore-bjt-dc-load-line] Струм `I_C` сильно залежить від напруги база–емітер: у спрощеній моделі `I_C = I_S*exp(38,6*V_BE)` при 300 K, тобто зміна V_BE на 2,6 мВ змінює струм приблизно на 10 %.[^fiore-ac-model-bjt]

Приклад: `V_CC = 12 В`, `R_C = 4,7 кОм`, робоча точка `I_C = 1 мА`, тоді `V_C = 12 - 1*4,7 = 7,3 В`. Вхідний сигнал додає до V_BE приблизно 2,6 мВ. Динамічний опір `r_e = 26 мВ / 1 мА = 26 Ом`, тому струм зростає на `2,6 мВ / 26 Ом = 0,1 мА`, до 1,1 мА. Тоді `V_C = 12 - 1,1*4,7 = 6,83 В`: коли вхід зростає, вихід спадає на 0,47 В, тобто інвертується.[^fiore-ac-model-bjt]

Інверсія належить схемі з виходом на колекторі, а не самому транзистору: більший струм дає більше падіння на `R_C`. Знак мінус у `A_v = -r_C/(r_e + r_E)` і є цією інверсією, тобто зсувом фази на 180° у середній смузі.[^fiore-common-emitter-amplifier] На частотах поблизу зрізів, які створюють конденсатори, фаза відхиляється від 180°; у RC-ланці випередження на критичній частоті зсув становить 45°.[^fiore-ac-circuit-analysis] Емітерний повторювач, навпаки, не інвертує, бо вихід знімається з емітера.[^fiore-ac-model-bjt]

**Типові помилки:**

- Вважати інверсію властивістю транзистора, а не схеми з виходом на колекторі.
- Вважати, що 180° зберігається на всіх частотах, зокрема поблизу зрізів.
- Плутати інверсію з обмеженням: її можна скасувати другим інвертувальним каскадом у ланцюжку.

## Sources

<!-- generated from frontmatter -->
