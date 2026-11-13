---
id: emb-elee-0030
title: "Why is a 100 nF ceramic capacitor placed in parallel with a large electrolytic in a supply filter?"
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
  - source_id: ti-switching-regulator-fundamentals
    title: "Texas Instruments: Switching regulator fundamentals"
    url: https://www.ti.com/lit/an/snva559c/snva559c.pdf
---

## Short answer

A large electrolytic capacitor provides bulk capacitance for lower frequencies and slower load steps, whereas a ceramic capacitor provides a low-ESR and low-ESL path for high-frequency ripple. This is not a universal rule for arbitrary component values: impedance varies with frequency, parasitics, and layout, so any specific pair must be validated in the circuit.[^ti-switching-regulator-fundamentals]

## Detailed explanation

In a typical power supply filter, a capacitor stores charge to reduce voltage fluctuations when the source or load cannot instantly deliver the required current. A large electrolytic component provides substantial bulk capacitance and is therefore useful for lower ripple frequencies and slower load-current steps. However, a real capacitor is not an ideal capacitance: its ESR and ESL influence impedance, and ESL limits its effectiveness at high frequencies.[^ti-switching-regulator-fundamentals]

A ceramic capacitor often features lower ESR and ESL, allowing it to shunt high-frequency current components locally. It is therefore placed in parallel with the larger capacitor to achieve complementary low-impedance ranges across different frequency bands. This describes a common engineering practice rather than a guarantee that any arbitrary pair of values will automatically form an effective filter: self-resonant frequency, noise frequencies, specific component characteristics, and parasitic trace inductance all influence the outcome.[^ti-switching-regulator-fundamentals]

For power decoupling, the ceramic component is placed close to the load power pins with a short return path to ground. Long traces introduce inductance that can completely negate the low-ESL benefit of the component itself. In a switching converter, the datasheet requirements for capacitance, ESR, and stability must also be followed; adding capacitors without verification can alter control-loop behavior.[^ti-switching-regulator-fundamentals]

Example: if both a slow voltage droop and brief high-frequency spikes are present at a switching regulator input, the larger capacitance can maintain the local charge reservoir, while the small ceramic component lowers high-frequency impedance near the input. Check the regulator requirements first, then measure the voltage across the target frequency band on the actual board layout.[^ti-switching-regulator-fundamentals]

**Common mistakes:**

- Assuming that a ceramic capacitor is always superior at any frequency; above its self-resonance, ESL can dominate its behavior.
- Placing the capacitor far from the load and neglecting trace inductance.
- Treating the "bulk plus 100 nF" pair as a universal circuit without checking manufacturer recommendations and measurements.
