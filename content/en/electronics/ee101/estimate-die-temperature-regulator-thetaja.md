---
id: emb-elee-0159
title: "How do you estimate the die temperature of a linear 12 V -> 5 V regulator at 0.2 A if `theta_JA` = 60 °C/W and `T_a` = 25 °C?"
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
  - source_id: ti-spra953d
    title: "Texas Instruments SPRA953D: Semiconductor and IC Package Thermal Metrics"
    url: https://www.ti.com/lit/an/spra953d/spra953d.pdf
---

## Short answer

For a linear regulator, power dissipation is `P = (12 - 5)*0.2 = 1.4 W`, yielding `T_j = T_a + P*theta_JA = 25 + 1.4*60 = 109 °C`.[^ti-slva079][^ti-spra953d] Compare this estimate against the datasheet maximum junction temperature with appropriate safety margin.[^ti-slva079] Because `theta_JA` depends heavily on PCB copper area and airflow, this is an estimate rather than a fixed universal constant.[^ti-spra953d]

## Detailed explanation

TODO
