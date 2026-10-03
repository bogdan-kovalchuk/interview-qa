---
id: emb-elcirc-0003
title: "Як знайти опір резистора, якщо задано бажаний струм і напругу джерела?"
description: "Як знайти опір резистора, якщо задано бажаний струм і напругу джерела?"
track: electronics
section: circuit-analysis
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
    applicability: "Походження питання: лекція 27, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
  - source_id: aac-direct-current
    title: "All About Circuits textbook, Volume I: DC"
    url: https://www.allaboutcircuits.com/textbook/direct-current/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: DC-кола, закон Ома, закони Кірхгофа, джерела й вимірювання; конкретні номінали й схеми курсу можуть відрізнятися."
  - source_id: aac-ohms-law
    title: "All About Circuits: Ohm's Law - How Voltage, Current, and Resistance Relate"
    url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-2/voltage-current-resistance-relate/
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: "Підтверджує закон Ома для резистивних кіл; не враховує напругу на інших послідовних компонентах."
  - source_id: aac-resistor-power
    title: "All About Circuits: Resistors"
    url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-2/resistors/
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: "Пояснює розрахунок потужності резистора та потребу вибрати достатню потужність з урахуванням умов охолодження."
---

## Short answer

Для ідеального резистора, під’єднаного безпосередньо до джерела, `R = V/I`.[^aac-ohms-law] За `V = 10.5 V` та `I = 25 mA` маємо `R = 420 Ω`, а потужність становить `P = V*I = 0.2625 W`; виберіть номінал потужності з належним запасом для температури й охолодження.[^aac-resistor-power]

## Detailed explanation

Щоб знайти опір, застосуйте закон Ома: для резистора `R = V/I`, де `V` – напруга саме на резисторі, а `I` – струм крізь нього. Якщо резистор під’єднаний безпосередньо до ідеального джерела, напруга на ньому дорівнює напрузі джерела. У колі зі світлодіодом, лампою чи іншим послідовним елементом треба відняти падіння напруги на цьому елементі: резистор не отримує всю напругу живлення.[^aac-ohms-law]

Перед обчисленням приведіть величини до узгоджених одиниць. Міліампер потрібно перетворити на ампер, а результат опору зручно записати в омах або кілоомах. Наприклад, для резистора без інших послідовних елементів, джерела 10.5 V і потрібного струму 25 mA розрахунок такий:

```text
I = 25 mA = 0.025 A
R = 10.5 V / 0.025 A = 420 Ω
P = 10.5 V * 0.025 A = 0.2625 W
```

Отже, ідеальне значення опору – 420 Ω. У реальному колі перевірте найближчий доступний номінал, допуск резистора та зміну струму від напруги джерела: вибір найближчого значення може дати струм трохи вище або нижче бажаного. Для світлодіода в чисельнику буде `V_supply - V_f`, а не вся напруга джерела.[^aac-ohms-law]

Потужність не визначає потрібний опір, але визначає, чи витримає компонент нагрівання. Після знаходження струму обчисліть `P = V*I` або `P = I²*R`, використовуючи напругу саме на резисторі. Номінальна потужність резистора є максимально допустимою за умов, зазначених виробником; висока температура довкілля, слабке охолодження та близькість до граничного режиму вимагають запасу або перевірки derating у документації компонента.[^aac-resistor-power]

**Типові помилки:**

- Підставити 25 замість 0.025 у формулу, отримавши відповідь у тисячу разів меншою.
- Використати напругу джерела, хоча частина її падає на послідовному навантаженні.
- Обрати резистор лише за опором і не перевірити його потужність та теплові умови.

## Sources

<!-- generated from frontmatter -->
