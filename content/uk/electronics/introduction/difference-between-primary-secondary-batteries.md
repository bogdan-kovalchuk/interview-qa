---
id: emb-elintro-0054
title: "Яка різниця між первинними і вторинними батареями?"
description: "Яка різниця між первинними і вторинними батареями?"
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
  - source_id: doe-primary-secondary-batteries
    title: "U.S. Department of Energy: Primer on Lead-Acid Storage Batteries"
    url: https://www.energy.gov/documents/doe-hdbk-1084-95
    accessed: 2026-10-04
    kind: official
    version: "DOE-HDBK-1084-95"
    applicability: "Наводить визначення первинних і вторинних батарей за можливістю заряджання; опис хімії та експлуатаційних меж стосується конкретних батарей і не робить будь-яку первинну батарею безпечною для заряджання."
---

## Short answer

Первинні батареї не призначені для повторного заряджання; вторинні батареї, або акумулятори, можна заряджати струмом у зворотному напрямку за умов, визначених виробником.[^doe-primary-secondary-batteries] Приклади первинних елементів – лужні AA та цинково-вуглецеві; вторинних – NiMH і Li-ion.[^doe-primary-secondary-batteries]

## Detailed explanation

Поділ на первинні й вторинні батареї стосується передусім того, чи передбачене їхнє повторне заряджання. У первинному елементі розряд витрачає реагенти так, що повернути його до робочого зарядженого стану звичайним пропусканням струму у зворотному напрямку не призначено. Такий елемент після вичерпання корисної ємності замінюють і утилізують належним способом.[^doe-primary-secondary-batteries]

У вторинному елементі електричний струм під час заряджання спрямовують так, щоб відновити заряджений стан хімічної системи. Це не означає, що батарея відновлюється безмежно: цикли заряджання й розряджання поступово зношують її, а допустимі напруга, струм, температура та алгоритм заряджання залежать від хімічного складу й конкретної моделі. Для Li-ion, наприклад, потрібен сумісний контроль заряджання; твердження «будь-яку батарею можна перезарядити» небезпечне.[^doe-primary-secondary-batteries]

До типових первинних побутових елементів належать лужні AA та цинково-вуглецеві елементи. Поширені вторинні хімічні системи – NiMH і Li-ion. Формат корпуса сам по собі не визначає тип: батареї однакового розміру можуть мати різну хімію, номінальну напругу та допустимий режим заряджання, тому потрібно перевіряти маркування виробника.[^doe-primary-secondary-batteries]

Приклад: звичайну лужну AA-батарейку не підключають до зарядного пристрою для NiMH AA лише тому, що вони мають однаковий розмір. Для заряджання важлива хімія та відповідний зарядний режим. Акумулятор NiMH можна заряджати сумісним зарядним пристроєм, проте строк служби й доступна ємність залежать від режиму використання.[^doe-primary-secondary-batteries]

## Sources

<!-- generated from frontmatter -->
