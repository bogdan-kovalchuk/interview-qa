---
id: emb-elintro-0193
title: "How do you choose the series resistor for a simple Zener regulator?"
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
  - source_id: aac-zener-regulator
    title: "All About Circuits: What Are Zener Diodes?"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/chpt-3/zener-diodes/
---

## Short answer

The series resistor must supply the maximum load current and the minimum Zener current at the lowest input voltage: `R_s = (V_in - V_Z)/(I_load,max + I_Z,min)`. Next, check the maximum input voltage and minimum load current so that the Zener diode and resistor do not exceed their allowable power ratings.[^aac-zener-regulator]

## Detailed explanation

The series resistor in a simple Zener regulator limits the total current from the source. In the regulation region, this current branches: part goes to the load, and the remainder flows through the Zener diode. Therefore, the calculation must simultaneously ensure the minimum Zener current for regulation without exceeding its allowable current and power limits.[^aac-zener-regulator]

First, check the worst case for maintaining regulation: the lowest source voltage combined with the highest load current. Under these conditions, the sum of the maximum load current and the minimum Zener current must pass through the resistor, so `R_s <= (V_in,min - V_Z)/(I_load,max + I_Z,min)`. If the load draws no current, nearly all resistor current passes through the Zener diode; this is why the maximum source voltage and component power ratings are checked separately.[^aac-zener-regulator]

Example: for a `5.1 V` Zener diode, a `9 V` source, a load up to `10 mA`, and a required minimum Zener current of `5 mA`, the boundary value from the regulation condition is `(9 V - 5.1 V)/(10 mA + 5 mA) = 260 Ω`. This is a calculated upper limit: choosing a standard value below it will increase the current, so you must also verify the power dissipations at maximum `V_in` and no-load conditions. The value `5 mA` here is given as a condition of the example, not a universal Zener characteristic.[^aac-zener-regulator]

**Common mistake:** considering only the load current. If no margin is left for `I_Z,min`, the Zener diode may drop out of the breakdown region under heavy load, causing the output voltage to fall. An overly small resistor is also dangerous at maximum input voltage, especially with no load.[^aac-zener-regulator]
