---
id: emb-elintro-0048
title: "How do you calculate the resistor for an `LED` if `V_supply = 5 V`, `V_f = 2 V`, `I = 20 mA`?"
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
    title: "All About Circuits: Series LED Resistor Calculator"
    url: https://www.allaboutcircuits.com/tools/led-resistor-calculator
---

## Short answer

For a single `LED`, the series resistor in this nominal example equals `R = (V_supply - V_f)/I = (5 V - 2 V)/0.020 A = 150 Ω`. The power dissipated across it is `P = I²*R = 0.060 W`; the actual `V_f` and allowable current should be verified in the LED datasheet.[^aac-led-resistor]

## Detailed explanation

The series resistor limits current through the `LED`: the remainder of the supply voltage drops across the resistor. For a given operating point, Ohm's law is applied to this part of the circuit. The formula assumes a single LED, a constant-voltage supply, and an approximately constant forward diode voltage; the `LED` itself is not a linear resistor, and without current limiting its operating point cannot be determined solely from the supply voltage rating.[^aac-led-resistor]

**Worked example:**

```text
V_R = 5 V - 2 V = 3 V
R = V_R / I = 3 V / 0.020 A = 150 Ω
P_R = V_R * I = 3 V * 0.020 A = 0.060 W
```

Thus, `150 Ω` gives a calculated `20 mA` under the assumed `5 V` supply and `2 V` forward voltage. A `180 Ω` resistor reduces nominal current to approximately `16.7 mA`, which may be appropriate for lower brightness or operating margin; one should also check supply tolerance, `V_f` spread, and the maximum rated current of the specific LED in its datasheet.[^aac-led-resistor]

The power dissipated in the resistor is `60 mW` under these idealized conditions. The component's power rating must exceed the dissipated power, taking into account temperature, cooling, and manufacturer recommendations; therefore, `1/4 W` provides ample margin here, though this is not a universal requirement for all such circuits.[^aac-led-resistor]

It is critical not to mix units: `20 mA = 0.020 A`. Substituting the number 20 instead of `0.020 A` underestimates the calculated resistance by a factor of one thousand. For multiple series LEDs, one subtracts the sum of their forward voltages in the formula; for a high-power LED, a simple resistor may be unsuitable, and a current regulator is required.[^aac-led-resistor]
