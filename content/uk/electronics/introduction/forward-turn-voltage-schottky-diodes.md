---
id: emb-elintro-0163
title: "Яка пряма напруга відкриття для Si, Ge і Шотткі-діода?"
description: "Яка пряма напруга відкриття для Si, Ge і Шотткі-діода?"
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
  - source_id: aac-pn-junction
    title: "All About Circuits: The P-N Junction"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/chpt-2/the-p-n-junction/
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: "Надає типові значення прямої напруги для Si й Ge P-N переходів та пояснює, чому падіння залежить від характеристики переходу; не задає гарантованих значень для довільних компонентів."
  - source_id: st-an4789
    title: "STMicroelectronics AN4789: Monolithic Schottky diode in ST F7 LV MOSFET technology"
    url: https://www.st.com/resource/en/application_note/an4789-monolithic-schottky-diode-in-st-f7-lv-mosfet-technology-improving-application-performance-stmicroelectronics.pdf
    accessed: 2026-10-04
    kind: official
    version: "Rev 1"
    applicability: "Описує нижче типове падіння Schottky у конкретному контексті інтегрованого 60 V MOSFET; не є універсальним специфікаційним значенням для всіх діодів."
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), картки курсу"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
    accessed: 2026-09-27
    kind: community
    version: null
    applicability: "Походження питання: лекція 16, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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
---

## Short answer

Для звичайних P-N діодів орієнтир прямої напруги становить 0.6–0.7 V для Si та близько 0.2 V для Ge; Schottky часто має менше падіння, близько 0.3 V у наведеному виробником прикладі. Це типові орієнтири, а не сталі пороги: значення залежить від струму, температури й конкретного компонента.[^aac-pn-junction][^st-an4789]

## Detailed explanation

Пряму напругу діода не можна визначити лише за назвою матеріалу: це напруга на компоненті за конкретного прямого струму, а не незмінний поріг перемикання. У звичайному P-N діоді електрони й дірки інжектуються через перехід, тому характеристика струму швидко зростає зі збільшенням прямої напруги. Для навчальних розрахунків часто беруть приблизно 0.6–0.7 V для кремнієвого переходу та близько 0.2 V для германієвого, але ці числа залежать від робочої точки.[^aac-pn-junction]

У Schottky контакт утворюється між металом і напівпровідником. У ньому перенесення струму переважно пов’язане з majority carriers, тож накопичується менше заряду, а пряме падіння в багатьох застосуваннях нижче, ніж у звичайного Si P-N діода. Значення близько 0.3 V зустрічається в прикладі ST для інтегрованого Schottky в конкретному 60 V MOSFET; його не можна переносити на кожен компонент без перевірки datasheet.[^st-an4789]

Для LED колір дає лише грубе уявлення про енергію випромінюваного фотона й часто корелює з більшим прямим падінням для короткохвильового світла. Проте точні `V_F` і струм треба брати з datasheet конкретного LED, оскільки впливають матеріал, струм і температура. LED – не просто звичайний червоний чи синій P-N діод: його склад і робоча точка визначають характеристику.[^aac-pn-junction]

Наприклад, якщо в розрахунку послідовного кола для Si діода припустити падіння 0.65 V, це лише наближення для оцінювання струму; остаточно треба звірити напругу за кривою або таблицею datasheet при потрібному струмі й температурі. Не слід додавати таке падіння як жорстку напругу ввімкнення, нижче якої струм завжди нульовий.[^aac-pn-junction]

**Типові помилки:**
- Вважати числа 0.7 V, 0.3 V або 0.2 V універсальними для всіх компонентів відповідного типу.
- Порівнювати прямі напруги без зазначення струму та температури.
- Вибирати `V_F` LED лише за кольором і не перевіряти datasheet.[^aac-pn-junction][^st-an4789]

## Sources

<!-- generated from frontmatter -->
