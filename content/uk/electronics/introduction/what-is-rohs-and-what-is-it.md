---
id: emb-elintro-0174
title: "Що таке `RoHS` і навіщо він потрібен?"
description: "Що таке `RoHS` і навіщо він потрібен?"
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
  - source_id: eu-rohs-directive
    title: "Directive 2011/65/EU on the restriction of the use of certain hazardous substances in electrical and electronic equipment"
    url: https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=CELEX:32011L0065
    accessed: 2026-10-04
    kind: spec
    version: "2011/65/EU, as amended"
    applicability: "Правова основа обмежень RoHS у ЄС, охоплені категорії обладнання, граничні концентрації в однорідних матеріалах та передбачені винятки; перевіряйте чинну редакцію і застосовність до виробу."
---

## Short answer

`RoHS` – законодавство ЄС, що обмежує певні небезпечні речовини в охопленому електричному й електронному обладнанні. Граничні концентрації застосовують до кожного однорідного матеріалу, а сфера дії та винятки залежать від категорії виробу й чинної редакції правил.[^eu-rohs-directive]

## Detailed explanation

`RoHS` – скорочена назва правил ЄС щодо обмеження певних небезпечних речовин в електричному й електронному обладнанні. Вимоги встановлює Директива 2011/65/EU з поправками. Вона стосується обладнання, що входить до визначених категорій, і не є загальною забороною будь-якої кількості речовини в будь-якому виробі.[^eu-rohs-directive]

Обмеження оцінюють за концентрацією в однорідному матеріалі, а не усереднюють по всьому пристрою. Наприклад, припій у з’єднанні й ізоляція дроту є окремими матеріалами для такого аналізу. Для шести речовин, включно зі свинцем, ртуттю та Cr(VI), типовий граничний рівень становить 0.1 % за масою; для кадмію – 0.01 %. Поправка (EU) 2015/863 додала чотири фталати до переліку, тож чинний Annex II містить десять обмежених речовин.[^eu-rohs-directive]

Директива передбачає винятки для визначених застосувань і строків, тому висновок про відповідність роблять для конкретного виробу, матеріалів та ринку. Компонент із позначкою RoHS compliant сам по собі не доводить відповідність усього зібраного пристрою: виробник кінцевого обладнання має врахувати компоненти, документацію постачальників і застосовні винятки.[^eu-rohs-directive]

**Типова помилка:** трактувати RoHS як стандарт електричної безпеки або як абсолютне твердження «свинцю немає». Це вимога щодо обмеження конкретних речовин із числовими порогами та винятками; вона не замінює перевірки інших правил безпеки й екологічності.

## Sources

<!-- generated from frontmatter -->
