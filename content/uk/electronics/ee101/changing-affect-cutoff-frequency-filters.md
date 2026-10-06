---
id: emb-elee-0122
title: "Як зміна R впливає на частоту зрізу RC- і RL-фільтрів?"
description: "Як зміна R впливає на частоту зрізу RC- і RL-фільтрів?"
track: electronics
section: ee101
level: junior
type: pitfall
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
    applicability: "Походження питання: лекція 53, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-06; курс не є доказом цих тверджень."
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
  - source_id: fontys-passive-hf
    title: "Fontys University of Applied Sciences: 1.2 Passive components at high frequency (LibreTexts)"
    url: https://eng.libretexts.org/Courses/Fontys_University_of_Applied_Sciences/Telecommunications/01:_Passive_Components/1.02:_Passive_components_at_high_frequency
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "Еквівалентна схема реальної котушки: ідеальна індуктивність, послідовний опір обмотки `R_s` і паралельна паразитна ємність `C_d`; практична котушка придатна лише нижче власної резонансної частоти (self-resonant frequency), а skin effect підвищує опір обмотки. Загальна модель, а не параметри конкретної котушки курсу."
---

## Short answer

Протилежно. У RC `f_c = 1/(2*pi*R*C)`, тому збільшення `R` зменшує зріз. У RL `f_c = R/(2*pi*L)`, тому збільшення `R` підвищує зріз: подвоєння `R` подвоює `f_c`.[^fiore-ac-circuit-analysis][^kuphaldt-low-pass-filters]

## Detailed explanation

**Звідки береться формула.** Зріз першого порядку лежить там, де реактивний опір дорівнює опору `R`: тоді вихід становить 70,7% рівня смуги пропускання, тобто `-3 dB`.[^kuphaldt-low-pass-filters] Для RC це `X_C = 1/(2*pi*f*C) = R`, звідки `f_c = 1/(2*pi*R*C)`.[^fiore-ac-circuit-analysis] Для RL умова `X_L = 2*pi*f*L = R` дає `f_c = R/(2*pi*L)`. Цю формулу легко перевірити: у дільнику `R` і `L` модуль передавальної функції ФНЧ дорівнює `R/sqrt(R^2 + X_L^2)`, і при `X_L = R` він справді `1/sqrt(2)`.

**Чому напрямок протилежний.** Реактивні опори поводяться навпаки: `X_C` зменшується з частотою, а `X_L` зростає. У RC за більшого `R` конденсатору, щоб зрівнятися з резистором, потрібен більший реактивний опір, а він настає на нижчій частоті: зріз зсувається вниз. У RL за більшого `R` котушці потрібно набрати більший `X_L`, а він зростає лише разом із частотою: зріз зсувається вгору. Ці залежності однакові для ФНЧ і ФВЧ однієї топології, бо вони мають спільну `f_c`.

**Приклад.** RC із `C = 100 nF`: при `R = 1.6 kΩ` маємо `f_c = 1/(2*pi*1600*1e-7) ≈ 995 Hz`, а при `R = 3.2 kΩ` – `≈ 497 Hz`, тобто вдвічі менше. RL із `L = 10 mH`: при `R = 1 kΩ` маємо `f_c = 1000/(2*pi*0.01) ≈ 15.9 kHz`, а при `R = 2 kΩ` – `≈ 31.8 kHz`, тобто вдвічі більше.

**Що саме є `R`.** У формулу входить повний опір, який бачить реактивний елемент: резистор плюс вихідний опір джерела, а для RL ще й опір обмотки котушки.[^fontys-passive-hf] Опір навантаження також змінює відгук фільтра, і формула без нього справджується лише для розімкненого виходу.[^kuphaldt-low-pass-filters] Тому «змінити R» на практиці означає змінити суму всіх таких опорів.

**Типові помилки:**

- Переносити інтуїцію з RC на RL: у RL збільшення `R` підвищує зріз, а не знижує.
- Плутати `f_c` у герцах із `ω_c` у рад/с: `ω_c = R/L`, `f_c = ω_c/(2*pi)`.
- Не враховувати вихідний опір джерела, опір обмотки і навантаження: реальний зріз відрізняється від розрахунку за номіналом резистора.

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
