---
id: emb-elintro-0257
title: "Why must `R_DS(on)` be read at a specific `V_GS`?"
track: electronics
section: introduction
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-direct-current
    title: "All About Circuits textbook, Volume I: DC"
    url: https://www.allaboutcircuits.com/textbook/direct-current/
  - source_id: infineon-optimos
    title: "Infineon OptiMOS Power MOSFET Datasheet Explanation"
    url: https://www.infineon.com/assets/row/public/documents/24/42/infineon-mosfet-optimos-datasheet-explanation-applicationnotes-en.pdf
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
---

## Short answer

`R_DS(on)` strongly depends on `V_GS`, drain current, and junction temperature, so design calculations must use guaranteed datasheet limits matched to actual driver and load conditions.[^infineon-optimos] The threshold voltage `V_GS(th)` represents only the onset of slight conduction at a small test current rather than full channel enhancement.[^infineon-optimos]

## Detailed explanation

On-resistance of a MOSFET is not a constant value independent of gate drive: `R_DS(on)` is measured under specified `V_GS`, drain current, and temperature conditions. A higher gate-source voltage typically enhances the channel more strongly and reduces on-resistance within the allowable operating range, but the maximum allowable gate voltage is also limited by the datasheet. For component selection, use the guaranteed limit rather than a typical graph value if the design must operate under worst-case conditions.[^infineon-optimos]

In the electrical characteristics table, look for the `R_DS(on)` rows with their test conditions. If a MOSFET is driven by a 3.3 V GPIO, a value guaranteed only at 10 V does not prove that the transistor will have the same on-resistance at 3.3 V. Check whether there is a guaranteed value at the available drive voltage; a typical characteristics curve can aid estimation, but it is not a production guarantee. At low `V_GS`, on-resistance also varies with temperature and current.[^infineon-optimos]

Do not confuse `V_GS(th)` with the full turn-on voltage. The threshold value is specified at a tiny test drain current, meaning it indicates only when the channel just begins to conduct. It does not guarantee a low voltage drop or minimal heating under load. To estimate losses in a simple fully turned-on state, use `P = I²*R_DS(on)`, with the resistance evaluated at the actual gate drive voltage and adjusted for elevated junction temperature.[^infineon-optimos]

**Common mistakes:**

- Comparing on-resistances at different `V_GS` levels as if the test conditions were identical.
- Selecting a logic-level MOSFET solely based on a low `V_GS(th)` without verifying `R_DS(on)`.
- Assuming a typical curve value is sufficient proof for a worst-case calculation.
