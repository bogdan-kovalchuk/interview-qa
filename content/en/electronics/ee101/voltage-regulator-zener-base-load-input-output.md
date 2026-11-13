---
id: emb-elee-0226
title: "Voltage regulator with a 5.6 V Zener on the base, 50 mA load, β ≈ 100, 9 V input. What are the output, the base current, and the transistor power?"
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
  - source_id: vishay-silicon-zener-diodes
    title: "Vishay: Silicon Zener Diodes (application document)"
    url: https://www.vishay.com/docs/84117/84117.pdf
  - source_id: fiore-bjt-basics
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 4.2 The Bipolar Junction Transistor"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/04:_Bipolar_Junction_Transistors_(BJTs)/4.2:_The_Bipolar_Junction_Transistor
  - source_id: fiore-bjt-dc-load-line
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 4.6 DC Load Lines"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/04:_Bipolar_Junction_Transistors_(BJTs)/4.6:_DC_Load_Lines
---

## Short answer

The output is `V_out ≈ 5.6 - 0.7 = 4.9 V`: the Zener clamps the base near 5.6 V while the emitter sits a `V_BE ≈ 0.7 V` drop lower.[^vishay-silicon-zener-diodes][^fiore-bjt-basics] Base drive current `I_B ≈ 0.5 mA` (`I_E/(β+1)`) is supplied from the 9 V rail through the resistor feeding the Zener diode. With `V_CE ≈ 4.1 V`, transistor power dissipation is `P ≈ 4.1*0.05 ≈ 0.2 W`.

## Detailed explanation

This is an emitter follower: the collector is connected to 9 V, the load sits in the emitter, and the base is held by a Zener diode. In breakdown mode, a Zener diode maintains an almost constant voltage, so it can be modeled as a source `V_Z0` with a small differential resistance.[^vishay-silicon-zener-diodes] Since `V_BE = V_B - V_E`, the emitter sits at `V_E = V_B - V_BE`. For silicon, `V_BE` is approximately 0.7 V, so `V_out = 5.6 - 0.7 = 4.9 V`.[^fiore-bjt-basics]

For a 50 mA load and β = 100, the emitter current is `I_E = 50 mA`. From `I_E = I_C + I_B` and `I_C = β * I_B`, it follows that `I_B = I_E / (β + 1) = 50 / 101 ≈ 0.495 mA ≈ 0.5 mA`, and `I_C ≈ 49.5 mA`.[^fiore-bjt-basics] The collector is at 9 V, so `V_CE = 9 - 4.9 = 4.1 V`, and the transistor power dissipation is `P = V_CE * I_C = 4.1 * 0.0495 ≈ 0.203 W`. If `I_C = 50 mA` is used, the result is 0.205 W; the difference is about 1%.

The circuit regulates the output only within certain limits. First, the Zener diode must operate in its breakdown region: at very low currents, its dynamic impedance rises sharply and regulation degrades, so the resistor must supply not only `I_B` but also sufficient Zener current.[^vishay-silicon-zener-diodes] Second, when the Zener bias resistor is powered from the same unregulated input rail, regulation drops out much earlier once the input falls below `V_Z` plus the voltage drop across the bias resistor (typically around 6–7 V), because the Zener leaves reverse breakdown. Even with an independent base reference supply, the collector input must remain above `V_out + V_CE(sat) ≈ 4.9 + 0.1 = 5.0 V`; below this, the transistor saturates,[^fiore-bjt-dc-load-line] and the output tracks the collector input minus `V_CE(sat)` without regulation. Third, `V_Z` has a temperature coefficient `α_VZ`, so the output depends on temperature.[^vishay-silicon-zener-diodes]

**Common mistakes:**

- Assuming the output equals `V_Z` (5.6 V) without subtracting `V_BE`.
- Confusing `I_B` with `I_E`: base current is only about `1 / (β + 1)` of the load current.
- Failing to check transistor power dissipation: at `V_CE = 4.1 V` and 50 mA, it is around 0.2 W.
