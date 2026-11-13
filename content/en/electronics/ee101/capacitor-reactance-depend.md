---
id: emb-elee-0019
title: "What does a capacitor's reactance `X_C` depend on?"
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
  - source_id: aac-capacitor-reactance
    title: "All About Circuits: AC Capacitor Circuits"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-4/ac-capacitor-circuits/
---

## Short answer

For a sinusoidal signal, `X_C = 1/(2π*f*C)`, where `f` is frequency and `C` is capacitance. Reactance decreases as either parameter increases; the ideal formula approaches infinity at `f = 0`, whereas a real capacitor exhibits leakage and parasitic components.[^aac-capacitor-reactance]

## Detailed explanation

Capacitive reactance `X_C` is measured in ohms and describes an ideal capacitor's opposition to alternating current. In sinusoidal steady state, it is calculated as `X_C = 1/(2π*f*C)`, where `f` is given in hertz and `C` in farads. This is not a fixed physical resistance of the material, but a signal- and frequency-dependent quantity; for a given voltage, lower `X_C` results in greater current in a purely capacitive model.[^aac-capacitor-reactance]

Frequency appears in the denominator: as frequency increases, voltage changes more rapidly, causing the plates to charge and discharge more frequently and thereby lowering the capacitive reactance. Increasing capacitance also reduces `X_C`, because a larger capacitor stores more charge for the same change in voltage. In complex circuits, `X_C` alone does not replace total impedance: resistive and inductive components, as well as the phase shift between current and voltage, must be taken into account.[^aac-capacitor-reactance]

Calculation example: for `C = 10 µF` at a frequency of `f = 1 kHz`:

```text
X_C = 1/(2*π*1000*10e-6)
X_C ≈ 15.9 Ω
```

Doubling the frequency to 2 kHz with capacitance held constant yields approximately 8.0 Ω in this model. Check the units before substituting: microfarads must be converted to farads, otherwise the calculated result will be off by a factor of one million.[^aac-capacitor-reactance]

At `f = 0`, the ideal sinusoidal formula approaches infinite reactance, corresponding to an open-circuit capacitor after charging is complete in DC analysis. This does not describe the transient state when connecting a source, during which current can be substantial and is determined by initial voltage and circuit resistance. Physical components also have leakage and parasitics; near self-resonance, the simple capacitive model becomes invalid, requiring component-specific characteristics for accurate design.[^aac-capacitor-reactance]

**Common mistake:** treating `X_C` as a fixed property of the capacitor or substituting frequency in kilohertz without converting to hertz. Always state the signal frequency and verify capacitance units, and for real-world circuits, analyze complex impedance and the datasheet.[^aac-capacitor-reactance]
