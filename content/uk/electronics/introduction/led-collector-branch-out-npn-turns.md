---
id: emb-elintro-0224
title: "Чому LED у колекторній гілці гасне, коли NPN відкривається?"
description: "Чому LED у колекторній гілці гасне, коли NPN відкривається?"
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
    applicability: "Походження питання: лекція 21, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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
  - source_id: aac-bjt-switch
    title: "All About Circuits: The Bipolar Junction Transistor (BJT) as a Switch"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/chpt-4/transistor-switch-bjt/
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: "Пояснює насичення NPN-ключа й низьку напругу колектора; ефект із LED залежить від топології гілки."
---

## Short answer

У цій схемі насичений NPN стягує колектор до низької напруги й шунтує LED-гілку, тому струм через LED зменшується. Це дає інверсію: активний високий сигнал на вході відповідає низькому рівню колектора.[^aac-bjt-switch]

## Detailed explanation

У типовому низькобічному ключі емітер NPN з’єднаний із землею, а колектор навантаження під’єднаний до живлення. Коли базовий струм переводить транзистор у насичення, напруга колектора наближається до напруги емітера. Вузол колектора стає низьким відносно землі – це інверсія вхідного керування.[^aac-bjt-switch]

LED згасне лише за такого з’єднання, у якому увімкнений транзистор зменшує напругу на LED або шунтує її струмову гілку. Сам вислів «LED у колекторній гілці» не визначає схему повністю. Якщо LED включено послідовно з навантаженням, яке живиться через колектор, NPN, навпаки, може пропускати крізь LED більший струм. Вирішальними є вузли під’єднання та полярність компонентів.[^aac-bjt-switch]

**Приклад:** якщо LED-гілка під’єднана між колекторним вузлом і землею, а NPN відкривається паралельно їй, низький `V_CE(sat)` залишає малу напругу на LED; її струм може стати недостатнім для видимого світіння. У конкретному вимірюванні слід перевірити напругу безпосередньо на LED, а не робити висновок лише з логічного стану бази.[^aac-bjt-switch]

**Типова помилка:** стверджувати, що відкритий NPN завжди вимикає LED. Спершу намалюйте замкнені шляхи струму в обох станах та визначте, чи транзистор стоїть послідовно з LED, чи шунтує її.[^aac-bjt-switch]

## Sources

<!-- generated from frontmatter -->
