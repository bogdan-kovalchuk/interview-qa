---
id: emb-elintro-0053
title: "Три способи генерувати напругу – назвіть їх?"
description: "Три способи генерувати напругу – назвіть їх?"
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
    applicability: "Походження питання: лекція 7, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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
  - source_id: openstax-electromagnetic-induction
    title: "OpenStax Physics: Electromagnetic Induction"
    url: https://openstax.org/books/physics/pages/20-3-electromagnetic-induction
    accessed: 2026-10-04
    kind: book
    version: "Physics"
    applicability: "Пояснює виникнення emf через зміну магнітного потоку та приклади генератора й трансформатора; не є повним переліком фізичних способів створення напруги."
  - source_id: doe-solar-cell-basics
    title: "U.S. Department of Energy: Solar Photovoltaic Cell Basics"
    url: https://www.energy.gov/cmei/systems/solar-photovoltaic-cell-basics
    accessed: 2026-10-04
    kind: official
    version: null
    applicability: "Пояснює фотогальванічне перетворення у напівпровіднику; не стверджує, що всі сонячні елементи працюють лише на одному типі переходу."
---

## Short answer

Напругу можна отримати внаслідок електрохімічних реакцій у батареї, електромагнітної індукції в генераторі та фотогальванічного ефекту в сонячному елементі.[^openstax-electromagnetic-induction][^doe-solar-cell-basics] У фотоелементі поглинуте світло створює носії заряду, які розділяються всередині напівпровідникової структури; це не просто вибивання електронів «із P-N переходу».[^doe-solar-cell-basics]

## Detailed explanation

Напруга – це різниця електричного потенціалу між двома точками. Джерело створює її, розділяючи заряди або підтримуючи їх розділення за допомогою різного фізичного процесу. Три поширені приклади – електрохімічна батарея, генератор і сонячний елемент; це не вичерпний перелік, адже існують також термоелектричні та п’єзоелектричні джерела.[^openstax-electromagnetic-induction][^doe-solar-cell-basics]

У батареї хімічні реакції на електродах створюють різницю потенціалів. Під час розряду хімічна енергія перетворюється на електричну, а електрони рухаються зовнішнім колом; акумулятор відрізняється тим, що його хімічний стан можна відновлювати заряджанням у допустимих умовах.[^aac-direct-current]

У генераторі відносний рух провідника й магнітного поля змінює магнітний потік через контур. За законом Фарадея ця зміна індукує електрорушійну силу; якщо контур замкнений, вона може спричинити струм. Трансформатор також працює завдяки змінному магнітному потоку, але передає енергію між обмотками, а не створює її з механічної роботи.[^openstax-electromagnetic-induction]

У фотогальванічному елементі напівпровідник поглинає фотони, енергія яких може утворити рухомі електрони та дірки. Внутрішнє електричне поле структури розділяє носії заряду, а контакти дають змогу отримати напругу й струм у зовнішньому колі. Тому поширене формулювання про фотони, які «вибивають електрони з P-N переходу», неточне: світло збуджує носії в матеріалі, а поле сприяє їх розділенню.[^doe-solar-cell-basics]

Приклад: якщо обертати котушку в магнітному полі, магнітний потік через неї змінюється, і на її кінцях виникає напруга. Якщо залишити магніт і котушку нерухомими відносно одне одного та незмінними, потік не змінюється і така індукована напруга не виникає; саме рух або інша зміна потоку є суттєвою умовою.[^openstax-electromagnetic-induction]

## Sources

<!-- generated from frontmatter -->
