---
id: emb-elee-0201
title: "What is an emitter follower (common collector), and what is it for?"
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
  - source_id: fiore-common-collector
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 7.4 Common Collector Amplifier"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/07:_BJT_Small_Signal_Amplifiers/7.4:_Common_Collector_Amplifier
  - source_id: fiore-bjt-basics
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 4.2 The Bipolar Junction Transistor"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/04:_Bipolar_Junction_Transistors_(BJTs)/4.2:_The_Bipolar_Junction_Transistor
  - source_id: fiore-bjt-ac-model
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 7.2 Simplified AC Model of the BJT"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/07:_BJT_Small_Signal_Amplifiers/7.2:_Simplified_AC_Model_of_the_BJT
---

## Short answer

The output is taken from the emitter, tracking the base input voltage with a DC shift of approximately `V_BE`. Although voltage gain is slightly less than unity, the stage provides current gain, high input impedance, and low output impedance. This minimizes loading on the preceding source while driving heavy loads effectively, serving as an impedance buffer.[^fiore-common-collector]

## Detailed explanation

An emitter follower is a common-collector circuit. The input signal is applied to the base, the output is taken from the emitter across resistor `R_E` to ground, and the collector is at AC ground potential because it is connected to the power supply.[^fiore-common-collector] The emitter voltage follows the base voltage with a base–emitter junction drop `V_BE`, approximately 0.7 V for silicon.[^fiore-bjt-basics] The phase is not inverted: an increase in the input produces an increase in the output.[^fiore-common-collector]

The gain can be seen from the small-signal circuit. The AC emitter current `i_e` flows through the dynamic junction resistance `r'_e` ≈ 26 mV / `I_E` and through `r_E`, which equals `R_E` or `R_E` ∥ `R_load`. The input voltage at the base is `v_in` = `i_e` × (`r'_e` + `r_E`), and the output at the emitter is `v_out` = `i_e` × `r_E`. Hence `A_v` = `r_E` / (`r'_e` + `r_E`), and this value is always less than unity because `r'_e` > 0. When `r_E` is significantly larger than `r'_e`, the gain is close to 1.[^fiore-common-collector][^fiore-bjt-ac-model]

The value of the follower lies in its impedances. The input resistance at the base equals β × (`r'_e` + `r_E`), which is large, but the parallel resistors of the base divider reduce it. The output resistance equals `R_E` ∥ (`r'_e` + (`r_B` ∥ `r_gen`) / β), which is small. In the textbook example, a 1 kΩ source with a 500 Ω load without a follower yields 100 mV × 500 / 1500 ≈ 33 mV across the load, whereas with the follower it delivers about 85 mV with an output resistance of ≈ 37 Ω.[^fiore-common-collector]

To avoid overestimating the circuit, two limitations must be kept in mind. First, `V_BE` and `r'_e` depend on the current `I_E` and temperature, so the DC offset between input and output is not constant. Second, `r'_e` is a small-signal quantity: it remains valid only as long as the AC component of the current is small; otherwise, the signal becomes distorted.[^fiore-bjt-ac-model]

**Common mistakes:**
- Expecting a voltage gain greater than 1: `A_v` is always less than 1.
- Assuming the output resistance equals `R_E`: more accurately, it is `R_E` ∥ (`r'_e` + (`r_B` ∥ `r_gen`) / β).[^fiore-common-collector]
- Assuming that the follower inverts the signal like a common-emitter stage: the phase is preserved.
