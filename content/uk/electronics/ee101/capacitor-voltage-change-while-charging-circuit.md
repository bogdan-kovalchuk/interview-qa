---
id: emb-elee-0031
title: "Як змінюється напруга на конденсаторі під час заряджання в RC-колі?"
description: "Як змінюється напруга на конденсаторі під час заряджання в RC-колі?"
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
    applicability: "Виведення експоненційних законів заряджання та розряджання і визначення τ=RC для простого послідовного RC-кола з ідеальними R і C."
---

## Short answer

Для незарядженого конденсатора, під’єднаного до сталої напруги `V_s` через резистор, `V_C(t) = V_s*(1 - e^(-t/τ))`, де `τ = R*C`. Напруга зростає експоненційно й наближається до `V_s`, але в ідеальній моделі не досягає його за скінченний час.[^gatech-rc-charging-discharging]

## Detailed explanation

Уявімо послідовне коло зі сталою напругою джерела `V_s`, резистором `R` та спочатку незарядженим конденсатором `C`. На початку напруга конденсатора дорівнює нулю, тому майже вся напруга джерела прикладена до резистора й струм найбільший. Коли на обкладинках накопичується заряд, напруга конденсатора зростає та протидіє джерелу; напруга на резисторі й струм поступово зменшуються.[^gatech-rc-charging-discharging]

Для такого ідеального кола закон напруги має вигляд `V_C(t) = V_s*(1 - e^(-t/(R*C)))`. Добуток `R*C` задає часовий масштаб процесу. Експонента описує не лінійний приріст: на початку крива крута, далі її нахил меншає, бо різниця між напругою джерела й напругою конденсатора стає меншою. Після тривалого часу струм прямує до нуля, а напруга конденсатора прямує до `V_s`.[^gatech-rc-charging-discharging]

Ця формула передбачає одне стале джерело, один резистор і конденсатор сталої ємності, без суттєвих витоків та інших елементів. Для іншої початкової напруги треба рахувати зміну від початкового стану до нового усталеного рівня, а не вважати, що конденсатор завжди починає з нуля. У складнішому колі для `τ` використовують опір, який бачить конденсатор у відповідному перехідному режимі.[^gatech-rc-charging-discharging]

Приклад: для `V_s = 5 V`, `R = 10 kΩ` і `C = 10 µF` маємо `τ = 0.1 s`. За `t = τ` напруга становить приблизно 63.2% від кінцевих 5 V, тобто близько 3.16 V. Це не означає, що за одну τ конденсатор «зарядився на 63.2% від поточного значення»: відсоток відраховується від повної зміни від початкового рівня до кінцевого.[^gatech-rc-charging-discharging]

**Типові помилки:**

- Малювати лінійний графік або стверджувати, що конденсатор досягає кінцевої напруги точно за `τ`.
- Застосовувати формулу до ненульової початкової напруги без урахування початкового стану.
- Плутати напругу конденсатора з напругою на резисторі: під час заряджання перша зростає, а друга спадає.

## Sources

<!-- generated from frontmatter -->
