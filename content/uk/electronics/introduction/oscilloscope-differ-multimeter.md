---
id: emb-elintro-0268
title: "Чим осцилограф відрізняється від мультиметра?"
description: "Чим осцилограф відрізняється від мультиметра?"
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
  - source_id: tek-oscilloscope-specs
    title: "Tektronix: Evaluating Oscilloscope Bandwidth, Sample Rate, and Key Specifications"
    url: https://www.tek.com/en/documents/primer/evaluating-oscilloscopes
    accessed: 2026-10-04
    kind: official
    version: null
    applicability: "Осцилограф дискретизує напругу в часі й показує форму хвилі; обмеження смуги пропускання, sample rate та record length впливають на деталі вимірювання."
---

## Short answer

Мультиметр показує вибране числове вимірювання, наприклад DC або RMS напругу, тоді як осцилограф відображає напругу як функцію часу.[^tek-oscilloscope-specs] Це допомагає побачити переходи й короткі зміни, але відображена форма обмежена характеристиками пробника та осцилографа.[^tek-oscilloscope-specs]

## Detailed explanation

Мультиметр і осцилограф дають різні подання електричного сигналу. Мультиметр призначений для числового вимірювання вибраної величини: наприклад, напруги DC, струму, опору або RMS-значення змінної напруги. Показ на дисплеї є одним числом за певний інтервал вимірювання; він не показує повну послідовність змін сигналу в часі.

Осцилограф захоплює напругу через часові інтервали й показує форму хвилі на екрані. За нею можна оцінити амплітуду, період, частоту, пульсації, шум, overshoot і тривалість фронту. Проте ці деталі видно лише настільки, наскільки дозволяють смуга пропускання, частота дискретизації, довжина запису та пробник. Недостатня смуга може згладити фронти, а рідкісна дискретизація – пропустити подію або показати її хибно.[^tek-oscilloscope-specs]

Приклад: стабільний вихід джерела живлення зручно швидко перевірити мультиметром. Якщо треба з’ясувати, чи на виході є високочастотна пульсація або короткий провал під час перемикання навантаження, осцилограф показує часову форму й тривалість явища. Звичайне показання мультиметра може усереднити таку коротку подію, тому два прилади відповідають на різні запитання.[^tek-oscilloscope-specs]

**Типові помилки:**

- Вважати, що будь-яке число мультиметра є середнім: режим може показувати, наприклад, RMS, а точне визначення залежить від приладу.
- Вважати осцилограму точною лише тому, що хвиля намальована: недостатня смуга чи дискретизація спотворює її.
- Обирати інструмент без урахування питання: для одного значення зручний мультиметр, для зміни в часі – осцилограф.

## Sources

<!-- generated from frontmatter -->
