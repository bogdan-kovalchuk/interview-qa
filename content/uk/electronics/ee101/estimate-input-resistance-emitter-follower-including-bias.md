---
id: emb-elee-0205
title: "Як оцінити вхідний опір емітерного повторювача з урахуванням подільника зміщення?"
description: "Як оцінити вхідний опір емітерного повторювача з урахуванням подільника зміщення?"
track: electronics
section: ee101
level: junior
type: concept
tags: []
status: published
updated: 2026-10-13
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
    applicability: "Походження питання: лекція 70, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-13; курс не є доказом цих тверджень."
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
  - source_id: fiore-common-collector-amplifier
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 7.4 Common Collector Amplifier"
    url: "https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/07:_BJT_Small_Signal_Amplifiers/7.4:_Common_Collector_Amplifier"
    accessed: 2026-10-13
    kind: book
    version: null
    applicability: "Розділ 7.4: емітерний повторювач – підсилення напруги близько одиниці, високий вхідний і низький вихідний опір, струмове підсилення; змінний опір в емітері r_E = R_E || R_L; Z_in(base) = β(r'_e + r_E), Z_in = R_B || Z_in(base), A_divider = Z_in/(Z_in + R_джерела); приклад з джерелом 1 кОм і навантаженням 500 Ом."
  - source_id: fiore-ac-model-bjt
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 7.2 Simplified AC Model of the BJT"
    url: "https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/07:_BJT_Small_Signal_Amplifiers/7.2:_Simplified_AC_Model_of_the_BJT"
    accessed: 2026-10-13
    kind: book
    version: null
    applicability: "Розділ 7.2: спрощена модель BJT для змінного сигналу; I_C = I_S*exp(38,6*V_BE) при 300 K; r'_e ≈ 26 мВ / I_C; у схемі зі спільним емітером фаза інвертується, у схемі зі спільним колектором – ні; модель для низьких і середніх частот."
---

## Short answer

Зі сторони бази вхід емітерного повторювача має опір `Z_in(base) = β*(r_e + r_E)`, де `r_E = R_E ∥ R_load` – змінний опір в емітері. При β = 100, r_e = 26 Ом і r_E = 1 кОм це ≈ 103 кОм. Резистори зміщення паралельні цьому входу: з еквівалентом 20 кОм загальний вхідний опір ≈ 16,7 кОм.[^fiore-common-collector-amplifier]

## Detailed explanation

Вхідний опір емітерного повторювача вимірюють зі сторони бази, бо саме туди подається сигнал і під’єднано подільник зміщення. Струм бази приблизно в β разів менший за струм емітера, тож опір в емітерному колі відбивається на базу з множником β: `Z_in(base) = β*(r_e + r_E)`, де `r_E = R_E ∥ R_load` – змінний опір в емітері.[^fiore-common-collector-amplifier] Тут `r_e` – динамічний опір емітерного переходу, `r_e ≈ 26 мВ / I_C`. Коли `I_C` близько 1 мА, `r_e` становить близько 26 Ом.[^fiore-ac-model-bjt]

Для прикладу візьмемо `β = 100`, `r_e = 26 Ом` і змінний опір в емітері `r_E = 1 кОм`. Тоді `Z_in(base) = 100*(26 + 1000)` ≈ 103 кОм. Резистори зміщення `R_B = R1 || R2` стоять паралельно до цього опору, тож `Z_in = R_B || Z_in(base)`. При `R_B = 20 кОм` маємо `Z_in = 1/(1/20000 + 1/102600)` ≈ 16,7 кОм.[^fiore-common-collector-amplifier] Подільник зміщення обмежує вхід: навіть при нескінченному β вхідний опір не може перевищити `R_B`.

Формула показує, від чого залежить результат. У повторювачі `R_E` шунтувати не можна: вихід знімають з емітера, і конденсатор замкнув би його на землю. Навантаження ж зменшує змінний опір в емітері, `r_E = R_E ∥ R_load`, а з ним і `Z_in(base)`; тому `R_E` у формулі означає саме змінний опір `R_E ∥ R_load`, а не номінал резистора.[^fiore-common-collector-amplifier] Вираз є наближенням для малого сигналу в області низьких і середніх частот.[^fiore-ac-model-bjt] Джерело з опором `R_S` не змінює `Z_in`, але разом з ним утворює подільник `Z_in/(Z_in + R_S)`, тому для точного розрахунку сигналу його треба враховувати окремо.[^fiore-common-collector-amplifier]

**Типові помилки:**

- Брати за `r_E` номінал `R_E`, ігноруючи паралельне навантаження, або забувати множник β чи паралельний `R_B`.
- Вважати, що великий β сам по собі гарантує великий вхідний опір: `R_B` тоді обмежує вхід згори.
- Не враховувати опір джерела при оцінці сигналу на вході.

## Sources

<!-- generated from frontmatter -->
