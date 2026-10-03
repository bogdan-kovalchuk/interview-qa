---
id: emb-elintro-0170
title: "Що таке зворотний струм витоку діода?"
description: "Що таке зворотний струм витоку діода?"
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
    applicability: "Походження питання: лекція 16, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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
  - source_id: vishay-1n400x
    title: "Vishay: 1N4001–1N4007 datasheet"
    url: https://www.vishay.com/docs/88503/1n4001.pdf
    accessed: 2026-10-04
    kind: official
    version: "29-Apr-2020"
    applicability: "Номінали VRRM, VDC і зворотного струму серії 1N4001–1N4007; не гарантує поведінку поза максимальними рейтингами."
---

## Short answer

У зворотному зміщенні реальний діод проводить малий reverse leakage current, хоча ідеальна модель вважала б його нульовим.[^aac-semiconductors] Його величина залежить від зворотної напруги, температури й конкретного компонента, тому її перевіряють за даташитом.

## Detailed explanation

Зворотний струм витоку – це малий струм, що проходить через реальний діод під час зворотного зміщення, коли катод має вищий потенціал за анод. Ідеальна модель діода вважає цей струм нульовим, але в реальному напівпровіднику теплово згенеровані носії та інші механізми спричиняють невеликий струм.[^aac-semiconductors]

Його не слід ототожнювати зі струмом у режимі пробою. Нижче граничної зворотної напруги витік зазвичай малий; при наближенні до рейтингу або його перевищенні характер поведінки змінюється, і струм може зрости різко. Значення з даташиту завжди треба читати разом з умовами вимірювання: виробник задає прикладену зворотну напругу та температуру, а не одну універсальну цифру для всіх режимів.[^aac-semiconductors]

Температура має практичне значення: у специфікаціях струм витоку часто помітно збільшується при нагріванні. Наприклад, у даташиті Vishay для сімейства 1N4001–1N4007 максимальний DC reverse current наведено як 5 μA при 25 °C і 50 μA при 125 °C за номінальної DC blocking voltage.[^vishay-1n400x] Це конкретні умови конкретної серії, а не загальне правило множення для будь-якого діода.

У високoомних сенсорних вузлах, схемах утримання заряду та точних вимірюваннях навіть малий витік може створити помітну похибку або повільно розряджати конденсатор. Типова помилка – вважати зворотно зміщений діод повністю розімкненим ключем; для оцінки витоку треба перевірити температурну характеристику й умови даташиту, а також врахувати витоки плати та вимірювального приладу.[^aac-semiconductors] [^vishay-1n400x]

## Sources

<!-- generated from frontmatter -->
