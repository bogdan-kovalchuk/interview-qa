---
id: emb-elee-0068
title: "У якій формі зручніше додавати, а в якій множити й ділити комплексні числа?"
description: "У якій формі зручніше додавати, а в якій множити й ділити комплексні числа?"
track: electronics
section: ee101
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
    applicability: "Походження питання: лекція 43, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
  - source_id: aac-alternating-current
    title: "All About Circuits textbook, Volume II: AC"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: AC-кола, реактивний опір, фазори, імпеданс, фільтри й трансформатори; конкретні номінали й схеми курсу можуть відрізнятися."
  - source_id: aac-complex-arithmetic
    title: "All About Circuits: Complex Number Arithmetic"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-2/complex-number-arithmetic/
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: "Правила додавання та віднімання в прямокутній формі, множення й ділення в полярній формі."
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: діоди, стабілітрони, біполярні й польові транзистори та джерела живлення; конкретні номінали й схеми курсу можуть відрізнятися."
---

## Short answer

Додавати й віднімати зручно у прямокутній формі, покомпонентно. Множити й ділити зручно в полярній: модулі перемножують або ділять, а кути додають або віднімають. Множення на `j` обертає комплексне число на `+90°`, а на `-j` – на `-90°`.[^aac-complex-arithmetic]

## Detailed explanation

У прямокутній формі `a + jb` комплексне число задане двома координатами. Під час додавання треба скласти відповідні координати: `(a + jb) + (c + jd) = (a + c) + j(b + d)`. Той самий покомпонентний принцип працює для віднімання. Тому ця форма зручна, коли величини треба скласти, наприклад, для знаходження повного імпедансу послідовних компонентів.[^aac-complex-arithmetic]

У полярній формі число задають модулем і кутом, `r∠θ`. При множенні результат має модуль, що дорівнює добутку модулів, і кут, що дорівнює сумі кутів; при діленні модулі ділять, а кут знаменника віднімають. Це зручно для фазорних співвідношень на кшталт `I = V/Z`. Якщо операція поєднує додавання та множення, часто доводиться конвертувати форму між кроками.[^aac-complex-arithmetic]

Множення на `j` еквівалентне повороту на `+90°`, оскільки `j = 1∠90°`; множення на `-j` повертає на `-90°`. Це стосується комплексної площини та алгебри фазорів, а не механічного повороту реального компонента. У розрахунках важливо не змішувати градуси й радіани в калькуляторі та зберігати квадрант під час конвертації прямокутної форми в полярну.[^aac-complex-arithmetic]

Приклад: `3 + j4` і `1 - j2` легко додати в прямокутній формі: `4 + j2`. Щоб перемножити їх, можна перевести обидва числа в полярну форму або скористатися розкриттям дужок. Перевірка результату в іншій формі допомагає виявити помилку знака уявної координати чи кута.[^aac-complex-arithmetic]

**Типові помилки:**

- Додавати полярні модулі й кути як звичайні координати.
- Під час ділення віднімати кут чисельника від кута знаменника замість навпаки.
- Вважати, що `j` додає фазу незалежно від множення.[^aac-complex-arithmetic]

## Sources

<!-- generated from frontmatter -->
