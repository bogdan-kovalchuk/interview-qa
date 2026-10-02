---
id: emb-elintro-0088
title: "Чому значення мережі `230 V RMS` не означає, що максимум лише 230 V?"
description: "Чому значення мережі 230 V RMS не означає, що максимум лише 230 V?"
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
  - source_id: aac-rms
    title: "All About Circuits: Introduction to RMS Measurements"
    url: https://www.allaboutcircuits.com/textbook/designing-analog-chips/analog-measurements/introduction-to-rms-measurements/
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: "Підтверджує визначення RMS та співвідношення RMS і піка для синусоїди; допуски мережі й вимоги до перенапруг тут не визначено."
---

## Short answer

`RMS` – це ефективне значення, а не пікова напруга. Для чистої синусоїди `230 V RMS` відповідає приблизно `325 V` від нуля до піка та `650 V` від піка до піка, тому ізоляцію й компоненти добирають з урахуванням піків і перехідних перенапруг.[^aac-rms]

## Detailed explanation

Ефективне значення (RMS) змінної напруги визначають за її тепловою дією: це така напруга постійного струму, яка в резистивному навантаженні виділяє таку саму середню потужність. Тому RMS не є ані середнім значенням миттєвої синусоїди за повний період, ані її максимумом. Для чистої синусоїди пікове значення більше за RMS у `√2` раза.[^aac-rms]

Це співвідношення залежить від форми сигналу. Наприклад, для імпульсної або обрізаної напруги множник `√2` загалом непридатний; потрібне справжнє RMS-вимірювання або аналіз форми хвилі. Побутове позначення мережі `230 V` зазвичай означає номінальне RMS-значення синусоїдальної напруги, а не обіцянку, що миттєва напруга ніколи не перевищить 230 V.[^aac-rms]

**Приклад розрахунку:** для ідеальної синусоїди з `230 V RMS` пікова напруга дорівнює `230*√2 ≈ 325 V`. Розмах від негативного піка до позитивного дорівнює подвоєному піку, тобто приблизно `650 V` peak-to-peak. Реальна мережа має допуски й перехідні імпульси, тому ці числа не замінюють вимоги стандарту чи паспортний запас ізоляції.[^aac-rms]

**Типова помилка:** вибрати конденсатор або транзистор з межею лише трохи вище RMS-значення. У випрямлячі без навантаження конденсатор може зарядитися близько до піка, а короткі перенапруги додають окремий запас, який треба враховувати в проєкті.[^aac-rms]

## Sources

<!-- generated from frontmatter -->
