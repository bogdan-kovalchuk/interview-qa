---
id: emb-elee-0033
title: "До якої частки напруги джерела заряджається конденсатор за 1τ, 2τ, 3τ і 5τ?"
description: "До якої частки напруги джерела заряджається конденсатор за 1τ, 2τ, 3τ і 5τ?"
track: electronics
section: ee101
level: junior
type: concept
tags: []
status: published
updated: 2026-10-04
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
    applicability: "Походження питання: лекція 37, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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
  - source_id: gatech-rc-charging-discharging
    title: "Georgia Tech Physics Book: Charging and Discharging a Capacitor"
    url: https://physicsbook.gatech.edu/Charging_and_Discharging_a_Capacitor
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: "Експоненційний закон заряджання та частки кінцевої напруги за кратних τ в ідеальному RC-колі."
---

## Short answer

За `1τ`, `2τ`, `3τ` і `5τ` напруга ідеально заряджуваного конденсатора становить відповідно близько 63.2%, 86.5%, 95.0% і 99.3% кінцевої напруги. Після `5τ` лишається приблизно 0.7% різниці до кінцевого рівня, тому «практично заряджений» залежить від потрібного допуску.[^gatech-rc-charging-discharging]

## Detailed explanation

Для ідеального послідовного RC-кола, в якому незаряджений конденсатор під’єднано через резистор до сталої напруги `V_s`, напруга описується формулою `V_C(t) = V_s*(1 - e^(-t/τ))`, де `τ = R*C`. Якщо підставити час, виражений у кратних τ, частка кінцевої напруги залежить лише від експоненти, а не від конкретних номіналів резистора й конденсатора.[^gatech-rc-charging-discharging]

Наприклад, при `t = τ` маємо `1 - e^(-1)`, тобто приблизно 63.2%. При `2τ` це `1 - e^(-2)`, приблизно 86.5%; при `3τ` – приблизно 95.0%; при `5τ` – приблизно 99.3%. Відповідно, різниця між напругою конденсатора та кінцевою напругою джерела спадає як `e^(-t/τ)`. Саме тому кожний наступний однаковий проміжок часу зменшує залишкову похибку в однакове число разів, а не додає ту саму кількість відсоткових пунктів.[^gatech-rc-charging-discharging]

Ці частки стосуються напруги від початкового нуля до кінцевого значення. Якщо конденсатор уже мав початкову напругу, за `τ` він проходить 63.2% саме різниці між цим початковим рівнем і новим усталеним рівнем. У реальному колі значення також залежить від фактичних `R` і `C`, витоків, навантаження та того, наскільки добре модель одного RC-полюса описує схему.[^gatech-rc-charging-discharging]

Приклад для джерела 5 V: після `3τ` напруга буде приблизно `5 V*0.950 = 4.75 V`; після `5τ` – приблизно `5 V*0.993 = 4.965 V`. Отже, твердження «за `5τ` заряджено повністю» є практичним наближенням із залишком приблизно 35 mV у цьому прикладі, а не математично точним завершенням.[^gatech-rc-charging-discharging]

**Типові помилки:**

- Змішувати частку, яку вже набрала напруга, із часткою, якої ще бракує до кінцевого значення.
- Вважати `5τ` точним моментом повного заряджання замість домовленого рівня точності.
- Переносити наведені відсотки на коло з іншою початковою напругою без перерахунку відносно повного перепаду.

## Sources

<!-- generated from frontmatter -->
