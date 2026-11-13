---
id: emb-elee-0082
title: "How can one series RL circuit be both a low-pass and a high-pass filter?"
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

The output tapping point determines the filter type. In a series RL circuit, taking the output across R forms a low-pass filter, because as frequency increases, a greater fraction of the input voltage drops across the inductor. Taking the output across L forms a high-pass filter, as inductive impedance increases and the inductor voltage approaches the input. This holds for ideal components and an unloaded output.[^aac-series-rl]

## Detailed explanation

A single series RL circuit can implement either a low-pass or a high-pass filter, because a filter is determined not only by the choice of components, but also by where the output is taken. In both cases, the current passes through R and L, and their impedances equal `R` and `j*ω*L`. As frequency increases, the magnitude of the inductive impedance increases, thereby altering the ratio of the voltages across the two components.[^aac-series-rl]

If the output is taken across the resistor, at low frequencies the inductor has low reactance, the circuit passes more current, and a substantial portion of the voltage appears across R. At high frequencies, the reactance of L is large, and the current and voltage across R decrease. Consequently, the output across R transmits low frequencies better than high frequencies, behaving as a low-pass filter. If the output is taken across the inductor, the situation is reversed: at low frequencies, the voltage across L is small, and as frequency increases, it rises. This is a high-pass filter.[^aac-series-rl]

The transition boundary is set approximately where `X_L = R`, yielding `f_c = R/(2π*L)` for this simple topology. At this frequency, the magnitude of each output equals approximately 0.707 of the input for an unloaded ideal circuit; the phase angles of the outputs differ. Connected loading can alter the transfer function, so a measuring instrument or subsequent stage cannot always be neglected.[^aac-series-rl]

Example: with a 1 V RMS sinusoidal input and `X_L = R`, the voltage magnitudes across R and L are each about 0.707 V RMS, but one phasor lags or leads the other. This does not mean both filters are connected in series simultaneously in different modes: these are two circuits using the same pair of components, but with different output terminals. In a practical inductor, its internal resistance and parasitic capacitance shift the response from the ideal calculation.[^aac-series-rl]

**Common mistake:** calling the entire RL circuit simply a low-pass filter or simply a high-pass filter without specifying the output node. In an answer, one should identify the measurement nodes, trace the behavior of `X_L` at low and high frequencies, and state whether the output is loaded. Next, verify that the filter name corresponds specifically to the variation of the ratio `V_out/V_in`, rather than merely to the presence of an inductor in the circuit.[^aac-series-rl]
