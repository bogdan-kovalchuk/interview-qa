---
id: emb-elcmproj-0038
title: "How does LDO dropout voltage determine usable device battery lifespan?"
track: electronics
section: circuitmaker-projects
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), картки курсу"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: circuitmaker-docs
    title: "CircuitMaker documentation"
    url: https://www.altium.com/documentation/altium-circuitmaker
  - source_id: ti-ldo-definitions
    title: "Texas Instruments: Understanding the Terms and Definitions of LDO Voltage Regulators (SLVA079)"
    url: https://www.ti.com/lit/an/slva079/slva079.pdf
  - source_id: ti-lm2940-datasheet
    title: "Texas Instruments: LM2940 1A Low Dropout Regulator Datasheet"
    url: https://www.ti.com/lit/ds/symlink/lm2940-n.pdf
---

## Short answer

The minimum regulated input voltage is governed by `V_in(min) = V_out + V_DO`. Lowering `V_DO` allows the device to continue operating along the flat plateau of the battery discharge curve below 7 V. A lithium 9 V battery maintains significantly flatter discharge voltage compared to a standard alkaline cell.[^udemy-electronics-course][^ti-ldo-definitions]

## Detailed explanation

TODO
