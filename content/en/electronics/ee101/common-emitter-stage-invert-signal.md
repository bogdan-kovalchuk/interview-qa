---
id: emb-elee-0208
title: "Why does a common-emitter stage invert the signal?"
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
  - source_id: fiore-ac-model-bjt
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 7.2 Simplified AC Model of the BJT"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/07:_BJT_Small_Signal_Amplifiers/7.2:_Simplified_AC_Model_of_the_BJT
  - source_id: fiore-common-emitter-amplifier
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 7.3 Common Emitter Amplifier"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/07:_BJT_Small_Signal_Amplifiers/7.3:_Common_Emitter_Amplifier
  - source_id: fiore-bjt-dc-load-line
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 4.6 DC Load Lines"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/04:_Bipolar_Junction_Transistors_(BJTs)/4.6:_DC_Load_Lines
  - source_id: fiore-ac-circuit-analysis
    title: "James M. Fiore: AC Electrical Circuit Analysis, A Practical Approach (sections 1.5 and 10.3)"
    url: https://www2.mvcc.edu/users/faculty/jfiore/Circuits2/ACElectricalCircuitAnalysis.pdf
---

## Short answer

When a positive input excursion increases base-emitter voltage, collector current increases, causing a larger voltage drop across `R_C`, which drives `V_C = V_CC - I_C*R_C` downward.[^fiore-ac-model-bjt][^fiore-bjt-dc-load-line] The output signal is therefore 180° out of phase with the input in the midband frequency range.[^fiore-common-emitter-amplifier]

## Detailed explanation

A common-emitter stage applies the input signal to the base and takes the output from the collector. The collector current determines the voltage at the collector: for DC, `V_C = V_CC - I_C*R_C`, so higher collector current causes a lower collector voltage.[^fiore-bjt-dc-load-line] Current `I_C` depends strongly on the base–emitter voltage: in the simplified model, `I_C = I_S*exp(38.6*V_BE)` at 300 K, meaning a change in `V_BE` of just 2.6 mV changes the current by approximately 10%.[^fiore-ac-model-bjt]

Example: let `V_CC = 12 V`, `R_C = 4.7 kΩ`, and the quiescent operating point be `I_C = 1 mA`, yielding `V_C = 12 - 1*4.7 = 7.3 V`. An input signal increases `V_BE` by approximately 2.6 mV. The dynamic resistance is `r_e = 26 mV / 1 mA = 26 Ω`, so collector current increases by `2.6 mV / 26 Ω = 0.1 mA`, up to 1.1 mA. Then `V_C = 12 - 1.1*4.7 = 6.83 V`: when the input rises, the output drops by 0.47 V, which represents signal inversion.[^fiore-ac-model-bjt]

Inversion is a property of the circuit topology with the output taken from the collector, not of the transistor itself: higher current creates a larger voltage drop across `R_C`. The negative sign in `A_v = -r_C/(r_e + r_E)` represents this inversion, corresponding to a 180° phase shift in the midband.[^fiore-common-emitter-amplifier] At frequencies near the cutoffs introduced by capacitors, the phase deviates from 180°; in a lead RC network, the phase shift is 45° at the critical frequency.[^fiore-ac-circuit-analysis] An emitter follower, by contrast, does not invert because the output is taken from the emitter.[^fiore-ac-model-bjt]

**Common mistakes:**

- Treating inversion as an intrinsic property of the transistor rather than of the circuit configuration with collector output.
- Assuming the 180° phase shift holds at all frequencies, particularly near cutoff boundaries.
- Confusing phase inversion with clipping: inversion can be cancelled by adding a second inverting stage in the signal chain.
