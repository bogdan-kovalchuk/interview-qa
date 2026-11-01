---
id: emb-elintro-0093
title: "What is the formula for real power in an `AC` circuit with a phase shift?"
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
  - source_id: aac-sinusoidal-real-power
    title: "All About Circuits: Sinusoidal Steady-State Power Calculations"
    url: https://www.allaboutcircuits.com/technical-articles/sinusoidal-steady-state-power-calculations/
  - source_id: aac-power-factor
    title: "All About Circuits: Calculating Power Factor"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-11/calculating-power-factor/
---

## Short answer

For sinusoidal voltage and current, average real power is `P = V_rms*I_rms*cos(phi)`, where `phi` is their phase difference. For an ideal resistor, the factor equals one, whereas for an ideal reactive load, average real power is zero.[^aac-sinusoidal-real-power]

## Detailed explanation

Real power `P` is the time-average of instantaneous power `p(t) = v(t)*i(t)` over a full period. For sinusoidal voltage and current expressed in RMS values, the formula is `P = V_rms*I_rms*cos(phi)`, where `phi` is the phase difference between voltage and current. The product `V_rms*I_rms` by itself is apparent power, and the factor `cos(phi)` indicates what fraction of it constitutes average real power.[^aac-sinusoidal-real-power]

If the load is purely resistive, current and voltage are in phase, `phi = 0`, giving `cos(phi) = 1`; real power equals apparent power. In an ideal inductor or capacitor, the phase shift is 90°, so average real power is zero: energy is periodically stored in the component's field and returned to the source. Real reactive components exhibit losses, and therefore consume a certain amount of real power.[^aac-sinusoidal-real-power]

Example for a sinusoidal circuit: with `V_rms = 120 V`, `I_rms = 2 A`, and `phi = 60°`, the real power is `120*2*cos(60°) = 120 W`, while apparent power is `240 VA`. Real power is measured in watts, and apparent power in volt-amperes.[^aac-sinusoidal-real-power]

**Common mistake:** substituting peak values instead of RMS without the required factor, or assuming a single phase angle suffices for any arbitrary waveform. For non-sinusoidal waveforms, real power is defined as the average of `v(t)*i(t)`, but the simple cosine of the angle between fundamental components may be insufficient.[^aac-sinusoidal-real-power]
