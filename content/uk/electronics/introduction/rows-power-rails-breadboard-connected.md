---
id: emb-elintro-0105
title: "Як з'єднані ряди і рейки живлення на breadboard?"
description: "Як з'єднані ряди і рейки живлення на breadboard?"
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
  - source_id: adafruit-breadboards
    title: "Adafruit Learning System: Breadboards for Beginners"
    url: https://learn.adafruit.com/breadboards-for-beginners?view=all
    accessed: 2026-10-04
    kind: official
    version: "current"
    applicability: "Підтверджує типову будову й електричні зв’язки; конкретна реалізація може відрізнятися."
---

## Short answer

У типовій breadboard п’ять отворів кожного поперечного ряду в центральному полі з’єднані між собою, а центральна канавка розділяє ліву та праву групи. Бічні power rails призначені для розподілу живлення, але можуть бути перервані посередині або не з’єднані між собою; перевірте конкретну плату.[^adafruit-breadboards]

## Detailed explanation

У типовій solderless breadboard металеві пружні контакти під отворами утворюють електричні вузли. У центральному полі зазвичай п’ять отворів одного поперечного ряду з одного боку канавки з’єднані разом; п’ять отворів навпроти становлять окрему групу. Ці контактні групи дають змогу з’єднувати ніжки компонентів короткими перемичками, але розташування отворів саме по собі не визначає електричне з’єднання – його задають внутрішні металеві контакти.[^adafruit-breadboards]

Довгі бічні power rails дають зручні точки для підведення живлення та землі до різних ділянок схеми. Позначки «+» і «−» лише підказують типове призначення: рейка не має заданої полярності, доки ви не під’єднаєте до неї джерело. У багатьох платах кожна рейка з’єднана вздовж, але рейки з протилежних боків зазвичай окремі, а довга рейка іноді має розрив посередині.[^adafruit-breadboards]

**Типові помилки:**
- Не припускайте, що плюсова й мінусова рейки або ліва й права рейки з’єднані між собою. За потреби з’єднайте їх перемичками.
- Перевірте, чи рейка не розділена на секції. Якщо потрібен безперервний вузол, з’єднайте секції перемичкою.
- Перед подачею живлення перевірте сумнівні точки прозвонюванням, особливо на іншій або мініатюрній моделі плати.[^adafruit-breadboards]

## Sources

<!-- generated from frontmatter -->
