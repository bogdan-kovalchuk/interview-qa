---
id: emb-elee-0070
title: "Чому для кута комплексного числа краще atan2, ніж звичайний arctan(b/a)?"
description: "Чому для кута комплексного числа краще atan2, ніж звичайний arctan(b/a)?"
track: electronics
section: ee101
level: junior
type: pitfall
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
    applicability: "Походження питання: лекція 43, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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
  - source_id: aac-atan2-quadrants
    title: "All About Circuits: Quadrature Frequency and Phase Demodulation"
    url: https://www.allaboutcircuits.com/textbook/radio-frequency-analysis-design/radio-frequency-demodulation/quadrature-frequency-and-phase-demodulation/
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: "Пояснює, що atan2 використовує знаки I та Q для визначення кута в усіх квадрантах; приклад стосується фазового демодулятора."
---

## Short answer

Звичайний `arctan(b/a)` не визначає квадрант комплексного числа, бо відношення не зберігає знаки обох компонентів: для `-3 + j4` воно дає −53.13°, тоді як кут числа дорівнює 126.87°. `atan2(b, a)` приймає обидві координати й повертає кут із правильним квадрантом; перевірте, чи результат подано в радіанах або градусах.[^aac-atan2-quadrants]

## Detailed explanation

Аргумент комплексного числа `z = a + jb` – це напрям вектора від початку координат до точки `(a, b)`. Функція `arctan(b/a)` обчислює нахил за відношенням координат, але однакове відношення мають точки в протилежних квадрантах. Тому за самим результатом не можна визначити знаки дійсної та уявної частин, а ділення на нульове `a` взагалі неможливе.[^aac-atan2-quadrants]

`atan2(b, a)` отримує обидві координати окремо й застосовує їхні знаки для вибору квадранта. Порядок аргументів залежить від мови програмування або калькулятора: зазвичай це `atan2(y, x)`, де `y` відповідає уявній, а `x` дійсній частині. Також результат може бути в радіанах або градусах, і це потрібно узгодити з подальшими обчисленнями. У точці `(0, 0)` напрям не визначений, тож не слід трактувати результат функції там як фізично змістовний кут.[^aac-atan2-quadrants]

Для `z = -3 + j4` точка лежить у другому квадранті. Звичайне ділення дає `b/a = -4/3`, і `arctan(-4/3)` повертає приблизно −53.13°, що описує вектор у четвертому квадранті. `atan2(4, -3)` повертає приблизно 126.87° (або 2.214 rad), тобто правильний напрям. Модуль числа окремо дорівнює `sqrt(a² + b²) = 5`; кут і модуль разом задають полярну форму.[^aac-atan2-quadrants]

**Типові помилки:**
- Передавати аргументи до `atan2` у зворотному порядку.
- Плутати градуси з радіанами або вважати, що результат обов’язково лежить у діапазоні 0–360°.
- Використовувати `atan2` для нульового комплексного числа, аргумент якого не існує.

Під час перевірки обчислення подивіться на знаки обох компонентів, визначте очікуваний квадрант і лише тоді оцінюйте число, яке повернув калькулятор.[^aac-atan2-quadrants]

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
