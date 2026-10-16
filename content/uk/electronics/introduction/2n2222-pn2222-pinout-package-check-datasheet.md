---
id: emb-elintro-0210
title: "Порядок виводів 2N2222/PN2222 у корпусі `TO-92` – чому треба перевіряти datasheet?"
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
  - source_id: pn2222-datasheet
    title: "onsemi PN2222A datasheet"
    url: https://www.onsemi.com/pdf/datasheet/pn2222a-d.pdf
---

## Short answer

Універсального порядку ніжок для всіх 2N2222/PN2222 у `TO-92` немає: він залежить від конкретного part number і виробника.[^pn2222-datasheet] Звірте рисунок корпуса й нумерацію виводів у його datasheet, орієнтуючи деталь так само, як на рисунку.[^pn2222-datasheet]

## Detailed explanation

Розпіновку 2N2222 або PN2222 визначають за datasheet конкретного виробника й корпусу: назви подібних деталей не гарантують однакового порядку виводів.[^pn2222-datasheet]

Маркування 2N2222, PN2222 і PN2222A часто позначає споріднені NPN-транзистори, але може відповідати різним виконанням. Наприклад, onsemi публікує окремі документи для металевого корпусу P2N2222A та пластикового PN2222A; схема ніжок і спосіб показу корпуса в механічному кресленні належать саме до описаного виробником part number.[^pn2222-datasheet]

Щоб знайти ніжки, звірте повне маркування, виробника і корпус, знайдіть у datasheet секцію `Pin Configuration` або креслення корпуса, а потім орієнтуйте деталь так само, як на рисунку. Не припускайте, що вигляд пласкою стороною до себе завжди дає `E-B-C`: рисунок може бути поданий знизу, згори або з боку ніжок. Зіставте напрямок і нумерацію виводів, а не тільки зовнішню форму.[^pn2222-datasheet]

Помилкове підключення може не дати очікуваного перемикання чи підсилення і за несприятливих умов перевищити допустимі напругу або струм переходів. Навіть якщо переставлені колектор і емітер транзистор інколи проводить у зворотному активному режимі, його gain та граничні параметри там не рівнозначні штатному підключенню. Перед живленням перевірте розпіновку, полярність, межі струму й розсіювану потужність у datasheet.[^pn2222-datasheet]

**Типова помилка:** переносити pinout із випадкового рисунка на іншу маркування або корпус. Для прототипу запишіть part number і виробника, а для заміни повторіть перевірку за документом нового компонента.
