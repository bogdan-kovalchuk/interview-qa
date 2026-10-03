---
id: emb-elintro-0193
title: "Як вибрати послідовний резистор для простого Зенер-стабілізатора?"
description: "Як вибрати послідовний резистор для простого Зенер-стабілізатора?"
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
    applicability: "Походження питання: лекція 18, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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
  - source_id: aac-zener-regulator
    title: "All About Circuits: What Are Zener Diodes?"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/chpt-3/zener-diodes/
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: "Пояснює роботу паралельного стабілізатора Зенера, розподіл струмів і межу регулювання за навантаженням."
---

## Short answer

Послідовний резистор має забезпечити максимальний струм навантаження та мінімальний струм Зенера за найменшої вхідної напруги: `R_s = (V_in - V_Z)/(I_load,max + I_Z,min)`. Потім перевіряють найбільшу вхідну напругу й найменший струм навантаження, щоб Зенер і резистор не перевищили допустимих потужностей.[^aac-zener-regulator]

## Detailed explanation

Послідовний резистор у простому стабілізаторі Зенера обмежує загальний струм від джерела. У режимі стабілізації цей струм розгалужується: частина йде в навантаження, решта – через Зенер. Тому розрахунок має одночасно забезпечити мінімальний струм Зенера для регулювання та не перевищити його допустимі струм і потужність.[^aac-zener-regulator]

Спочатку перевіряють найгірший випадок для збереження регулювання: найнижчу напругу джерела разом із найбільшим струмом навантаження. За цих умов через резистор має пройти сума максимального струму навантаження та мінімального струму Зенера, отже `R_s <= (V_in,min - V_Z)/(I_load,max + I_Z,min)`. Якщо навантаження не споживає струму, майже весь струм резистора проходить через Зенер; саме тому окремо перевіряють максимальну напругу джерела й потужність компонентів.[^aac-zener-regulator]

Приклад: для стабілітрона `5.1 V`, джерела `9 V`, навантаження до `10 mA` і потрібного мінімального струму Зенера `5 mA` граничне значення за умовою регулювання становить `(9 V - 5.1 V)/(10 mA + 5 mA) = 260 Ω`. Це розрахункове верхнє обмеження: вибір стандартного номіналу нижче нього збільшить струм, тож треба ще перевірити потужності при максимальному `V_in` і холостому ході. Значення `5 mA` тут задане як умова прикладу, а не універсальна характеристика Зенера.[^aac-zener-regulator]

**Типова помилка:** врахувати лише струм навантаження. Якщо не залишити запас для `I_Z,min`, Зенер може вийти з області пробою при великому навантаженні, і вихідна напруга знизиться. Надто малий резистор також небезпечний на максимальній вхідній напрузі, особливо без навантаження.[^aac-zener-regulator]

## Sources

<!-- generated from frontmatter -->
