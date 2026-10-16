---
id: emb-elintro-0006
title: Яка функція діода?
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
  - source_id: vishay-diode
    title: "Vishay 1N4001-1N4007 rectifier datasheet"
    url: https://www.vishay.com/docs/88503/1n4001.pdf
---

## Short answer

Rectifier diode проводить переважно від anode до cathode за forward bias та блокує більшість струму за reverse bias в межах своїх ratings. Реальні діоди мають forward voltage та reverse leakage; `V_RRM` – максимальна повторювана пікова зворотна напруга, а не поріг нульового струму. [^vishay-diode]

## Detailed explanation

Forward bias означає, що anode достатньо позитивний відносно cathode для потрібного струму. Forward current сильно нелінійно залежить від напруги; діод не є сталим резистором чи ідеальним switch. Його forward drop залежить від струму, температури й технології компонента.

Reverse bias значно зменшує провідність звичайного rectifier, але не усуває її. Datasheet Vishay 1N4001-1N4007 задає максимальний reverse leakage за rated blocking voltage: 5 µA при 25 °C та 50 µA при 125 °C. Ці rating і температура стосуються саме цієї сім’ї, а не всіх діодів. [^vishay-diode]

В ideal-diode задачі можна наближено вважати forward conduction коротким замиканням, а reverse conduction – розривом. Це наближення потрібно назвати явно. Для hardware обирайте forward-current, reverse-voltage і thermal ratings та враховуйте transient/recovery behavior. Breakdown не слід вважати штатним режимом rectifier лише тому, що деякі інші типи діодів навмисно працюють у ньому.
