---
id: emb-elintro-0102
title: "Знайдіть I, V_R1 та V_R2 для R_1 = 100 Ω, R_2 = 330 Ω і джерела 3 V?"
description: "Знайдіть I, V_R1 та V_R2 для R_1 = 100 Ω, R_2 = 330 Ω і джерела 3 V?"
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
    applicability: "Походження питання: лекція 11, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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
  - source_id: aac-series-circuits
    title: "All About Circuits: Series Circuits and the Application of Ohm’s Law"
    url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-5/simple-series-circuits/
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: "Підтверджує правила послідовних кіл; числа залежать від заданих номіналів."
---

## Short answer

Для ідеального джерела 3 V і послідовних резисторів 100 Ω та 330 Ω загальний опір дорівнює `R_total = 430 Ω`, а струм `I = 3 V/430 Ω ≈ 6.98 mA`. Падіння напруги становлять `V_R1 ≈ 0.698 V` і `V_R2 ≈ 2.30 V`; їхня сума дорівнює 3 V з урахуванням округлення.[^aac-series-circuits]

## Detailed explanation

У послідовному колі резистори утворюють один шлях, тому через обидва проходить однаковий струм. Спочатку замінюємо їх еквівалентним опором: `R_total = R_1 + R_2 = 100 Ω + 330 Ω = 430 Ω`. Далі застосовуємо закон Ома до всього кола: `I = V/R_total = 3 V/430 Ω ≈ 0.00698 A = 6.98 mA`.[^aac-series-circuits]

Щоб знайти напругу на кожному резисторі, множимо цей самий струм на його опір: `V_R1 = I*R_1 ≈ 0.698 V`, а `V_R2 = I*R_2 ≈ 2.30 V`. Перевірка законом Кірхгофа дає `V_R1 + V_R2 ≈ 0.698 V + 2.30 V = 3.00 V`. Невелика різниця останніх десяткових знаків виникає через округлення; у фізичному колі додадуться допуск резисторів і внутрішній опір джерела.[^aac-series-circuits]

**Типові помилки:**
- Не діліть напругу джерела окремо на кожен резистор, щоб отримати струм. Для струму всього послідовного кола використовуйте загальний опір.
- Не плутайте mA з A: `0.00698 A` дорівнює `6.98 mA`.
- Напруга джерела прикладена до обох резисторів разом, а окремі падіння визначаються за `V = I*R`.[^aac-series-circuits]

## Sources

<!-- generated from frontmatter -->
