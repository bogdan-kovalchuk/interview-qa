---
id: emb-elcirc-0035
title: "How do you practically choose the absolute values of R1 and R2 in a divider?"
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

First, set the ratio required for the target `V_out`, then choose the divider current taking the load into account. Lower resistor values decrease output impedance but increase power consumption and heat dissipation. Higher values conserve current but react more strongly to loading and input bias current.[^aac-direct-current]

## Detailed explanation

First determine the desired voltage ratio, as it sets the ratio of the branches: `V_out/V_in = R_2/(R_1+R_2)`. This does not fix absolute values: doubling both resistors leaves the ideal unloaded voltage unchanged. The absolute scale is chosen based on requirements for current, loading, precision, and allowable heating.[^aac-direct-current]

For a given `V_in` and resistor values, the divider current equals `V_in/(R_1+R_2)`. Lowering the resistance values increases current and power consumption, but it reduces the output resistance `R_1 || R_2`, meaning the load causes less deviation at the output node. If the divider feeds a microcontroller input to read voltage, compare the source impedance with the input impedance and leakage current of that pin; for an ADC, also consider sampling time requirements from the datasheet. A voltmeter loads a high-resistance circuit unless its input impedance is substantially larger than the lower branch resistance.[^aac-direct-current]

Check the power dissipation of each resistor using `P = I²*R` against its rated power under actual operating conditions. Account for resistor tolerance and input voltage variations if the output must remain within specified limits: tolerance error in one branch alters the division ratio. There is no universal guideline like "always use 10 kΩ" – the choice depends on current, accuracy, and loading.[^aac-direct-current]

Calculation example:

For `V_in = 12 V` and `V_out = 4 V`, the ratio `R_1:R_2` must be `2:1`. Choosing `R_1 = 20 kΩ` and `R_2 = 10 kΩ` results in an unloaded current of `12 V/30 kΩ = 0.4 mA`, and the power dissipated by the top resistor is `(0.4 mA)²*20 kΩ = 3.2 mW`. Using resistance values ten times smaller would preserve the ideal `4 V`, but would increase both current and dissipated power by a factor of ten.

**Common mistakes:**

- Selecting component values solely based on the ratio without checking current draw and power dissipation.
- Using excessively high resistances for an input with significant bias/leakage current or for measurements, causing the load to distort the divided voltage.
