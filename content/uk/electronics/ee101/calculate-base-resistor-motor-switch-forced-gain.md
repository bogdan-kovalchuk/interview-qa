---
id: emb-elee-0220
title: "Як розрахувати базовий резистор для ключа двигуна 100 мА з примусовим коефіцієнтом 10 при керуванні 5 В?"
description: "Як розрахувати базовий резистор для ключа двигуна 100 мА з примусовим коефіцієнтом 10 при керуванні 5 В?"
track: electronics
section: ee101
level: junior
type: concept
tags: []
status: published
updated: 2026-10-14
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
    applicability: "Походження питання: лекція 73, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-14; курс не є доказом цих тверджень."
  - source_id: aac-alternating-current
    title: "All About Circuits textbook, Volume II: AC"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: AC-кола, реактивний опір, фазори, імпеданс, фільтри й трансформатори; конкретні номінали й схеми курсу можуть відрізнятися."
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: діоди, стабілітрони, біполярні й польові транзистори та джерела живлення; конкретні номінали й схеми курсу можуть відрізнятися."
  - source_id: rohm-bjt-basics
    title: "ROHM: Bipolar Junction Transistor (BJT) Basics: Operation and Applications (NPN & PNP)"
    url: https://techweb.rohm.com/product/transistors-diodes/transistors/27319/
    accessed: 2026-10-14
    kind: official
    version: "2026.02.17"
    applicability: "Посібник виробника ROHM: умова I_B ≥ I_C/β_forced; β_forced обирають нижче мінімального h_FE з паспорта (типова відправна точка 5–10); для кремнієвих NPN типові V_BE 0,7–0,9 В у насиченні та V_CE нижче 0,3 В. Значення типові й залежать від приладу та струму; паспорт конкретного транзистора має пріоритет."
  - source_id: mit-6071-bjt-notes
    title: "MIT OCW 6.071/22.071 (Spring 2006): Transistors: Bipolar Junction Transistors (BJT), lecture notes"
    url: "https://ocw.mit.edu/courses/6-071j-introduction-to-electronics-signals-and-measurement-spring-2006/b30aa58fb0c9915da21e5a5855384818_19_bjt_1.pdf"
    accessed: 2026-10-14
    kind: book
    version: "Spring 2006"
    applicability: "Лекційні нотатки університетського курсу: у насиченні база–колекторний перехід прямий, а зв’язок між I_C і I_B нелінійний. Не документ виробника; конкретні транзистори можуть відрізнятися."
---

## Short answer

Базовий струм `I_B` має бути не меншим за `I_C`/`β_forced` = 100 мА / 10 = 10 мА.[^rohm-bjt-basics] Тоді `R_B` = (5-0.8)/0.01 ≈ 420 Ом, де `V_BE` = 0,8 В лежить у межах 0,7–0,9 В для насичення.[^rohm-bjt-basics] Значення `β_forced` має бути нижчим за мінімальне `h_FE` з паспорта при цьому струмі.[^rohm-bjt-basics] Джерело сигналу при 5 В має віддавати 10 мА.

## Detailed explanation

Ключ працює в насиченні: двигун отримує живлення майже повністю, а транзистор лише пропускає струм. Щоб утримати транзистор у насиченні, базовий струм має бути достатнім. У насиченні зв’язок між `I_C` і `I_B` стає нелінійним, а база–колекторний перехід відкривається.[^mit-6071-bjt-notes] Тому базовий струм задають не через типове β активного режиму, а через примусовий коефіцієнт `β_forced`, який обирають нижче мінімального `h_FE` з паспорта. Типова відправна точка – 5–10, тож `β_forced` = 10 уже на верхній межі.[^rohm-bjt-basics]

Базовий резистор задає струм від керуючого виходу з напругою `V_drive` = 5 В: `R_B` = (`V_drive`-`V_BE`)/`I_B`. Для `V_BE` = 0,8 В маємо `R_B` = (5-0.8)/0.01 = 420 Ом. Межі 0,7–0,9 В дають `R_B` = 430 Ом і 410 Ом, тобто розкид ±10 Ом, близько 2,4 %. Якщо округлити до 430 Ом, `I_B` ≈ 9,8 мА і `β_forced` ≈ 10,2, тобто запасу майже немає. Округлення вниз, наприклад до 390 Ом, дає `I_B` ≈ 10,8 мА і `β_forced` ≈ 9,3.

Розрахунок справедливий лише тоді, коли транзистор справді насичений. Тоді `V_CE` мале: за даними ROHM типово нижче 0,3 В, а втрати `V_CE`*`I_C` невеликі.[^rohm-bjt-basics] Якщо фактичне `h_FE` при 100 мА нижче `β_forced`, 10 мА дають менше 100 мА, транзистор не насичується, і `V_CE` та втрати зростають. Резистор задає `I_B`, а не `I_C`: струм двигуна визначає навантаження, тому при іншому струмі, наприклад пусковому (див. `qid:emb-elee-0221`), базовий струм і `R_B` треба перераховувати.

**Типові помилки:**

- Брати `h_FE` з паспорта як `β_forced` без запасу: тоді транзистор стоїть на межі насичення.
- Рахувати `R_B` за типовим β активного режиму: при β = 100 вийде 1 мА, а не 10 мА (див. `qid:emb-elee-0221`).
- Не перевіряти `V_CE` за паспортом після розрахунку: сам `R_B` не доводить насичення.

## Sources

<!-- generated from frontmatter -->
