---
id: emb-elintro-0083
title: "Яка формула пов’язує `V_rms` і `V_pp` для синусоїди?"
track: electronics
section: introduction
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), картки курсу"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-direct-current
    title: "All About Circuits textbook, Volume I: DC"
    url: https://www.allaboutcircuits.com/textbook/direct-current/
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
  - source_id: aac-ac-magnitude
    title: "All About Circuits: Measurements of AC Magnitude"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-1/measurements-ac-magnitude/
---

## Short answer

Для чистої синусоїди `V_rms = V_pp/(2*sqrt(2))`, або приблизно `0.3536*V_pp`; обернено, `V_pp = 2*sqrt(2)*V_rms` (приблизно `2.828*V_rms`). Це співвідношення не є загальним для довільної форми сигналу.[^aac-ac-magnitude]

## Detailed explanation

RMS (root mean square) – це ефективне значення змінної напруги: така сама напруга постійного струму виділяла б на резисторі таку саму середню потужність. Для чистої синусоїди з нульовим середнім значенням пікове значення `V_peak` у `sqrt(2)` раза більше за RMS, а розмах від від’ємного до додатного піка дорівнює `V_pp = 2*V_peak`. Поєднавши ці два означення, отримуємо `V_rms = V_pp/(2*sqrt(2))`.[^aac-ac-magnitude]

Коефіцієнт залежить від форми хвилі, а не лише від назви «AC». Для прямокутного, обрізаного чи спотвореного сигналу потрібно обчислити RMS з форми хвилі або скористатися True-RMS приладом у його діапазоні частот і crest factor. Звичайний прилад, відкалібрований для синусоїди, може показувати хибне RMS для іншої форми сигналу.[^aac-ac-magnitude]

Приклад: для синусоїди з `V_pp = 10 V` пікова амплітуда дорівнює `5 V`, а RMS становить приблизно `5/sqrt(2) = 3.54 V`. Типова помилка – застосувати цей множник до peak-to-peak сигналу без ділення на два, або використати його для прямокутної хвилі. Перед перерахунком з’ясуйте, чи подане значення є піковим, peak-to-peak або RMS.[^aac-ac-magnitude]
