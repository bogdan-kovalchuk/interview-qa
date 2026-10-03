---
id: emb-elintro-0121
title: "Чому LED не можна підключати напряму до джерела напруги без резистора?"
description: "Чому LED не можна підключати напряму до джерела напруги без резистора?"
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
    applicability: "Походження питання: лекція 12, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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
---

## Short answer

Після відкривання LED його струм швидко зростає зі збільшенням напруги, тому джерело напруги саме по собі не задає безпечного струму. Послідовний резистор або драйвер струму обмежує його; для джерела 5 V, LED із `V_f = 2 V` і струму 10 mA ідеальний розрахунок дає `R = (5 V - 2 V)/0.01 A = 300 Ω`.[^aac-semiconductors] Реальні `V_f` та допустимий струм беруть із datasheet конкретного LED.[^aac-direct-current]

## Detailed explanation

LED є діодом, для якого струм у прямому напрямку нелінійно зростає зі збільшенням напруги. Поблизу робочої точки невелика зміна напруги може спричинити значну зміну струму, тому підключення до джерела, яке лише підтримує задану напругу, не гарантує безпечного режиму.[^aac-semiconductors]

Послідовний резистор створює спад напруги, пропорційний струму, і стабілізує його відносно змін параметрів LED. Резистор обирають із напруги живлення, очікуваного `V_f` за потрібного струму та цільового струму; також перевіряють потужність резистора й граничні параметри LED.[^aac-direct-current] Замість резистора можна застосувати драйвер, який регулює струм безпосередньо.[^aac-semiconductors]

Приклад розрахунку:

```text
V_supply = 5 V
V_f = 2 V; I = 10 mA = 0.01 A
R = (V_supply - V_f)/I = 300 Ω
P_R = I²*R = 0.03 W
```

Це ідеальний приклад; на практиці враховують розкид `V_f`, напруги живлення, допуск резистора та запас за потужністю. Типова помилка – вважати, що номінальна напруга LED сама обмежує струм.[^aac-direct-current]

Під час вибору перевіряють не лише типовий режим, а й найгірші умови: найбільшу напругу джерела разом із найменшим `V_f` дають найбільший струм, а найменшу напругу з найбільшим `V_f` – найменший. Для живлення від GPIO враховують його допустимий вихідний струм і падіння напруги під навантаженням. Якщо потрібна яскравість за широкого діапазону живлення, стабілізатор струму зазвичай дає кращий контроль, але також має власні межі напруги та розсіювання потужності.[^aac-direct-current]

## Sources

<!-- generated from frontmatter -->
