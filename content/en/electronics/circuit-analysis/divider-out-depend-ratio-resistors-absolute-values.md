---
id: emb-elcirc-0029
title: "Does a divider's V_out depend on the ratio of the resistors or on their absolute values?"
track: electronics
section: circuit-analysis
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-direct-current
    title: "All About Circuits textbook, Volume I: DC"
    url: https://www.allaboutcircuits.com/textbook/direct-current/
  - source_id: ti-slaa067
    title: "Texas Instruments: Understanding Basic Analog – Circuit Equations"
    url: https://www.ti.com/lit/pdf/slaa067
---

## Short answer

For an unloaded divider, `V_out = V_in*R_2/(R_1+R_2)`, so scaling both resistors by the same factor preserves output voltage while altering quiescent current. When an external load is connected, absolute resistor values become critical because they dictate the divider's output impedance and the resulting voltage sag under load.[^ti-slaa067]

## Detailed explanation

For an unloaded divider, output voltage is determined by the ratio of resistances to their sum, rather than by the absolute scale of the component values. Multiplying `R_1` and `R_2` by the same factor leaves the ratio unchanged. This follows from the fact that the same current flows through both series resistors, and the voltage drop across each is proportional to its resistance.[^ti-slaa067]

Absolute values nevertheless dictate the quiescent current drawn by the divider itself: `I = V_in/(R_1+R_2)`. Increasing both resistances tenfold reduces this current tenfold for a given supply voltage. While this conserves power, it simultaneously raises the divider's output impedance. Consequently, a measurement instrument or subsequent input stage will exert a greater loading effect on `V_out` unless its input resistance is substantially higher than the resistance of the lower branch.[^ti-slaa067]

Example: for `V_in = 12 V`, `R_1 = 10 kΩ`, and `R_2 = 10 kΩ`, the unloaded output is 6 V, and the divider current is 0.6 mA. If values of `100 kΩ` and `100 kΩ` are used instead, the output remains 6 V, but current drops to 0.06 mA. Connecting `R_load = 100 kΩ` to the second configuration creates a parallel combination `100 kΩ || 100 kΩ = 50 kΩ`; output voltage then drops to 4 V. Thus, voltage equivalence held true only for the unloaded divider.[^ti-slaa067]

**Common mistakes:**

- Asserting that absolute resistance values never matter. That holds true only for an ideal unloaded output.
- Increasing resistor values solely to reduce power consumption without verifying load resistance and input bias current.
- Calculating `V_out` using the unloaded formula when a load component is connected to the output; in that case, `R_2` must be replaced by `R_2 || R_load`.

Component values are also selected considering resistor power ratings and available standard values. If load fluctuates or demands substantial current, a buffer stage or voltage regulator typically provides a much more predictable output than merely increasing divider quiescent current.[^ti-slaa067]
