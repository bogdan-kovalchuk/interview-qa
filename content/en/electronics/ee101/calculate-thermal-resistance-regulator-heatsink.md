---
id: emb-elee-0160
title: "How do you calculate the thermal resistance of a regulator with a heatsink?"
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
  - source_id: ti-sboa020
    title: "Texas Instruments (Burr-Brown) SBOA020 / AB-037: Mounting Considerations for TO-3 Packages"
    url: https://www.ti.com/lit/an/sboa020/sboa020.pdf
  - source_id: ti-lm340
    title: "TI: LM340, LM340A, LM7805 family wide VIN 1.5-A fixed voltage regulators (datasheet)"
    url: https://www.ti.com/lit/ds/symlink/lm340.pdf
  - source_id: ti-slva079
    title: "Texas Instruments SLVA079: Understanding the Terms and Definitions of LDO Voltage Regulators"
    url: https://www.ti.com/lit/an/slva079/slva079.pdf
  - source_id: ti-spra953
    title: "Texas Instruments SPRA953: Semiconductor and IC Package Thermal Metrics"
    url: https://www.ti.com/lit/pdf/spra953
---

## Short answer

Thermal resistance from junction to ambient is the sum of series thermal resistances: `θ_JA = θ_JC + θ_CS + θ_SA` (°C/W), representing junction-to-case, case-to-sink (interface material), and sink-to-ambient.[^ti-sboa020] Thermal paste lowers `θ_CS` relative to dry contact, whereas an electrical insulator generally adds higher `θ_CS` than paste alone.[^ti-sboa020] Electrical insulation is often mandatory because the regulator mounting tab connects to ground or output.[^ti-lm340]

## Detailed explanation

TODO
