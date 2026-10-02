---
id: emb-elintro-0110
title: "Чому навантаження змінює напругу подільника?"
description: "Чому навантаження змінює напругу подільника?"
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
    applicability: "Походження питання: лекція 11, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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
  - source_id: aac-voltage-divider
    title: "All About Circuits: Voltage Dividers: What They Are and What They Do"
    url: https://www.allaboutcircuits.com/technical-articles/voltage-and-current-dividers-what-they-are-and-what-they-do/
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: "Підтверджує поділ напруги пропорційно опорам; навантажену схему слід аналізувати з еквівалентним опором паралельної гілки."
---

## Short answer

Навантаження, підключене від виходу до спільного проводу, стоїть паралельно нижньому резистору та зменшує еквівалентний опір цієї гілки. Через це вихідна напруга зазвичай нижча, ніж у незавантаженому подільнику; величина зміни залежить від опору навантаження.[^aac-voltage-divider]

## Detailed explanation

У незавантаженому подільнику нижній резистор `R2` є єдиним шляхом струму від вихідного вузла до спільного проводу. Коли навантаження `R_L` під’єднують до виходу, воно утворює паралельну гілку з `R2`. Еквівалентний опір цієї гілки стає меншим за `R2`, тож через `R1` тече більший струм, а більша частка вхідної напруги падає на верхньому резисторі. Вихідна напруга зменшується; це звичайний наслідок навантаження джерела з ненульовим вихідним опором, а не несправність подільника.[^aac-voltage-divider]

Розрахунок роблять, замінивши пару `R2` і `R_L` їхнім паралельним еквівалентом `R_eq = R2*R_L/(R2 + R_L)`, а потім застосувавши формулу подільника: `V_out = V_in*R_eq/(R1 + R_eq)`. Наприклад, за `V_in = 10 V`, `R1 = 10 kΩ`, `R2 = 10 kΩ` без навантаження вихід дорівнює 5 V. Якщо `R_L = 10 kΩ`, то `R_eq = 5 kΩ`, а `V_out` становить приблизно 3.33 V. Усі значення тут ідеальні; фактичні допуски резисторів можуть дещо змінити результат.[^aac-voltage-divider]

Якщо опір навантаження набагато більший за `R2`, його вплив малий і виміряна напруга близька до розрахунку без навантаження. Коли `R_L` порівнянний із `R2` або менший за нього, вплив уже суттєвий. Сам вольтметр також є навантаженням: його скінченний вхідний опір підключений паралельно `R2`, хоча в багатьох схемах він достатньо великий, щоб похибкою можна було знехтувати.[^aac-voltage-divider]

Типова помилка – вважати, що вихід визначається лише номіналами двох резисторів незалежно від того, що до нього під’єднано. Щоб уникнути її, намалюйте навантаження між виходом і спільним вузлом та включіть його опір у паралельну еквівалентну гілку. Для живлення навантаження зі значним або змінним струмом подільник часто замінюють буфером чи стабілізатором, які краще утримують вихідну напругу.[^aac-voltage-divider]

## Sources

<!-- generated from frontmatter -->
