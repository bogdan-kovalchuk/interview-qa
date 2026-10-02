---
id: emb-elintro-0039
title: "Що таке валентний електрон і чому він важливий в електроніці?"
description: "Що таке валентний електрон і чому він важливий в електроніці?"
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
    applicability: "Походження питання: лекція 5, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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
  - source_id: openstax-semiconductor-doping
    title: "OpenStax University Physics Volume 3, 9.6 Semiconductors and Doping"
    url: https://openstax.org/books/university-physics-volume-3/pages/9-6-semiconductors-and-doping
    accessed: 2026-10-04
    kind: book
    version: "University Physics Volume 3"
    applicability: "Пояснює валентні електрони кремнію, електронні стани та вплив домішкового легування на носії заряду; приклади стосуються кремнієвого кристала."

  - source_id: aac-conductors-valence
    title: "All About Circuits: Introduction to Conductance and Conductors"
    url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-12/introduction-conductance-and-conductors/
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: "Пояснює роль валентних електронів і структури матеріалу; застерігає, що їх кількість сама по собі не визначає провідність."

---

## Short answer

Валентні електрони – це електрони зовнішньої оболонки атома, що беруть участь у хімічних зв’язках і впливають на електронні властивості матеріалу.[^aac-semiconductors] У кремнії чотири валентні електрони утворюють зв’язки в кристалічній ґратці; додавання домішок змінює кількість доступних носіїв заряду.[^openstax-semiconductor-doping] Але провідність не визначається лише кількістю валентних електронів – важливі також структура матеріалу й енергетичні стани.[^aac-conductors-valence]

## Detailed explanation

Валентними називають електрони зовнішньої електронної оболонки, які беруть участь у зв’язках між атомами. Їхня поведінка разом зі структурою речовини визначає, наскільки легко заряд може переноситися матеріалом.[^aac-conductors-valence]

У кристалі кремнію кожен атом має чотири валентні електрони й утворює ковалентні зв’язки з сусідніми атомами. За достатньої енергії електрон може перейти до стану, де він бере участь у провідності, залишаючи дірку у валентній зоні.[^openstax-semiconductor-doping]

Легування дає змогу цілеспрямовано змінювати концентрацію носіїв: донорні домішки додають електрони, а акцепторні сприяють появі дірок. Так керують властивостями напівпровідника в діодах і транзисторах.[^openstax-semiconductor-doping]

Приклад: атом фосфору має п’ять валентних електронів. У кремнієвій ґратці чотири з них беруть участь у зв’язках, а п’ятий слабше зв’язаний і може перейти в зону провідності за кімнатної температури.[^openstax-semiconductor-doping]

Саме можливість змінювати число рухомих носіїв робить домішки важливим інструментом схемотехніки. Різні ділянки одного кристала можна легувати по-різному, утворюючи області з різними електричними властивостями. На межі таких областей виникають переходи, поведінка яких лежить в основі діодів і транзисторів. Валентні електрони допомагають зрозуміти утворення зв’язків і перші носії, але не описують повністю геометрію приладу чи його роботу в колі.[^openstax-semiconductor-doping]

## Sources

<!-- generated from frontmatter -->
