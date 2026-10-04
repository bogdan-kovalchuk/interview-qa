---
id: emb-elee-0034
title: "Як змінюється напруга на конденсаторі під час розряджання через резистор?"
description: "Як змінюється напруга на конденсаторі під час розряджання через резистор?"
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
    applicability: "Закон експоненційного розряджання та струм у резистивному контурі для ідеального RC-кола."
---

## Short answer

Якщо заряджений конденсатор розряджається через резистор, його напруга спадає за законом `V_C(t) = V_0*e^(-t/τ)`, де `τ = R*C` для простого RC-контуру. Після `1τ`, `3τ` і `5τ` залишається відповідно близько 36.8%, 5.0% і 0.7% початкової напруги.[^gatech-rc-charging-discharging]

## Detailed explanation

Розгляньмо конденсатор, який спочатку заряджений до напруги `V_0` і під’єднаний до резистора без джерела в замкненому контурі. Напруга конденсатора створює струм через резистор. У міру відтоку заряду напруга зменшується, а отже зменшується й струм; цей взаємозв’язок приводить до експоненційного, а не лінійного спаду.[^gatech-rc-charging-discharging]

Для ідеального резистора `R` та конденсатора `C` напруга дорівнює `V_C(t) = V_0*e^(-t/(R*C))`. Постійна часу `τ = R*C` визначає швидкість спаду. Після кожної τ напруга стає приблизно 36.8% від значення на початку відповідного інтервалу: після першої τ залишається 36.8% від `V_0`, після другої – 36.8% від того залишку, тобто близько 13.5% від `V_0`.[^gatech-rc-charging-discharging]

Напруга в ідеальній моделі наближається до нуля асимптотично. Тому слова «розрядився» зазвичай означають, що напруга впала нижче заданого порога, а не стала математично рівною нулю. У реальному пристрої також можуть бути інші шляхи струму, навантаження чи захисні компоненти, тож часову сталу визначає опір, який бачить конденсатор у фактичному контурі розряду.[^gatech-rc-charging-discharging]

Приклад: конденсатор із `V_0 = 10 V`, `R = 100 kΩ` і `C = 10 µF` має `τ = 1 s`. Через 3 s напруга становить `10 V*e^(-3)`, приблизно 0.50 V, тобто близько 5% початкової. Цей розрахунок передбачає незмінні `R` і `C` та відсутність додаткових струмів витоку.[^gatech-rc-charging-discharging]

**Типові помилки:**

- Використовувати закон заряджання зі знаком «мінус» у показнику замість закону спадання від початкової напруги.
- Казати, що після `τ` напруга впала на 36.8%; насправді вона впала приблизно на 63.2% і зберегла 36.8%.
- Плутати напрямок струму розряду з умовним напрямком струму заряджання.

## Sources

<!-- generated from frontmatter -->
