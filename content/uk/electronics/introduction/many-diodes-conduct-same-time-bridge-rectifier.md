---
id: emb-elintro-0181
title: "Скільки діодів одночасно проводить у bridge rectifier?"
description: "Скільки діодів одночасно проводить у bridge rectifier?"
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
    applicability: "Походження питання: лекція 17, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
  - source_id: aac-direct-current
    title: "All About Circuits textbook, Volume I: DC"
    url: https://www.allaboutcircuits.com/textbook/direct-current/
    accessed: 2026-09-27
    kind: community
    version: null
    applicability: "Авторитетне джерело рівня секції: DC-кола, закон Ома, закони Кірхгофа, джерела й вимірювання; конкретні номінали й схеми курсу можуть відрізнятися."
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: діоди, стабілітрони, біполярні й польові транзистори та джерела живлення; конкретні номінали й схеми курсу можуть відрізнятися."
  - source_id: bridge-rectifier-operation
    title: "Full Wave Rectifier and Bridge Rectifier Theory"
    url: https://www.electronics-tutorials.ws/diode/diode_6.html
    accessed: 2026-10-04
    kind: community
    version: null
    applicability: "Explains the bridge conduction paths, two conducting diodes per half-cycle, doubled ripple frequency, and typical forward-drop example."
---

## Short answer

У кожну напівхвилю проводить пара діодів, тому на шляху струму є два падіння `V_F`. Це важливо для низьковольтних джерел, де втрата `2V_F` може бути значною.[^bridge-rectifier-operation] [^aac-semiconductors]

## Detailed explanation

У мостовому випрямлячі під час кожної півхвилі проводять дві діагонально розташовані діоди, а дві інші блокують струм. Напрямок струму через навантаження лишається однаковим, хоча полярність напруги джерела змінюється.[^aac-semiconductors]

Коли вхідна напруга має одну полярність, струм іде від одного входу змінного струму через перший діод до позитивного виходу, проходить крізь навантаження й повертається через другий діод до іншого входу. На наступній півхвилі провідною стає інша діагональна пара. Тому обидві півхвилі створюють імпульси тієї самої полярності.[^aac-semiconductors]

Це не означає, що всі чотири діоди проводять водночас. У кожному шляху струму послідовно працюють два діоди, тож їхні прямі падіння додаються й зменшують доступну напругу навантаження. Реальне падіння залежить від струму, температури та типу діода; розрахунок за сталою величиною є лише наближенням.[^aac-semiconductors]

Приклад: у позитивну півхвилю проводить пара D1–D2, а в негативну – D3–D4. Якщо кожен діод має приблизно 0.7 V падіння за конкретного струму, шлях втрачає близько 1.4 V; це ілюстрація, а не гарантований параметр.[^aac-semiconductors]

**Типова помилка:** вважати, що через міст одночасно проходить струм через усі чотири діоди, або відняти падіння лише одного діода. Щоб перевірити схему, простежте замкнений шлях для обох полярностей джерела.

## Sources

<!-- generated from frontmatter -->
