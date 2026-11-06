---
id: emb-elee-0155
title: "Does an LDO make linear conversion efficient, for example 12 V -> 3.3 V?"
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
---

## Short answer

No. A low dropout voltage only allows operation with a small input-to-output headroom; it does not improve conversion efficiency across wide spreads. All load current passes through the regulator pass device, dissipating approximately `P = (V_in - V_out)*I_out`, with efficiency fundamentally limited by `V_out/V_in`. Stepping 12 V down to 3.3 V yields around 27.5% efficiency, with the remaining power wasted as heat.[^ti-slva079]

## Detailed explanation

TODO
