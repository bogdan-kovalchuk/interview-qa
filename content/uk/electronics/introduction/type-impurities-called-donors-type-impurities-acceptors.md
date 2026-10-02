---
id: emb-elintro-0040
title: "Чому домішки N-типу називають донорами, а P-типу – акцепторами?"
description: "Чому домішки N-типу називають донорами, а P-типу – акцепторами?"
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
    applicability: "Пояснює донорні й акцепторні домішки на прикладах атомів із п’ятьма або трьома валентними електронами в ґратці кремнію."

---

## Short answer

У кремнії домішка з п’ятьма валентними електронами може віддати слабко зв’язаний п’ятий електрон для провідності, тому її називають донорною; матеріал стає `n`-типу.[^openstax-semiconductor-doping] Домішка з трьома валентними електронами може прийняти електрон для заповнення зв’язку, залишаючи рухому дірку, тому її називають акцепторною; матеріал стає `p`-типу.[^openstax-semiconductor-doping] Назви типів указують на основних носіїв заряду, а не на сумарний заряд кристала.

## Detailed explanation

У кристалі кремнію атоми утворюють чотири ковалентні зв’язки, бо кремній має чотири валентні електрони. Якщо один атом кремнію замінити атомом із п’ятьма валентними електронами, наприклад фосфором, чотири електрони беруть участь у зв’язках, а п’ятий слабко утримується ґраткою. Він може перейти до зони провідності; домішку називають донорною, а напівпровідник – `n`-типу.[^openstax-semiconductor-doping]

Атом із трьома валентними електронами, наприклад алюміній, не має електрона для одного зі зв’язків із сусідніми атомами кремнію. Такий стан може прийняти електрон із валентної зони, а в ній залишиться дірка, що поводиться як рухомий позитивний носій. Цю домішку називають акцепторною, а матеріал – `p`-типу.[^openstax-semiconductor-doping]

Приклад: фосфор у кремнії є типовою донорною домішкою, а бор – типовою акцепторною. Літери `n` і `p` описують знак основних рухомих носіїв, а не те, що весь легований кристал має відповідно негативний або позитивний заряд.[^openstax-semiconductor-doping]

Після передавання електрона донор стає нерухомим позитивним іоном у ґратці, а електрон може переносити заряд через кристал. Коли акцептор захоплює електрон із валентного зв’язку, нерухомий акцепторний іон має від’ємний заряд, а незаповнений зв’язок проявляється як рухома дірка. У звичайному зразку сумарний заряд залишається практично нейтральним: нерухомі заряджені домішки врівноважують рухомих носіїв.[^openstax-semiconductor-doping]

## Sources

<!-- generated from frontmatter -->
