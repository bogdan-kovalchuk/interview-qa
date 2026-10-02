---
id: emb-elintro-0037
title: "Скільки електронів у валентній оболонці у провідника, ізолятора і напівпровідника?"
description: "Скільки електронів у валентній оболонці у провідника, ізолятора і напівпровідника?"
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
  - source_id: aac-conductors-valence
    title: "All About Circuits: Introduction to Conductance and Conductors"
    url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-12/introduction-conductance-and-conductors/
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: "Пояснює, чому кількість валентних електронів сама по собі не визначає провідність: важливі енергетичні стани й хімічний зв’язок; наводить приклади графіту й алмазу."

---

## Short answer

У простій моделі для металевого провідника часто наводять 1–3 слабко зв’язані валентні електрони, для кремнію як напівпровідника – 4, а для багатьох ізоляторів – заповнену зовнішню оболонку.[^aac-conductors-valence] Це лише навчальне наближення: провідність визначають також кристалічна структура та доступні енергетичні стани, тому одного числа електронів недостатньо для класифікації матеріалу.[^aac-conductors-valence]

## Detailed explanation

Кількість валентних електронів не утворює універсального правила для класифікації провідників, ізоляторів і напівпровідників: електропровідність залежить від енергетичних станів електронів і зв’язків у матеріалі.[^aac-conductors-valence] У базовій моделі кремній має чотири валентні електрони, які утворюють ковалентні зв’язки з сусідніми атомами; для металів спрощено говорять про доступні для руху електрони, а в багатьох ізоляторах електрони залишаються зв’язаними.[^aac-semiconductors]

Тому твердження «провідник має стільки-то електронів, а ізолятор – стільки-то» не є загальним законом. Наприклад, графіт і алмаз складаються з атомів карбону з однаковою кількістю валентних електронів, але мають різну провідність через різну структуру зв’язків.[^aac-conductors-valence]

Приклад: кремній без домішок є напівпровідником; додавання донорів чи акцепторів змінює концентрацію носіїв, а отже й електричну поведінку кристала.[^aac-semiconductors]

У металі електрони можуть займати стани, що дають змогу реагувати на електричне поле й переносити заряд; у ізоляторі за звичайних умов таких доступних станів значно менше. У напівпровіднику кількість носіїв можна помітно змінити температурою, освітленням або легуванням. Тому підрахунок електронів зовнішньої оболонки корисний для першої інтуїції, але для прогнозу потрібна також модель зон і зв’язків конкретного матеріалу.[^aac-conductors-valence]

## Sources

<!-- generated from frontmatter -->
