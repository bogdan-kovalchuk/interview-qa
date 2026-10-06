---
id: emb-elee-0173
title: "Які основні співвідношення ідеального трансформатора і що означає його номінал у VA?"
description: "Які основні співвідношення ідеального трансформатора і що означає його номінал у VA?"
track: electronics
section: ee101
level: junior
type: concept
tags: []
status: published
updated: 2026-10-06
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
    applicability: "Походження питання: лекція 64, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-06; курс не є доказом цих тверджень."
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
  - source_id: kuphaldt-transformer-operation
    title: "Tony R. Kuphaldt: Lessons In Electric Circuits, Vol. II (AC), 10.1 Mutual Inductance and Basic Operation (LibreTexts)"
    url: https://workforce.libretexts.org/Bookshelves/Electronics_Technology/Electric_Circuits_II_-_Alternating_Current_(Kuphaldt)/10:_Transformers/10.01:_Mutual_Inductance_and_Basic_Operation
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "Миттєва напруга на котушці дорівнює кількості витків, помноженій на швидкість зміни потоку, що пронизує її; спільний потік у осерді індукує напругу у вторинній обмотці (взаємна індуктивність). Ідеалізований розгляд без втрат."
  - source_id: kuphaldt-transformer-ratios
    title: "Tony R. Kuphaldt: Lessons In Electric Circuits, Vol. II (AC), 10.2 Step-up and Step-down Transformers (LibreTexts)"
    url: https://workforce.libretexts.org/Bookshelves/Electronics_Technology/Electric_Circuits_II_-_Alternating_Current_(Kuphaldt)/10:_Transformers/10.02:_Step-up_and_Step-down_Transformers
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "Коефіцієнт перетворення напруги й струму дорівнює відношенню кількості витків, напруга й струм змінюються в протилежних напрямках, бо трансформатор не створює потужності, а лише перетворює її; відношення витків дорівнює кореню з відношення індуктивностей. Приклад 10:1 з SPICE; втрат не враховано."
  - source_id: kuphaldt-transformer-practical
    title: "Tony R. Kuphaldt: Lessons In Electric Circuits, Vol. II (AC), 10.8 Practical Considerations – Transformers (LibreTexts)"
    url: https://workforce.libretexts.org/Bookshelves/Electronics_Technology/Electric_Circuits_II_-_Alternating_Current_(Kuphaldt)/10:_Transformers/10.08:_Practical_Considerations_-_Transformers
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "Номінали трансформатора за напругою обмоток і VA (струм виводиться з VA); приклад 120 В / 48 В, 1 kVA; ККД сучасних силових трансформаторів зазвичай понад 95 %, втрати в обмотках і осерді, індуктивність розсіювання знижує напругу вторинної обмотки зі зростанням струму. Загальний навчальний текст."
  - source_id: fiore-rectification
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 3.2 Rectification"
    url: "https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/03:_Diode_Applications/3.2:_Rectification"
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "Розділ 3.2.2: у ідеалі напруга змінюється у відношенні витків, струм у зворотному, втрат у трансформаторі немає; номінал VA є добутком номінальної напруги вторинної обмотки на максимально допустимий струм вторинної; розділ 3.2.3: за конденсатора після випрямляча струм діода має короткі піки, а розділ 3.2.4: приклад 24 В * 0,3 А = 7,2 VA як мінімум. Навчальний розгляд, не норма."
  - source_id: fiore-ac-apparent-power
    title: "James M. Fiore: AC Electrical Circuit Analysis, A Practical Approach (section 7.2, Power Waveforms)"
    url: https://www2.mvcc.edu/users/faculty/jfiore/Circuits2/ACElectricalCircuitAnalysis.pdf
    accessed: 2026-10-06
    kind: book
    version: "1.1.2, 22 April 2021"
    applicability: "Розділ 7.2: повна потужність S має одиницю вольт-ампер (VA) і є добутком показів вольтметра й амперметра; без врахування кута фази між напругою й струмом вона не дорівнює активній потужності в ватах."
---

## Short answer

Для ідеального трансформатора `V_s/V_p = N_s/N_p` і `I_s/I_p = N_p/N_s`: напруга й струм змінюються в протилежних напрямках, а потужність зберігається.[^kuphaldt-transformer-ratios] Номінал у VA – це повна потужність `S = V_s,RMS*I_s,RMS` за номінальної напруги вторинної обмотки; він задає максимальний RMS-струм вторинної обмотки `I_s,max = S/V_s`, а не потужність у ватах.[^kuphaldt-transformer-practical][^fiore-ac-apparent-power]

## Detailed explanation

Ідеальний трансформатор – це модель без втрат і з повним магнітним зв’язком обох обмоток. Напруга на обмотці пропорційна кількості її витків і швидкості зміни спільного потоку,[^kuphaldt-transformer-operation] тому напруги відносяться як числа витків: `V_s/V_p = N_s/N_p`. Оскільки трансформатор лише перетворює потужність, а не створює її, струми змінюються у зворотному відношенні: `I_s/I_p = N_p/N_s`, і вхідна потужність дорівнює вихідній.[^kuphaldt-transformer-ratios] Тому step-down трансформатор, який знижує напругу, підвищує струм у вторинній обмотці, і вторинну обмотку мотають товщим дротом.[^kuphaldt-transformer-ratios] Приклад: для мережевого трансформатора `230 В / 12 В` відношення витків `N_p/N_s = 230/12 ≈ 19,2`; якщо вторинна обмотка віддає `2 А`, то в ідеальному випадку первинна споживає `2*12/230 ≈ 0,104 А`.

Номінал у вольт-амперах задає межу навантаження. Обмотки мають витримувати свій струм без перегріву, тому трансформатор паспортизують за напругами обмоток і значенням VA, з якого виводять допустимий струм: `I = S/V`.[^kuphaldt-transformer-practical] Для трансформатора 120 В / 48 В і 1 kVA максимальний струм первинної обмотки `1000/120 ≈ 8,33 А`, вторинної `1000/48 ≈ 20,8 А`.[^kuphaldt-transformer-practical] Тобто номінал у VA – це добуток номінальної напруги вторинної обмотки на максимально допустимий струм вторинної.[^fiore-rectification]

Номінал дається у VA, а не у ватах, бо обмотки обмежує струм (нагрівання дроту), а не активна потужність навантаження.[^kuphaldt-transformer-practical] Добуток RMS-напруги й RMS-струму – це повна потужність, і вона дорівнює активній лише для чисто резистивного навантаження; за зсуву фаз між напругою й струмом активна потужність менша.[^fiore-ac-apparent-power] Трансформатор не знає, яким буде навантаження, тож обмежує саме струм за заданої напруги. Показовий випадок – навантаження у вигляді випрямляча з конденсатором: діод проводить короткими імпульсами, і в прикладі з розділу про випрямлення пік струму заряджання конденсатора (близько 800 мА) значно перевищує струм, який бере навантаження 100 Ω за напруги 8–9 В.[^fiore-rectification] RMS-струм вторинної обмотки тоді більший, ніж постійний струм навантаження, тому за таких навантажень номінал беруть із запасом, а розрахунок «напруга на струм навантаження» вважають мінімумом.

Реальний трансформатор відхиляється від ідеальних співвідношень. Є втрати в обмотках і в осерді, а індуктивність розсіювання діє як послідовний опір, тож зі зростанням струму напруга вторинної обмотки знижується; ККД сучасних силових трансформаторів зазвичай вищий за 95 %.[^kuphaldt-transformer-practical] Отже, `V_s/V_p ≈ N_s/N_p` – хороше наближення для оцінки, але не точна рівність під навантаженням.

**Типові помилки:**

- Плутати відношення: напруга пропорційна `N_s/N_p`, а струм – `N_p/N_s`.[^kuphaldt-transformer-ratios]
- Ділити VA на напругу не тієї обмотки: струм вторинної обмотки дорівнює `S/V_s`, а первинної – `S/V_p`.[^kuphaldt-transformer-practical]
- Читати VA як ватти й не враховувати зсув фаз чи форму струму.[^fiore-ac-apparent-power]
- Очікувати рівно номінальну напругу на вторинній обмотці під навантаженням.[^kuphaldt-transformer-practical]

## Sources

<!-- generated from frontmatter -->
