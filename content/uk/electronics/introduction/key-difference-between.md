---
id: emb-elintro-0077
title: "Яка ключова відмінність між `DC` і `AC`?"
description: "Яка ключова відмінність між `DC` і `AC`?"
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
    applicability: "Походження питання: лекція 9, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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
  - source_id: aac-dc-ac-direction
    title: "All About Circuits: Voltage and Current"
    url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-1/voltage-current/
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: "Визначає DC як односпрямований струм і AC як струм, що періодично змінює напрямок; не стверджує, що DC обов’язково має сталу величину."
---

## Short answer

`DC` означає струм, що тече в одному напрямку; його величина може змінюватися. `AC` періодично змінює напрямок струму (або полярність напруги). Батарея зазвичай дає `DC`, а побутова мережа – `AC`.[^aac-dc-ac-direction]

## Detailed explanation

`DC` (direct current) – струм, напрямок якого не змінюється; `AC` (alternating current) періодично змінює напрямок. Розрізняти їх слід за напрямком, а не за тим, чи є графік ідеально рівною лінією.[^aac-dc-ac-direction]

У батарейному колі полярність джерела зазвичай стала, тому умовний струм через навантаження спрямований незмінно. Це не означає, що його величина мусить бути постійною: наприклад, напруга пульсуючого випрямляча може змінюватися в часі, хоча струм не розвертається. Таку форму не слід плутати з чистим змінним струмом.[^aac-dc-ac-direction]

У звичайному синусоїдальному `AC` напруга змінює знак кожні півперіоду, а струм в простому резистивному колі змінює напрямок разом із нею. Частота описує кількість повних циклів за секунду, а амплітуда – максимальне відхилення від нуля. Реальне змінне живлення може мати спотворену форму, але ключовою ознакою залишається реверсування.[^aac-dc-ac-direction]

**Приклад:** батарея, що живить лампу, дає односпрямований струм. Мережеве джерело змушує струм у резистивному навантаженні рухатися то в один, то в протилежний бік. Якщо після випрямляча напруга пульсує, її напрямок у навантаженні все одно може залишатися одним.[^aac-dc-ac-direction]

**Типова помилка:** називати будь-який струм зі змінною величиною `AC`. Перевіряйте знак струму або полярність напруги в часі; зміна величини сама по собі не означає зміни напрямку.[^aac-dc-ac-direction]

## Sources

<!-- generated from frontmatter -->
