---
id: emb-elintro-0052
title: "Чим енергія відрізняється від потужності?"
description: "Чим енергія відрізняється від потужності?"
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
    applicability: "Походження питання: лекція 6, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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
  - source_id: openstax-electric-power-energy
    title: "OpenStax College Physics: Electric Power and Energy"
    url: https://openstax.org/books/college-physics/pages/20-4-electric-power-and-energy
    accessed: 2026-10-04
    kind: book
    version: "College Physics"
    applicability: "Визначає потужність як швидкість передавання енергії та пов’язує джоулі, секунди й вати; не задає характеристики конкретного пристрою."
---

## Short answer

Енергія характеризує кількість переданої або перетвореної енергії та вимірюється в джоулях або ват-годинах. Потужність – це швидкість передавання енергії: `P = E/t`, а `1 W = 1 J/s`.[^openstax-electric-power-energy]

## Detailed explanation

Енергія описує загальну кількість роботи або тепла, переданого системі чи від неї. У електричному колі вона може перейти, наприклад, з електричної форми у світло й тепло в лампі. Джоуль є одиницею енергії в SI; ват-година також є одиницею енергії, а не потужності.[^openstax-electric-power-energy]

Потужність показує, з якою швидкістю енергія передається або перетворюється. Для сталої потужності енергія дорівнює потужності, помноженій на час: `E = P*t`. У колі електрична потужність також обчислюється як `P = V*I`, де `V` – напруга, а `I` – струм; одиниця ват дорівнює джоулю за секунду.[^openstax-electric-power-energy]

Звідси видно різницю між двома приладами з однаковою потужністю, що працюють різний час: прилад потужністю 10 W за 2 години споживає 20 Wh, а за 5 годин – 50 Wh за умови сталої потужності. Потужність відповідає на запитання «наскільки швидко», а енергія – «скільки загалом».[^openstax-electric-power-energy]

Приклад: лампа потужністю 60 W, яка працює 3 години зі сталою потужністю, споживає `E = P*t = 60 W*3 h = 180 Wh`, або 0.18 kWh. Ват-години не можна називати ватами: перші враховують час роботи, другі характеризують швидкість передавання енергії.[^openstax-electric-power-energy]

## Sources

<!-- generated from frontmatter -->
