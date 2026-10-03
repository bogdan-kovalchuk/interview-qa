---
id: emb-elintro-0204
title: "Як розрахувати `I_B` через базовий резистор?"
description: "Як розрахувати базовий струм через базовий резистор?"
track: electronics
section: introduction
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
    applicability: "Походження питання: лекція 19, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
  - source_id: aac-direct-current
    title: "All About Circuits textbook, Volume I: DC"
    url: https://www.allaboutcircuits.com/textbook/direct-current/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: DC-кола, закон Ома, закони Кірхгофа, джерела й вимірювання; конкретні номінали й схеми курсу можуть відрізнятися."
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: діоди, стабілітрони, біполярні й польові транзистори та джерела живлення; конкретні номінали й схеми курсу можуть відрізнятися."
  - source_id: aac-ohms-law
    title: "Ohm’s Law – How Voltage, Current, and Resistance Relate, All About Circuits"
    url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-2/voltage-current-resistance-relate/
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: "Закон Ома для струму через резистор; застосування формули до базового кола потребує врахувати падіння на переході та топологію кола."
---

## Short answer

Якщо емітер під’єднаний до 0 V, а джерело керування подає `V_in` через `R_B`, то `I_B ≈ (V_in - V_BE)/R_B`. Для `V_in = 5 V`, `R_B = 3.3 kΩ` і припущення `V_BE = 0.7 V` маємо `I_B ≈ 1.3 mA`; фактичне `V_BE` залежить від транзистора та струму.[^aac-ohms-law]

## Detailed explanation

Струм бази в простому колі з одним резистором обчислюють із закону Ома: напруга на резисторі, поділена на його опір. Якщо емітер NPN заземлений, один кінець `R_B` під’єднаний до джерела `V_in`, а другий – до бази, то приблизно `I_B = (V_in - V_BE)/R_B`. Тут від напруги джерела віднімають падіння між базою та емітером, бо саме решта напруги припадає на резистор.[^aac-ohms-law]

Формула передбачає, що джерело має відоме вихідне значення, емітер має вказаний опорний потенціал, а перехід база–емітер проводить у прямому напрямку. Якщо емітер не на землі, треба використовувати напругу відносно нього. Якщо між джерелом та резистором є вихідний опір або інші елементи, їх також враховують у повному колі; не можна просто підставити напругу джерела замість фактичної напруги на резисторі.[^aac-ohms-law]

Для прикладу з `V_in = 5 V`, `V_BE = 0.7 V` та `R_B = 3.3 kΩ` напруга на резисторі близько 4.3 V. Розрахунок дає `4.3 V / 3300 Ω ≈ 0.00130 A`, тобто приблизно 1.3 mA. Значення 0.7 V є наближенням для кремнієвого переходу: воно залежить від струму, температури та компонента. Для точнішого проєктування використовують умови datasheet або модель транзистора.[^aac-ohms-law]

Розрахунок базового струму – лише частина вибору резистора. Потрібно перевірити, чи керувальне джерело може віддати цей струм, чи не перевищено граничні параметри входу, та який струм навантаження треба комутувати. Для ключа базовий струм зазвичай задають із запасом відносно мінімального коефіцієнта підсилення, щоб транзистор надійно перейшов у saturation.[^aac-ohms-law]

**Типова помилка:** використовувати `V_in/R_B` і забувати падіння `V_BE`, або автоматично вважати емітер заземленим. Спочатку визначте напругу на обох кінцях резистора, а потім застосуйте закон Ома.

## Sources

<!-- generated from frontmatter -->
