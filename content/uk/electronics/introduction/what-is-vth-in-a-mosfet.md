---
id: emb-elintro-0239
title: "Що таке `V_th` у MOSFET?"
description: "Що таке V_th у MOSFET?"
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
    applicability: "Походження питання: лекція 22, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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

`V_GS(th)` – напруга gate-source, виміряна за заданого малого drain current і тестових умов datasheet; вона не є напругою повного ввімкнення. Для низького `R_DS(on)` зазвичай потрібна більша `V_GS`, яку слід брати з умов специфікації конкретного MOSFET.[^aac-semiconductors]

## Detailed explanation

`V_GS(th)` – це порогова напруга між gate і source, але в datasheet вона визначається не абстрактним моментом «повного відкривання», а вимірюванням за конкретного малого drain current і заданих напруг та температури. Значення є характеристикою конкретного компонента й має допуск; у різних MOSFET тестовий струм та інші умови можуть відрізнятися.[^aac-semiconductors]

Поблизу порога канал лише починає проводити невеликий струм. Для роботи як силового ключа потрібно перевірити таблицю `R_DS(on)`: виробник гарантує цей опір за конкретного `V_GS` і `I_D`. Якщо мікроконтролер дає меншу напругу, ніж зазначено в таких умовах, мале типове значення опору не гарантоване. Також треба врахувати зміну характеристик із температурою та розкид між екземплярами.[^aac-semiconductors]

Наприклад, напис «threshold 2 V» не означає, що при 2 V транзистор уже проводить десятки ампер із малими втратами. Це лише поріг, виміряний за малим контрольним струмом. Для вибору драйвера порівнюють його напругу з умовами `R_DS(on)` і перевіряють граничне `V_GS(max)`, щоб не пошкодити затвор.[^aac-semiconductors]

**Типові помилки:**
- Трактувати `V_GS(th)` як рекомендовану напругу керування або повністю ввімкнений стан.
- Порівнювати пороги без тестових умов та допусків.
- Ігнорувати специфіковану напругу для `R_DS(on)` та абсолютну межу gate-source.

## Sources

<!-- generated from frontmatter -->
