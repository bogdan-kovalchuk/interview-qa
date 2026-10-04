---
id: emb-elee-0040
title: "Від чого залежить реактивний опір індуктора `X_L`?"
description: "Від чого залежить реактивний опір індуктора X_L?"
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
    applicability: "Походження питання: лекція 38, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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
---

## Short answer

Для синусоїдального сигналу ідеальний індуктор має реактивний опір `X_L = 2*pi*f*L`, який зростає з частотою `f` та індуктивністю `L`. На DC у сталому режимі `f = 0`, тому його ідеальний `X_L` дорівнює нулю; реальна обмотка має опір дроту.[^aac-alternating-current]

## Detailed explanation

Індуктивний реактивний опір описує, як ідеальна індуктивність протидіє синусоїдальному струму. Він не є звичайним опором, на якому активна потужність перетворюється на тепло: для ідеального індуктора напруга випереджає струм на чверть періоду, а енергія циклічно переходить між джерелом і магнітним полем.[^aac-alternating-current]

Формула `X_L = 2*pi*f*L` стосується синусоїдального усталеного режиму лінійного індуктора з незмінною індуктивністю. Частота вимірюється в герцах, індуктивність – у генрі, а результат – в омах. Подвоєння `f` або `L` подвоює `X_L`, якщо інші умови не змінюються. Для несинусоїдального сигналу його гармоніки мають різні частоти й, відповідно, різні реактивні опори.[^aac-alternating-current]

Приклад: для ідеального індуктора `L = 10 mH` на частоті `f = 1 kHz` маємо `X_L = 2*pi*1000*0.01 ≈ 62.8 Ω`. Це значення саме по собі не визначає струм: потрібні напруга та решта імпедансу кола. У сталому DC струм більше не змінюється, тому ідеальна індуктивна складова напруги дорівнює нулю; опір дроту реальної котушки залишається.[^aac-alternating-current]

**Типові помилки:**

- Називати `X_L` опором обмотки й приписувати йому теплові втрати. Тепло пов’язане з активним опором дроту та втратами осердя.
- Застосовувати формулу без перевірки частоти, режиму та припущення про сталу `L`.
- Поширювати правило зростання `X_L` на частоти вище власного резонансу реальної котушки: паразитна ємність змінює поведінку компонента.[^aac-alternating-current]

## Sources

<!-- generated from frontmatter -->
