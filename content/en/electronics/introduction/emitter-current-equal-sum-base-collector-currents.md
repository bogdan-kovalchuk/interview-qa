---
id: emb-elintro-0227
title: "Why does the emitter current equal the sum of the base and collector currents?"
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

By conservation of charge, the currents at the three terminals of a BJT satisfy `I_E = I_B + I_C`: in an NPN transistor the base and collector currents enter while the emitter current exits, and in a PNP the directions are reversed. Consequently, the magnitude of the emitter current equals the sum of the base and collector current magnitudes.[^aac-semiconductors]

## Detailed explanation

In a BJT, current does not disappear inside the package: in steady state, charge entering through certain terminals must exit through others. For an NPN in normal operation, current enters the collector and base and exits through the emitter; therefore, by Kirchhoff's current law, `I_E = I_B + I_C`. For a PNP, directions are reversed, but the equality of magnitudes remains the same. The signed formulation depends on the chosen reference directions for currents.[^aac-semiconductors]

The base controls conduction of the base–emitter junction, while collector current constitutes the main portion of load current. Part of the current flows through the base, so the emitter branch carries both contributions. In active amplification, the approximation `I_C ≈ β*I_B` is frequently used, but the `β` factor depends on the specific component, current, temperature, and voltage; in saturation, this approximation is no longer a reliable way to determine current. The nodal balance `I_E = I_B + I_C` remains valid in every operating region.[^aac-semiconductors]

Example: if measured `I_B = 2 mA` and `I_C = 98 mA`, then `I_E = 100 mA`. An ammeter connected in series with the emitter will show the sum, while a meter in the collector branch will measure only collector current. Discrepancies in real measurements can arise from instrument tolerances, leakage, transients, or different measurement reference points, not from a violation of charge conservation. A common mistake is saying that emitter current is "amplified" relative to collector current without explaining the base contribution.[^aac-semiconductors]
