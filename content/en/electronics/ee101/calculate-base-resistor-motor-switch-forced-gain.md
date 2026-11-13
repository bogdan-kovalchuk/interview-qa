---
id: emb-elee-0220
title: "How do you calculate the base resistor for a 100 mA motor switch with a forced gain of 10 driven from 5 V?"
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
  - source_id: rohm-bjt-basics
    title: "ROHM: Bipolar Junction Transistor (BJT) Basics: Operation and Applications (NPN & PNP)"
    url: https://techweb.rohm.com/product/transistors-diodes/transistors/27319/
  - source_id: mit-6071-bjt-notes
    title: "MIT OCW 6.071/22.071 (Spring 2006): Transistors: Bipolar Junction Transistors (BJT), lecture notes"
    url: https://ocw.mit.edu/courses/6-071j-introduction-to-electronics-signals-and-measurement-spring-2006/b30aa58fb0c9915da21e5a5855384818_19_bjt_1.pdf
---

## Short answer

Base drive current must satisfy `I_B ≥ I_C/β_forced = 100 mA / 10 = 10 mA`.[^rohm-bjt-basics] This gives `R_B = (5 - 0.8)/0.01 ≈ 420 Ω`, where saturated `V_BE = 0.8 V` typically falls in the 0.7–0.9 V range.[^rohm-bjt-basics] The chosen `β_forced` must sit well below the datasheet minimum `h_FE` at this current.[^rohm-bjt-basics] The 5 V control source must be capable of sourcing the required 10 mA.

## Detailed explanation

The switch operates in saturation: the motor receives nearly the full supply voltage, while the transistor acts simply to complete the current path. To maintain saturation, base drive current must be sufficient. In saturation, the relationship between `I_C` and `I_B` becomes non-linear, and the base–collector junction becomes forward-biased.[^mit-6071-bjt-notes] Therefore, base drive is calculated not from the typical active-region β, but using a forced gain `β_forced`, selected well below the minimum datasheet `h_FE`. A typical starting point is 5–10, so `β_forced` = 10 is already at the upper limit of this recommended range.[^rohm-bjt-basics]

The base resistor sets the drive current from a control logic output at `V_drive` = 5 V: `R_B` = (`V_drive`-`V_BE`)/`I_B`. For `V_BE` = 0.8 V, this yields `R_B` = (5-0.8)/0.01 = 420 Ω. The typical variation range of 0.7–0.9 V gives `R_B` = 430 Ω and 410 Ω, a spread of ±10 Ω (about 2.4%). Rounding up to a standard 430 Ω resistor gives `I_B` ≈ 9.8 mA and `β_forced` ≈ 10.2, leaving minimal margin. Rounding down to 390 Ω provides `I_B` ≈ 10.8 mA and `β_forced` ≈ 9.3, which ensures stronger saturation.

This calculation is valid only if the transistor genuinely remains in saturation. Under saturation, `V_CE` is low: ROHM data indicates typically under 0.3 V, keeping conduction losses `V_CE`*`I_C` small.[^rohm-bjt-basics] If the actual `h_FE` at 100 mA is lower than `β_forced`, 10 mA of base drive will support less than 100 mA, pulling the transistor out of saturation and dramatically increasing `V_CE` and power dissipation. Resistor `R_B` sets `I_B`, not `I_C`: motor current is determined by the load, so under different operating currents (such as motor stall or starting inrush current, see qid:emb-elee-0221), base drive current and `R_B` must be recalculated.

**Common mistakes:**

- Using the datasheet `h_FE` directly as `β_forced` without safety margin: this leaves the transistor on the verge of desaturation.
- Calculating `R_B` using typical active-region β: for β = 100, this yields only 1 mA instead of the required 10 mA (see qid:emb-elee-0221).
- Failing to verify datasheet `V_CE(sat)` curves after calculation: sizing `R_B` alone does not prove the transistor achieves saturation.
