---
id: emb-elee-0032
title: "Що таке постійна часу τ RC-кола?"
description: "Що таке постійна часу τ RC-кола?"
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
    applicability: "Походження питання: лекція 37, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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
  - source_id: gatech-rc-charging-discharging
    title: "Georgia Tech Physics Book: Charging and Discharging a Capacitor"
    url: https://physicsbook.gatech.edu/Charging_and_Discharging_a_Capacitor
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: "Визначення τ=RC, одиниці та частки напруги в простих ідеальних RC-перехідних процесах."
---

## Short answer

Постійна часу простого RC-кола дорівнює `τ = R*C` і вимірюється в секундах, бо `Ω*F = s`. За одну τ напруга під час заряджання проходить 63.2% повної різниці до нового усталеного рівня; під час розряджання залишається 36.8% початкової напруги.[^gatech-rc-charging-discharging]

## Detailed explanation

Постійна часу `τ` описує часовий масштаб перехідного процесу в простому колі з резистором і конденсатором. У найпростішому послідовному колі вона дорівнює `R*C`: більший опір обмежує струм сильніше, а більша ємність потребує більше заряду для тієї самої зміни напруги, тому кожна з цих змін робить реакцію повільнішою. Одиниці узгоджуються: `Ω*F = s`.[^gatech-rc-charging-discharging]

За одну τ заряджання від нуля до сталої напруги джерела досягає приблизно 63.2% кінцевої напруги. Це наслідок експоненційного закону: після кожної наступної τ залишається така сама частка ще не пройденої різниці до кінцевого значення. У розряді після однієї τ лишається приблизно 36.8% початкової напруги. Отже, τ не є часом повного заряджання чи розряджання; експоненційна крива асимптотично наближається до межі.[^gatech-rc-charging-discharging]

У колі з кількома резисторами не можна механічно підставляти будь-який один резистор у `τ = R*C`. Для одного конденсатора першого порядку використовують еквівалентний опір, який видно з його виводів, коли незалежні ідеальні джерела занулені згідно з методом аналізу. Якщо мережа має кілька накопичувальних елементів, вона може мати кілька часових масштабів, і проста одна τ вже не описує всю відповідь.[^gatech-rc-charging-discharging]

Приклад розрахунку:

```text
R = 10 kΩ = 10,000 Ω
C = 10 µF = 0.000010 F
τ = R*C = 10,000*0.000010 = 0.1 s = 100 ms
```

Таке значення означає, що через 100 ms ідеальна напруга при заряджанні пройшла 63.2% від повної зміни. Воно не каже, що заряджання завершиться саме тоді; практичне наближення до кінцевого рівня залежить від допустимої похибки.[^gatech-rc-charging-discharging]

**Типові помилки:**

- Називати τ часом повного заряджання; на практиці кілька τ дають дедалі ближче наближення.
- Не переводити мікрофаради й кілооми до сумісних одиниць, через що результат має неправильний масштаб.
- Ігнорувати опір решти кола, який також бачить конденсатор.

## Sources

<!-- generated from frontmatter -->
