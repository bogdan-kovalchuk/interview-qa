---
id: emb-elee-0230
title: "Як розрахувати нижню частоту зрізу розділового конденсатора аудіокаскаду?"
description: "Як розрахувати нижню частоту зрізу розділового конденсатора аудіокаскаду?"
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
    applicability: "Походження питання: лекція 75, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-14; курс не є доказом цих тверджень."
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
  - source_id: fiore-ac-circuit-analysis
    title: "James M. Fiore: AC Electrical Circuit Analysis, A Practical Approach (sections 1.5 and 10.3)"
    url: https://www2.mvcc.edu/users/faculty/jfiore/Circuits2/ACElectricalCircuitAnalysis.pdf
    accessed: 2026-10-14
    kind: book
    version: "1.1.2, 22 April 2021"
    applicability: "Підручник з відкритою ліцензією (Creative Commons), розділ про lead network (глава 10): RC-ланцюг з виходом на резисторі є фільтром верхніх частот; f_c = 1/(2*pi*R*C) – частота, на якій сигнал спадає на 3 дБ; втрата A'v = -10*log10(1+(f_c/f)^2) (приклад 10.13); X_C = 1/(2*pi*f*C). Формули для одного RC-ланцюга."
  - source_id: fiore-common-emitter-amplifier
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 7.3 Common Emitter Amplifier"
    url: "https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/07:_BJT_Small_Signal_Amplifiers/7.3:_Common_Emitter_Amplifier"
    accessed: 2026-10-14
    kind: book
    version: null
    applicability: "Підручник, розділ 7.3: розділові конденсатори – розімкнення для постійного струму і коротке замикання для сигналу, якщо їх реактивний опір значно менший за сусідні резистори; A_v = -r_C/(r'_e + r_E) має мінус (інверсія, зсув фази на 180°); Z_out ≈ R_C, коли R_C значно менший за r'_C; з навантаженням A_divider = R_L/(R_L + R_C) (приклад 7.1)."
---

## Short answer

Для одного RC-ланцюга з розділовим конденсатором частота зрізу, на якій сигнал спадає на 3 дБ, дорівнює `f_c = 1/(2*pi*R*C)`, де R – опір, який бачить конденсатор.[^fiore-ac-circuit-analysis] За R = 10 кОм конденсатор 1 мкФ дає ≈ 15,9 Гц, а 100 нФ – ≈ 159 Гц; зменшення C вдесятеро підвищує зріз вдесятеро.

## Detailed explanation

Розділовий конденсатор між двома каскадами пропускає змінну складову сигналу і блокує постійну, тож зміщення одного каскаду не змінює режим іншого. Коли його реактивний опір `X_C` малий порівняно з сусідніми резисторами (на частотах у кілька разів вищих за `f_c`), він працює як коротке замикання для сигналу.[^fiore-common-emitter-amplifier] Разом з опором у контурі він утворює фільтр верхніх частот: чим нижча частота, тим більший реактивний опір `X_C = 1/(2*pi*f*C)` і тим сильніше сигнал послаблюється.[^fiore-ac-circuit-analysis]

Величина R у формулі – це опір, який бачить конденсатор, якщо дивитися з його висновків на решту кола з джерелом напруги, закороченим. У типовому ланцюзі опір джерела (вихідний опір попереднього каскаду) стоїть послідовно з конденсатором, а вхідний опір наступного каскаду разом із резисторами зміщення бази – між вузлом після конденсатора і землею. Їхня сума й дає R, тому номінал резистора на схемі не завжди дорівнює R.

**Приклад:** при R = 10 кОм зріз `1/(2*pi*10000*1e-6)` дає ≈ 15,9 Гц для C = 1 мкФ, а для C = 100 нФ – ≈ 159 Гц. Для зрізу 159 Гц втрата на 100 Гц становить `10*log10(1+(159/100)^2)` ≈ 5,5 дБ, а на 1 кГц – лише ≈ 0,11 дБ. Конденсатор 100 нФ уже помітно зрізає низькі звукові частоти, тоді як 1 мкФ майже не змінює їх.

Формула описує один RC-ланцюг першого порядку. Якщо в схемі кілька RC-ланок (наприклад, конденсатор у емітері, що шунтує резистор, теж утворює свій зріз), кожна дає свою частоту, і сумарну характеристику рахують для всієї схеми. Точка `f_c` – це не межа, за якою сигнал зникає, а місце, де втрата становить 3 дБ; нижче неї втрати зростають приблизно на 20 дБ на декаду.[^fiore-ac-circuit-analysis]

**Типові помилки:**

- Брати для R номінал резистора на схемі й ігнорувати опір джерела та вхідний опір наступного каскаду.
- Вважати `f_c` межею, нижче якої сигнал зникає: на `f_c` втрата лише 3 дБ.
- Рахувати одну RC-ланку, коли в схемі працює ще одна, наприклад конденсатор у емітері.

## Sources

<!-- generated from frontmatter -->
