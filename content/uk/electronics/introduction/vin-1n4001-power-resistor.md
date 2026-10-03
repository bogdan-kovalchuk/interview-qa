---
id: emb-elintro-0192
title: "`V_in` = 12 V, R = 100 Ω, 1N4001. Яка потужність на резисторі?"
description: "V_in = 12 V, R = 100 Ω, 1N4001. Яка потужність на резисторі?"
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
  - source_id: onsemi-1n4001-datasheet
    title: "onsemi: 1N4001–1N4007 Axial-Lead Glass Passivated Standard Recovery Rectifiers"
    url: https://www.onsemi.com/pdf/datasheet/1n4001-d.pdf
    accessed: 2026-10-04
    kind: official
    version: null
    applicability: "Номінальні характеристики сімейства 1N4001–1N4007; максимальне падіння 1.1 V задане при 1 A, а не як точне значення при струмі цього прикладу."
---

## Short answer

За наближенням падіння на прямозміщеному діоді 0.7 V струм становить `(12 V - 0.7 V)/100 Ω ≈ 113 mA`, а розсіювана резистором потужність – `I²*R ≈ 1.28 W`. Резистор 0.25 W перевищує цей розрахунковий режим; практичний номінал треба вибирати з урахуванням температурного derating і теплового монтажу.[^aac-direct-current] [^aac-semiconductors]

## Detailed explanation

У цій послідовній схемі струм через резистор і діод однаковий. Для першої оцінки беремо кремнієвий діод із прямим падінням близько `0.7 V`; тоді на резисторі лишається `12 V - 0.7 V = 11.3 V`, а за законом Ома струм дорівнює `11.3 V/100 Ω = 0.113 A`.[^aac-direct-current] [^aac-semiconductors]

Потужність резистора можна знайти як добуток напруги на ньому і струму або як `P = I²*R`. Для наведеного наближення це `0.113²*100 ≈ 1.28 W`. Отже, резистор на `0.25 W` не підходить: він розсіював би понад п’ятикратну номінальну потужність. Номінал `2 W` перевищує обчислене значення, але потрібний запас визначають температура довкілля, вентиляція, монтаж на платі та правила derating виробника; це не автоматична гарантія для будь-якого корпусу.[^aac-direct-current]

Падіння `0.7 V` є приблизною моделлю, а не фіксованою властивістю 1N4001. Datasheet onsemi задає максимум `1.1 V` при `1 A`; це не можна переносити як точне значення при `113 mA`, тому точний струм потребує характеристики діода у відповідних умовах. Ця різниця трохи змінює результат, але не змінює висновок, що резистор 0.25 W недостатній.[^onsemi-1n4001-datasheet]

Приклад розрахунку для моделі `V_F = 0.7 V`:

```text
I = (12 V - 0.7 V)/100 Ω = 0.113 A
P_R = I²*R = 0.113²*100 Ω ≈ 1.28 W
```

**Типова помилка:** рахувати `12²/100 = 1.44 W`, ніби всі 12 V падають на резисторі. Частина напруги припадає на діод; водночас паспортне максимальне падіння діода не слід вважати його типовим точним падінням у цій схемі.[^aac-direct-current] [^onsemi-1n4001-datasheet]

## Sources

<!-- generated from frontmatter -->
