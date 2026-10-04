---
id: emb-elee-0074
title: "RC-коло: R = 1 kΩ, C = 100 nF, f ≈ 1591.5 Hz, вхід 1 V RMS. Які струм і напруги на R та C?"
description: "RC-коло: R = 1 kΩ, C = 100 nF, f ≈ 1591.5 Hz, вхід 1 V RMS. Які струм і напруги на R та C?"
track: electronics
section: ee101
level: junior
type: concept
tags: []
status: published
updated: 2026-10-04
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
    applicability: "Походження питання: лекція 44, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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
  - source_id: aac-series-rc-analysis
    title: "All About Circuits: Series Resistor-Capacitor Circuits"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-4/series-resistor-capacitor-circuits/
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: "Підтримує розрахунок фазорного струму, напруг на R і C та перевірку їхньої векторної суми в послідовному RC-колі."
---

## Short answer

За `f ≈ 1591.5 Hz`, `R = 1 kΩ` і `C = 100 nF`, `X_C ≈ 1 kΩ`, тож `Z ≈ 1000 - j1000 Ω`. Для входу `1 V RMS∠0°` струм становить приблизно `0.707 mA∠45°`, а `V_R ≈ 0.707 V∠45°` і `V_C ≈ 0.707 V∠−45°`; їхня комплексна сума дорівнює вхідному фазору. Округлення проміжних чисел дає лише приблизні значення.[^aac-series-rc-analysis]

## Detailed explanation

У послідовному колі струм однаковий у резисторі та конденсаторі, а джерело живить суму двох комплексних імпедансів. Для `R = 1 kΩ`, `C = 100 nF` і `f = 1591.5 Hz` ємнісний опір за модулем дорівнює приблизно `1000.03 Ω`, близько до опору резистора. Вхід `1 V RMS` задано фазовим відліком 0°; усі наступні фазорні значення також є RMS.[^aac-series-rc-analysis]

**Розрахунок:**
```text
X_C = 1/(2π*f*C) ≈ 1000.03 Ω
Z = R - j*X_C ≈ 1000 - j1000.03 Ω
I = V_in/Z ≈ 0.7071 mA∠45.001°
V_R = I*R ≈ 0.7071 V∠45.001° = 0.5000 + j0.5000 V
V_C = I*(-j*X_C) ≈ 0.7071 V∠−44.999° = 0.5000 - j0.5000 V
V_R + V_C ≈ 1.0000 + j0 V
```

Напруга резистора збігається за фазою зі струмом, тоді як напруга конденсатора відстає від струму на 90°. Їхні модулі приблизно однакові біля частоти зрізу, але вони не співфазні; тому не можна складати `0.7071 V + 0.7071 V` як звичайні числа. Складайте прямокутні компоненти або комплексні фазори – тоді уявні складові взаємно компенсуються, а дійсні дають вхідну напругу.[^aac-series-rc-analysis]

Частота зрізу для ідеального ненавантаженого кола становить `1/(2π*R*C) ≈ 1591.55 Hz`. У вихідному формулюванні частота округлена до 1591.5 Hz, тому значення фаз і реактивного опору також округлюються. Реальне джерело з ненульовим вихідним опором або навантаження, підключене паралельно конденсатору, змінять результат.[^aac-series-rc-analysis]

## Sources

<!-- generated from frontmatter -->
