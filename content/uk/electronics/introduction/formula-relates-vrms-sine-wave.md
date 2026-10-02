---
id: emb-elintro-0083
title: "Яка формула пов'язує `V_rms` і `V_pp` для синусоїди?"
description: "Формула для переходу між RMS та peak-to-peak напругою чистої синусоїди."
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
    applicability: "Походження питання: лекція 9, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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
  - source_id: aac-ac-magnitude
    title: "All About Circuits: Measurements of AC Magnitude"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-1/measurements-ac-magnitude/
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: "Визначає RMS, пікову та peak-to-peak амплітуди; сталі співвідношення наведені для чистої синусоїди."
---


## Short answer

Для чистої синусоїди `V_rms = V_pp/(2*sqrt(2))`, або приблизно `0.3536*V_pp`; обернено, `V_pp = 2*sqrt(2)*V_rms` (приблизно `2.828*V_rms`). Це співвідношення не є загальним для довільної форми сигналу.[^aac-ac-magnitude]

## Detailed explanation

RMS (root mean square) – це ефективне значення змінної напруги: така сама напруга постійного струму виділяла б на резисторі таку саму середню потужність. Для чистої синусоїди з нульовим середнім значенням пікове значення `V_peak` у `sqrt(2)` раза більше за RMS, а розмах від від’ємного до додатного піка дорівнює `V_pp = 2*V_peak`. Поєднавши ці два означення, отримуємо `V_rms = V_pp/(2*sqrt(2))`.[^aac-ac-magnitude]

Коефіцієнт залежить від форми хвилі, а не лише від назви «AC». Для прямокутного, обрізаного чи спотвореного сигналу потрібно обчислити RMS з форми хвилі або скористатися True-RMS приладом у його діапазоні частот і crest factor. Звичайний прилад, відкалібрований для синусоїди, може показувати хибне RMS для іншої форми сигналу.[^aac-ac-magnitude]

Приклад: для синусоїди з `V_pp = 10 V` пікова амплітуда дорівнює `5 V`, а RMS становить приблизно `5/sqrt(2) = 3.54 V`. Типова помилка – застосувати цей множник до peak-to-peak сигналу без ділення на два, або використати його для прямокутної хвилі. Перед перерахунком з’ясуйте, чи подане значення є піковим, peak-to-peak або RMS.[^aac-ac-magnitude]

## Sources

<!-- generated from frontmatter -->
