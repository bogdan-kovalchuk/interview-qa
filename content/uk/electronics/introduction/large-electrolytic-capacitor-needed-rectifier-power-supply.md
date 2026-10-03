---
id: emb-elintro-0178
title: "Для чого потрібен великий електролітичний конденсатор після випрямляча у блоці живлення?"
description: "Для чого потрібен великий електролітичний конденсатор після випрямляча у блоці живлення?"
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
  - source_id: adi-rectifier-filter
    title: "Analog Devices Wiki: Chapter 6: Diode applications"
    url: https://wiki.analog.com/university/courses/electronics/text/chapter-6
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: "Пояснює залежність ємності фільтра від струму, ripple frequency і допустимої пульсації; правило для конкретного блока треба розраховувати."
  - source_id: aac-bridge-filter-lab
    title: "All About Circuits: Full-wave Bridge Rectifier With Output Filtering"
    url: https://www.allaboutcircuits.com/textbook/experiments/chpt-5/rectifier-filter-circuit/
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: "Підтверджує заряджання конденсатора біля піків, розряд між ними та зростання ripple під більшим навантаженням."
---

## Short answer

Великий електролітичний конденсатор після випрямляча накопичує заряд біля піків і віддає його навантаженню між піками, зменшуючи ripple. Потрібна ємність залежить від струму навантаження, частоти пульсацій і допустимої зміни напруги; правило «1000 мкФ на ампер» є лише грубим орієнтиром для конкретних припущень.[^adi-rectifier-filter]

## Detailed explanation

Після випрямлення напруга має повторювані піки, а між ними джерело майже не подає енергію в навантаження. Великий електролітичний конденсатор під’єднують паралельно виходу, щоб він заряджався поблизу піка випрямленої напруги, а потім підтримував струм навантаження, поки миттєва напруга джерела нижча за напругу конденсатора. Через це вихід стає ближчим до DC, хоча залишкова періодична зміна – ripple – нікуди не зникає повністю.[^aac-bridge-filter-lab][^adi-rectifier-filter]

Між піками конденсатор розряджається. За більших струму навантаження або інтервалу між піками він втрачає більше заряду; більша ємність зменшує цю зміну напруги. Для однофазного мосту є два піки на період вхідної синусоїди, отже ripple frequency удвічі вища за частоту джерела. Для half-wave є лише один пік за період, тому за інших однакових умов конденсатор має довше чекати на наступне підзаряджання.[^adi-rectifier-filter]

Для приблизної оцінки при відносно невеликій пульсації використовують `ΔV ≈ I_load/(f_ripple*C)`. Це наближення не враховує ESR, імпульсний характер струму через діоди, опір обмоток трансформатора та зміну навантаження, тому фінальний вибір перевіряють для реальної схеми й допустимого ripple. Занадто мала ємність дає помітні провали; надмірно велика може збільшити імпульсний струм заряджання та навантаження на діоди й трансформатор.[^adi-rectifier-filter][^aac-bridge-filter-lab]

**Приклад розрахунку:** для мосту від `50 Hz` маємо `f_ripple = 100 Hz`. Якщо навантаження споживає `0.5 A`, а цільова пульсація – `2 V`, ідеалізована оцінка дає `C ≈ 0.5/(100*2) = 0.0025 F`, тобто близько `2500 µF`. Це початкова оцінка, а не готовий номінал: додають запас і перевіряють допустиму напругу, ripple-current rating та пусковий струм.[^adi-rectifier-filter]

**Типова помилка:** вважати універсальним орієнтир `1000 µF на ампер`. Такий вислів не задає ні топології випрямляча, ні частоти, ні припустимого ripple, тому для іншого навантаження може дати непридатний результат.[^adi-rectifier-filter]

## Sources

<!-- generated from frontmatter -->
