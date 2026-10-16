---
id: emb-elee-0122
title: "Як зміна R впливає на частоту зрізу RC- і RL-фільтрів?"
track: electronics
section: ee101
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), картки курсу"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-alternating-current
    title: "All About Circuits textbook, Volume II: AC"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
  - source_id: fiore-ac-circuit-analysis
    title: "James M. Fiore: AC Electrical Circuit Analysis, A Practical Approach (sections 1.5 and 10.3)"
    url: https://www2.mvcc.edu/users/faculty/jfiore/Circuits2/ACElectricalCircuitAnalysis.pdf
  - source_id: kuphaldt-low-pass-filters
    title: "Tony R. Kuphaldt: Lessons In Electric Circuits, Vol. II (AC), 9.2 Low-pass Filters (LibreTexts)"
    url: https://workforce.libretexts.org/Bookshelves/Electronics_Technology/Electric_Circuits_II_-_Alternating_Current_(Kuphaldt)/09:_Filters/9.02:_Low-pass_Filters
  - source_id: fontys-passive-hf
    title: "Fontys University of Applied Sciences: 1.2 Passive components at high frequency (LibreTexts)"
    url: https://eng.libretexts.org/Courses/Fontys_University_of_Applied_Sciences/Telecommunications/01:_Passive_Components/1.02:_Passive_components_at_high_frequency
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
