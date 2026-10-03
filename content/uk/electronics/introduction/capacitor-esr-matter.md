---
id: emb-elintro-0131
title: "Що таке ESR конденсатора і чому він важливий?"
description: "Що таке ESR конденсатора і чому він важливий?"
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
    applicability: "Походження питання: лекція 13, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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
  - source_id: analog-devices-an1099-capacitor-selection
    title: "Analog Devices, AN-1099: Capacitor Selection Guidelines for Analog Devices, Inc., LDOs"
    url: https://www.analog.com/en/resources/app-notes/an-1099.html
    accessed: 2026-10-04
    kind: official
    version: null
    applicability: "Розглядає bypass-конденсатори та вплив їх ESR на стабільність LDO, зокрема для вказаних Analog Devices регуляторів; не задає універсальних меж для всіх регуляторів."
  - source_id: kemet-ripple-current-mlcc
    title: "KEMET, Ripple Current and MLCC: Basic Principles"
    url: https://www.kemet.com/en/us/technical-resources/ripple-current-and-mlcc-basic-principles.html
    accessed: 2026-10-04
    kind: official
    version: null
    applicability: "Пояснює ESR, нагрівання від RMS ripple current і залежність теплового результату від корпусу та монтажу; стосується MLCC і не задає універсального рейтингу ESR для всіх типів конденсаторів."
---

## Short answer

ESR (Equivalent Series Resistance) – еквівалентний послідовний опір, що моделює резистивні втрати реального конденсатора. Для струму пульсацій середньоквадратичного значення `I_rms` втрати приблизно дорівнюють `P = I_rms^2*ESR`, тому високий ESR може спричинити нагрівання; конкретне значення залежить від частоти й конструкції.[^kemet-ripple-current-mlcc]

## Detailed explanation

ESR – це не окремий резистор, який обов’язково можна знайти всередині корпусу, а спрощений параметр еквівалентної моделі. Реальний конденсатор має втрати в діелектрику, електродах і виводах; у певному діапазоні частот їх зручно описувати послідовним опором разом з ідеальною ємністю та індуктивністю.[^kemet-ripple-current-mlcc]

Коли через конденсатор проходить змінна складова струму, на ESR виникає падіння напруги, а частина енергії переходить у тепло. Для приблизно сталого ESR середні втрати оцінюють як `P = I_rms^2*ESR`: подвоєння струму дає приблизно чотириразове зростання втрат. `I_rms` тут є саме діючим значенням пульсаційного струму, а не його піком чи середнім значенням.[^kemet-ripple-current-mlcc]

Значення ESR не є сталою характеристикою незалежно від умов: воно змінюється з частотою, температурою та типом конденсатора. Нагрів також залежить від теплового опору корпуса, друкованої плати, мідних доріжок і навколишнього середовища, тому самої формули недостатньо, щоб підтвердити допустимість компонента.[^kemet-ripple-current-mlcc]

Приклад: якщо `I_rms = 0.5 A`, а ESR на робочій частоті дорівнює `0.1 Ω`, то оцінка становить `P = 0.5^2*0.1 = 0.025 W`. Це лише втрати в еквівалентному опорі, а не повний тепловий прогноз для плати.

**Типова помилка:** вважати «нижчий ESR» автоматично кращим у будь-якій схемі. Він часто зменшує втрати та пульсації, але допустимі ємність і ESR можуть бути задані вимогами стабільності регулятора; їх треба перевіряти за документацією саме цієї схеми.[^analog-devices-an1099-capacitor-selection]

## Sources

<!-- generated from frontmatter -->
