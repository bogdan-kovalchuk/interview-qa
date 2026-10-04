---
id: emb-elee-0021
title: "Що таке AC-зв’язок (coupling capacitor) і де його використовують?"
description: "Що таке AC-зв’язок (coupling capacitor) і де його використовують?"
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
    applicability: "Походження питання: лекція 35, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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
  - source_id: aac-input-output-coupling
    title: "All About Circuits: Input and Output Coupling"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/chpt-4/input-and-output-coupling/
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: "Розділовий capacitor блокує DC зміщення між каскадами, але його high-pass властивості послаблюють низькі частоти."
  - source_id: aac-capacitor-highpass
    title: "All About Circuits: High-pass Filters"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-8/high-pass-filters/
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: "Робота простого RC high-pass фільтра й частота зрізу з опором, який бачить capacitor."
---

## Short answer

Розділовий конденсатор послідовно із сигналом послаблює DC і утворює high-pass ланку з опорами джерела та навантаження. Це дає змогу передавати AC-сигнал між каскадами без прямого перенесення їхніх DC-рівнів. Для простої RC-ланки `f_c = 1/(2*π*R*C)`, де `R` – ефективний опір, який бачить конденсатор.[^aac-input-output-coupling] [^aac-capacitor-highpass]

## Detailed explanation

Розділовий конденсатор передає змінну складову сигналу, водночас відокремлюючи DC-рівень одного вузла від DC-рівня наступного. Наприклад, вихід попереднього каскаду може мати власне зміщення, потрібне для його робочої точки; безпосереднє з’єднання здатне змінити напругу зміщення наступного каскаду. Послідовний capacitor не пропускає сталу складову в ідеальній моделі, тому каскади можна зміщувати окремо.[^aac-input-output-coupling]

Це не ідеальний «провід лише для AC». Імпеданс capacitor залежить від частоти: зі зниженням частоти він зростає, тому разом із резистивним оточенням компонент утворює high-pass filter. Нижче частоти зрізу сигнал послаблюється, а поблизу зрізу змінюються і амплітуда, і фаза. Отже, розділення DC має ціну: достатньо низькі частоти чи повільні зміни форми сигналу можуть спотворюватися.[^aac-capacitor-highpass] [^aac-input-output-coupling]

У найпростішій схемі один capacitor з’єднаний послідовно з джерелом і навантаженням, а опір `R` у наближеній формулі – еквівалентний опір, видимий із його виводів. Якщо опори з обох боків суттєві, не можна автоматично підставити лише номінал навантаження; потрібно визначити ефективний опір кола. Складніші каскади, кілька coupling capacitor та частотно-залежний вхідний імпеданс вимагають аналізу всієї мережі, тож проста формула дає лише оцінку для першопорядкової ланки.[^aac-capacitor-highpass]

Приклад: у моделі, де capacitor бачить `10 kΩ`, значення `C = 10 µF` дає `f_c ≈ 1.59 Hz`. Це значення не є універсальним для будь-якого підсилювача: реальний опір може включати вихідний опір джерела, вхідний опір каскаду та інші елементи.[^aac-capacitor-highpass]

**Типова помилка:** казати, що capacitor повністю «відсікає DC і пропускає весь AC». Фактично він ослаблює DC після перехідного процесу, а низькочастотний AC теж послаблює; розмір ефекту визначають частота сигналу й опір, який бачить capacitor.[^aac-input-output-coupling]

## Sources

<!-- generated from frontmatter -->
