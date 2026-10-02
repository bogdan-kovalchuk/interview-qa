---
id: emb-elintro-0024
title: "Що таке ват?"
description: "Що таке ват?"
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
    applicability: "Походження питання: лекція 4, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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
  - source_id: bipm-si-brochure
    title: "BIPM: The International System of Units, 9th edition"
    url: https://www.bipm.org/en/si-brochure-9
    accessed: 2026-10-04
    kind: spec
    version: "9th edition, version 4.01"
    applicability: "Офіційна брошура SI; визначення ватта як одиниці потужності та джоуля за секунду."
---

## Short answer

Ват (W) – одиниця потужності; `1 W = 1 J/s`. Потужність описує швидкість передавання або перетворення енергії.[^bipm-si-brochure]

## Detailed explanation

Потужність показує, скільки енергії передається або перетворюється за одиницю часу. Ват дорівнює одному джоулю за секунду, тому `P = E/t` для сталої потужності.[^bipm-si-brochure]

В електричному колі потужність споживача може перетворюватися на тепло, світло, звук або механічну роботу. Назва результату залежить від пристрою, але одиниця характеризує темп перетворення енергії, а не загальну кількість енергії.[^aac-direct-current]

Для резистивного елемента у відповідному режимі можна також обчислити потужність як `P = V*I`. Якщо струм або напруга змінюються з часом, миттєва потужність теж змінюється, і для енергії за інтервал треба врахувати її зміну в часі.[^aac-direct-current]

Однакова потужність не означає однакову кількість переданої енергії: важлива також тривалість роботи. Наприклад, навантаження потужністю `5 W`, яке працює `10 s`, отримує `50 J`, якщо потужність стала. Для реального джерела та навантаження фактичні значення залежать від режиму роботи й втрат, тож номінальну потужність компонента не слід автоматично вважати потужністю, яку він споживає постійно.[^aac-direct-current]

**Приклад:** пристрій, що протягом `10 s` передає `50 J` енергії, має середню потужність `P = E/t = 50 J/10 s = 5 W`.

## Sources

<!-- generated from frontmatter -->
