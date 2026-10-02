---
id: emb-elintro-0087
title: "Що таке ripple після випрямляча?"
description: "Що таке ripple після випрямляча?"
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
  - source_id: aac-rectifier-ripple
    title: "All About Circuits: Full-wave Bridge Rectifier With Output Filtering"
    url: https://www.allaboutcircuits.com/textbook/experiments/chpt-5/rectifier-filter-circuit/
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: "Підтверджує заряд конденсатора біля піків, розряд між піками та збільшення пульсації під більшим навантаженням; числова оцінка є наближеною."
---

## Short answer

`Ripple` – залишкова пульсація напруги після перетворення `AC` у `DC`. Конденсатор фільтра заряджається біля піків синусоїди й розряджається між ними, тому напруга не ідеально рівна.[^aac-rectifier-ripple]

## Detailed explanation

Пульсація (ripple) – це періодична складова напруги, що залишається на виході випрямляча разом із середньою постійною складовою. Випрямляч змінює полярність або пропускає одну півхвилю, але сам по собі не створює ідеально сталу напругу. Конденсатор паралельно навантаженню заряджається біля піків випрямленої напруги, а між ними віддає заряд у навантаження, через що вихідна напруга поступово спадає до наступного піка.[^aac-rectifier-ripple]

Величина пульсації залежить від струму навантаження, ємності конденсатора та частоти повторення піків. Більше навантаження споживає заряд швидше й збільшує спад; більша ємність за інших однакових умов зменшує його. У повнохвильовому випрямлячі піки з’являються двічі за період мережі, а в однопівхвильовому – один раз, тому за тих самих інших умов повнохвильова схема зазвичай має меншу пульсацію.[^aac-rectifier-ripple]

**Приклад розрахунку:** для грубої оцінки конденсаторного фільтра використовують `ΔV ≈ I_load/(f_ripple*C)`. Якщо навантаження бере `0.1 A`, пульсація має частоту `100 Hz`, а конденсатор дорівнює `1000 µF`, спад між піками становить близько `1 V`. Це наближення для приблизно сталого струму навантаження; воно не враховує ESR конденсатора, падіння на діодах і форму зарядних імпульсів.[^aac-rectifier-ripple]

**Типова помилка:** називати будь-яку напругу після діодів чистим DC. Для чутливого навантаження пульсацію потрібно оцінювати під навантаженням і перевіряти осцилографом або придатним вимірювачем; регулятор може її зменшити лише в межах запасу вхідної напруги.[^aac-rectifier-ripple]

## Sources

<!-- generated from frontmatter -->
