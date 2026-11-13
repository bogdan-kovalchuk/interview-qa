---
id: emb-elee-0213
title: "What is AC ground in small-signal analysis?"
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
  - source_id: fiore-common-emitter-amplifier
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 7.3 Common Emitter Amplifier"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/07:_BJT_Small_Signal_Amplifiers/7.3:_Common_Emitter_Amplifier
---

## Short answer

In small-signal analysis, an ideal DC voltage supply carries zero AC variation, so its AC equivalent resistance is zero and it is modeled as an AC short circuit. Any circuit node connected to such a rail is referred to as an AC ground.[^fiore-common-emitter-amplifier] This is an analytical modeling technique, not an instruction to physically short power rails to ground.

## Detailed explanation

Small-signal analysis is performed in two separate steps. First, DC voltages and currents are calculated to find the transistor operating point. Second, the AC signal is analyzed independently using the superposition principle. In the AC equivalent circuit, coupling and bypass capacitors are replaced with short circuits, and DC sources are replaced by their ideal internal resistance, which is also a short circuit.[^fiore-common-emitter-amplifier]

The rationale is straightforward: an ideal DC voltage source maintains a constant voltage, so its AC variation is identically zero. Because an ideal source has zero internal resistance, no AC voltage can develop across its terminals, meaning any circuit node connected to such a rail has zero AC voltage relative to ground. In a common-emitter stage with `V_CC` = 10 V, this means the supply rail remains at +10 V DC, but functions as ground for AC signals.[^fiore-common-emitter-amplifier]

This leads directly to how component impedances are modeled. In the DC circuit, `R_C` is connected to `V_CC`, but in the AC circuit its upper terminal connects to ground. That is why in the small-signal equivalent circuit, the collector load resistor is placed between collector and ground rather than between collector and the power rail.[^fiore-common-emitter-amplifier]

AC ground is an analytical idealization. Real power supplies exhibit non-zero internal impedance, so the short-circuit assumption holds only when this impedance is negligibly small compared to circuit impedances at signal frequencies. The input signal source is an exception to this rule: its AC source is not shorted, because its time-varying signal is precisely what is being analyzed.[^fiore-common-emitter-amplifier]

**Common mistakes:**

- Treating AC ground as a physical connection to 0 V: a +10 V rail can be an AC ground, which does not mean its DC voltage is zero.[^fiore-common-emitter-amplifier]
- Replacing the input signal source with a short circuit: in the AC small-signal model, only DC sources are shorted.[^fiore-common-emitter-amplifier]
