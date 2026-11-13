---
id: emb-elcirc-0034
title: "Why is a voltage divider a poor power source for a load?"
track: electronics
section: circuit-analysis
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-direct-current
    title: "All About Circuits textbook, Volume I: DC"
    url: https://www.allaboutcircuits.com/textbook/direct-current/
  - source_id: aac-voltage-divider
    title: "All About Circuits: Voltage Divider Circuits"
    url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-6/voltage-divider-circuits/
---

## Short answer

A divider has a finite output resistance: the load shunts `R_2`, altering the lower resistance and dropping `V_out`. Smaller resistor values reduce this sag but increase quiescent current and power losses. Therefore, a divider is typically suitable for a signal or high-impedance input rather than for powering a variable load.[^aac-direct-current]

## Detailed explanation

A divider establishes a voltage only for known resistances and a defined load. Its output can be represented as a Thevenin source: the open-circuit divider voltage in series with an internal resistance of `R_1` in parallel with `R_2`. When the load draws current, a voltage drop develops across this internal resistance, lowering the voltage delivered to the load. As the load current varies, the output voltage fluctuates accordingly.[^aac-direct-current]

Output resistance can be reduced by scaling both resistors down proportionally without changing the nominal division ratio. However, this increases the quiescent current continuously drawn from the source and the power dissipated in the resistors. Increasing the resistances conserves this current, but it makes the output far more sensitive to load variations. A buffer amplifier can decouple a high-impedance divider from the load, while a voltage regulator provides power within its operating ratings.[^aac-direct-current]

Example:

A `12 V` divider made of two `10 kΩ` resistors produces `6 V` unloaded. Its output resistance is `10 kΩ || 10 kΩ = 5 kΩ`. If `R_L = 5 kΩ` is connected, the output drops to `6 V*5 kΩ/(5 kΩ+5 kΩ) = 3 V`. The same divider can be accurate for a high-impedance input yet completely unsuitable for a load that draws substantial current.

**Common mistakes:**

- Selecting the resistor ratio solely based on voltage without checking load current and required precision.
- Believing that increasing the power rating of the resistors eliminates voltage sag: higher wattage only handles heating, but does not reduce output resistance.
