---
id: emb-elcirc-0033
title: "Як резистивний подільник поводиться на змінних сигналах (АС)?"
description: "Як резистивний подільник поводиться на змінних сигналах (АС)?"
track: electronics
section: circuit-analysis
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
    applicability: "Походження питання: лекція 30, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
  - source_id: aac-direct-current
    title: "All About Circuits textbook, Volume I: DC"
    url: https://www.allaboutcircuits.com/textbook/direct-current/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: DC-кола, закон Ома, закони Кірхгофа, джерела й вимірювання; конкретні номінали й схеми курсу можуть відрізнятися."
  - source_id: aac-voltage-divider
    title: "All About Circuits: Voltage Divider Circuits"
    url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-6/voltage-divider-circuits/
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: "Пояснює DC-відношення резистивного подільника; частотні паразитні ефекти цим джерелом не специфіковано."
  - source_id: adi-frequency-divider
    title: "Analog Devices: Frequency Compensated Voltage Dividers"
    url: https://ez.analog.com/adiacademy/university-program/a/studentzone-articles/SA1045/adalm1000-smu-training-topic-11-frequency-compensated-voltage-dividers
    accessed: 2026-10-04
    kind: official
    version: null
    applicability: "Пояснює частотну незалежність ідеального резистивного подільника та вплив паразитної ємності; приклад стосується вимірювального входу ADALM1000."
---

## Short answer

В ідеальній схемі лише з резисторами коефіцієнт поділу AC-сигналу не залежить від частоти. У реальному колі паразитна ємність навантаження та монтажу може зробити передавання залежним від частоти; універсальної межі на кшталт десятків MHz немає.[^adi-frequency-divider]

## Detailed explanation

Ідеальний резистор не має реактивної складової імпедансу, тому в ідеальній схемі з двох резисторів відношення вихідної та вхідної напруг для синусоїдального сигналу таке саме, як для постійної напруги. Для ненавантаженої схеми воно задається `R_2/(R_1+R_2)`.[^adi-frequency-divider]

Практична схема не складається лише з ідеальних резисторів. Вхід наступного каскаду часто має ємність; разом із вихідним опором подільника вона утворює RC-ланку. Паразитна ємність впливає на частотну характеристику, а її ефект залежить від компонентів і навантаження, а не має універсального значення у MHz.[^adi-frequency-divider]

Приклад:

Якщо вихідний опір подільника разом із вхідною ємністю навантаження утворюють еквівалент `R` та `C`, характерний масштаб задає `τ = R*C`, а частота полюса для простої RC-ланки дорівнює `f_c = 1/(2π*R*C)`. Це наближення для однополюсної моделі, а не готова оцінка будь-якої плати.[^adi-frequency-divider]

**Типові помилки:**

- Переносити DC-формулу на реальне AC-коло без перевірки імпедансу джерела й навантаження.
- Називати фіксовану частоту, наприклад десятки MHz, межею для всіх подільників: межа визначається їхньою схемою та монтажем.

## Sources

<!-- generated from frontmatter -->
