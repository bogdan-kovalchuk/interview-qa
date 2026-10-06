---
id: emb-elee-0144
title: "Що таке динамічний опір стабілітрона `r_Z`?"
description: "Що таке динамічний опір стабілітрона `r_Z`?"
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
    applicability: "Походження питання: лекція 58, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-06; курс не є доказом цих тверджень."
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
  - source_id: nexperia-an90031
    title: "Nexperia AN90031: Zener diodes – physical basics, parameters and application examples"
    url: https://assets.nexperia.com/documents/application-note/AN90031.pdf
    accessed: 2026-10-06
    kind: official
    version: "Rev. 3.0, 7 June 2023"
    applicability: "Реальна характеристика стабілітрона в пробої не вертикальна, динамічний опір R_dyn = ΔV_Z/ΔI_Z більший за нуль; диференційний опір r_dif = ΔV_Z/ΔI_Z – крутизна кривої V_Z–I_Z, ідеал – 0 Ом; мінімальний струм стабілітрона приблизно 5 мА для діодів до 17 В; дані наведено для серій Nexperia, інші виробники можуть мати інші числа."
  - source_id: nexperia-bzx84
    title: "Nexperia BZX84 series: voltage regulator diodes (datasheet)"
    url: https://assets.nexperia.com/documents/data-sheet/BZX84_SER.pdf
    accessed: 2026-10-06
    kind: official
    version: "Rev. 7, 1 January 2023"
    applicability: "Максимальний r_dif при T_j = 25 °C: для 5,1 В (BZX84-C5V1) 480 Ом при 1 мА і 60 Ом при 5 мА, для 6,2 В – 150 Ом при 1 мА і 10 Ом при 5 мА; значення для цієї серії, а не для всіх стабілітронів."
---

## Short answer

Динамічний (диференційний) опір `r_Z = ΔV_Z/ΔI_Z` – крутизна характеристики стабілітрона в пробої в даній робочій точці, тож для малих змін `ΔV_Z ≈ r_Z*ΔI_Z`.[^nexperia-an90031] Він не нульовий і залежить від струму: для BZX84-C5V1 максимум 480 Ом при 1 мА і 60 Ом при 5 мА.[^nexperia-bzx84] Через `r_Z` вихід простого стабілізатора трохи змінюється зі струмом навантаження й вхідною напругою, і чим менший `r_Z`, тим стабільніший вихід.

## Detailed explanation

**Звідки береться `r_Z`.** Ідеальний стабілітрон тримав би `V_Z` сталою, хоч який струм через нього йде. Реальна вольт-амперна характеристика в пробої не вертикальна, тож напруга трохи зростає зі струмом, і динамічний опір `R_dyn = ΔV_Z/ΔI_Z` більший за нуль.[^nexperia-an90031] У datasheet його позначають `r_dif` і описують як крутизну кривої `V_Z–I_Z`: чим крутіша крива, тим менший опір і стабільніша напруга.[^nexperia-an90031] Для малих відхилень від робочої точки звідси `ΔV_Z ≈ r_Z*ΔI_Z`. Для великих змін струму лінійна модель уже не годиться.

**Це не `V_Z/I_Z`.** Динамічний опір – нахил характеристики, а не відношення напруги до струму в точці. Для BZX84-C5V1 при 5 мА статичне відношення дорівнює `5.1/0.005 ≈ 1.02 kΩ`, а максимальний `r_dif` при цьому струмі – лише 60 Ом.[^nexperia-bzx84] Різниця щонайменше в 17 разів. Для наближення `ΔV_Z ≈ r_Z*ΔI_Z` потрібен саме `r_dif`.

**Залежність від струму й типу.** `r_Z` не є константою діода. Для BZX84-C5V1 максимум становить 480 Ом при 1 мА і 60 Ом при 5 мА, тобто при меншому струмі крива положистіша.[^nexperia-bzx84] Для 6,2 В у тій самій серії максимум при 5 мА – лише 10 Ом.[^nexperia-bzx84] Тому в Nexperia радять тримати мінімальний струм стабілітрона приблизно 5 мА (для діодів до 17 В), щоб він працював на крутій ділянці.[^nexperia-an90031] Усі ці числа – максимуми для конкретної серії при `T_j = 25 °C`; значення для вашого діода й струму беруть із його datasheet.

**Вплив у стабілізаторі.** У схемі з резистором `R` послідовно й навантаженням паралельно стабілітрону зміна `V_in` або струму навантаження перерозподіляє струм і змінює `V_out` на `r_Z*ΔI_Z`. Для малих змін із простої лінійної моделі `ΔV_out/ΔV_in = r_Z/(R + r_Z)`. При `R = 390 Ом` і `r_Z = 60 Ом` це `60/450 ≈ 0.13`: зміна входу на 1 В дає до ≈ 133 мВ на виході. Для `r_Z = 480 Ом` було б `480/870 ≈ 0.55`. Докладніше про line і load regulation – у `qid:emb-elee-0141`.

**Типові помилки:**

- Плутати `r_Z` зі статичним відношенням `V_Z/I_Z`: ≈ 1.02 kΩ проти ≤ 60 Ом у прикладі.
- Вважати `r_Z` сталою величиною діода й брати значення для іншого струму, ніж у схемі.
- Застосовувати `ΔV_Z ≈ r_Z*ΔI_Z` до великих змін струму або поза пробоєм.

## Sources

<!-- generated from frontmatter -->
