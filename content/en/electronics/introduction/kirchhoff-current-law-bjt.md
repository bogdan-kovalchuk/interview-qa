---
id: emb-elintro-0199
title: "What is Kirchhoff's current law for a `BJT`?"
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
---
## Short answer

According to Kirchhoff's current law, the sum of currents entering any node equals the sum of currents leaving it. For standard BJT operation with consistent current reference directions, this yields `I_E = I_C + I_B`; the approximation `I_E ≈ I_C` is permissible only when `I_B` is indeed small compared to `I_C`.[^aac-semiconductors]

## Detailed explanation

Kirchhoff's current law (KCL) is a consequence of conservation of electric charge: charge does not accumulate indefinitely at a node, so the algebraic sum of currents at that node is zero. For the three terminals of a transistor, this relationship links the emitter, collector, and base currents.[^aac-semiconductors]

If you define the emitter current as entering the transistor and the base and collector currents as leaving it, this gives `I_E = I_B + I_C`. For NPN and PNP, the physical current directions are different; the equation remains valid under consistently chosen signs and reference directions. You should not mechanically substitute current magnitudes if the chosen sign convention defines different directions.[^aac-semiconductors]

Because `I_B` is much smaller than `I_C` in many operating modes, you can assume `I_E ≈ I_C` for a rough estimate. However, this approximation introduces an error roughly equal to the base current fraction. For accurate power balance, measurement, or bias calculations, the base current must be included.[^aac-semiconductors]

Example: if `I_B = 0.02 mA` and `I_C = 2.00 mA`, the node law gives `I_E = 2.02 mA`. The approximation would yield 2.00 mA, which is an error of about 1% relative to the exact emitter current value. This is an assumption, not a different law.[^aac-semiconductors]

**Common mistakes:** writing `I_E = I_C - I_B` with inconsistent reference directions; assuming `I_E` equals `I_C` without qualification; forgetting the base current in precise calculations.[^aac-semiconductors]
