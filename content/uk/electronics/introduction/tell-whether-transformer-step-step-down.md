---
id: emb-elintro-0157
title: "Як визначити, чи трансформатор step-up чи step-down?"
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
  - source_id: electronics-tutorials-transformer-basics
    title: "Electronics Tutorials: Transformer Basics and Transformer Principles"
    url: https://www.electronics-tutorials.ws/transformer/transformer-basics.html
---

## Short answer

Порівняйте число витків вторинної та первинної обмоток: `N2 > N1` означає step-up, а `N2 < N1` – step-down.[^electronics-tutorials-transformer-basics] Для ідеального трансформатора напруга пропорційна числу витків; реальна напруга під навантаженням залежить також від втрат і внутрішнього опору.[^electronics-tutorials-transformer-basics]

## Detailed explanation

Трансформатор називають step-up або step-down за тим, чи є вторинна напруга вища або нижча за первинну. У базовій моделі напруга на обмотці пропорційна її числу витків, бо той самий змінний магнітний потік проходить крізь витки обох обмоток.[^electronics-tutorials-transformer-basics]

Тому для первинної та вторинної обмоток виконується співвідношення `V2/V1 = N2/N1` для ідеального трансформатора. Якщо вторинна має більше витків, ніж первинна, напруга зростає і це step-up; якщо менше – напруга знижується і це step-down. За однакової кількості витків отримуємо трансформатор із приблизно однаковими напругами на обмотках.[^electronics-tutorials-transformer-basics]

Наприклад, якщо `N1 = 500` і `N2 = 1000`, то ідеальне відношення напруг `V2/V1 = 2`; для первинних `12 V` очікуємо близько `24 V` на вторинній обмотці без навантаження. Це розрахунок за припущенням ідеального зв’язку обмоток, а не гарантія точного значення для будь-якого реального пристрою.[^electronics-tutorials-transformer-basics]

Уважно визначайте, де первинна, а де вторинна обмотка: назви визначаються підключенням і напрямком передавання енергії в конкретній схемі, а не тим, яка обмотка фізично більша. Для багатовивідних трансформаторів потрібно також з’ясувати, між якими саме виводами вимірюють напругу; обмотка з відводом може мати різні ефективні числа витків.[^electronics-tutorials-transformer-basics]

**Типова помилка:** трактувати число витків як єдину умову реальної вихідної напруги. Воно задає ідеальне співвідношення; просідання під навантаженням, частота та допустима потужність залежать від конструкції трансформатора.[^electronics-tutorials-transformer-basics]
