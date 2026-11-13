---
id: emb-elee-0060
title: "What does the sign of the impedance angle φ mean?"
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
  - source_id: aac-rxz-review
    title: "All About Circuits: Review of R, X, and Z (Resistance, Reactance and Impedance)"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-5/review-of-r-x-and-z/
---

## Short answer

For a passive circuit with impedance `Z = R + jX`, a positive angle indicates predominantly inductive behavior, where voltage leads current. A negative angle indicates predominantly capacitive behavior, where current leads voltage, while a pure resistor has an angle of 0°.[^aac-rxz-review]

## Detailed explanation

The sign of the impedance angle indicates which reactive component predominates in an AC circuit. Under the convention `Z = R + jX`, a positive imaginary part `X` corresponds to inductive behavior, while a negative one corresponds to capacitive behavior; this is consistent with the phase angle `φ = atan2(X,R)` for a non-negative resistance `R`.[^aac-rxz-review]

For an ideal resistor, voltage and current vary in phase, so the angle is zero. In an ideal inductor, voltage leads current by 90°, and in an ideal capacitor, current leads voltage by 90°. In a mixed circuit, the angle typically lies between these limits because resistance and reactance act together.[^aac-rxz-review]

The angle belongs to the total impedance, rather than to an individual resistor or single component in an arbitrary circuit. It depends on frequency, component ratings, and circuit topology: in a series RLC circuit, inductive and capacitive components can partially cancel each other out. Thus, the sign of the angle does not define the type of each component, but rather describes the net network response to a sinusoidal signal.[^aac-rxz-review]

**Common mistake:** interpreting a positive angle as "current leads voltage". Under the passive convention, the sign is read from `Z = V/I`: an inductive angle is positive and voltage leads current; for a capacitive angle, the phase order is reversed.[^aac-rxz-review]
