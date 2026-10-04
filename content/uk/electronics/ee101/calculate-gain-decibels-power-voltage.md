---
id: emb-elee-0097
title: "Як обчислити підсилення в децибелах за потужністю і за напругою?"
description: "Як обчислити підсилення в децибелах за потужністю і за напругою?"
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
    applicability: "Походження питання: лекція 49, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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
  - source_id: rs-decibel-guide
    title: "Rohde & Schwarz: Radar and electronic warfare eGuide"
    url: https://www.allaboutcircuits.com/uploads/articles/Radar-and-electronic-warfare_eGuide-REVISED.pdf
    accessed: 2026-10-04
    kind: official
    version: "01.00, April 2022"
    applicability: "Визначення dB як логарифма відношення потужностей та еквівалентна формула для напруги за однакового імпедансу."
---

## Short answer

Підсилення за потужністю дорівнює `G_P = 10*log10(P_out/P_in)` dB. Для напруги використовують `G_V = 20*log10(|V_out/V_in|)` лише за однакового імпедансу на вході й виході; інакше слід обчислити потужності. Додатне значення означає gain, від’ємне – ослаблення, а 0 dB – відношення 1:1.[^rs-decibel-guide]

## Detailed explanation

Децибел – логарифмічна форма відношення двох величин, а не самостійна одиниця абсолютної потужності. Для потужностей порівнюють вихідне значення з вхідним: `G_P = 10*log10(P_out/P_in)`. Якщо відомі напруги, співвідношення можна перевести у dB як `G_V = 20*log10(|V_out/V_in|)`, коли вимірювання відповідають одному й тому самому активному опору. Це випливає з `P = V²/R`: за однакового `R` квадрат відношення напруг стає відношенням потужностей, а множник 10 перед логарифмом перетворюється на 20.[^rs-decibel-guide]

Абсолютні значення напруги можна порівнювати за цією формулою, якщо обидві напруги RMS для змінного сигналу та опори однакові. Для різних опорів однакове відношення напруг не означає однакового відношення потужностей. У такому разі спершу знаходять реальну потужність на кожному порту, враховуючи його навантаження, і застосовують формулу для `P_out/P_in`. Приклад: подвоєння напруги на тому самому резисторі збільшує потужність у чотири рази, тобто дає приблизно `10*log10(4) ≈ 6.02 dB`, а не 3 dB.[^rs-decibel-guide]

Знаки інтерпретують відносно того, що стоїть у чисельнику: додатне значення означає, що вихідна величина більша за вхідну за обраним визначенням; від’ємне – менша. Нуль dB означає рівність величин. Зворотний розрахунок для напруги дає `|V_out/V_in| = 10^(G_V/20)`, а для потужності – `P_out/P_in = 10^(G_P/10)`. Тому 20 dB відповідає десятикратному відношенню напруг, але стократному відношенню потужностей за рівного імпедансу.[^rs-decibel-guide]

**Приклад:** вхід `0.2 V RMS` і вихід `0.4 V RMS` на однакових резистивних опорах утворюють відношення напруг 2:1, тому `G_V = 20*log10(2) ≈ 6.02 dB`. Якщо ж опори різні, це число не є автоматично gain за потужністю.

**Типові помилки:**

- Використовувати `10*log10` для відношення напруг без переходу до потужності.
- Використовувати `20*log10` для напруг без перевірки однаковості опорів.
- Називати dB абсолютним рівнем без указання опорної величини.[^rs-decibel-guide]

## Sources

<!-- generated from frontmatter -->
