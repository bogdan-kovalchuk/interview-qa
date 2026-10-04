---
id: emb-elee-0003
title: "Які знання з розділу 2 потрібні перед розділом 4?"
description: "Які знання з розділу 2 потрібні перед розділом 4?"
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
    applicability: "Походження питання: лекція 32, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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
  - source_id: udemy-course-sections-2-and-4
    title: "Udemy: Crash Course Electronics and PCB Design, course outline"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
    accessed: 2026-10-04
    kind: official
    version: null
    applicability: "Опублікована програма вступного розділу 2 та розділу 4 цього курсу; підтверджує навчальну послідовність, а не універсальні передумови для всіх курсів."
  - source_id: aac-series-parallel-method
    title: "All About Circuits: Solving Series and Parallel Circuits With the Table Method and Ohm's Law"
    url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-5/solving-series-and-parallel-circuits-with-the-table-method-and-ohms-law/
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: "Застосування закону Ома та правил послідовного й паралельного з’єднання для розрахунку струмів, напруг і опорів."
---

## Short answer

Перед переходом корисно впевнено знати напругу, струм, закон Ома `V = I*R` і базовий аналіз послідовних та паралельних кіл. Основи конденсаторів та індукторів і розрізнення DC/AC допоможуть у наступних темах, але розгорнутий аналіз реактивних кіл починається вже в розділі 4 курсу.[^aac-series-parallel-method] [^udemy-course-sections-2-and-4]

## Detailed explanation

Перед розділом 4 варто розуміти основні величини кола – напругу, струм, опір і потужність – та вміти пов’язати їх законом Ома. В описі вступного розділу 2 курсу є закон Ома й базовий аналіз кіл; розділ 4 далі спирається на ці поняття під час розгляду реактивних компонентів і AC.[^udemy-course-sections-2-and-4] [^aac-series-parallel-method]

Для резистивних DC-кіл потрібно розрізняти послідовне й паралельне з’єднання та співвідносити величини з конкретним елементом або ділянкою. Наприклад, у послідовному колі струм однаковий через усі резистори, а напруга джерела розподіляється між ними; у паралельному колі напруга на гілках однакова, а струми гілок додаються. Поширена помилка – підставити загальну напругу джерела та струм окремої гілки в одне рівняння `V = I*R`, хоча величини стосуються різних частин кола.[^aac-series-parallel-method]

Знання про конденсатор, індуктор і відмінність DC/AC корисні, але не потрібно наперед знати весь матеріал секції: у переліку розділу 4 є окремі лекції про конденсатори, індуктори, RC/RL-кола, фазори та імпеданс. Складніша математика потрібна поступово, коли з’являється AC-аналіз, а не для першої базової перевірки резистивної схеми.[^udemy-course-sections-2-and-4] [^aac-alternating-current]

**Приклад самоперевірки:**

Для ідеального джерела 9 V і резисторів 3 kΩ та 6 kΩ послідовно сумарний опір становить 9 kΩ, а струм – `I = 9 V / 9 kΩ = 1 mA`. Така проста оцінка допомагає помітити помилку в одиницях чи з’єднаннях до переходу до складніших моделей.[^aac-series-parallel-method]

## Sources

<!-- generated from frontmatter -->
