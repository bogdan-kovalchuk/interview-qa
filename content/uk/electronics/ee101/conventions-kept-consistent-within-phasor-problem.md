---
id: emb-elee-0071
title: "Які домовленості треба зберігати в одній фазорній задачі?"
description: "Які домовленості треба зберігати в одній фазорній задачі?"
track: electronics
section: ee101
level: junior
type: pitfall
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
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: діоди, стабілітрони, біполярні й польові транзистори та джерела живлення; конкретні номінали й схеми курсу можуть відрізнятися."
  - source_id: aac-phasor-conventions
    title: "All About Circuits: Simple AC Circuit Calculations"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-1/simple-ac-circuit-calculations/
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: "Підтримує вимогу виражати AC-величини в одному узгодженому форматі амплітуди; фазорний аналіз стосується синусоїд однакової частоти."
---

## Short answer

У межах одного фазорного розрахунку використовуйте спільне подання амплітуди – наприклад, усі значення RMS або всі пікові – і одну домовленість про фазу. Фазори безпосередньо описують синусоїдальні величини однієї частоти; складові різних частот аналізують окремо, а їхні миттєві сигнали підсумовують у часовій області.[^aac-phasor-conventions]

## Detailed explanation

Фазор – це комплексне подання амплітуди та фази синусоїдального сигналу на заданій частоті. Воно спрощує диференціальні співвідношення кола до алгебри з комплексними імпедансами, але всі напруги й струми в одному такому розрахунку мають відповідати тій самій частоті. Тому сума фазорів не описує суму синусоїд різних частот як один фазор.[^aac-phasor-conventions]

Виберіть одну форму хвилі як фазовий відлік, наприклад джерело з кутом 0°, і послідовно вимірюйте решту фаз від неї. Також використовуйте спільне значення амплітуди: RMS, peak або peak-to-peak. Можна перейти з одного виду в інший, але треба перетворити всі величини, а не частину з них. Для синусоїди `V_RMS = V_peak/sqrt(2)`, тож змішування RMS-джерела з піковою напругою на елементі створює помилку у відношеннях і перевірках.[^aac-phasor-conventions]

Наприклад, якщо резистор і конденсатор послідовно підключені до джерела 1 V RMS, задайте джерелу кут 0° і знайдіть обидві напруги як RMS-фазори. Їхня векторна сума має відтворити фазор джерела згідно із законом Кірхгофа; додавання лише модулів зазвичай не спрацює, бо напруги мають різні фази.[^aac-phasor-conventions]

**Типові помилки:**
- Додавати фазори різних частот без окремого частотного аналізу.
- Змішувати RMS і пікові значення в одному рівнянні.
- Змінювати фазовий відлік посеред розв’язання або додавати модулі замість комплексних величин.

Після розрахунку перевірте одиниці амплітуди, частоту кожного фазора й комплексну суму напруг у контурі.[^aac-phasor-conventions]

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
