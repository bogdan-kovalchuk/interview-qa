---
id: emb-elcirc-0032
title: "How does a load R_L change a divider's V_out and how do you calculate it?"
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

Connecting a load `R_L` places it in parallel with `R_2`, reducing the effective lower resistance to `R_2,eff = R_2*R_L/(R_2+R_L)`. Substitute `R_2,eff` in place of `R_2` in the standard voltage divider equation. A smaller load resistance `R_L` results in a lower effective resistance and a lower output voltage `V_out`.[^aac-direct-current]

## Detailed explanation

The load is connected between the divider output and common ground, that is, in parallel with `R_2`. For parallel resistances, the equivalent is smaller than either individual value: `R_2,eff = R_2*R_L/(R_2+R_L)`. This equivalent becomes the new lower branch, while the upper resistor `R_1` remains in series with it. Connecting the load alters the ratio of the resistances and therefore changes the output voltage.[^aac-direct-current]

Another way to see the same effect is to represent the unloaded divider as a Thevenin equivalent. Its open-circuit voltage equals the previous `V_out`, and its series output resistance equals `R_1` in parallel with `R_2`. The load current causes a voltage drop across this internal resistance. This model is convenient when comparing several different loads without recalculating the circuit from scratch.[^aac-direct-current]

Calculation example:

Let `V_in = 12 V`, `R_1 = 10 kΩ`, `R_2 = 10 kΩ`, and `R_L = 10 kΩ`. The parallel combination of the lower resistors equals `5 kΩ`, so `V_out = 12 V*5 kΩ/(10 kΩ+5 kΩ) = 4 V`. Without a load, the output would be `6 V`; connecting the resistor halved the lower equivalent resistance, causing the output to sag.

**Common mistakes:**

- Placing `R_L` in series with `R_2`, even though they are connected to the same two nodes.
- Assuming the unloaded divider equation remains exact for any subsequent stage input; the loading effect is determined by the ratio of `R_L` to the divider resistances.
