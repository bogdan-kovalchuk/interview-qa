---
id: emb-elee-0120
title: "Чому вихід RL-ФВЧ (напруга на котушці) має додатну фазу відносно джерела?"
description: "Чому вихід RL-ФВЧ (напруга на котушці) має додатну фазу відносно джерела?"
track: electronics
section: ee101
level: junior
type: concept
tags: []
status: published
updated: 2026-10-06
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
    applicability: "Походження питання: лекція 53, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-06; курс не є доказом цих тверджень."
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
  - source_id: fiore-ac-circuit-analysis
    title: "James M. Fiore: AC Electrical Circuit Analysis, A Practical Approach (sections 1.5 and 10.3)"
    url: https://www2.mvcc.edu/users/faculty/jfiore/Circuits2/ACElectricalCircuitAnalysis.pdf
    accessed: 2026-10-06
    kind: book
    version: "1.1.2, 22 April 2021"
    applicability: "Розділ 1.5: напруга на ідеальній котушці випереджає струм на 90°, реактивний опір `X_L = j*2*pi*f*L`. Розділ 10.3: для RC lead-мережі зріз лежить на 3 dB нижче рівня смуги пропускання, `f_c = 1/(2*pi*R*C)`, фаза виходу +90° на низьких частотах і +45° на критичній. Фільтр RL там окремо не розглянуто: співвідношення для RL тут виведено з тих самих формул дільника напруги."
  - source_id: kuphaldt-high-pass-filters
    title: "Tony R. Kuphaldt: Lessons In Electric Circuits, Vol. II (AC), 9.3 High-pass Filters (LibreTexts)"
    url: https://workforce.libretexts.org/Bookshelves/Electronics_Technology/Electric_Circuits_II_-_Alternating_Current_(Kuphaldt)/09:_Filters/9.03:_High-pass_Filters
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "Індуктивний ФВЧ: резистор послідовно, котушка паралельно навантаженню (вихід знімають на котушці); зріз – частота, на якій вихід дорівнює 70,7% входу; на високих частотах котушки поводяться несподівано через skin effect і втрати в осерді. Формул RL у читаному тексті сторінки немає (вони лише на рисунках), тому тут вони виведені окремо."
  - source_id: fontys-passive-hf
    title: "Fontys University of Applied Sciences: 1.2 Passive components at high frequency (LibreTexts)"
    url: https://eng.libretexts.org/Courses/Fontys_University_of_Applied_Sciences/Telecommunications/01:_Passive_Components/1.02:_Passive_components_at_high_frequency
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "Еквівалентна схема реальної котушки: ідеальна індуктивність, послідовний опір обмотки `R_s` і паралельна паразитна ємність `C_d`; практична котушка придатна лише нижче власної резонансної частоти (self-resonant frequency), а skin effect підвищує опір обмотки. Загальна модель, а не параметри конкретної котушки курсу."
---

## Short answer

Струм у RL-колі відстає від напруги джерела на кут `arctan(2*pi*f*L/R)`, а напруга на L випереджає сам струм на 90°. Тому фаза виходу `φ = 90° - arctan(2*pi*f*L/R)` завжди додатна: близько +90° на низьких частотах, +45° на `f_c` і прямує до 0° на високих.[^fiore-ac-circuit-analysis]

## Detailed explanation

**Схема й два зсуви.** У RL-ФВЧ джерело з’єднане послідовно з резистором `R` і котушкою `L`, а вихід знімають із котушки.[^kuphaldt-high-pass-filters] Через обидва елементи тече один і той самий струм `I`, тому фазу виходу зручно рахувати в два кроки. Для ідеальної котушки `v = L*di/dt`, отже напруга на ній випереджає власний струм на 90°.[^fiore-ac-circuit-analysis] Сам струм задає повний імпеданс `R + j*2*pi*f*L`, чия реактивна частина додатна, тому `I` відстає від напруги джерела на кут від 0° до 90°.

**Сумарна фаза.** Складаємо ці два зсуви: `φ = 90° - arctan(X_L/R)`, де `X_L = 2*pi*f*L`.[^fiore-ac-circuit-analysis] Модуль дає той самий дільник: `|V_out/V_in| = X_L/sqrt(R^2 + X_L^2)`. На частоті `f_c = R/(2*pi*L)` реактивний опір дорівнює `R`, тож амплітуда становить `1/sqrt(2) ≈ 0.707` (`-3.01 dB`), а фаза рівно +45°. Вихід завжди випереджає вхід, але ніколи не більш ніж на 90°. Таку саму форму має RC-ФВЧ, де вихід знімають із резистора: +90° на низьких частотах, +45° на критичній і майже 0° на дуже високих.[^fiore-ac-circuit-analysis]

**Приклад.** Нехай `R = 1 kΩ`, `L = 10 mH`; тоді `f_c = 1000/(2*pi*0.01) ≈ 15.9 kHz`. На `0.1*f_c ≈ 1.59 kHz` відношення `X_L/R = 0.1`, тож фаза `90° - 5.71° = +84.29°`, а `|V_out/V_in| ≈ 0.0995` (`-20.04 dB`). На `f_c` маємо +45° і 0.707. На `10*f_c ≈ 159 kHz` фаза `+5.71°`, а амплітуда `≈ 0.995` (`-0.04 dB`).

**Межі моделі.** Усе вище – для ідеальної котушки без навантаження. Реальна котушка має опір обмотки й паразитну ємність.[^fontys-passive-hf] Через опір обмотки напруга на клемах котушки на низьких частотах уже не наближається до +90°: на постійному струмі вона не нуль, а фаза прямує до 0° (див. `qid:emb-elee-0121`). Якщо ж вихід узяти з резистора, а не з котушки, фаза стане від’ємною (`-arctan(X_L/R)`), і це вже RL-ФНЧ.

**Типові помилки:**

- Міркувати «струм відстає, отже й вихід відстає»: вихід – це напруга на L, вона випереджає струм на 90° і лише частково компенсується відставанням самого струму.
- Вважати, що на котушці завжди рівно +90° відносно джерела: це лише межа для `f` значно менших за `f_c` і для ідеальної котушки.
- Брати вихід на `R` замість `L`: тоді виходить RL-ФНЧ із фазою від 0° до -90°.

## Sources

<!-- generated from frontmatter -->
