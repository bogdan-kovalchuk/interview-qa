---
id: emb-elintro-0145
title: "What is the basic inductor formula?"
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

The voltage of an ideal inductor is proportional to the rate of change of current: `v = L*(di/dt)`. At steady current, the ideal inductive component has zero voltage, but a real coil also has winding resistance.[^aac-direct-current]

## Detailed explanation

The basic relationship of an ideal inductor relates the voltage across its terminals to the rate of change of current: `v = L*(di/dt)`. Here, `L` – inductance in henries, `i` – current, and the sign depends on the chosen reference directions of current and voltage; physically, the induced voltage opposes the change in current.[^aac-direct-current]

This relationship explains why an inductor does not allow current to change instantaneously. If a constant voltage is applied, the current of an ideal coil changes linearly with a slope of `di/dt = v/L`. Doubling the inductance at the same voltage halves the slope, and doubling the voltage at the same inductance doubles it.[^aac-direct-current]

At steady current, `di/dt = 0`, so the voltage across the ideal inductance equals zero. In a real component, there is winding resistance, so the total voltage also has a resistive component; a simple model is written as the sum of the inductance voltage and the drop across the wire resistance. Core saturation can also make the effective inductance depend on current, so a constant `L` is an approximation within the component's operating range.[^aac-direct-current]

Example: if `4 V` is applied across an ideal `2 H` coil, the current will rise at a rate of `2 A/s`. In `0.5 s`, it will increase by `1 A`, provided the initial current is zero and the voltage truly remains constant.

**Common mistake:** Confusing the inductor formula with Ohm's law for a resistor. For a resistor, voltage is determined by the instantaneous current, whereas for an inductor it is set by the rate of change of current; therefore, the same current can correspond to different voltages depending on how rapidly it is changing.[^aac-direct-current]
