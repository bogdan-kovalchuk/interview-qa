---
id: emb-elee-0121
title: "Чому реальний RL-ФВЧ дає ненульовий вихід на DC і не пропускає «будь-які» високі частоти?"
description: "Чому реальний RL-ФВЧ дає ненульовий вихід на DC і не пропускає «будь-які» високі частоти?"
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
  - source_id: kuphaldt-high-pass-filters
    title: "Tony R. Kuphaldt: Lessons In Electric Circuits, Vol. II (AC), 9.3 High-pass Filters (LibreTexts)"
    url: https://workforce.libretexts.org/Bookshelves/Electronics_Technology/Electric_Circuits_II_-_Alternating_Current_(Kuphaldt)/09:_Filters/9.03:_High-pass_Filters
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "Індуктивний ФВЧ: резистор послідовно, котушка паралельно навантаженню (вихід знімають на котушці); зріз – частота, на якій вихід дорівнює 70,7% входу; на високих частотах котушки поводяться несподівано через skin effect і втрати в осерді. Формул RL у читаному тексті сторінки немає (вони лише на рисунках), тому тут вони виведені окремо."
  - source_id: fontys-passive-hf
    title: "Fontys University of Applied Sciences: 1.2 Passive components at high frequency (LibreTexts)"
    url: https://eng.libretexts.org/Courses/Fontys_University_of_Applied_Sciences/Telecommunications/01:_Passive_Components/1.02:_Passive_components_at_high_frequency
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "Еквівалентна схема реальної котушки: ідеальна індуктивність, послідовний опір обмотки `R_s` і паралельна паразитна ємність `C_d`; практична котушка придатна лише нижче власної резонансної частоти (self-resonant frequency), а skin effect підвищує опір обмотки. Загальна модель, а не параметри конкретної котушки курсу."
  - source_id: tektronix-abcs-probes
    title: "Tektronix: ABCs of Probes Primer"
    url: https://download.tek.com/document/02_ABCs-of-Probes-Primer.pdf
    accessed: 2026-10-06
    kind: official
    version: null
    applicability: "Пробник і осцилограф мають обмежену смугу (на межі смуги сигнал спадає на 3 dB; для точних амплітуд радять запас смуги в 3–5 разів), а пробник навантажує джерело, зокрема ємністю наконечника, і цим знижує смугу системи. Загальні положення, не конкретні моделі приладів курсу."
  - source_id: vishay-inductors-primer
    title: "Vishay: Inductors 101 – Primer Instructional Guide"
    url: https://www.vishay.com/docs/49782/49782.pdf
    accessed: 2026-10-06
    kind: official
    version: "VMN-SG2139-1203"
    applicability: "Визначення DCR, SRF і розподіленої ємності котушки: вище SRF переважає ємнісний реактанс, а менша розподілена ємність за тієї самої індуктивності дає вищу SRF. Числових значень для котушки курсу не дає; їх беруть з datasheet конкретної котушки."
---

## Short answer

Через опір обмотки `r_L`: на DC ідеальна котушка – коротке замикання, тож залишається дільник `V_out = V_in*r_L/(R + r_L)`, а не нуль (вихід знято з котушки без навантаження).[^fontys-passive-hf] На дуже високих частотах паразитна ємність котушки створює власний резонанс (SRF), вище якого переважає ємнісний реактанс і котушка поводиться як ємність.[^vishay-inductors-primer] Смугу вимірювань обмежують ще й осцилограф та пробник.[^tektronix-abcs-probes]

## Detailed explanation

**Реальна котушка – це не лише `L`.** Еквівалентна схема справжньої котушки містить ідеальну індуктивність, послідовний опір обмотки `r_L` і паралельну паразитну ємність `C_d`.[^fontys-passive-hf] Тому вихід «на котушці» – це напруга на ланцюжку `r_L` + `L`. На постійному струмі реактивний опір дорівнює нулю, лишається тільки `r_L`, і разом із `R` він утворює резистивний дільник. Наприклад, `R = 1 kΩ`, `r_L = 50 Ω`: `V_out/V_in = 50/1050 ≈ 0.0476`, тобто ≈ 4.8% входу (`-26.4 dB`), а не 0, як давала б ідеальна модель.

**Як це змінює АЧХ.** Передавальна функція стає `(r_L + j*2*pi*f*L)/(R + r_L + j*2*pi*f*L)`. Вона має нуль на `r_L/(2*pi*L)` і полюс на `(R + r_L)/(2*pi*L)`. Для `L = 10 mH` нуль лежить на ≈ 796 Hz, а полюс на ≈ 16.7 kHz замість ідеальних 15.9 kHz, бо в зріз тепер входить повний послідовний опір `R + r_L`. Нижче нуля характеристика не спадає далі, а виходить на плато ≈ 4.8%. На частоті 16.7 kHz амплітуда вже ≈ 0.707 від рівня смуги пропускання, а фаза не доходить до +90° на низьких частотах і прямує до 0° на постійному струмі.

**Чому не пропускає «будь-які» високі частоти.** Паралельна ємність `C_d` разом з індуктивністю утворює власний резонанс. Вище його частоти (self-resonant frequency, SRF) переважає ємнісний реактанс, і котушка поводиться як ємність.[^vishay-inductors-primer] Тому практична котушка придатна лише нижче цієї межі.[^fontys-passive-hf] На високих частотах також зростає ефективний опір обмотки через skin effect і втрати в осерді.[^kuphaldt-high-pass-filters] Отже, справжній ФВЧ на котушці має «вікно» між зрізом і резонансом котушки, а не нескінченну смугу пропускання. Окремо працює обмеження самого вимірювання: осцилограф і пробник мають власну смугу, на її межі сигнал уже спадає на 3 dB, а пробник додатково навантажує схему ємністю наконечника.[^tektronix-abcs-probes]

**Типові помилки:**

- Очікувати майже нуль на виході RL-ФВЧ на DC: реальна котушка має скінченний `r_L`, тож вихід є дільником, а не нулем.
- Не додавати `r_L` (і вихідний опір джерела) до `R` при розрахунку зрізу.
- Вважати спад АЧХ на дуже високих частотах помилкою схеми, хоча це може бути резонанс котушки або смуга пробника й осцилографа.

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
