---
id: emb-elintro-0032
title: "Що відбувається на межі P-N переходу?"
description: "Що відбувається на межі P-N переходу?"
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
    applicability: "Походження питання: лекція 5, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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
  - source_id: aac-pn-junction
    title: "All About Circuits: The P-N Junction"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/chpt-2/the-p-n-junction/
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: "Описує дифузію носіїв, область збіднення, зміщення переходу та приблизний прямий спад напруги; числові значення залежать від матеріалу й режиму."
---

## Short answer

Носії дифундують через межу P- і N-областей та рекомбінують, утворюючи область збіднення і потенціальний бар’єр. Його величина залежить від матеріалу; для кремнієвого діода часто наводять орієнтир близько 0.6–0.7 V, а не універсальне значення.[^aac-pn-junction]

## Detailed explanation

На межі P- та N-легованих ділянок електрони й дірки дифундують через межу та рекомбінують, залишаючи область збіднення на рухомі носії заряду.[^aac-semiconductors]

У N-області після відходу електронів залишаються нерухомі позитивні донори, а в P-області біля межі – негативні акцепторні іони. Це розділення зарядів створює внутрішнє поле, яке протидіє подальшій дифузії основних носіїв. Так виникають область збіднення та потенціальний бар’єр.[^aac-semiconductors]

У рівновазі дифузію основних носіїв урівноважує дрейфове перенесення у внутрішньому полі, тому не можна описувати перехід як ділянку, де носії просто зупинилися. Пряме зміщення зменшує бар’єр і звужує область збіднення, завдяки чому через межу проходить значний струм. Зворотне зміщення розширює область; реальний діод усе одно має малий витік, а достатня зворотна напруга спричиняє пробій.[^aac-pn-junction]

Приклад: для звичайного кремнієвого випрямного діода значення `0.7 V` може бути зручним наближенням у простому розрахунку, але точний спад треба брати з характеристики або datasheet при заданому струмі й температурі. Якщо діод послідовно з резистором підключити до джерела, саме резистор обмежує струм після відкривання переходу; одне лише наближення прямого спаду не задає безпечний струм.[^aac-pn-junction]

## Sources

<!-- generated from frontmatter -->
