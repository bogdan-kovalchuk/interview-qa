---
id: emb-elee-0164
title: "A 7805 is fed from 9 V and loaded with 100 Ω. What are the current and powers?"
track: electronics
section: ee101
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-alternating-current
    title: "All About Circuits textbook, Volume II: AC"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
  - source_id: ti-slva079
    title: "Texas Instruments SLVA079: Understanding the Terms and Definitions of LDO Voltage Regulators"
    url: https://www.ti.com/lit/an/slva079/slva079.pdf
  - source_id: ti-ua78
    title: "TI: uA7805, uA7808, uA7810, uA7812, uA7815, uA7824 positive-voltage regulators (datasheet)"
    url: https://www.ti.com/lit/ds/symlink/ua78.pdf
---

## Short answer

Output is 5 V, so load current is `I = 5/100 = 0.05 A` (50 mA) and resistor dissipation is `P = V²/R = 25/100 = 0.25 W` (0.5 W rated for margin). The regulator dissipates `(9 - 5)*0.05 = 0.2 W`[^ti-slva079] plus `V_in*I_q`: per the uA7805 datasheet `I_q` is a few milliamps, adding tens of milliwatts.[^ti-ua78] At 50 Ω, load current, resistor power, and `(V_in - V_out)*I_out` double (0.1 A, 0.5 W, 0.4 W), while `V_in*I_q` stays constant.

## Detailed explanation

TODO
