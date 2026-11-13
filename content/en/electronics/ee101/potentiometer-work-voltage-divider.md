---
id: emb-elee-0012
title: "How does a potentiometer work as a voltage divider?"
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
  - source_id: bourns-potentiometer
    title: "Bourns: 3386 Trimpot Trimming Potentiometer Datasheet"
    url: https://bourns.com/docs/Product-Datasheets/3386.pdf
---

## Short answer

The outer terminals of the potentiometer connect to `V_in` and GND, with the output taken from the wiper. For an unloaded ideal divider, `V_out = V_in*R_2/(R_1+R_2)`, where `R_1+R_2 = R_total`; thus, the output varies between the voltages at the outer terminals. Output loading alters this voltage division, so the unloaded formula does not always describe a real circuit.[^bourns-potentiometer]

## Detailed explanation

A potentiometer operates as a voltage divider when voltage is applied across its outer terminals and the output is taken from the movable wiper contact. The wiper divides the resistive track into two segments: `R_1` from the high end to the contact and `R_2` from the contact to ground. In the absence of load, the same current flows through both segments, so the output voltage is determined by the ratio of the lower segment's resistance to the total resistance.[^bourns-potentiometer]

When the outer terminal voltages are `V_in` and `0 V`, an ideal potentiometer yields `V_out = V_in*R_2/(R_1+R_2)`. Moving the wiper increases `R_1` while decreasing `R_2` or vice versa, depending on which terminal is chosen as reference. At the extreme positions, the output approaches the voltage of the corresponding end terminal, but contact and residual end resistance may prevent reaching exactly zero or the full supply rail.[^bourns-potentiometer]

Calculation example:

```text
V_in = 5 V
R_1 = 6 kΩ, R_2 = 4 kΩ
V_out = 5 V*4/(6+4) = 2 V
```

This calculation assumes that the output is unloaded. If an input with finite impedance is connected to the wiper, that impedance appears in parallel with `R_2`, reducing the effective lower resistance and typically lowering `V_out`. To keep loading effects minimal, the input impedance of the subsequent stage must be significantly higher than the resistance of the divider section; if necessary, a buffer is added.[^bourns-potentiometer]

**Common mistake:** assuming that a potentiometer is an ideal regulator that always delivers an exact fixed fraction of `V_in`. The ratio depends on wiper position, taper curve, and loading; furthermore, the allowable voltage, power dissipation, and contact current of the specific model must always be checked.[^bourns-potentiometer]
