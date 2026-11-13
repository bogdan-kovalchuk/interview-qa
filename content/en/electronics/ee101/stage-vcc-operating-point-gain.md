---
id: emb-elee-0210
title: "CE stage: `V_CC` = 10 V, `I_E` ≈ 1 mA, `R_E` = 1 kΩ, `R_C` = 4.7 kΩ. What are the operating point and the gain?"
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
  - source_id: fiore-bjt-basics
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 4.2 The Bipolar Junction Transistor"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/04:_Bipolar_Junction_Transistors_(BJTs)/4.2:_The_Bipolar_Junction_Transistor
  - source_id: fiore-bjt-dc-load-line
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 4.6 DC Load Lines"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/04:_Bipolar_Junction_Transistors_(BJTs)/4.6:_DC_Load_Lines
  - source_id: fiore-bjt-ac-model
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 7.2 Simplified AC Model of the BJT"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/07:_BJT_Small_Signal_Amplifiers/7.2:_Simplified_AC_Model_of_the_BJT
  - source_id: fiore-common-emitter-amplifier
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 7.3 Common Emitter Amplifier"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/07:_BJT_Small_Signal_Amplifiers/7.3:_Common_Emitter_Amplifier
  - source_id: mit-6071-bjt-notes
    title: "MIT OCW 6.071/22.071 (Spring 2006): Transistors: Bipolar Junction Transistors (BJT), lecture notes"
    url: https://ocw.mit.edu/courses/6-071j-introduction-to-electronics-signals-and-measurement-spring-2006/b30aa58fb0c9915da21e5a5855384818_19_bjt_1.pdf
---

## Short answer

The DC bias levels are `V_E ≈ 1 V`, `V_B ≈ 1.7 V`, and `V_C ≈ 10 - 4.7 = 5.3 V`, yielding `V_CE ≈ 4.3 V` with adequate headroom to both the supply rail and saturation.[^fiore-bjt-basics][^mit-6071-bjt-notes] If `R_E` is unbypassed, voltage gain is `A_v = -R_C/(r'_e + R_E)` with `r'_e ≈ 26 Ω`, giving `A_v ≈ -4.6` neglecting external loading and transistor output impedance.[^fiore-bjt-ac-model][^fiore-common-emitter-amplifier]

## Detailed explanation

The operating point is determined from DC voltages and currents, and only then is the AC signal analyzed. The emitter current here is given as `I_E` ≈ 1 mA. For β = 100, we have `I_C` ≈ `I_E`,[^mit-6071-bjt-notes] so the collector current produces a drop of 1 mA · 4.7 kΩ = 4.7 V across `R_C`, giving `V_C` = 10 - 4.7 = 5.3 V. Across `R_E`, the drop is `V_E` = 1 mA · 1 kΩ = 1 V. The base–emitter junction is forward-biased, with `V_BE` ≈ 0.7 V for silicon, giving `V_B` ≈ 1.7 V.[^fiore-bjt-basics]

Operating boundaries are defined by the DC load line. In cutoff, `I_C` = 0, and the collector is pulled up to `V_CC`, so `V_C` = 10 V.[^mit-6071-bjt-notes] In saturation, `V_CE` drops to approximately 0.2 V.[^mit-6071-bjt-notes] The load line here is determined by `R_C` + `R_E` because `R_E` is unbypassed: `I_C(sat)` ≈ (`V_CC` - `V_CE(sat)`)/(`R_C` + `R_E`) ≈ 9.8/5.7 ≈ 1.7 mA.[^fiore-bjt-dc-load-line] Then `V_E` ≈ 1.7 V and `V_C` ≈ `V_E` + 0.2 V ≈ 1.9 V. Thus, the collector voltage can swing downward by approximately 3.4 V (down to `V_C` ≈ 1.9 V) and upward by 4.7 V to cutoff. The stage therefore operates well inside the active region with generous headroom in both directions.

AC voltage gain is set by the resistance in the emitter circuit. The dynamic junction resistance is `r'_e` = 26 mV / `I_C` = 26 Ω; it is derived from the exponential junction model and varies with `I_C` and temperature.[^fiore-bjt-ac-model] Because `R_E` is not bypassed with a capacitor, its full resistance enters the AC loop, yielding `A_v` = `-R_C`/(`r'_e` + `R_E`) = -4700/(26 + 1000) ≈ -4.6. The negative sign denotes 180° phase inversion, and stage output resistance is approximately `R_C`.[^fiore-common-emitter-amplifier] The internal output impedance of the transistor itself (on the order of 100 kΩ according to Fiore) is neglected here, which slightly reduces gain magnitude in practice.[^fiore-common-emitter-amplifier]

**Example:** if `R_E` is completely bypassed by a capacitor, `r_E` becomes zero in the AC circuit, and `A_v` = `-R_C`/`r'_e` = -4700/26 ≈ -181. Voltage gain increases by nearly 40 times, but distortion increases as well: partial bypassing (swamping) is specifically used to mitigate this distortion.[^fiore-common-emitter-amplifier]

**Common mistakes:**

- Treating `A_v` = `-R_C`/`R_E` as an exact formula: it is an approximation valid only when `R_E` is much larger than `r'_e`.[^fiore-common-emitter-amplifier]
- Calculating gain without checking whether `R_E` is bypassed: a bypass capacitor changes `A_v` by an order of magnitude.[^fiore-common-emitter-amplifier]
- Treating `r'_e` as constant: it depends directly on `I_C` and temperature.[^fiore-bjt-ac-model]
