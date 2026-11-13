---
id: emb-elee-0080
title: "If the frequency in an RL circuit is increased 10 times, do the current and voltages also increase 10 times?"
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
  - source_id: aac-series-rl
    title: "All About Circuits: Series Resistor-Inductor Circuits"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-3/series-resistor-inductor-circuits/
---

## Short answer

No. For constant inductance, `X_L = 2π*f*L`, so a tenfold increase in frequency yields a tenfold increase in inductive reactance, but current and voltages depend on the total complex impedance of the circuit. The voltages across the resistor and inductor are phasors, so their magnitudes cannot simply be added as scalar numbers.[^aac-series-rl]

## Detailed explanation

In a series RL circuit, frequency alters the inductive reactance, but it does not automatically scale all currents and voltages by the same factor. For an ideal inductor, `X_L = 2π*f*L`: if `L` is constant, a tenfold increase in `f` indeed increases `X_L` tenfold. However, the total circuit impedance equals `Z = R + j*X_L`, and current is governed by the relation `I = V_in/Z`; hence its magnitude depends on R and the initial relationship between R and `X_L`.[^aac-series-rl]

The voltage across the resistor is `V_R = I*R`, and across the inductor is `V_L = I*j*X_L`. When frequency changes, both the current and the impedance phase angle change. Therefore, at one output the voltage may decrease, at the other it may increase or approach a limit, but it is not required to change tenfold. In an exact calculation, these voltages add as complex quantities according to Kirchhoff's voltage law, rather than as their positive magnitudes.[^aac-series-rl]

Example: suppose the input sine wave has a constant amplitude, and resistance R equals the inductor's reactance at the initial frequency. The impedance magnitude is then `√2*R`; after a tenfold increase in frequency, it equals `√101*R`. Thus, the current magnitude decreases by `√(101/2)`, approximately a factor of 7.1, rather than increasing tenfold. This is an illustration for ideal components and an unchanging source, not a universal number for every RL circuit.[^aac-series-rl]

**Common mistake:** noticing a tenfold increase in `X_L` and concluding that current or every voltage drop will scale by the same factor. Before answering, one should check the circuit schematic, output tapping point, source amplitude, and initial values of R and L, and then recalculate the complex divider for both frequencies. A real inductor has losses and parasitic parameters, so the `j*ω*L` model holds only within its operating range.[^aac-series-rl]
