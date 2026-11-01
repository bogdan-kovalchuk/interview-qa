---
id: emb-elintro-0190
title: "A Si diode + Schottky + green `LED` in series: what is the total voltage drop?"
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
  - source_id: aac-diode-forward-voltage
    title: "All About Circuits: Introduction to Diodes and Rectifiers"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/chpt-3/introduction-to-diodes-and-rectifiers/
  - source_id: aac-led-forward-voltage
    title: "All About Circuits: Special-purpose Diodes"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/chpt-3/special-purpose-diodes/
---

## Short answer

The total voltage drop in a series circuit equals the sum of the diodes' instantaneous forward voltages at their actual operating current, rather than a fixed sum for all components.[^aac-diode-forward-voltage] The values `0.7 V`, `0.3 V`, and `2.1 V` yield only a rough estimate of `3.1 V`; at `12 V` and `330 Ω`, it predicts a current of approximately `27 mA`, which must be checked against the LED datasheet rather than automatically assumed acceptable.[^aac-led-forward-voltage]

## Detailed explanation

The total voltage drop across a series diode string at a given operating point equals the sum of the voltages across each individual element. The value `0.7 V` for a silicon diode is a convenient approximation, not a constant property at any current. In a Schottky diode the drop is typically lower, while in an LED it depends on the semiconductor material, color, current, and temperature.[^aac-diode-forward-voltage] [^aac-led-forward-voltage]

First, you must set or estimate the circuit current, and then take the corresponding forward voltages from the datasheet of each specific component. For a series circuit, the current is identical in all elements, and the resistor must drop the remainder of the supply voltage: `I = (V_supply - ΣV_f)/R`. The formula is convenient for an initial estimate; however, if the current changes, the drops across the diodes also change; a more accurate solution is found consistently with their characteristics or verified by measurement.[^aac-diode-forward-voltage] [^aac-led-forward-voltage]

Worked example: if, for illustration, drops of `0.7 V`, `0.3 V`, and `2.1 V` are assumed, the sum is `3.1 V`. With a `12 V` supply and a `330 Ω` resistor, this gives an estimate of `I = (12 V - 3.1 V)/330 Ω ≈ 27 mA`. This calculation assumes these specific forward voltages and does not confirm that the selected LED can be operated safely at `27 mA`: you must check the maximum continuous current and power dissipation, as well as supply tolerances. Green LEDs have a wide voltage spread across models, so the color alone is insufficient.[^aac-led-forward-voltage]

**Common mistakes:**

- Adding typical drops and assuming the sum is guaranteed regardless of current and temperature.
- Calling the resulting `27 mA` "normal" for any LED without checking the specific datasheet and thermal limits.[^aac-led-forward-voltage]
