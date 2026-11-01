---
id: emb-elintro-0120
title: "Calculate the series resistor for a red `LED`: V = 5 V, V_f = 1.9 V, I = 15 mA?"
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
  - source_id: aac-led-resistor
    title: "All About Circuits: Special-purpose Diodes"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/chpt-3/special-purpose-diodes/
---

## Short answer

With an ideal `5 V` source and a given forward drop `V_f = 1.9 V`, the calculation gives `R = (5 - 1.9)/0.015 ≈ 207 Ω`; the nearest higher standard value `220 Ω` sets approximately `14.1 mA`.[^aac-led-resistor] The actual `V_f` varies between individual parts and with current and temperature, so this calculation is for the specified assumptions rather than an exact guaranteed current.

## Detailed explanation

A series resistor for an `LED` is selected based on the difference between the source voltage and the forward drop across the diode, divided by the desired current; under the given conditions of `5 V`, `1.9 V`, and `15 mA`, the ideal result is approximately `207 Ω`.[^aac-led-resistor]

In a series circuit, the same current flows through the resistor and the `LED`. By Kirchhoff's voltage law, the sum of the voltage drops equals the source voltage, so the resistor must take up what remains after the forward drop across the diode. Ohm's law gives `R = (V_supply - V_f)/I`. The `V_f` value depends on diode type, current, and temperature; the value `1.9 V` in this problem is a given assumption for calculation, not a universal parameter of every red `LED`.[^aac-led-resistor]

Substituting the numbers gives `3.1 V` across the resistor. Dividing by `0.015 A` gives approximately `206.7 Ω`, so for an educational example you can choose the standard `220 Ω`. Under the same ideal `5 V` and `1.9 V`, the current will be around `14.1 mA`, and the resistor power dissipation – around `44 mW`. This is below the typical resistor rating of `0.125 W`, but a real design must account for temperature and the derating of the specific resistor.[^aac-led-resistor]

```text
V_R = 5 - 1.9 = 3.1 V
R_ideal = 3.1 / 0.015 = 206.7 Ω
I_at_220Ω = 3.1 / 220 = 0.0141 A ≈ 14.1 mA
P_at_220Ω = 3.1 * 0.0141 ≈ 0.044 W
```

**Common mistakes:**

- Dividing the full `5 V` voltage by the current and forgetting the forward drop across the `LED`. Then the resistor will turn out too large for the specified current.
- Substituting `15` instead of `0.015` into the formula with ohms. Current must be expressed in amperes.
- Assuming that `220 Ω` guarantees exactly `15 mA`. The actual current depends on resistor tolerance, supply voltage, and `V_f` spread; check the calculation at datasheet limits.[^aac-led-resistor]
