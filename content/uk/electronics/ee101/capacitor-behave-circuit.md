---
id: emb-elee-0018
title: "Як конденсатор поводиться в колі постійного і змінного струму?"
description: "Як конденсатор поводиться в колі постійного і змінного струму?"
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
    applicability: "Походження питання: лекція 35, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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
  - source_id: aac-capacitor-transient
    title: "All About Circuits: Capacitor Transient Response"
    url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-16/capacitor-transient-response/
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: "Описує заряджання конденсатора в RC-колі, спадання струму та наближення до розімкненого кола в усталеному режимі."
  - source_id: aac-capacitor-reactance
    title: "All About Circuits: AC Capacitor Circuits"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-4/ac-capacitor-circuits/
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: "Пояснює реактивний опір ідеальної ємності та залежність від частоти; не описує всі втрати реального конденсатора."
---

## Short answer

Після перехідного процесу в ідеальному DC-колі конденсатор має сталу напругу й струм через нього дорівнює нулю, тобто він поводиться як розрив. Під час заряджання струм спадає з часом; в AC-колі напруга змінюється, тож конденсатор циклічно заряджається й розряджається, а його ідеальний реактивний опір зменшується зі зростанням частоти.[^aac-capacitor-transient] [^aac-capacitor-reactance]

## Detailed explanation

Конденсатор складається з двох провідних обкладок, розділених діелектриком, і зберігає енергію в електричному полі. Струм через його виводи пов’язаний зі швидкістю зміни напруги: коли напруга змінюється, накопичений заряд змінюється, тому в зовнішньому колі є струм. У простій RC-схемі з джерелом постійної напруги спочатку незаряджений конденсатор заряджається через резистор. Напруга на ньому поступово наближається до напруги джерела, а струм зменшується до нуля; процес не відбувається миттєво.[^aac-capacitor-transient]

Швидкість перехідного процесу задає стала часу `τ = R*C`, де `R` – опір, через який заряджається конденсатор, а `C` – ємність. Через одну сталу часу напруга конденсатора під час заряджання досягає приблизно 63 % різниці між початковим і кінцевим значеннями. Тому твердження «конденсатор блокує DC» стосується усталеного стану ідеального кола, а не моменту підключення. Реальний конденсатор має витік, ESR та обмеження за напругою, тому струм не обов’язково стає буквально нульовим.[^aac-capacitor-transient]

Приклад: якщо `R = 10 kΩ`, а `C = 100 µF`, то `τ = 1 s`. Після підключення до 5 V з нульового початкового заряду через одну секунду напруга на конденсаторі становить приблизно 3.16 V, а далі зростає до 5 V; струм у резистивній гілці відповідно спадає. Це пояснює затримки, фільтрування та згладжування змін напруги в RC-колах.[^aac-capacitor-transient]

Для синусоїдальної напруги конденсатор циклічно заряджається й розряджається, тож у зовнішньому колі тече змінний струм. В ідеальній моделі величина реактивного опору `X_C = 1/(2π*f*C)` зменшується, коли частота або ємність зростає. Це корисне наближення для аналізу AC, але на високих частотах паразитна індуктивність, а на низьких частотах витік і втрати можуть бути важливими; звіряйте діапазон із паспортом компонента.[^aac-capacitor-reactance]

**Типова помилка:** казати, що конденсатор завжди є розривом для постійного струму або що струм буквально проходить крізь ізоляційний шар. У колі є зарядний чи розрядний струм у провідниках, але після усталення ідеальний конденсатор не пропускає DC; реальний має малий струм витоку.[^aac-capacitor-transient]

## Sources

<!-- generated from frontmatter -->
