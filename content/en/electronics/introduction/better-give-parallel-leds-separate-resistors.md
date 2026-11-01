---
id: emb-elintro-0122
title: "Why is it better to give parallel LEDs separate resistors?"
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

Even identical LEDs have a spread in `V_f`, so in a parallel connection the current can be distributed unevenly. A separate series resistor in each branch helps limit and equalize the current; for precise control, you can use a constant-current driver.[^aac-direct-current] Heating can decrease `V_f`, but by itself does not mean inevitable thermal runaway: the outcome depends on the circuit and heat dissipation.[^aac-semiconductors]

## Detailed explanation

In a parallel connection, nearly the same voltage is across each LED, but their current-voltage characteristics and `V_f` are not identical. Because of the steep diode characteristic, even a small difference in forward voltage can cause a difference in currents. An LED with a lower `V_f` can draw most of the current, while the other branch will shine dimmer.[^aac-semiconductors]

A separate resistor in each branch creates local negative feedback: as current increases, the voltage drop across the resistor increases, which restrains further growth. A single shared resistor limits only the total current and does not guarantee its distribution between the LEDs.[^aac-direct-current] Each resistor is calculated for the corresponding supply voltage, `V_f`, and target current, and then tolerance and power dissipation are verified.

Example: for two branches with a 5 V source, an LED with an approximate `V_f = 2 V`, and a current of 10 mA in each, separate resistors `R = (5 V - 2 V)/0.01 A = 300 Ω` are required. A shared resistor of 150 Ω will supply 20 mA in total only with perfectly identical components, but will not balance out the difference in characteristics.

**Common mistake:** assuming that the same voltage across parallel LEDs means the same current. In a series string, the current is identical through each component, whereas parallel branches require their own current limiting or separate regulated outputs.[^aac-semiconductors]
