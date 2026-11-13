---
id: emb-elee-0053
title: "How does the phase shift between voltage and current affect power?"
track: electronics
section: ee101
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-alternating-current
    title: "All About Circuits textbook, Volume II: AC"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/
  - source_id: aac-ac-power
    title: "All About Circuits: True, Reactive, and Apparent Power"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-11/true-reactive-and-apparent-power/
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
---

## Short answer

For a single-phase sinusoidal steady state with RMS values, real power `P = V*I*cos(φ)` is measured in W, reactive power `Q = V*I*sin(φ)` in var, and apparent power `S = V*I` in VA. The power factor equals `P/S`, and an ideal purely reactive load has zero average real power.[^aac-ac-power]

## Detailed explanation

In an AC circuit, instantaneous power equals the product of instantaneous voltage and current, and its average over a period depends on the phase angle between the sinusoids. For single-phase sinusoidal steady state, where `V` and `I` are RMS values, real power equals `P = V*I*cos(φ)`. It is measured in watts and represents the average rate of energy transfer to the load. [^aac-ac-power]

Apparent power `S = V*I` is measured in volt-amperes. Reactive power `Q = V*I*sin(φ)` is measured in var and describes the exchange of energy with reactive elements. For sinusoidal operation, these quantities satisfy the relationship `S² = P² + Q²`; the power factor is `P/S = cos(φ)`. One should not call `S` real power: the same voltage and current can deliver different real power under different phase angles. [^aac-ac-power]

In a purely resistive load, voltage and current are in phase, so `φ = 0°`, `P = S`, and `Q = 0`. In an ideal inductor or capacitor, the angle magnitude is 90°: the element alternately absorbs energy from the source and returns it, so average real power over a complete cycle is zero. Real coils and capacitors exhibit losses and are thus not purely reactive. [^aac-ac-power]

**Example:** for `V = 120 V`, `I = 2 A`, and `φ = 60°`, we have `S = 240 VA`, `P = 120 W`, `Q ≈ 208 var`. These values are RMS values for single-phase sinusoidal operation; substituting peak amplitudes without the appropriate conversion would yield an incorrect result.

**Common mistakes:**

- Calculating real power as `V*I` while ignoring the phase angle.
- Assuming that an ideal reactive element draws zero current. It can carry current and apparent power even though its average real power is zero. [^aac-ac-power]
