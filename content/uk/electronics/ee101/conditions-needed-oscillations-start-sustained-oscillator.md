---
id: emb-elee-0248
title: "Які умови потрібні для виникнення і підтримання коливань у генераторі?"
description: "Які умови потрібні для виникнення і підтримання коливань у генераторі?"
track: electronics
section: ee101
level: junior
type: concept
tags: []
status: published
updated: 2026-10-14
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
    applicability: "Походження питання: лекція 79, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-14; курс не є доказом цих тверджень."
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
  - source_id: libretexts-fiore-oscillators
    title: "Fiore: Operational Amplifiers and Linear Integrated Circuits, 9.4 Summary (Oscillators and Frequency Generators)"
    url: "https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Operational_Amplifiers_and_Linear_Integrated_Circuits_-_Theory_and_Application_(Fiore)/09%3A_Oscillators_and_Frequency_Generators/9.4%3A_Summary"
    accessed: 2026-10-14
    kind: book
    version: null
    applicability: "Розділ 9.4 підручника: умова Баркгаузена (фаза контуру 0° або кратна 360°; добуток підсилення й зворотного зв’язку більший за одиницю для запуску і рівний одиниці для підтримання), обмежувальний елемент у ланці від’ємного зворотного зв’язку та залежність точності частоти від компонентів. Викладено для генераторів на операційних підсилювачах; кварцові схеми не розглядає."
---

## Short answer

У сталому режимі `|A*beta| ≈ 1`, а фаза контуру кратна 360°; для запуску потрібне `|A*beta| > 1`, щоб мале збурення наростало.[^libretexts-fiore-oscillators] Щоб підсилення спадало до одиниці, у ланці від’ємного зворотного зв’язку ставлять обмежувальний елемент, наприклад діод або лампу.[^libretexts-fiore-oscillators] Тут `beta` – коефіцієнт зворотного зв’язку, а не струмове підсилення BJT.

## Detailed explanation

Генератор – це підсилювач із додатним зворотним зв’язком, у якому частина вихідного сигналу повертається на вхід. Петлю описують добутком підсилення `A` і коефіцієнта зворотного зв’язку `beta`, тобто `A*beta`. Умова Баркгаузена вимагає, щоб фаза контуру дорівнювала 0° або кратному 360°, а добуток підсилення на зворотний зв’язок для підтримання коливань лишався рівним одиниці.[^libretexts-fiore-oscillators] Тоді сигнал, що пройшов петлю, повертається з тією самою фазою й амплітудою, і коливання можуть підтримуватися.

Для запуску потрібне більше одиниці: при `|A*beta| > 1` кожен прохід петлею збільшує амплітуду, і мале збурення, наприклад шум у момент ввімкнення, наростає.[^libretexts-fiore-oscillators] Амплітуда не може рости нескінченно. Тому в ланці від’ємного зворотного зв’язку ставлять обмежувальний елемент, наприклад діод або лампу, який зменшує підсилення до одиниці.[^libretexts-fiore-oscillators] Стале коливання – це стан, у якому нелінійність тримає `|A*beta|` біля одиниці.

Умова фази вибирає частоту, на якій петля замикається, а точність цієї частоти визначають елементи ланки. У RC-генераторах на ОП частоту задає RC-мережа, а точність залежить від допусків цих компонентів і, меншою мірою, від самого підсилювача.[^libretexts-fiore-oscillators]

Приклад: нехай `|A*beta| = 1.02`, а початкове збурення 1 мВ. Після `n` проходів амплітуда дорівнює `1 мВ * 1.02^n`. Щоб вона дійшла до 1 В, потрібно `n = ln(1000)/ln(1.02) ≈ 349` проходів: `1.02^348 ≈ 984`, а `1.02^349 ≈ 1003`. Якщо ж `|A*beta| = 0.98`, після 349 проходів амплітуда буде `1 мВ * 0.98^349 ≈ 0,87 мкВ`, тобто коливання згасають. Числа ілюстративні, бо затримки в реальному контурі не враховано.

**Типові помилки:**

- Розраховувати лише на `|A*beta| = 1`: для запуску потрібне `|A*beta| > 1`.[^libretexts-fiore-oscillators]
- Плутати `beta` із струмовим підсиленням транзистора: тут це коефіцієнт зворотного зв’язку.
- Вважати, що умова Баркгаузена задає точну частоту: точність визначають компоненти ланки, наприклад RC-мережа.[^libretexts-fiore-oscillators]

## Sources

<!-- generated from frontmatter -->
