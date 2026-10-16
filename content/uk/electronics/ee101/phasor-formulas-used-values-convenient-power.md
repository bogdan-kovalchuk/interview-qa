---
id: emb-elee-0066
title: "Коли можна використовувати фазорні формули і які значення зручні для потужності?"
track: electronics
section: ee101
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), картки курсу"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-alternating-current
    title: "All About Circuits textbook, Volume II: AC"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/
  - source_id: aac-single-frequency-phasors
    title: "All About Circuits: Introduction to Complex Numbers"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-2/introduction-to-complex-numbers/
  - source_id: aac-ac-rms
    title: "All About Circuits: Measurements of AC Magnitude"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-1/measurements-ac-magnitude
  - source_id: aac-power-phase
    title: "All About Circuits: Power in Resistive and Reactive AC Circuits"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-11/power-resistive-reactive-ac-circuits/
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
---

## Short answer

Фазорні формули застосовують до усталених синусоїдальних величин однієї частоти; різні частоти треба аналізувати окремо. Для звичних формул потужності зручно брати RMS-значення, але вони не замінюють умову синусоїдального режиму.[^aac-single-frequency-phasors] [^aac-ac-rms]

## Detailed explanation

Фазор – це комплексне подання амплітуди синусоїди та її фази відносно спільного часового відліку. Воно перетворює диференційні співвідношення елементів кола на алгебричні: наприклад, індуктивність та ємність подаються частотно-залежними імпедансами. Це спрощення коректне для лінійного кола в усталеному синусоїдальному режимі; для кожної частоти потрібен окремий розрахунок.[^aac-single-frequency-phasors]

Перехідний процес після перемикання, нелінійний елемент або суміш частот не описуються одним фазором. У таких випадках розглядають окремі гармоніки, часові рівняння чи нелінійний аналіз. Якщо величини задані як пікові, усі розрахункові напруги й струми лишаються піковими; якщо задані як RMS – розрахунок через імпеданс дає RMS. Не можна змішувати різні домовленості про амплітуду.[^aac-single-frequency-phasors] [^aac-ac-rms]

Для синусоїдальних напруги й струму середню активну потужність обчислюють як `P = V_RMS*I_RMS*cos(φ)`, де `φ` – кут між напругою та струмом. Добуток RMS сам по собі дає повну потужність у вольт-амперах, а коефіцієнт `cos(φ)` враховує фазовий зсув. Для несинусоїдальної форми RMS усе ще має значення для нагрівання резистора, але наведена проста формула активної потужності може бути недостатньою.[^aac-power-phase] [^aac-ac-rms]

**Типові помилки:**

- Застосовувати один фазор до сигналів різних частот або під час перехідного процесу.
- Плутати пікове значення з RMS і отримувати помилку масштабу.
- Називати `V_RMS*I_RMS` активною потужністю, не врахувавши коефіцієнт потужності.[^aac-single-frequency-phasors] [^aac-ac-rms]
