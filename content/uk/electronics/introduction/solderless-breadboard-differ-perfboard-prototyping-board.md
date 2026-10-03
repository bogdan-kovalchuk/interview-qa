---
id: emb-elintro-0279
title: "Чим solderless breadboard відрізняється від perfboard/протоплати?"
description: "Чим solderless breadboard відрізняється від perfboard/протоплати?"
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
    applicability: "Походження питання: лекція 25, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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
    url: https://learn.adafruit.com/breadboards-for-beginners/breadboards
    accessed: 2026-10-04
    kind: official
    version: null
    applicability: "Описує пружинні контакти та внутрішні з’єднання solderless breadboard, її повторне використання і погіршення контактів з часом."
  - source_id: digikey-perfboard
    title: "DigiKey: Solderless Breadboard to Soldered Circuit"
    url: https://www.digikey.com/en/maker/blogs/2023/from-solderless-breadboard-to-soldered-circuit-with-becky-stern
    accessed: 2026-10-04
    kind: official
    version: null
    applicability: "Пояснює перехід від макетної плати без паяння до паяної perfboard і різновиди перфорованих плат."
---

## Short answer

Solderless breadboard з’єднує компоненти пружинними контактами без паяння, тож її зручно швидко перебудовувати. На perfboard компоненти паяють до майданчиків, тому монтаж фіксований; тип з’єднань залежить від конкретного рисунка плати.[^adafruit-breadboards]

## Detailed explanation

Solderless breadboard – це багаторазова плата для тимчасового макетування, в якій виводи компонентів вставляються в отвори та затискаються внутрішніми металевими контактами. У типовій платі групи отворів з’єднані прихованими смужками: наприклад, п’ять отворів одного ряду можуть бути спільним вузлом, а центральний проміжок розділяє ліву й праву половини. Схему зручно змінювати без паяння, але перед підключенням треба перевірити реальну розводку саме своєї моделі.[^adafruit-breadboards]

Perfboard – це перфорована плата для паяного монтажу. У простому варіанті кожен отвір має окремий мідний майданчик, а електричні вузли утворюють виводами деталей або короткими перемичками. Інші протоплати мають ряди з’єднаних майданчиків чи повторюють геометрію solderless breadboard; слово «perfboard» саме собою не гарантує конкретної схеми доріжок. Паяний прототип важче змінити, зате з’єднання механічно закріплені припоєм і плату зручніше переносити як зібраний вузол.[^digikey-perfboard]

Вибір залежить від етапу роботи. Для перевірки принципу, швидкої заміни номіналів і навчальних схем підходить solderless breadboard. Після налагодження просту схему можна перенести на перфоровану плату, обравши її рисунок під потрібні з’єднання. Для високих частот, значного струму, вібрації чи довготривалої експлуатації жоден з цих варіантів не слід автоматично вважати придатним: оцініть паразитні параметри, контактний опір, механічну міцність і допустимі рейтинги конкретної плати.[^adafruit-breadboards][^digikey-perfboard]

**Типова помилка:** припускати, що всі отвори breadboard з’єднані однаково або що будь-яка perfboard уже має потрібні доріжки. Перед монтажем перевірте схему контактів документацією чи мультиметром у режимі continuity; для паяної плати простежте мідні майданчики та перемички за її кресленням. Зношені пружинні контакти можуть втрачати надійність, тому переривчасту роботу варто перевірити легким рухом проводу та оглядом плати.[^adafruit-breadboards]

## Sources

<!-- generated from frontmatter -->
