---
id: emb-elintro-0153
title: "Чому не можна бездумно подавати прямокутний сигнал на трансформатор?"
description: "Чому не можна бездумно подавати прямокутний сигнал на трансформатор?"
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
    applicability: "Походження питання: лекція 15, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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
  - source_id: ti-magnetics-design-2
    title: "Texas Instruments: Magnetics Design 2 – Magnetic Core Characteristics"
    url: https://www.ti.com/lit/ml/slup124/slup124.pdf
    accessed: 2026-10-04
    kind: official
    version: null
    applicability: "Зміна потоку пропорційна volt-seconds; нерівність протилежних імпульсів може спричинити flux walking і насичення осердя."
---

## Short answer

Трансформатор може працювати з прямокутними імпульсами, якщо його осердя, частота, амплітуда, duty cycle і баланс volt-seconds відповідають проєкту. Якщо вольт-секунди за цикл не компенсуються, магнітний потік зміщується до насичення, через що зростає струм намагнічування й нагрівання. Тому трансформатор для синусоїдальної мережі 50/60 Hz не можна без перевірки під’єднувати до довільного прямокутного сигналу.[^ti-magnetics-design-2]

## Detailed explanation

Трансформатор може передавати прямокутні імпульси, але лише коли його магнітне осердя і схема керування розраховані на відповідні напругу, частоту, тривалість імпульсів та режим скидання потоку. За законом Фарадея зміна потоку залежить від інтеграла напруги за часом, тобто від volt-seconds на виток. Потік мусить повертатися до робочого рівня; якщо додатні й від’ємні вольт-секунди не компенсуються, виникає flux walking і осердя може насититися.[^ti-magnetics-design-2]

При насиченні індуктивність намагнічування різко зменшується, тому первинний струм може швидко зрости. Це перегріває обмотку або навантажує ключі перетворювача. У симетричних push-pull чи bridge схемах навіть невелика різниця тривалості імпульсів або падіння напруги на ключах здатна створювати накопичений дисбаланс; саме тому потрібні обмеження duty cycle і коректний reset осердя.[^ti-magnetics-design-2]

Частота також критична. Для тієї самої напруги довший імпульс створює більшу зміну потоку, а трансформатор, спроєктований на мережеві 50/60 Hz, зазвичай не можна без розрахунку живити сигналом іншої форми чи частоти. Водночас прямокутна форма сама по собі не є забороненою: SMPS використовують трансформатори з імпульсним збудженням, обмежуючи volt-seconds та передбачаючи шлях скидання потоку.[^ti-magnetics-design-2]

Приклад: у push-pull перетворювачі позитивний і негативний імпульси мають створювати приблизно рівні за модулем вольт-секунди. Якщо один імпульс довший, залишковий потік зростає від циклу до циклу й може привести осердя до насичення.[^ti-magnetics-design-2]

**Типові помилки:**
- вважати, що трансформатор не працює з прямокутною формою сигналу;
- перевіряти лише амплітуду, ігноруючи частоту та тривалість імпульсу;
- забувати про баланс volt-seconds і розмагнічування осердя.

## Sources

<!-- generated from frontmatter -->
