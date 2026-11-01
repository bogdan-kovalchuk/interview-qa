---
id: emb-elintro-0095
title: "What is the power factor cos(θ) and why does it matter for power engineering?"
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
  - source_id: aac-power-factor
    title: "All About Circuits: Calculating Power Factor"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-11/calculating-power-factor/
  - source_id: aac-sinusoidal-real-power
    title: "All About Circuits: Sinusoidal Steady-State Power Calculations"
    url: https://www.allaboutcircuits.com/technical-articles/sinusoidal-steady-state-power-calculations/
---

## Short answer

For a sinusoidal circuit, the power factor is `PF = P/S = cos(phi)`, where `S = V_rms*I_rms` and `phi` is the phase difference between voltage and current. A lower `PF` requires a larger current to deliver the same real power at the same voltage; for inductive loads, it is frequently corrected using capacitors placed near the load.[^aac-power-factor]

## Detailed explanation

The power factor `PF` indicates how effectively alternating current delivers real power to a load. For sinusoidal signals, `PF = P/S = cos(phi)`, where `P` is average real power in watts, `S = V_rms*I_rms` is apparent power in volt-amperes, and `phi` is the phase angle between voltage and current. Thus, `cos(phi)` is the power factor under sinusoidal conditions, rather than a separate power quantity.[^aac-power-factor]

When the power factor is less than one, delivering the same real power at a given voltage requires a larger line current: `I = P/(V*PF)` for a single-phase sinusoidal circuit. Higher current increases `I^2*R` losses in conductors and places greater burden on the source and distribution equipment. An ideal resistive load has `PF = 1`; an ideal reactive load has zero average real power, even though current through it may be substantial.[^aac-power-factor] [^aac-sinusoidal-real-power]

For an inductive load, such as an electric motor, a parallel capacitor can compensate for part of the inductive reactive power and reduce the current drawn from the mains. The capacitor is sized for the specific installation: excessive capacitance can overcompensate the load. A capacitor does not eliminate all reactive current circulating within the load branch, nor does it replace evaluating harmonics or varying consumption patterns.[^aac-power-factor]

Example: for a single-phase load with `P = 10 kW` at `V = 230 V` and `PF = 0.5`, the current is approximately `87 A`; at `PF = 1` for the same real power, it would be approximately `43 A`. This simplified comparison assumes a sinusoidal regime and constant voltage.[^aac-power-factor]

**Common mistakes:**
- Referring to the power factor as the fraction of "useful" energy without specifying apparent power and signal conditions.
- Assuming that `cos(phi)` completely describes the power factor under distorted current: for non-sinusoidal signals, harmonics also degrade the `P/S` ratio.[^aac-power-factor]
