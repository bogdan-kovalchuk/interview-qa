---
id: emb-elintro-0287
title: "Що таке reflow-профіль для SMD-пайки?"
description: "Що таке reflow-профіль для SMD-пайки?"
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
    applicability: "Походження питання: лекція 25, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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
  - source_id: indium-reflow-profile
    title: "Matching a Reflow Profile to a Solder Paste Spec"
    url: https://www.indium.com/blog/matching-a-reflow-profile-to-a-solder-paste-spec/
    accessed: 2026-10-04
    kind: official
    version: null
    applicability: "Пояснює порівняння ramp, time above liquidus, пікової температури й охолодження з конкретною специфікацією пасти Indium8.9HF; наведені числові межі стосуються саме цієї пасти."
---

## Short answer

Reflow-профіль описує зміну температури плати й компонентів у часі під час оплавлення паяльної пасти. Його параметри – швидкість нагрівання, можливе вирівнювання температури, пікова температура, час вище liquidus та охолодження – мають відповідати специфікації конкретної пасти й компонентів.[^indium-reflow-profile]

Цільові межі беруть зі специфікацій виробника пасти й компонентів, а не переносять автоматично між процесами.[^indium-reflow-profile]

## Detailed explanation

Reflow-профіль – це температурний графік, якого дотримуються під час нагрівання зібраної SMD-плати, щоб паста розплавилася й утворила паяні з’єднання, а деталі не перегрілися. У типовому процесі плата поступово нагрівається, може мати ділянку soak для вирівнювання температури, проходить вище liquidus пасти, а потім контрольовано охолоджується. Не кожна паста потребує окремої ділянки soak: це визначає її виробник.[^indium-reflow-profile]

Профіль важливий, бо одна й та сама піч може нагрівати різні плати по-різному. Великі мідні площини, масивні компоненти й розміщення на конвеєрі змінюють фактичний час і температуру в місцях з’єднань. Тому специфікація зазвичай обмежує швидкість ramp-up, час вище температури liquidus (TAL), пікову температуру та швидкість охолодження. Профіль перевіряють термопарами, закріпленими на платі, а не лише за заданою температурою печі.[^indium-reflow-profile]

Приклад розрахунку з профілю Indium для пасти Indium8.9HF: перетин liquidus відбувається на 3.1 хвилині, а охолодження нижче liquidus – на 4.4 хвилині. Отже, TAL становить 4.4 – 3.1 = 1.3 хвилини, тобто 78 секунд; виробник порівнює це значення з вимогами саме цієї пасти. Це не універсальна ціль для кожного сплаву чи компонента.[^indium-reflow-profile]

**Типові помилки:** переносити один числовий профіль на всі пасти або орієнтуватися лише на температуру печі. Спочатку звіряють технічний опис пасти й допустимий нагрів компонентів, потім вимірюють профіль реальної плати. Занадто короткий або холодний цикл може лишити неповністю сформовані з’єднання, а надмірний час чи пік здатні пошкодити деталі або флюс.[^indium-reflow-profile]

## Sources

<!-- generated from frontmatter -->
