---
id: emb-elintro-0263
title: "Для чого потрібен лабораторний блок живлення з режимами `CV` і `CC`?"
description: "Для чого потрібен лабораторний блок живлення з режимами `CV` і `CC`?"
track: electronics
section: introduction
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
    applicability: "Походження питання: лекція 24, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
  - source_id: aac-direct-current
    title: "All About Circuits textbook, Volume I: DC"
    url: https://www.allaboutcircuits.com/textbook/direct-current/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: DC-кола, закон Ома, закони Кірхгофа, джерела й вимірювання; конкретні номінали й схеми курсу можуть відрізнятися."
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: діоди, стабілітрони, біполярні й польові транзистори та джерела живлення; конкретні номінали й схеми курсу можуть відрізнятися."
  - source_id: keysight-bench-power-supply
    title: "Keysight: An In-Depth Guide to Bench Power Supplies"
    url: https://www.keysight.com/blogs/en/tech/educ/2023/bench-power-supply
    accessed: 2026-10-04
    kind: official
    version: null
    applicability: "Описує регулювання CV і CC та приклади навантажень; поведінка й захист залежать від можливостей конкретної моделі."
---

## Short answer

У режимі `CV` блок підтримує задану напругу, доки навантаження не досягне встановленого струмового ліміту. У режимі `CC` він регулює струм на заданому рівні, змінюючи вихідну напругу відповідно до навантаження.[^keysight-bench-power-supply] Струмовий ліміт може зменшити струм при короткому замиканні, але не гарантує захисту від кожного перехідного процесу чи пошкодження.

## Detailed explanation

Лабораторний блок живлення має керувати двома величинами: напругою, яку отримує навантаження, і максимально дозволеним струмом. У `CV` (constant voltage) він змінює вихід так, щоб напруга лишалася біля заданого значення; величину струму тоді переважно визначає саме навантаження. Якщо струм доходить до встановленої межі, блок переходить до регулювання струму, а напруга може знизитися.[^keysight-bench-power-supply]

У `CC` (constant current) блок намагається підтримувати заданий струм, а потрібна напруга залежить від опору та поведінки навантаження. Це корисно, наприклад, для перевірки LED або зарядного кола, коли важливо обмежити струм. CV і CC – режими регулювання, а не два незалежні виходи: реальний режим визначається заданими межами та навантаженням.[^keysight-bench-power-supply]

Приклад: для живлення плати 5 V задають `CV = 5 V` і вибирають струмовий ліміт, придатний для плати та проводів. Якщо несправність створить дуже низький опір, блок може перейти в CC і знизити напругу, щоб не перевищити ліміт. При цьому можливий короткий пусковий струм, а сам ліміт не замінює запобіжник або інші засоби захисту, тому перевіряйте специфікацію конкретного приладу та чутливість навантаження до перехідних процесів.[^keysight-bench-power-supply]

Типова помилка – сприймати CC як режим, який завжди «видає» заданий струм незалежно від кола. Якщо навантаження потребує напруги вище межі приладу або струмового ліміту недостатньо, заданий струм не буде досягнутий. Перед підключенням корисно оцінити нормальний робочий струм, установити напругу й ліміт та спостерігати, який індикатор режиму світиться під час роботи.[^keysight-bench-power-supply]

## Sources

<!-- generated from frontmatter -->
