---
id: emb-elee-0123
title: "Як практично перевірити RL-ФНЧ і ФВЧ на макеті?"
description: "Як практично перевірити RL-ФНЧ і ФВЧ на макеті?"
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
    applicability: "Походження питання: лекція 54, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-06; курс не є доказом цих тверджень."
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
    accessed: 2026-10-06
    kind: book
    version: "1.1.2, 22 April 2021"
    applicability: "Розділ 1.5: напруга на ідеальній котушці випереджає струм на 90°, реактивний опір `X_L = j*2*pi*f*L`. Розділ 10.3: для RC lead-мережі зріз лежить на 3 dB нижче рівня смуги пропускання, `f_c = 1/(2*pi*R*C)`, фаза виходу +90° на низьких частотах і +45° на критичній. Фільтр RL там окремо не розглянуто: співвідношення для RL тут виведено з тих самих формул дільника напруги."
  - source_id: kuphaldt-low-pass-filters
    title: "Tony R. Kuphaldt: Lessons In Electric Circuits, Vol. II (AC), 9.2 Low-pass Filters (LibreTexts)"
    url: https://workforce.libretexts.org/Bookshelves/Electronics_Technology/Electric_Circuits_II_-_Alternating_Current_(Kuphaldt)/09:_Filters/9.02:_Low-pass_Filters
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "Зріз ФНЧ – частота, вище якої вихід менший за 70,7% входу; для RC-ФНЧ це частота, на якій реактивний опір дорівнює опору R; відгук фільтра залежить і від опору навантаження; котушки мають суттєві резистивні втрати (дріт, осердя). Формули зрізу RL у читаному тексті сторінки немає (лише на рисунках), тому вона виведена окремо."
  - source_id: tektronix-abcs-probes
    title: "Tektronix: ABCs of Probes Primer"
    url: https://download.tek.com/document/02_ABCs-of-Probes-Primer.pdf
    accessed: 2026-10-06
    kind: official
    version: null
    applicability: "Пробник і осцилограф мають обмежену смугу (на межі смуги сигнал спадає на 3 dB; для точних амплітуд радять запас смуги в 3–5 разів), а пробник навантажує джерело, зокрема ємністю наконечника, і цим знижує смугу системи. Загальні положення, не конкретні моделі приладів курсу."
---

## Short answer

Для кожної схеми подати малий синус на `0.1*f_c`, `f_c` і `10*f_c`, записати частоту, `V_in`, `V_out` і зсув фази та порівняти з розрахунком. У ФНЧ вихід із частотою спадає, у ФВЧ зростає; зріз – частота, на якій вихід дорівнює ≈ 70,7% рівня смуги пропускання (≈ `-3.01 dB`).[^kuphaldt-low-pass-filters][^fiore-ac-circuit-analysis]

## Detailed explanation

**Що перевіряємо.** Фільтр першого порядку має три характерні точки. Для RL-фільтра з `R = 470 Ω` і `L = 10 mH` розрахунковий зріз `f_c = R/(2*pi*L) = 470/(2*pi*0.01) ≈ 7.48 kHz`, тож перевіряємо `≈ 748 Hz`, `≈ 7.48 kHz` і `≈ 74.8 kHz`. Для RL-ФНЧ (вихід на резисторі) очікуємо `|V_out/V_in|` ≈ 0.995, 0.707 і 0.0995 (`-0.04 dB`, `-3.01 dB`, `-20.04 dB`) та фазу `-5.7°`, `-45°`, `-84.3°`. Для RL-ФВЧ (вихід на котушці) амплітуди йдуть у зворотному порядку – 0.0995, 0.707, 0.995, а фаза дорівнює `+84.3°`, `+45°`, `+5.7°`. Зріз визначають як точку, де вихід на 3 dB нижче рівня смуги пропускання (множник 0.707).[^fiore-ac-circuit-analysis][^kuphaldt-low-pass-filters]

**Порядок вимірювання.** Генератор подає синус на вхід фільтра. Канал 1 осцилографа підключають до входу фільтра, канал 2 – до виходу, а земляні затискачі з’єднують разом. Обидві схеми природно мають спільну землю з виходом: у ФВЧ котушка йде на землю, у ФНЧ на землю йде резистор. Амплітуду `V_in` перевіряють на кожній частоті, бо фільтр навантажує генератор, і вона може відхилятися. Потім частоту підстроюють, поки `V_out` не стане 0.707 від рівня смуги пропускання (у ФНЧ – показання на низьких частотах, у ФВЧ – на високих); на цій частоті зсув фази має бути близько 45°, і це друга незалежна ознака зрізу.

**Чому результат відрізняється від розрахунку.** Розрахунок дає номінальне значення, а вимірювання – реальне. Допуск індуктивності зсуває `f_c`, опір обмотки додається до `R`, а вихідний опір генератора й опір навантаження теж змінюють відгук.[^kuphaldt-low-pass-filters] Вимірювальний тракт також має власну смугу: на межі смуги осцилограф і пробник уже занижують сигнал на 3 dB, а пробник додатково навантажує схему ємністю наконечника.[^tektronix-abcs-probes] Тому на найвищій перевірній частоті треба переконатися, що вона далека від меж приладів. Зворотний розрахунок допомагає знайти реальну індуктивність: якщо виміряний зріз `7.0 kHz`, то `L = R/(2*pi*f_c) = 470/(2*pi*7000) ≈ 10.7 mH`.

**Типові помилки:**

- Вважати зрізом точку, де вихід упав удвічі (`-6 dB`): зріз лежить на `-3 dB`, тобто на 0.707, а не на 0.5.
- Один раз виміряти `V_in` на генераторі й далі вважати її сталою: навантаження фільтра змінює її з частотою.
- Порівнювати амплітуди з одиницею, коли реальна смуга пропускання менша за 1: зріз треба відлічувати від виміряного рівня смуги.
- Брати для перевірки лише одну частоту: щоб відрізнити ФНЧ від ФВЧ і оцінити нахил, потрібні щонайменше три точки.

## Sources

<!-- generated from frontmatter -->
