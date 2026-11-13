---
id: emb-elee-0065
title: "What does a negative impedance angle of a circuit mean?"
track: electronics
section: ee101
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-alternating-current
    title: "All About Circuits textbook, Volume II: AC"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/
  - source_id: aac-rc-phase
    title: "All About Circuits: Series Resistor-Capacitor Circuits"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-4/series-resistor-capacitor-circuits/
  - source_id: aac-power-factor-angle
    title: "All About Circuits: Calculating Power Factor"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-11/calculating-power-factor/
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
---

## Short answer

A negative impedance angle indicates that the circuit is overall capacitive in sinusoidal steady state. Current leads voltage by the absolute value of this angle; for an ideal capacitor, this lead is 90°.[^aac-power-factor-angle] [^aac-rc-phase]

## Detailed explanation

In sinusoidal steady state at a single frequency, impedance is the complex ratio of voltage and current phasors, `Z = V/I`; its angle represents the phase shift of voltage relative to current. A negative angle therefore means that voltage lags current, or equivalently, that current leads voltage.[^aac-rc-phase]

For passive ideal components, a resistor has a zero angle, an inductor has a positive angle, and a capacitor has a negative angle. In a combination of R, L, and C, the sign of the angle describes the net response at the specified frequency: inductive and capacitive components can partially cancel each other out. This does not mean the circuit necessarily contains only a capacitor, nor does it mean negative resistance; a negative angle simply indicates that the circuit is overall more capacitive than inductive.[^aac-power-factor-angle]

For example, for a series RC circuit, `Z = R - j*X_C`. If `R = 3 Ω` and `X_C = 4 Ω`, then `Z = 3 - j4 Ω`, its magnitude equals `5 Ω`, and the angle is approximately `-53.13°`. Thus, for a source voltage with phase `0°`, the current has a phase of approximately `+53.13°`. In a real circuit, parasitic parameters and frequency variations can alter the sign or magnitude of the angle, so this conclusion applies to the measured or calculated impedance specifically under the specified conditions.[^aac-rc-phase]

**Common mistakes:**

- Treating a negative angle as negative resistance, even though it indicates a phase relationship.
- Swapping the current and voltage phases: `angle(I) = angle(V) - angle(Z)`.
- Calling any circuit containing a capacitor capacitive without accounting for inductance and frequency.[^aac-rc-phase]
