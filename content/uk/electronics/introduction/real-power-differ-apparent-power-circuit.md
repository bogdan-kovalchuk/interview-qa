---
id: emb-elintro-0098
title: "Чим активна потужність відрізняється від повної в `AC`-колі?"
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
  - source_id: aac-ac-power
    title: "True, Reactive, and Apparent Power"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-11/true-reactive-and-apparent-power/
---

## Short answer

Активна потужність `P` – це середня за період потужність, що передає енергію в інші форми, наприклад тепло або механічну роботу; її вимірюють у `W`. Повна потужність `S = V_rms*I_rms` вимірюється у `VA` і задає добуток діючих значень напруги та струму; для синусоїдального режиму `P = S*cos(φ)`, де `φ` – фазовий зсув.[^aac-ac-power]

## Detailed explanation

Активна потужність `P` – це середнє значення миттєвої потужності за період, тобто швидкість, з якою електрична енергія переходить у тепло, механічну роботу чи іншу невідновлювану форму.[^aac-ac-power] У синусоїдальному колі її можна записати як `P = V_rms*I_rms*cos(φ)`, де `φ` – кут між фазами напруги та струму. Одиниця активної потужності – ват (`W`).[^aac-ac-power]

Повна потужність `S = V_rms*I_rms` вимірюється у вольт-амперах (`VA`). Вона описує навантаження, яке джерело, проводи й трансформатори мають передати за заданих діючих напруги та струму. Для лінійного синусоїдального кола реактивна потужність `Q` описує періодичний обмін енергією між джерелом і магнітним чи електричним полем; її одиниця – `var`. Для такого режиму величини пов’язані трикутником потужностей: `S^2 = P^2 + Q^2`, а `P = S*cos(φ)`.[^aac-ac-power]

Приклад: якщо `V_rms = 120 V`, `I_rms = 2 A`, а `cos(φ) = 0.5`, то `S = 240 VA`, але `P = 120 W`. Різниця не означає, що решта `120` одиниць є ватами, які зникли: струм створює періодичний енергетичний обмін, який враховується як `Q`; реальне навантаження та втрати також можуть споживати активну потужність. Розрахунок припускає синусоїдальні напругу й струм; при спотворених формах хвилі простий косинус фазового зсуву може не описувати повністю power factor.[^aac-ac-power]

**Типова помилка:** називати `VA` активною потужністю або прирівнювати `S` до `P` без умови `cos(φ) = 1`. Для суто резистивного навантаження напруга й струм синфазні, тому `P = S`; у реактивному навантаженні ці величини відрізняються.
