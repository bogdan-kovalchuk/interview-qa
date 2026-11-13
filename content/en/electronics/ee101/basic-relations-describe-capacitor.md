---
id: emb-elee-0020
title: "Which basic relations describe a capacitor?"
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
  - source_id: aac-capacitor-calculus
    title: "All About Circuits: Capacitors and Calculus"
    url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-13/capacitors-and-calculus/
  - source_id: aac-capacitor-fields
    title: "All About Circuits: Electric Fields and Capacitance"
    url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-13/electric-fields-capacitance/
  - source_id: aac-capacitor-factors
    title: "All About Circuits: Factors Affecting Capacitance"
    url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-13/factors-affecting-capacitance/
---

## Short answer

For a linear capacitor, `Q = C*V`, `i = C*dV/dt`, and stored energy is `E = C*V²/2`. For ideal parallel plates, `C = ε*A/d`; physical components also exhibit tolerances, leakage, and parasitic parameters.[^aac-capacitor-calculus] [^aac-capacitor-fields]

## Detailed explanation

A capacitor is characterized by capacitance `C`, which relates the charge on its plates to the voltage between them. For a linear device, the charge is `Q = C*V`: greater capacitance or higher voltage results in a larger magnitude of stored charge. This refers to the charge on one plate; the opposite plate holds an equal charge of opposite polarity.[^aac-capacitor-fields]

Current is determined not by the voltage itself, but by its rate of change: `i = C*dV/dt` under the passive sign convention. If the voltage is constant, the derivative is zero, so an ideal capacitor passes no steady current once the transient response has finished. Current flows during charging or discharging; a faster change in voltage yields a higher current. Physical components exhibit leakage, so DC current in steady state is not necessarily exactly zero.[^aac-capacitor-calculus] [^aac-capacitor-fields]

Energy is stored in the electric field, and for a linear capacitor it equals `E = C*V²/2`. The parallel-plate formula `C = ε*A/d` is an idealized model: `A` is plate overlap area, `d` is separation distance, and `ε` is dielectric permittivity. Larger area and higher permittivity increase capacitance, whereas greater distance decreases it; fringing fields and real component geometry are neglected in this formula.[^aac-capacitor-fields] [^aac-capacitor-factors]

Example: if `C = 100 µF` and voltage changes by `2 V` in `1 ms`, the average current in the ideal model is `0.2 A` in the charging direction. This does not mean the capacitor always draws this current: the value depends on the instantaneous voltage slope and the external circuit.

**Common mistake:** regarding a capacitor as an "open circuit to current" under all conditions. Steady ideal DC does not pass once charged, but time-varying signals induce current, and physical components have leakage current and voltage limits.
