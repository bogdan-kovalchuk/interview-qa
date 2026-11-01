---
id: emb-elintro-0115
title: "What is the formula for an `LED` current-limiting resistor?"
track: electronics
section: introduction
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-direct-current
    title: "All About Circuits textbook, Volume I: DC"
    url: https://www.allaboutcircuits.com/textbook/direct-current/
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
  - source_id: idec-led-current-limiting-resistor
    title: "IDEC: A1, A2, A8 Series Miniature Pilot Lights"
    url: https://media.digikey.com/pdf/Data%20Sheets/IDEC%20PDFs/A1%2CA2%2CA8_Miniature_Switches_Pilot_lights.pdf
---

## Short answer

For a series resistor, `R = (V_supply - V_f)/I_LED`. With `V_supply = 5 V`, `V_f = 2.1 V`, and a target current of `15 mA`, the calculation yields `193 Ω`; choosing `220 Ω` gives approximately `13.2 mA` under these assumptions.[^idec-led-current-limiting-resistor]

## Detailed explanation

A series resistor limits the current through an LED by dropping a portion of the supply voltage. In a simple single-LED circuit, Kirchhoff's voltage law gives `V_supply = V_f + V_R`, and Ohm's law for the resistor gives `R = V_R/I_LED`. This yields the formula `R = (V_supply - V_f)/I_LED`. It assumes a constant voltage source, a single LED and resistor in series, and a current that is identical through both components in this branch.[^idec-led-current-limiting-resistor]

Units must be consistent: current in the formula is specified in amperes if voltage is specified in volts, which yields resistance in ohms. `V_f` is not a strict constant, so calculating with a typical value yields an approximation. For a safe design, check the maximum rated LED current in the datasheet and repeat the calculation for minimum `V_f` and maximum supply voltage – this combination produces the highest current.[^idec-led-current-limiting-resistor]

Worked example for `5 V`, a typical `V_f = 2.1 V`, and a target current of `15 mA`:
```text
R = (5 - 2.1)/0.015 = 193.3 Ω
I_LED at R = 220 Ω: (5 - 2.1)/220 = 0.0132 A
P_R = (5 - 2.1)*0.0132 ≈ 0.038 W
```
Therefore, `220 Ω` gives about `13.2 mA`; the resistor requires a power rating above the calculated approximately `0.038 W`, with a safety margin based on operating temperature and mounting conditions. With other real-world supply tolerances or `V_f` values, the current will differ.[^idec-led-current-limiting-resistor]

**Common mistakes:**
- Substituting `15` instead of `0.015` for a current of `15 mA`.
- Dividing the full supply voltage by the current, forgetting to subtract the voltage drop across the LED.
- Treating the calculated number as a guaranteed current without checking parameter variation.
