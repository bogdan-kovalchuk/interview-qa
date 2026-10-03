---
id: emb-elintro-0299
title: "Як правильно планувати розміщення компонентів на perfboard?"
description: "Як правильно планувати розміщення компонентів на perfboard?"
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
    applicability: "Походження питання: лекція 26, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
  - source_id: aac-direct-current
    title: "All About Circuits textbook, Volume I: DC"
    url: https://www.allaboutcircuits.com/textbook/direct-current/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: DC-кола, закон Ома, закони Кірхгофа, джерела й вимірювання; конкретні номінали й схеми курсу можуть відрізнятися."
  - source_id: adafruit-perfboard
    title: "Adafruit: Collin's Lab, Breadboards & Perfboards"
    url: https://learn.adafruit.com/collins-lab-breadboards-and-perfboards?view=all
    accessed: 2026-10-04
    kind: community
    version: null
    applicability: "Перенесення перевіреної схеми на perfboard, роль ізольованих площадок, виводів компонентів і дротів-перемичок; плати мають різні схеми з’єднань."
  - source_id: mit-perfboard
    title: "MIT OpenCourseWare: 8.01x Physics I, Low Voltage Power Supply Lab"
    url: https://mitocw.ups.edu.ec/courses/physics/8-01x-physics-i-classical-mechanics-with-an-experimental-focus-fall-2002/labs/801x.pdf
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: "Навчальний приклад перенесення схеми на perfboard: розміщення частин для зменшення кількості дротів, окремі вигляди компонентного й монтажного боків та перевірка з’єднань. Це приклад конкретного блока живлення, а не універсальне правило компонування."
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: діоди, стабілітрони, біполярні й польові транзистори та джерела живлення; конкретні номінали й схеми курсу можуть відрізнятися."
---

## Short answer

Спочатку продумайте розміщення компонентів і маршрут з’єднань, а також полярність LED та місце для роз’єму, кнопки й резистора. Залиште простір для перемичок і перевірки монтажу; розміщення на perfboard має відповідати електричній схемі.[^mit-perfboard]

## Detailed explanation

Розміщення на perfboard варто спланувати до пайки, бо отвори не визначають автоматично всі електричні з’єднання: багато вузлів доведеться з’єднати окремими дротами або виводами компонентів. Спершу перенесіть схему на ескіз із видом зверху та з боку мідних площадок, позначте полярність, живлення, землю й місця перемичок. Такий план допомагає помітити перетини та нестачу місця до того, як компоненти будуть припаяні.[^adafruit-perfboard]

Розташуйте роз’єми й органи керування так, щоб до них був фізичний доступ, а полярні компоненти можна було перевірити за маркуванням. Залишайте місце для ширини корпусів, висоти компонентів, дротів і наконечника паяльника. На типовій perfboard із ізольованими площадками сусідні отвори самі по собі не з’єднані; однак є плати з іншою схемою мідних доріжок, тому перед монтажем перевірте саме свій тип плати мультиметром або за документацією.[^adafruit-perfboard]

Після розміщення позначте кожне електричне з’єднання на стороні пайки й перевірте маршрут від вузла до вузла. Коротші перемички зазвичай спрощують огляд і зменшують імовірність помилкового дотику, але не можна прокладати їх так, щоб вони закривали сусідні площадки чи заважали компонентам. Корисно спершу зібрати схему на breadboard, перевірити її роботу, а потім перенести підтверджені з’єднання на perfboard; для прототипу це зменшує кількість переробок, але не замінює фінальну перевірку монтажу мультиметром.[^adafruit-perfboard]

## Sources

<!-- generated from frontmatter -->
