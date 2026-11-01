---
id: emb-elintro-0121
title: "Why must an LED not be connected directly to a voltage source without a resistor?"
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
---

## Short answer

After an LED turns on, its current increases rapidly with increasing voltage, so a voltage source by itself does not establish a safe current. A series resistor or a current driver limits it; for a 5 V source, an LED with `V_f = 2 V`, and a current of 10 mA, the ideal calculation gives `R = (5 V - 2 V)/0.01 A = 300 Ω`.[^aac-semiconductors] Actual `V_f` and permissible current are taken from the specific LED's datasheet.[^aac-direct-current]

## Detailed explanation

An LED is a diode for which the forward current increases non-linearly with increasing voltage. Near the operating point, a small change in voltage can cause a significant change in current, so connecting to a source that merely maintains a set voltage does not guarantee a safe operating mode.[^aac-semiconductors]

A series resistor creates a voltage drop proportional to the current and stabilizes it against variations in LED parameters. The resistor is selected from the supply voltage, the expected `V_f` at the required current, and the target current; you also check the resistor power dissipation and the LED's limit parameters.[^aac-direct-current] Instead of a resistor, you can use a driver that regulates the current directly.[^aac-semiconductors]

Worked example:

```text
V_supply = 5 V
V_f = 2 V; I = 10 mA = 0.01 A
R = (V_supply - V_f)/I = 300 Ω
P_R = I²*R = 0.03 W
```

This is an ideal example; in practice, you account for the spread in `V_f`, supply voltage variation, resistor tolerance, and power margin. A common mistake – assuming that the nominal LED voltage limits the current on its own.[^aac-direct-current]

When selecting, check not only the typical operating conditions but also worst-case conditions: the highest source voltage together with the lowest `V_f` gives the highest current, while the lowest voltage with the highest `V_f` gives the lowest. For powering from a GPIO, take into account its permissible output current and the voltage drop under load. If brightness across a wide supply range is required, a current regulator usually provides better control, but also has its own voltage limits and power dissipation.[^aac-direct-current]
