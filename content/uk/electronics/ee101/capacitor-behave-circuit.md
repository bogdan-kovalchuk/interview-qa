---
id: emb-elee-0018
title: "Як конденсатор поводиться в колі постійного і змінного струму?"
track: electronics
section: ee101
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), картки курсу"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-alternating-current
    title: "All About Circuits textbook, Volume II: AC"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
  - source_id: aac-capacitor-transient
    title: "All About Circuits: Capacitor Transient Response"
    url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-16/capacitor-transient-response/
  - source_id: aac-capacitor-reactance
    title: "All About Circuits: AC Capacitor Circuits"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-4/ac-capacitor-circuits/
---

## Short answer

Після перехідного процесу в ідеальному DC-колі конденсатор має сталу напругу й струм через нього дорівнює нулю, тобто він поводиться як розрив. Під час заряджання струм спадає з часом; в AC-колі напруга змінюється, тож конденсатор циклічно заряджається й розряджається, а його ідеальний реактивний опір зменшується зі зростанням частоти.[^aac-capacitor-transient] [^aac-capacitor-reactance]

## Detailed explanation

Конденсатор складається з двох провідних обкладок, розділених діелектриком, і зберігає енергію в електричному полі. Струм через його виводи пов’язаний зі швидкістю зміни напруги: коли напруга змінюється, накопичений заряд змінюється, тому в зовнішньому колі є струм. У простій RC-схемі з джерелом постійної напруги спочатку незаряджений конденсатор заряджається через резистор. Напруга на ньому поступово наближається до напруги джерела, а струм зменшується до нуля; процес не відбувається миттєво.[^aac-capacitor-transient]

Швидкість перехідного процесу задає стала часу `τ = R*C`, де `R` – опір, через який заряджається конденсатор, а `C` – ємність. Через одну сталу часу напруга конденсатора під час заряджання досягає приблизно 63 % різниці між початковим і кінцевим значеннями. Тому твердження «конденсатор блокує DC» стосується усталеного стану ідеального кола, а не моменту підключення. Реальний конденсатор має витік, ESR та обмеження за напругою, тому струм не обов’язково стає буквально нульовим.[^aac-capacitor-transient]

Приклад: якщо `R = 10 kΩ`, а `C = 100 µF`, то `τ = 1 s`. Після підключення до 5 V з нульового початкового заряду через одну секунду напруга на конденсаторі становить приблизно 3.16 V, а далі зростає до 5 V; струм у резистивній гілці відповідно спадає. Це пояснює затримки, фільтрування та згладжування змін напруги в RC-колах.[^aac-capacitor-transient]

Для синусоїдальної напруги конденсатор циклічно заряджається й розряджається, тож у зовнішньому колі тече змінний струм. В ідеальній моделі величина реактивного опору `X_C = 1/(2π*f*C)` зменшується, коли частота або ємність зростає. Це корисне наближення для аналізу AC, але на високих частотах паразитна індуктивність, а на низьких частотах витік і втрати можуть бути важливими; звіряйте діапазон із паспортом компонента.[^aac-capacitor-reactance]

**Типова помилка:** казати, що конденсатор завжди є розривом для постійного струму або що струм буквально проходить крізь ізоляційний шар. У колі є зарядний чи розрядний струм у провідниках, але після усталення ідеальний конденсатор не пропускає DC; реальний має малий струм витоку.[^aac-capacitor-transient]
