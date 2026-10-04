---
id: emb-elee-0006
title: "Чим momentary-кнопка відрізняється від latching-перемикача і що означають NO та NC?"
description: "Чим momentary-кнопка відрізняється від latching-перемикача і що означають NO та NC?"
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
    applicability: "Походження питання: лекція 33, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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
  - source_id: aratas-switch-basics
    title: "ARATAS (formerly Omron): What is an Electrical Switch?"
    url: https://www.aratas.com/sg-en/products/basic-knowledge/switches/basics
    accessed: 2026-10-04
    kind: official
    version: null
    applicability: "Визначення momentary та alternate/latching роботи, а також контактів NO і NC."
---

## Short answer

Momentary перемикач утримує активний стан, поки його натискають, і повертається після відпускання; latching зберігає стан до наступного натискання. NO означає розімкнений контакт у нормальному, неактивованому стані, NC – замкнений; активування змінює відповідний стан.[^aratas-switch-basics]

## Detailed explanation

Momentary та latching описують механічну поведінку привода після дії, а NO та NC – початковий електричний стан контактів. Це дві незалежні характеристики: кнопка може бути momentary з NO, momentary з NC або мати обидва контакти, а механічний перемикач може фіксуватися в положенні. Не слід виводити тип контакту з форми кнопки чи називати всі кнопкові перемикачі momentary.[^aratas-switch-basics]

У momentary-моделі пружина повертає привод, коли користувач припиняє натискання, і контакт повертається у вихідний стан. У latching-моделі механізм утримує вибране положення після відпускання; наступна дія змінює його. Виробники можуть називати цю дію alternate або self-holding, а конкретні положення та контактна схема вказані в документації деталі.[^aratas-switch-basics]

NO розшифровується як normally open: у нормальному стані між відповідними контактами немає провідного шляху, а дія перемикає його в замкнений стан. NC, normally closed, означає провідний шлях у нормальному стані, який переривається під час дії. «Нормальний» тут – визначений конструкцією стан без активування, наприклад відпущена кнопка, а не стан, який найчастіше бачать у конкретній системі.[^aratas-switch-basics]

Приклад: у momentary-кнопки NO мікроконтролер бачить замикання лише під час натискання; у latching-вимикача NO контакт може лишитися замкненим після відпускання і розімкнутися лише при наступному перемиканні. Реальна логічна напруга залежить від підключення, pull-up/pull-down та схеми входу, тому NO не означає автоматично логічну одиницю.

**Типова помилка:** вважати NO синонімом «увімкнено». NO описує розімкнутість контакту в нормальному механічному стані; полярність логічного сигналу визначає зовнішня схема.[^aratas-switch-basics]

## Sources

<!-- generated from frontmatter -->
