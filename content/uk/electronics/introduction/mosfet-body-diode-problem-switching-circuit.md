---
id: emb-elintro-0259
title: "Коли body diode MOSFET може бути проблемою в ключовій схемі?"
description: "Коли body diode MOSFET може бути проблемою в ключовій схемі?"
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
    applicability: "Походження питання: лекція 23, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
  - source_id: aac-direct-current
    title: "All About Circuits textbook, Volume I: DC"
    url: https://www.allaboutcircuits.com/textbook/direct-current/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: DC-кола, закон Ома, закони Кірхгофа, джерела й вимірювання; конкретні номінали й схеми курсу можуть відрізнятися."
  - source_id: infineon-mosfet-layout
    title: "Infineon: Designing with power MOSFETs"
    url: https://www.infineon.com/assets/row/public/documents/24/42/infineon-designing-with-power-mosfets-applicationnotes-en.pdf?fileId=8ac78c8c7ddc01d7017e6c619a490f47
    accessed: 2026-10-04
    kind: official
    version: "V1.1, 2022-02-10"
    applicability: "Описує внутрішній body diode та reverse recovery в switching circuits; детальні параметри треба брати з datasheet конкретного MOSFET."
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: діоди, стабілітрони, біполярні й польові транзистори та джерела живлення; конкретні номінали й схеми курсу можуть відрізнятися."
---

## Short answer

У силового MOSFET є внутрішній body diode, що може проводити при вимкненому каналі, якщо схема прикладає до нього пряме зміщення.[^infineon-mosfet-layout] У bridge-схемах важливі dead time та reverse recovery, а в захисті від зворотного струму одна деталь не завжди блокує струм в обох напрямках.[^infineon-mosfet-layout]

## Detailed explanation

Body diode – внутрішній PN junction між body та drain у звичайному power MOSFET; body зазвичай з’єднаний із source. Тому при вимкненому gate diode все одно створює напрямлений шлях струму, якщо її анод і катод отримують пряму напругу. У N-channel MOSFET типовий шлях body diode спрямований від source до drain, але для практичного підключення звіряйте символ і полярність конкретної деталі.[^infineon-mosfet-layout]

У напівмосту струм індуктивного навантаження не може миттєво зникнути. Під час dead time він може перейти у body diode нижнього або верхнього ключа. Коли протилежний MOSFET увімкнеться, diode має припинити провідність; накопичений заряд створює reverse-recovery current, додаткові втрати та напругові/струмові піки. Ризик залежить від струму, швидкості перемикання, dead time та параметрів `Q_rr` і `t_rr`, тому на практиці дивляться на форми сигналу й межі datasheet.[^infineon-mosfet-layout]

Ще один випадок – одноключовий захист або high-side перемикач. Коли MOSFET вимкнений, body diode може залишити шлях у небажаному напрямку, наприклад від навантаження назад до джерела. Якщо потрібно блокувати струм в обох напрямках, застосовують відповідну топологію, часто два MOSFET із протилежно зорієнтованими body diode; конкретну реалізацію визначають напруги, керування gate та очікуваний режим.[^infineon-mosfet-layout]

**Типові помилки:**

- Припускати, що `V_GS = 0` означає електричну ізоляцію між drain і source в обох напрямках.
- Забувати про коротку провідність body diode під час dead time і reverse recovery при комутації.
- Вважати, що body diode є безкоштовним ідеальним діодом: перевіряйте прямий спад, допустимий струм і recovery характеристики.

## Sources

<!-- generated from frontmatter -->
