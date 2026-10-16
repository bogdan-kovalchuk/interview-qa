---
id: emb-elintro-0015
title: Яка функція мультиметра – що він вимірює?
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
  - source_id: fluke-meter
    title: "Fluke 3000 FC Users Manual"
    url: https://media.fluke.com/437e18a0-de4d-4090-ab8a-b0df016de4fd_original%20file.pdf
---

## Short answer

Multimeter поєднує voltage, current і resistance measurement; багато моделей також мають continuity, diode test, capacitance чи frequency. Доступні functions, terminals, ranges та limits залежать від моделі. Для кожного вимірювання використовуйте правильні function і connection. [^fluke-meter]

## Detailed explanation

Voltage вимірюють між двома вузлами; current – послідовно в гілці. Resistance вимірюють test stimulus приладу, тому перед resistance measurement вимкніть живлення кола й розрядіть конденсатори. Один display може показувати дуже різні величини, оскільки meter перемикає input circuitry між functions. [^fluke-meter]

Continuity – зручна threshold-based indication, а не precision resistance measurement. Diode test показує junction voltage за test conditions приладу, а не maximum current діода чи повні datasheet characteristics. Capacitance і frequency – приклади додаткових capabilities: звертайтеся до actual manual замість припущення, що кожен прилад їх має. [^fluke-meter]

Auto-ranging може обрати measurement range, але не виправляє неправильні function, lead jack чи небезпечне connection. Measurement resolution також відрізняється від accuracy: більше digits на display не означають автоматично точніше вимірювання. Для змістовного результату перевірте specified accuracy, input impedance, допустиму waveform і rating для потрібного застосування.
