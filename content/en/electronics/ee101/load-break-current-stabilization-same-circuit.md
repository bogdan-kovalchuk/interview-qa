---
id: emb-elee-0195
title: "Why does a 4.7 kΩ load break current stabilization in the same circuit (`V_B` = 1.7 V, `R_E` = 1 kΩ, +5 V)?"
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
  - source_id: fiore-bjt-collector-curves
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 4.3 BJT Collector Curves"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/04:_Bipolar_Junction_Transistors_(BJTs)/4.3:_BJT_Collector_Curves
  - source_id: fiore-bjt-dc-load-line
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 4.6 DC Load Lines"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/04:_Bipolar_Junction_Transistors_(BJTs)/4.6:_DC_Load_Lines
---

## Short answer

A 4.7 kΩ load between +5 V and the collector drops 4.7 V at 1 mA, leaving `V_C ≈ 0.3 V`, which falls below `V_E ≈ 1 V`. The collector must remain above the emitter by at least the saturation voltage of a few tenths of a volt.[^fiore-bjt-collector-curves] Without this headroom, the transistor enters saturation, dropping out of constant-current regulation and reducing load current.

## Detailed explanation

The circuit operates as a constant-current source. The base is held at 1.7 V, placing the emitter approximately 0.7 V lower: `V_E` = 1.7 V - 0.7 V = 1.0 V. The emitter current is set by the resistor: `I_E` = 1.0 V / 1 kΩ = 1 mA. For silicon `V_BE ≈ 0.7 V`, with `I_E = I_C + I_B` and `I_C = β * I_B`. Because `I_C` is substantially larger than `I_B`, collector current virtually equals `I_E`, or 1 mA, as long as the transistor operates in active mode.[^fiore-bjt-basics]

At `I_C = 1 mA`, a load between +5 V and the collector drops `1 mA * 4.7 kΩ = 4.7 V`, leaving the collector at `5 V - 4.7 V = 0.3 V`. This is lower than the emitter potential: `V_CE = 0.3 V - 1.0 V = -0.7 V`. For the transistor to remain in the constant-current region, `V_CE` must exceed the saturation voltage. In the textbook example, `V_CE(sat) ≈ 0.15 V` at `I_C = 10 mA` and `I_B = 0.3 mA`, and for small-signal devices it is typically around a tenth of a volt.[^fiore-bjt-dc-load-line]

Assuming `V_CE(sat) ≈ 0.15 V` as a reference, the collector cannot drop below `V_E + 0.15 V ≈ 1.15 V`, so the maximum load resistance that still supports 1 mA is `(5 V - 1.15 V) / 1 mA ≈ 3.85 kΩ`. With 4.7 kΩ, the transistor enters saturation. If `V_B` remains an ideal source (emitter at 1.0 V, base supplying excess current of ≈ 0.18 mA), the current through the load becomes `(5 V - 1.15 V) / 4.7 kΩ ≈ 0.82 mA`, approximately 18% below 1 mA. The textbook explains that when the calculated current exceeds the compliance limit, the transistor is saturated and the actual current equals the circuit limit.[^fiore-bjt-dc-load-line]

To sustain 1 mA, voltage headroom should be checked before calculating current: `V_CC - I_C * R_L >= V_E + V_CE(sat)`. For 4.7 kΩ and 1 mA, this requires `V_CC >= 5.85 V`. Otherwise, one must either increase the supply voltage or reduce the load to approximately 3.85 kΩ. The exact `V_CE(sat)` depends on current and the specific transistor, and should be taken from datasheet curves.[^fiore-bjt-dc-load-line]

**Common mistakes:**

- Assuming `R_E` guarantees 1 mA under any load without checking collector voltage.
- Assuming `V_CE(sat) = 0`: this overstates available voltage headroom.[^fiore-bjt-dc-load-line]
- Comparing collector voltage to ground instead of checking `V_CE` relative to the emitter.
