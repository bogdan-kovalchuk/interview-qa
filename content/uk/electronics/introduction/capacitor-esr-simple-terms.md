---
id: emb-elintro-0135
title: "Що таке ESR конденсатора простими словами?"
description: "Що таке ESR конденсатора простими словами?"
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
  - source_id: kemet-ripple-current-mlcc
    title: "KEMET, Ripple Current and MLCC: Basic Principles"
    url: https://www.kemet.com/en/us/technical-resources/ripple-current-and-mlcc-basic-principles.html
    accessed: 2026-10-04
    kind: official
    version: null
    applicability: "Пояснює ESR як еквівалентний опір втрат і формулу нагрівання від діючого ripple current; конкретна частотна поведінка й теплові межі залежать від компонента та монтажу."
---

## Short answer

`ESR` – еквівалентний послідовний опір, що моделює втрати реального конденсатора. Пульсаційний струм нагріває його приблизно на `P = I_rms^2*ESR`; допустимість залежить від струму, частоти й теплового режиму. Для імпульсного джерела підбирають компонент за datasheet, а не лише за позначкою low-ESR.[^kemet-ripple-current-mlcc]

## Detailed explanation

У простій моделі конденсатор має ідеальну ємність, послідовний ESR і паразитну індуктивність ESL. ESR узагальнює резистивні втрати в діелектрику, електродах і контактах. Це еквівалентний параметр: реальний розподіл втрат складніший і залежить від частоти.[^kemet-ripple-current-mlcc]

Уявімо конденсатор як невеликий накопичувач заряду з внутрішнім опором. Коли через нього проходить ripple current, на ESR виникає додаткове падіння напруги, а потужність розсіюється як тепло. Для оцінки беруть діюче значення струму: `P = I_rms^2*ESR`. Пікове значення струму напряму підставляти в цю формулу не можна, якщо воно не дорівнює RMS.[^kemet-ripple-current-mlcc]

Значення ESR залежить від частоти вимірювання, температури та конструкції. Навіть однакові ємність і корпус не гарантують однаковий ESR у різних серій. Нагрів компонента також залежить від відведення тепла платою та повітрям, тому перевіряють частотні криві, допустимий ripple current і температурні умови в datasheet.[^kemet-ripple-current-mlcc]

Приклад: за `I_rms = 0.2 A` та ESR `0.5 Ω` втрати становлять `0.2^2*0.5 = 0.02 W`. За незмінного ESR збільшення струму до `0.4 A` збільшує оцінку до `0.08 W`, тобто вчетверо.

**Типова помилка:** називати ESR «ємністю» або вважати його значення однаковим на всіх частотах. Для практичного порівняння дивляться ESR на потрібній частоті й переконуються, що нагрівання та пульсації вкладаються в обмеження схеми й компонента.[^kemet-ripple-current-mlcc]

## Sources

<!-- generated from frontmatter -->
