---
id: emb-elee-0150
title: "Навіщо в діодній схемі bleeder-резистор паралельно конденсатору?"
description: "Навіщо в діодній схемі bleeder-резистор паралельно конденсатору?"
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
    applicability: "Походження питання: лекція 59, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-06; курс не є доказом цих тверджень."
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
  - source_id: kuphaldt-bleeder-supply
    title: "Workforce LibreTexts: Electric Circuits VI – Experiments (Kuphaldt), 5.19 Vacuum Tube Audio Amplifier"
    url: "https://workforce.libretexts.org/Bookshelves/Electronics_Technology/Electric_Circuits_VI_-_Experiments_(Kuphaldt)/05:_Discrete_Semiconductor_Circuits/5.19:_Vacuum_Tube_Audio_Amplifier"
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "У схемі блока живлення з фільтрувальним конденсатором резистор 100 кОм паралельно конденсатору дає йому шлях розряду після вимкнення змінної напруги; без нього конденсатор, імовірно, довго тримав би небезпечний заряд. Приклад 47 мкФ і 100 кОм дає сталу часу 4,7 с, а більший конденсатор потребує меншого резистора або довшого очікування. Книга описує конкретний навчальний експеримент, а не норми безпеки."
  - source_id: vishay-pre-charge-bleed
    title: "Vishay: Pre-charge resistor and bleed resistor selection (Did You Know?, MS8772259-1810)"
    url: https://www.vishay.com/docs/48468/_ms8772259-1810-didyouknow-rs_rh-nh.pdf
    accessed: 2026-10-06
    kind: official
    version: "MS8772259-1810, 2018"
    applicability: "Одне речення про те, що bleed-резистор безпечно розряджає конденсатори інвертора, коли пристрій не працює (гібридні й електричні автомобілі), та перелік параметрів для вибору такого резистора. Документ не наводить формул і значень опору."
  - source_id: fiore-rectification
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 3.2 Rectification"
    url: "https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/03:_Diode_Applications/3.2:_Rectification"
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "Конденсатор у випрямлячі заряджається, поки діод проводить, а коли діод закривається, розряджається в навантаження; за легкого навантаження вихід тримається біля піка вторинної напруги з малими пульсаціями. Книга не розглядає bleeder-резистор окремо."
  - source_id: fiore-peak-detector
    title: "Engineering LibreTexts: Operational Amplifiers and Linear Integrated Circuits (Fiore), 7.2 Precision Rectifiers"
    url: "https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Operational_Amplifiers_and_Linear_Integrated_Circuits_-_Theory_and_Application_(Fiore)/07:_Nonlinear_Circuits/7.02:_Precision_Rectifiers"
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "Піковий детектор на операційних підсилювачах: після піка діод закривається, конденсатор розряджається через опір, стала розряду задає, наскільки довго тримається пік; за довгої сталої вихід майже постійний, за коротшої він повторює огинальну; витоки конденсатора обмежують найбільший опір розряду. Схема з операційними підсилювачами, а не звичайний мережевий випрямляч."
  - source_id: gatech-rc-charging-discharging
    title: "Georgia Tech Physics Book: Charging and Discharging a Capacitor"
    url: https://physicsbook.gatech.edu/Charging_and_Discharging_a_Capacitor
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "Розряд конденсатора через резистор: стала часу τ = R*C, заряд Q(t) = Q0*e^(-t/(R*C)), тож напруга спадає за тим самим експоненційним законом; ідеальне RC-коло без додаткового навантаження й витоків."
---

## Short answer

Bleeder-резистор дає конденсатору шлях розряду, бо діод не пропускає струм назад: без нього заряджений конденсатор довго тримає напругу після вимкнення живлення, що небезпечно, і повільно слідує за зниженням вхідної пікової напруги.[^kuphaldt-bleeder-supply][^fiore-peak-detector] Наприклад, 100 кОм і 1 мкФ дають `τ = R*C = 0,1 с`; через `5τ` лишається ≈ 0,67% початкової напруги.[^gatech-rc-charging-discharging] Ціна – постійна потужність, що розсіюється на резисторі.

## Detailed explanation

Діод пропускає струм лише в один бік. У схемі «діод плюс конденсатор» (випрямляч із фільтром або піковий детектор) конденсатор заряджається до піка вхідної напруги, а коли вхід падає нижче напруги на конденсаторі, діод закривається. Відтоді розрядити конденсатор можуть лише навантаження й власні витоки.[^fiore-rectification] Тому за легкого навантаження вихід тримається біля піка з малими пульсаціями, а без навантаження напруга спадає дуже повільно, обмежена тільки витоками.[^fiore-rectification][^fiore-peak-detector]

Bleeder-резистор паралельно конденсатору створює гарантований шлях розряду. Перша причина – безпека: у блоці живлення такий резистор розряджає фільтрувальний конденсатор після вимкнення мережі, інакше конденсатор міг би довго тримати небезпечний заряд.[^kuphaldt-bleeder-supply] У високовольтних системах (наприклад, інвертори електромобілів) роль та сама – безпечно розрядити конденсатори, коли пристрій не працює.[^vishay-pre-charge-bleed] Друга причина функціональна: у піковому детекторі або випрямлячі з майже відсутнім навантаженням саме стала розряду визначає, як швидко вихід реагує на зниження амплітуди входу; за довгої сталої вихід майже постійний, за коротшої він повторює огинальну.[^fiore-peak-detector]

Швидкість розряду описує `V(t) = V0*e^(-t/(R*C))`, `τ = R*C`.[^gatech-rc-charging-discharging] Для 100 кОм і 1 мкФ `τ = 10^5 * 10^-6 = 0,1 с`, а через `5τ = 0,5 с` лишається `e^-5 ≈ 0,0067`, тобто ≈ 0,67% початкової напруги. Експеримент Kuphaldt: 47 мкФ і 100 кОм дають `τ = 4,7 с`; більший конденсатор потребує меншого резистора або довшого очікування.[^kuphaldt-bleeder-supply]

**Приклад компромісу.** Випрямлена мережа 230 В RMS дає пік `230*√2 ≈ 325 В`. Для конденсатора 1000 мкФ і резистора 100 кОм `τ = 100 с`, а до 50 В (рівень узято для прикладу, це не норма) напруга спадає за `t = τ*ln(325/50) ≈ 100*1,87 ≈ 187 с`, тобто приблизно 3 хвилини. Водночас на резисторі постійно розсіюється `P = V²/R = 325²/10^5 ≈ 1,06 Вт`. Менший опір розряджає швидше, але гріється й марнує енергію весь час, поки пристрій працює; резистор вибирають і за потужністю, і за робочою напругою.

**Типові помилки:**

- Вважати bleeder гарантією безпеки: резистор може вийти з ладу, тому перед обслуговуванням напругу на конденсаторі вимірюють.
- Брати занадто малий опір (великі втрати й нагрівання) або занадто великий (розряд триває хвилинами).
- Думати, що розряд закінчується точно за `5τ`: експонента лише наближається до нуля, і лишається ≈ 0,67%.

## Sources

<!-- generated from frontmatter -->
