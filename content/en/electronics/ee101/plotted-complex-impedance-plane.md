---
id: emb-elee-0062
title: "How are R, L and C plotted on the complex impedance plane?"
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

In the complex impedance plane, resistance has a positive real part `R`, inductance has a positive imaginary part `jωL`, and capacitance has a negative imaginary part `-j/(ωC)`. Consequently, their ideal impedances point to the right, upward, and downward, respectively.[^aac-rxz-review]

## Detailed explanation

Complex impedance is expressed as `Z = R + jX`: the real part `R` is plotted along the horizontal axis, and the reactive part `X` along the vertical axis. This notation captures both the opposition to alternating current and the phase relationship between voltage and current.[^aac-rxz-review]

For an ideal resistor, `Z_R = R`, so its point lies on the positive real axis. For an ideal inductor, `Z_L = jωL`, where `ω = 2π*f`; the positive sign of the imaginary part places the impedance on the positive imaginary axis. For an ideal capacitor, `Z_C = -j/(ω*C)`, so its imaginary part is negative.[^aac-rxz-review]

In a series RLC circuit, impedances add as complex numbers: `Z = R + j(X_L - X_C)`. The total impedance point has a horizontal coordinate `R`, while the vertical coordinate represents the net reactance. When they are equal, the vertical component is zero and the net impedance lies on the real axis; on either side of this condition, the sign of the reactive part differs.[^aac-rxz-review]

For example, when `X_L > X_C`, the net impedance vector points above the real axis, corresponding to inductive behavior; when `X_C > X_L`, it points below it. This vector representation explains why one cannot add reactance magnitudes as ordinary positive numbers: their signs are opposite.[^aac-rxz-review]

**Common mistake:** assuming that the vertical coordinate is always positive because reactance is measured in ohms. The unit is the same for `R` and `X`, but the sign of `X` encodes phase. Also, do not confuse the complex impedance plane with a plot of a physical component: the vector position represents the model at a specified frequency.[^aac-rxz-review]
