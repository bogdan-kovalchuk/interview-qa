---
id: emb-elee-0172
title: "Що означає offline-живлення і що робить мережевий трансформатор?"
description: "Що означає offline-живлення і що робить мережевий трансформатор?"
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
  - source_id: ti-an556
    title: "Texas Instruments AN-556 (SNVA006B): Introduction to Power Supplies"
    url: https://www.ti.com/lit/an/snva006b/snva006b.pdf
    accessed: 2026-10-06
    kind: official
    version: "SNVA006B, May 2004"
    applicability: "Функції блока живлення від мережі (випрямлення, перетворення напруги, фільтрація, регулювання, ізоляція, захист); лінійний блок із 50/60 Hz трансформатором, випрямлячем, конденсатором і регулятором; означення off-line (напруга для ключа формується безпосередньо з мережі), обов’язкова ізоляція в off-line-перетворювачах 110/220 В, виконана трансформатором, і менший розмір високочастотного трансформатора. Огляд 2004 року; конкретні схеми й потужності не є нормою."
  - source_id: kuphaldt-transformer-operation
    title: "Tony R. Kuphaldt: Lessons In Electric Circuits, Vol. II (AC), 10.1 Mutual Inductance and Basic Operation (LibreTexts)"
    url: https://workforce.libretexts.org/Bookshelves/Electronics_Technology/Electric_Circuits_II_-_Alternating_Current_(Kuphaldt)/10:_Transformers/10.01:_Mutual_Inductance_and_Basic_Operation
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "Принцип роботи трансформатора: змінний струм змінює потік у спільному осерді, змінний потік індукує напругу у вторинній обмотці (взаємна індуктивність). Ідеалізований розгляд без втрат."
  - source_id: kuphaldt-transformer-isolation
    title: "Tony R. Kuphaldt: Lessons In Electric Circuits, Vol. II (AC), 10.3 Electrical Isolation (LibreTexts)"
    url: https://workforce.libretexts.org/Bookshelves/Electronics_Technology/Electric_Circuits_II_-_Alternating_Current_(Kuphaldt)/10:_Transformers/10.03:_Electrical_Isolation
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "Трансформатор передає потужність між колами без провідного з’єднання (електрична ізоляція), а синфазна напруга на вторинному колі не потрапляє на первинне; ізолювальні трансформатори мають співвідношення 1:1. Це модель зі SPICE, а не норма безпеки."
  - source_id: kuphaldt-transformer-practical
    title: "Tony R. Kuphaldt: Lessons In Electric Circuits, Vol. II (AC), 10.8 Practical Considerations – Transformers (LibreTexts)"
    url: https://workforce.libretexts.org/Bookshelves/Electronics_Technology/Electric_Circuits_II_-_Alternating_Current_(Kuphaldt)/10:_Transformers/10.08:_Practical_Considerations_-_Transformers
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "Номінали трансформатора за напругою обмоток і VA (струм виводиться з VA); приклад 120 В / 48 В, 1 kVA; обмотки мають бути достатньо ізольовані одна від одної, щоб зберегти електричну ізоляцію; насичення осердя за зниженої частоти (50 замість 60 Hz). Загальний навчальний текст."
---

## Short answer

Offline-живлення отримує енергію безпосередньо з мережі змінного струму. Мережевий трансформатор (50/60 Hz) за допомогою магнітного зв’язку перетворює напругу, а за розділених обмоток може давати й гальванічну ізоляцію, але не випрямляє і не стабілізує: на вторинній обмотці лишається змінна напруга.[^ti-an556][^kuphaldt-transformer-isolation] В offline-імпульсних блоках мережу випрямляють до трансформатора, а ізоляцію забезпечує трансформатор на високій частоті.[^ti-an556]

## Detailed explanation

Слово offline тут про джерело енергії, а не про відсутність підключення: блок живлення «від мережі» бере енергію з мережі змінного струму, а не з батареї чи готового низьковольтного джерела. У документі TI AN-556 offline-імпульсний блок названо так, бо постійну напругу для ключа формують безпосередньо з мережі.[^ti-an556] Задачі такого блока ті самі, що й будь-якого іншого: випрямити, перетворити напругу до потрібного рівня, відфільтрувати, стабілізувати й ізолювати вихід від мережі; у лінійному блоці ці функції виконують окремі вузли.[^ti-an556]

Звичайний лінійний блок із мережевим трансформатором будується послідовно: трансформатор зі вторинною обмоткою (з відведенням від середини або під міст), діоди, фільтрувальний конденсатор і лінійний стабілізатор.[^ti-an556] Трансформатор у цьому ланцюжку лише змінює рівень змінної напруги й розділяє кола: змінний струм у первинній обмотці створює змінний потік у спільному осерді, а він індукує напругу у вторинній.[^kuphaldt-transformer-operation] Для постійної напруги на первинній обмотці потік у сталому режимі не змінювався б, тож вторинної напруги не було б. Наприклад, для 12 В RMS на вторинній обмотці амплітуда становить `12*sqrt(2) ≈ 17,0 В`, але вона змінює знак, і до випрямлення з неї не можна живити схему, якій потрібна постійна напруга.

Гальванічна ізоляція виникає тому, що енергія передається магнітним полем, без провідного з’єднання між колами, і синфазна напруга на вторинній стороні не потрапляє на первинну.[^kuphaldt-transformer-isolation] Це властивість трансформатора з окремими обмотками, і вона залежить від виконання: обмотки мають бути достатньо ізольовані одна від одної.[^kuphaldt-transformer-practical] Мережевий трансформатор працює на частоті 50 або 60 Hz; його розмір обернено пропорційний частоті (в певних межах), тому такі трансформатори громіздкі.[^ti-an556]

Саме тому в сучасних offline-імпульсних блоках мережу спочатку випрямляють і лише потім перетворюють високочастотним ключем. AN-556 пояснює, що для живлення від мережі 110/220 В електрична ізоляція обов’язкова, і в flyback-схемі її забезпечує трансформатор на місці дроселя; на високій частоті він значно менший за трансформатор на 50/60 Hz, а зворотний зв’язок теж має бути ізольований (малим трансформатором чи оптопарою).[^ti-an556] Отже, offline не означає «із мережевим трансформатором», а мережевий трансформатор не робить блок стабілізованим.

**Типові помилки:**

- Вважати, що трансформатор дає постійну напругу або стабілізує її: ці функції виконують випрямляч, конденсатор і стабілізатор.[^ti-an556]
- Ототожнювати offline-блок із блоком із трансформатором на 50/60 Hz: в offline-імпульсному блоці мережу випрямляють до трансформатора.[^ti-an556]
- Вважати гальванічну ізоляцію автоматичною: вона залежить від конструкції обмоток і ізоляції між ними.[^kuphaldt-transformer-practical]

## Sources

<!-- generated from frontmatter -->
