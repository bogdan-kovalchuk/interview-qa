---
id: emb-elintro-0239
title: "What is `V_th` in a MOSFET?"
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

`V_GS(th)` is the gate-source voltage measured at a specified small drain current and test conditions in the datasheet; it is not the full turn-on voltage. Achieving low `R_DS(on)` typically requires a significantly higher `V_GS`, which should be taken from the specified test conditions of the given MOSFET.[^aac-semiconductors]

## Detailed explanation

`V_GS(th)` is the threshold voltage between gate and source, but in a datasheet it is defined not by an abstract point of "full turn-on," but by measurement at a specific small drain current under defined voltages and temperature. This value is a parameter of the specific component and carries a tolerance; across different MOSFETs, the test current and other conditions can vary.[^aac-semiconductors]

Near threshold, the channel only begins to conduct a tiny current. For operation as a power switch, one must consult the `R_DS(on)` table: the manufacturer guarantees this on-resistance at specific `V_GS` and `I_D` values. If a microcontroller supplies a lower voltage than specified under those test conditions, the low rated resistance is not guaranteed. Variations across temperature and unit-to-unit spread must also be taken into account.[^aac-semiconductors]

For example, a datasheet rating of "threshold 2 V" does not mean that at 2 V the transistor conducts tens of amperes with low losses. It is merely the threshold measured at a small test current. To select a driver, compare its output voltage with the specified `R_DS(on)` conditions and verify the absolute maximum `V_GS(max)` rating to prevent gate damage.[^aac-semiconductors]

**Common mistakes:**
- Treating `V_GS(th)` as the recommended drive voltage or full on-state.
- Comparing threshold ratings without checking test conditions and tolerances.
- Ignoring the specified test voltage for `R_DS(on)` and the absolute gate-to-source voltage limit.
