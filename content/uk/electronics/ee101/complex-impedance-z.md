---
id: emb-elee-0057
title: "Що таке комплексний імпеданс Z?"
description: "Що таке комплексний імпеданс Z?"
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
  - source_id: aac-impedance-definition
    title: "All About Circuits: Series Resistor-Inductor Circuits"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-3/series-resistor-inductor-circuits/
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: "Визначення імпедансу як комплексного опору, закон Ома для AC та фазові властивості резистивної й реактивної складових."
---

## Short answer

Імпеданс `Z` – комплексне відношення фазорів напруги та струму, `Z = V/I`, яке узагальнює опір для AC. Для послідовних `R` і реактивної складової його записують як `Z = R + j*X`; модуль дорівнює `|Z| = sqrt(R² + X²)`, а фазовий кут визначають як `atan2(X, R)`. Імпеданс вимірюють в омах, а його кут задає фазове співвідношення напруги й струму.[^aac-impedance-definition]

## Detailed explanation

Імпеданс узагальнює дію опору та реактивних елементів у синусоїдальному колі: для фазорів напруги й струму виконується `Z = V/I`. Це комплексна величина, вимірювана в омах, яка одночасно показує співвідношення амплітуд і фазовий зсув. Для чистого резистора кут імпедансу дорівнює нулю; реактивні елементи додають уявну складову.[^aac-impedance-definition]

У прямокутній формі `Z = R + j*X`, де `R` – дійсна складова, а `X` – реактивна складова зі знаком. Додатний `X` відповідає індуктивному характеру, від’ємний – ємнісному. Модуль `|Z| = sqrt(R² + X²)` описує відношення модулів напруги й струму, а аргумент `φ = atan2(X, R)` – їх фазову різницю за пасивної системи знаків. Для складного кола значення залежать від частоти, тож одного числа для всього діапазону частот зазвичай недостатньо.[^aac-impedance-definition]

Приклад: для послідовного кола з `R = 3 Ω` і `X_L = 4 Ω` імпеданс має вигляд `Z = 3 + j*4 Ω`. Його модуль становить `5 Ω`, а кут – приблизно `53.1°`; отже, за заданої частоти струм має фазу на `53.1°` позаду напруги за прийнятого пасивного знаку. Значення `5 Ω` саме по собі не зберігає інформацію про фазу і не замінює комплексний імпеданс у розрахунку кола.[^aac-impedance-definition]

Імпеданс послідовних елементів складають комплексним додаванням; для паралельних гілок використовують комплексні провідності або обернену суму. Тому не можна окремо додати модулі гілок, наче це резистори: фаза є частиною результату. Застосовність фазорної моделі передбачає лінійний усталений режим на спільній частоті.[^aac-impedance-definition]

**Типові помилки:**

- Називати імпеданс лише модулем і втрачати кут.
- Використовувати знак `X` без розрізнення індуктивної й ємнісної реактивності.
- Застосовувати просте додавання скалярних опорів до комплексних величин.[^aac-impedance-definition]

## Sources

<!-- generated from frontmatter -->
