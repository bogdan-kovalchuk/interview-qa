---
id: emb-elee-0191
title: "Where does the energy of the amplified signal come from in a transistor amplifier?"
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
  - source_id: fiore-biasing-need
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 5.2 The Need For Biasing"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/05:_BJT_Biasing/5.2:_The_Need_For_Biasing
  - source_id: fiore-ebers-moll
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 4.5 Ebers-Moll Model"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/04:_Bipolar_Junction_Transistors_(BJTs)/4.5:_Ebers-Moll_Model
  - source_id: fiore-emitter-bias
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 5.3 Two-Supply Emitter Bias"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/05:_BJT_Biasing/5.3:_Two-Supply_Emitter_Bias
  - source_id: fiore-amplifier-model
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 6.2 Amplifier Model"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/06:_Amplifier_Concepts/6.2:_Amplifier_Model
---

## Short answer

Energy comes from the DC power supply rather than from the input signal: amplification is impossible without an external power source.[^fiore-biasing-need] The transistor merely modulates this power flow, using a small base current to control a larger collector current.[^fiore-ebers-moll] This collector current is drawn directly from `V_CC` through the load.[^fiore-emitter-bias]

## Detailed explanation

An amplifier does not create energy from nothing. The input signal at the base merely determines how current delivered by the power supply into the collector circuit is modulated. Without an auxiliary energy source, amplification is impossible.[^fiore-biasing-need]

At the quiescent operating point, collector current is steady: it flows from `+V_CC` through load `R_C` and the transistor to ground. A change in base current by `ΔI_B` produces a change in collector current `ΔI_C = β * ΔI_B`.[^fiore-ebers-moll] The voltage at the collector `V_C = V_CC - I_C * R_C` then varies in the opposite direction, and this alternating voltage constitutes the output signal.[^fiore-emitter-bias]

For example: at the quiescent point, collector current is 0.99 mA with +5 V and a 1 kΩ load. The supply delivers DC power of 5 V × 0.99 mA ≈ 4.95 mW into the collector circuit. Suppose the AC component of the collector current has an amplitude of 0.1 mA. Its RMS value is 0.1 mA / √2 ≈ 0.071 mA, yielding an AC power in the load of `(0.071 mA)² × 1 kΩ ≈ 5 µW`. This useful signal power represents approximately 0.1% of the power drawn from the supply. The signal governs what fraction of this supply power is converted into the load signal, but does not generate it.

Power gain is the ratio `P_out / P_in`, so a value greater than 1 does not violate conservation of energy. A textbook example: 50 mW at the output with 10 mW at the input yields a power gain of 5.[^fiore-amplifier-model] The required energy is drawn from the power supply, not from the signal itself.

**Common mistakes:**

- Believing an amplifier "adds" energy to a signal because output power exceeds input power.
- Conflating `P_out / P_in` with an energy source: it is merely a ratio of two power levels.
- Applying an AC signal without DC bias: the negative half-cycle and positive voltages below roughly 0.7 V will fail to turn on the junction.[^fiore-biasing-need]
