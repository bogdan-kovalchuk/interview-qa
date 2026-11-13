---
id: emb-elintro-0295
title: "Why do antiparallel LEDs still need a resistor?"
track: electronics
section: introduction
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-direct-current
    title: "All About Circuits textbook, Volume I: DC"
    url: https://www.allaboutcircuits.com/textbook/direct-current/
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
  - source_id: ti-led-resistor
    title: "Texas Instruments: AN-1293 Driving RGB LED Using LP3936"
    url: https://www.ti.com/jp/lit/pdf/snva071
  - source_id: kingbright-led-ratings
    title: "Kingbright: 2022–2023 Catalog, Technical Notes"
    url: https://www.kingbrightusa.com/webimages/2021/ecatalog/files/basic-html/page63.html
---

## Short answer

An antiparallel connection determines which LED conducts for each polarity, but it does not limit the forward current. A series resistor sets the current to approximately `(V_supply - V_f)/R` and protects the conducting LED from overcurrent.[^ti-led-resistor]

## Detailed explanation

In an antiparallel pair, one LED conducts in the forward direction under one polarity, and the other conducts under the opposite polarity. However, an LED exhibits a non-linear current-voltage characteristic: a small voltage increase above its forward drop can cause a sharp surge in current. The mere fact that the pair alternates which LED conducts does nothing to limit current.[^ti-led-resistor]

A resistor connected in series with the pair limits current in both polarities. For a given supply polarity, the estimated current is `I = (V_supply - V_f)/R`, where `V_f` is the forward voltage drop of the currently conducting LED. For the reverse polarity, substitute the forward drop of the second LED. Because their `V_f` values may differ, the forward currents in each direction may also differ.[^ti-led-resistor]

Example: with a 5 V source, `V_f = 2 V`, and a 330 Ω resistor, the circuit current is approximately 9.1 mA. This assumes a stable supply voltage and nominal resistor value; practical circuit design must account for power supply fluctuations, resistor tolerance, forward voltage spreads of both LEDs, and maximum continuous current ratings.[^ti-led-resistor]

**Common mistake:** connecting an antiparallel LED pair directly across a voltage source without current limiting. The conducting LED can easily exceed its maximum safe operating limits. Also verify the reverse voltage rating of the non-conducting LED in its datasheet; while the series resistor limits circuit current, it does not by itself guarantee a safe reverse voltage under all fault conditions.[^kingbright-led-ratings]

Thus, a series resistor is required for both current directions, with its value selected based on supply voltage, diode parameters, and desired luminous intensity. For AC or switched signals, the resistor power rating and switching characteristics must also be verified.
