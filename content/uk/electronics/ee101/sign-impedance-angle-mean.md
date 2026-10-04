---
id: emb-elee-0060
title: "Що означає знак кута імпедансу φ?"
description: "Що означає знак кута імпедансу φ?"
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
    applicability: "Походження питання: лекція 41, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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
  - source_id: aac-rxz-review
    title: "All About Circuits: Review of R, X, and Z (Resistance, Reactance and Impedance)"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-5/review-of-r-x-and-z/
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: "Знак фазового кута і співвідношення фаз для ідеальних R, L і C; не описує паразитні параметри реальних компонентів."
---

## Short answer

Для пасивного кола з імпедансом `Z = R + jX` додатний кут означає переважно індуктивний характер: напруга випереджає струм. Від’ємний кут означає переважно ємнісний характер: струм випереджає напругу; чистий резистор має кут 0°.[^aac-rxz-review]

## Detailed explanation

Знак кута імпедансу показує, яка реактивна складова переважає в колі змінного струму. Для домовленості `Z = R + jX` додатна уявна частина `X` відповідає індуктивному характеру, а від’ємна – ємнісному; це узгоджується з фазовим кутом `φ = atan2(X,R)` за невід’ємного опору `R`.[^aac-rxz-review]

Для ідеального резистора напруга й струм змінюються синфазно, тому кут дорівнює нулю. В ідеальній котушці напруга випереджає струм на 90°, а в ідеальному конденсаторі струм випереджає напругу на 90°. У змішаному колі кут зазвичай лежить між цими межами, бо опір і реактивність діють разом.[^aac-rxz-review]

Кут належить усьому імпедансу, а не окремому резистору чи одному компоненту в довільному колі. Він залежить від частоти, номіналів і з’єднання елементів: у послідовному RLC-колі індуктивна та ємнісна складові можуть частково компенсувати одна одну. Тому знак кута не визначає тип кожного компонента, а описує сумарну реакцію мережі на синусоїдальний сигнал.[^aac-rxz-review]

**Типова помилка:** сприймати додатний кут як «струм випереджає напругу». Для пасивної конвенції знак читають з `Z = V/I`: індуктивний кут додатний і напруга випереджає струм; для ємнісного кута порядок фаз протилежний.[^aac-rxz-review]

## Sources

<!-- generated from frontmatter -->
