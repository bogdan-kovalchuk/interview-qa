---
id: emb-elintro-0084
title: "Який зв'язок між `V_peak`, `V_pp` і `V_rms` для синусоїди?"
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

Для чистої синусоїди `V_pp = 2*V_peak`, а `V_rms = V_peak/sqrt(2)`. Отже, `230 V RMS` відповідає піку приблизно `325 V`; ці співвідношення не застосовують до довільної форми сигналу.[^aac-ac-magnitude]

## Detailed explanation

Для синусоїди з нульовим середнім `V_peak` – найбільша миттєва напруга відносно нуля, тоді як `V_pp` – повна відстань від мінімуму до максимуму. Симетрична хвиля має від’ємний пік `-V_peak` і додатний `+V_peak`, тому `V_pp = 2*V_peak`. RMS визначається як квадратний корінь із середнього квадрата миттєвої напруги за період; для синусоїди це дає `V_rms = V_peak/sqrt(2)`.[^aac-ac-magnitude]

Ці величини описують різні аспекти одного сигналу. Peak-to-peak корисний для перевірки, чи сигнал поміщається в діапазон входу, а RMS пов’язаний із нагріванням резистивного навантаження. У формулах мається на увазі симетрична чиста синусоїда без DC-зсуву; якщо хвиля має зсув, асиметрію чи спотворення, загальна RMS величина вже не визначається одним лише `V_peak`.[^aac-ac-magnitude]

Приклад: для синусоїди `230 V RMS` амплітуда `V_peak = 230*sqrt(2) ≈ 325 V`, а `V_pp ≈ 650 V`. Номінальне RMS значення мережі не означає, що миттєва напруга весь час дорівнює 230 V; вона змінюється між піками. Типова помилка – називати 230 V піковою напругою або плутати `V_pp` із відстанню від нуля до одного піка.[^aac-ac-magnitude]
