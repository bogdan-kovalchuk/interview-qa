---
id: emb-elee-0157
title: "Where should power supply design start?"
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
  - source_id: ti-tps752q1-datasheet
    title: "Texas Instruments TPS752-Q1 datasheet"
    url: https://www.ti.com/lit/ds/symlink/tps752-q1.pdf
---

## Short answer

Start with requirements: output voltage, continuous and peak load currents, input voltage range, and permissible ripple. From these, estimate dissipation `P = (V_in - V_out)*I_out` to decide whether a linear regulator is viable. Then consult the IC datasheet to verify recommended operating conditions, dropout headroom, output capacitor stability requirements, and thermal constraints.[^ti-slva079][^ti-tps752q1-datasheet]

## Detailed explanation

TODO
