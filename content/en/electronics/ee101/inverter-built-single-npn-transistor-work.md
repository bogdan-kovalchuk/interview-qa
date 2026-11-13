---
id: emb-elee-0236
title: "How does an inverter built on a single NPN transistor work?"
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
---

## Short answer

The collector is pulled up to the supply via `R_C`, the emitter is grounded, and the input drives the base through `R_B`. A LOW input holds the transistor in cutoff so the output rises HIGH; a HIGH input drives it into saturation so the output drops LOW, producing a logical NOT. Along the DC load line `I_C = (V_CC - V_CE)/R_C`, with a 5 V supply, `R_C = 4.7 kΩ`, and `V_CE,sat ≈ 0.2 V`, the collector saturation current is ≈ 1.02 mA.[^fiore-bjt-dc-load-line]

## Detailed explanation

The transistor here operates as a switch. When the input is LOW, the base–emitter voltage is below the turn-on voltage, virtually no base current flows, collector current is zero, and there is no voltage drop across `R_C`: the output equals the supply voltage. When the input is HIGH, the base receives current through `R_B`, and the silicon base–emitter junction turns on at approximately 0.7 V.[^fiore-bjt-basics] The base current is then `I_B = (V_in - 0.7) / R_B`.

The external circuit determines the collector current, not the β coefficient alone. The DC load line describes this relationship: `V_CE = V_CC - I_C * R_C`, or `I_C = (V_CC - V_CE) / R_C`.[^fiore-bjt-dc-load-line] When the transistor is saturated, `V_CE` drops to `V_CE,sat`, which for small-signal devices is tenths of a volt (in Fiore's example, 0.15 V at 10 mA). Therefore, the LOW output level equals a few tenths of a volt, not zero.

For the transistor to saturate, the actual β must be no less than `I_C / I_B`. For small-signal devices, β is typically 100–200.[^fiore-bjt-basics] Taking β = 100 as a lower estimate: `I_C / 100 = 1.02 mA / 100 = 0.0102 mA` (around 10 µA). A resistor `R_B = 10 kΩ` gives `I_B = (5 - 0.7) / 10000 = 0.43 mA`, which is about 42 times more than required; saturation is maintained as long as the actual β exceeds `1.02 / 0.43 ≈ 2.4`. If `R_B = 470 kΩ` is used, `I_B ≈ 0.0091 mA` (9.1 µA) is less than 10.2 µA, and with β = 100 the transistor might not saturate, leaving the output higher than `V_CE,sat`.

The circuit inverts correctly only when the input voltage clearly falls into the LOW or HIGH range and the base receives sufficient current. Without `R_B`, the base current is limited only by the driver output impedance and the base–emitter junction, which may overload the driver. A floating input produces an undefined state because the base has no established potential.

**Common mistakes:**

- Assuming that the output drops to 0 V: a saturated transistor provides only `V_CE,sat`, which is typically tenths of a volt.[^fiore-bjt-dc-load-line]
- Treating β as a guaranteed constant: the typical range is broad, so base current must be designed with adequate margin.[^fiore-bjt-basics]
- Leaving the input floating: a base without a defined potential results in an undefined output state.
