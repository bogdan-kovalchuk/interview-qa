---
id: emb-elintro-0177
title: "Чим half-wave rectifier відрізняється від bridge rectifier?"
description: "Чим half-wave rectifier відрізняється від bridge rectifier?"
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
    applicability: "Походження питання: лекція 17, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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
  - source_id: aac-half-wave-lab
    title: "All About Circuits: Si Lab - Half-wave Rectifier"
    url: https://www.allaboutcircuits.com/textbook/experiments/chpt-5/half-wave-rectifier/
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: "Показує пропускання однієї напівхвилі та пульсівну форму виходу; конкретна схема тут навчальна."
  - source_id: aac-bridge-filter-lab
    title: "All About Circuits: Full-wave Bridge Rectifier With Output Filtering"
    url: https://www.allaboutcircuits.com/textbook/experiments/chpt-5/rectifier-filter-circuit/
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: "Показує повнохвильовий мостовий випрямляч, фільтрацію конденсатором і залежність ripple від навантаження."
---

## Short answer

Half-wave rectifier пропускає одну напівхвилю `AC`, а bridge rectifier випрямляє обидві, тому його пульсації після фільтрації зазвичай менші. У мостовій схемі струм проходить через два діоди за кожну напівхвилю, тож треба враховувати сумарне пряме падіння; середня вихідна напруга залежить від навантаження, фільтра та діодів.[^aac-half-wave-lab][^aac-bridge-filter-lab]

## Detailed explanation

Half-wave rectifier перетворює змінну напругу на однонапрямлені імпульси, пропускаючи лише одну напівхвилю вхідного сигналу. Найпростіша схема має один діод: під час прямої напівхвилі він проводить, а під час зворотної блокує струм. Без згладжувального конденсатора вихід не є сталою напругою – це пульсівна напруга з паузою між імпульсами.[^aac-half-wave-lab]

Bridge rectifier, або повнохвильовий мостовий випрямляч, використовує чотири діоди. У кожну половину періоду проводить своя пара діодів, але струм через навантаження тече в тому самому напрямку. Тому за один період джерела на виході виникають два імпульси замість одного; для мережі 60 Гц основна частота пульсацій після мосту становить 120 Гц, а для 50 Гц – 100 Гц. Міст не створює ідеального DC: без фільтра напруга все одно пульсує.[^aac-bridge-filter-lab]

Якщо обидві схеми мають конденсатор паралельно навантаженню, він заряджається біля піків і віддає заряд навантаженню між ними. У повнохвильової схеми проміжок між піками коротший, тому за однакових ємності та струму конденсатор розряджається менше і ripple зазвичай менший. Проте міст має два послідовні переходи діодів у шляху струму, що знижує пікову напругу на виході; фактичну напругу визначають також трансформатор, діоди, навантаження та конденсатор.[^aac-bridge-filter-lab]

**Приклад:** якщо вхід має частоту 50 Гц, half-wave дає один зарядний пік за період, тобто 50 піків за секунду, а bridge – два, тобто 100. Це пояснює різницю частот ripple, але саме по собі не визначає його амплітуду: вона залежить від навантаження і ємності.[^aac-half-wave-lab][^aac-bridge-filter-lab]

**Типова помилка:** казати, що мостовий випрямляч завжди дає більшу середню напругу без уточнень. Згладжування та навантаження змінюють середнє значення, а два прямі переходи мосту додають падіння напруги; порівнювати треба за однакових умов.[^aac-bridge-filter-lab]

## Sources

<!-- generated from frontmatter -->
