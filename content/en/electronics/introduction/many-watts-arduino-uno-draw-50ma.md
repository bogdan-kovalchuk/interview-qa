---
id: emb-elintro-0049
title: "How many watts does an Arduino Uno draw (5V, ~50mA)?"
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
  - source_id: aac-electric-power
    title: "All About Circuits: Calculating Electric Power"
    url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-2/calculating-electric-power/
---

## Short answer

If the board operates from `5 V` and draws `50 mA`, its input power equals `P = V*I = 5 V*0.050 A = 0.25 W`. This is a calculation for the specified current, rather than a universal power consumption figure for every Uno configuration.[^aac-electric-power]

## Detailed explanation

Electric power describes the rate of energy transfer or conversion. For a direct current circuit, it is calculated as the product of voltage and current: `P = V*I`. First, current must be expressed in amperes: `50 mA = 0.050 A`; thus, at a voltage of `5 V`, the result is `0.25 W`.[^aac-electric-power]

This value applies to the total current drawn from the power source under the stated conditions. The actual power consumption of an Arduino Uno is influenced by connected modules, GPIO load currents, USB peripherals, and the power supply method. Therefore, the `50 mA` in the question prompt should be read as a given assumption for an exercise rather than a fixed characteristic of all boards across every operating mode. If current varies over time, the product of instantaneous `V` and `I` varies as well; the simple result presented here describes steady-state operation.[^aac-electric-power]

**Unit conversion example:**

```text
50 mA = 50/1000 A = 0.050 A
P = 5 V * 0.050 A = 0.25 W
```

A common mistake is to multiply `5` by `50` and assign units of watts to the result. Such a calculation neglects converting milliamperes to amperes and overestimates the answer by a factor of one thousand. Input power is also not automatically equal to heat dissipated in a single component: it is distributed across the board and connected loads, while a voltage regulator may convert a portion of the energy into heat.[^aac-electric-power]
