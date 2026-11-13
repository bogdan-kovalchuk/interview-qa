---
id: emb-elee-0216
title: "Why is the load in parallel with `R_C` in the AC model of a stage?"
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

In midband frequencies, the output coupling capacitor acts as an AC short circuit, connecting the load directly to the collector. The DC supply rail feeding `R_C` acts as an AC ground via bypass capacitors, placing `R_load` directly in AC parallel with `R_C` to ground.[^fiore-common-emitter-amplifier]

## Detailed explanation

**DC and AC operation.** The output coupling capacitor acts as an open circuit for DC, ensuring that external loading does not shift the transistor Q-point.[^fiore-common-emitter-amplifier] The capacitor is sized so that its reactance at operating frequencies is much smaller than the surrounding circuit resistances. Consequently, for AC signals it acts as a short circuit, connecting `R_load` from the collector to AC ground rather than in series with `R_C`.[^fiore-common-emitter-amplifier]

**Why the power rail is AC ground.** In the AC equivalent circuit, DC voltage sources are replaced by their internal resistances, which equal zero for ideal supplies. Therefore, the `V_CC` node becomes an AC ground.[^fiore-common-emitter-amplifier] Real supply rails exhibit non-zero impedance and noise. Bypass capacitors placed close to active devices lower the rail impedance to AC, making this idealization accurate in practice.[^fiore-common-emitter-amplifier]

**Impact on gain.** The AC collector resistance to AC ground is `R_C || R_load = 4.7 kΩ || 10 kΩ ≈ 3.20 kΩ`. This exact value enters `A_v = -r_C/(r'_e + r_E)` with `r_C = R_C || R_load`.[^fiore-common-emitter-amplifier] Therefore, loading changes AC gain even though DC collector voltage remains unchanged: for an unbypassed `R_E` stage, voltage gain drops from -4.54 to -3.09 (see qid:emb-elee-0215). If `R_E` is bypassed, the emitter becomes AC ground, `r_E` drops to zero, and the gain is determined by `r'_e` and that same `r_C`.[^fiore-common-emitter-amplifier]

**Common mistakes:**

- Assuming `R_load` is in series with `R_C`: for AC signals, both connect in parallel from collector to AC ground.
- Substituting only `R_load` into the gain formula while forgetting `R_C`.
- Assuming power rails act as ideal AC ground without proper decoupling capacitors.[^fiore-common-emitter-amplifier]
