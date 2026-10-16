---
id: emb-elintro-0037
title: "Скільки електронів у валентній оболонці у провідника, ізолятора і напівпровідника?"
track: electronics
section: introduction
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), картки курсу"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-direct-current
    title: "All About Circuits textbook, Volume I: DC"
    url: https://www.allaboutcircuits.com/textbook/direct-current/
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
  - source_id: aac-conductors-valence
    title: "All About Circuits: Introduction to Conductance and Conductors"
    url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-12/introduction-conductance-and-conductors/
---

## Short answer

У простій моделі для металевого провідника часто наводять 1–3 слабко зв’язані валентні електрони, для кремнію як напівпровідника – 4, а для багатьох ізоляторів – заповнену зовнішню оболонку.[^aac-conductors-valence] Це лише навчальне наближення: провідність визначають також кристалічна структура та доступні енергетичні стани, тому одного числа електронів недостатньо для класифікації матеріалу.[^aac-conductors-valence]

## Detailed explanation

Кількість валентних електронів не утворює універсального правила для класифікації провідників, ізоляторів і напівпровідників: електропровідність залежить від енергетичних станів електронів і зв’язків у матеріалі.[^aac-conductors-valence] У базовій моделі кремній має чотири валентні електрони, які утворюють ковалентні зв’язки з сусідніми атомами; для металів спрощено говорять про доступні для руху електрони, а в багатьох ізоляторах електрони залишаються зв’язаними.[^aac-semiconductors]

Тому твердження «провідник має стільки-то електронів, а ізолятор – стільки-то» не є загальним законом. Наприклад, графіт і алмаз складаються з атомів карбону з однаковою кількістю валентних електронів, але мають різну провідність через різну структуру зв’язків.[^aac-conductors-valence]

Приклад: кремній без домішок є напівпровідником; додавання донорів чи акцепторів змінює концентрацію носіїв, а отже й електричну поведінку кристала.[^aac-semiconductors]

У металі електрони можуть займати стани, що дають змогу реагувати на електричне поле й переносити заряд; у ізоляторі за звичайних умов таких доступних станів значно менше. У напівпровіднику кількість носіїв можна помітно змінити температурою, освітленням або легуванням. Тому підрахунок електронів зовнішньої оболонки корисний для першої інтуїції, але для прогнозу потрібна також модель зон і зв’язків конкретного матеріалу.[^aac-conductors-valence]
