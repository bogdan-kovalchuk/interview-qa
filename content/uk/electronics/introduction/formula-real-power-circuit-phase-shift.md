---
id: emb-elintro-0093
title: "Формула активної потужності `AC`-кола з урахуванням зсуву фаз?"
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
  - source_id: aac-sinusoidal-real-power
    title: "All About Circuits: Sinusoidal Steady-State Power Calculations"
    url: https://www.allaboutcircuits.com/technical-articles/sinusoidal-steady-state-power-calculations/
  - source_id: aac-power-factor
    title: "All About Circuits: Calculating Power Factor"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-11/calculating-power-factor/
---

## Short answer

Для синусоїдальних напруги й струму середня активна потужність дорівнює `P = V_rms*I_rms*cos(phi)`, де `phi` – різниця їхніх фаз. Для ідеального резистора коефіцієнт дорівнює одиниці, а для ідеального реактивного навантаження середня активна потужність дорівнює нулю.[^aac-sinusoidal-real-power]

## Detailed explanation

Активна потужність `P` – це середнє за період значення миттєвої потужності `p(t) = v(t)*i(t)`. Для синусоїдальних напруги та струму зі значеннями RMS формула має вигляд `P = V_rms*I_rms*cos(phi)`, де `phi` є фазовою різницею між напругою і струмом. Добуток `V_rms*I_rms` сам по собі є повною потужністю, а множник `cos(phi)` показує, яка її частина припадає на середню активну потужність.[^aac-sinusoidal-real-power]

Якщо навантаження ідеально резистивне, струм і напруга синфазні, `phi = 0`, тож `cos(phi) = 1`; активна потужність дорівнює повній. В ідеальному індукторі або конденсаторі зсув становить 90°, тому середня активна потужність дорівнює нулю: енергія періодично накопичується в полі компонента та повертається до джерела. Реальні реактивні компоненти мають втрати, тому споживають певну активну потужність.[^aac-sinusoidal-real-power]

Приклад для синусоїдального кола: за `V_rms = 120 V`, `I_rms = 2 A` і `phi = 60°` активна потужність дорівнює `120*2*cos(60°) = 120 W`, тоді як повна потужність становить `240 VA`. Активну потужність вимірюють у ватах, повну – у вольт-амперах.[^aac-sinusoidal-real-power]

**Типова помилка:** підставляти пікові значення замість RMS без потрібного коефіцієнта або вважати, що одного фазового кута досить для будь-якого сигналу. Для несинусоїдальних форм хвилі активну потужність визначають як середнє `v(t)*i(t)`, але простий косинус кута між основними синусоїдами може бути недостатнім.[^aac-sinusoidal-real-power]
