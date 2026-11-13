---
id: emb-elintro-0252
title: "Why does a MOSFET need a pull-down resistor on the gate?"
track: electronics
section: introduction
sources:
  - source_id: infineon-gate-drive
    title: "Infineon: Gate drive for power MOSFETs in switching applications"
    url: https://www.infineon.com/assets/row/public/documents/24/42/infineon-gate-drive-for-power-mosfets-in-switchtin-applications-applicationnotes-en.pdf
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

The gate stores charge capacitively, so when the driving output floats or disconnects, the gate voltage becomes indeterminate. A resistor between gate and source establishes `V_GS ≈ 0` for an off N-channel MOSFET and bleeds off charge, preventing accidental partial turn-on. Its resistance is chosen considering driver loading and turn-off speed rather than by a universal rule.[^infineon-gate-drive]

## Detailed explanation

The MOSFET gate is isolated from the channel by an insulating layer and electrically behaves largely as a capacitive load. When a GPIO is in a high-impedance state during reset, startup, or physical disconnection, it does not provide a defined logic level. Stray charge, coupled noise, or leakage currents can raise `V_GS`, causing the MOSFET to partially turn on and unintentionally energize the load.[^infineon-gate-drive]

A pull-down resistor is connected between the gate and source of an N-channel switch. It establishes a defined off-state, bleeds off residual gate charge, and provides a path for leakage currents to the source. For a low-side switch with its source grounded, this also ties the gate to `GND`; for other topologies, what matters is the gate voltage relative to the source rather than to an arbitrary ground. Gate driver manufacturers often integrate weak pull-down circuitry from gate to source when the driver output is disabled.[^infineon-gate-drive]

Selecting the resistor value is an engineering trade-off. A lower resistance holds the gate off more robustly and discharges it faster, but increases the steady-state current drawn from the driving output when high. A higher resistance reduces this current draw, but offers weaker immunity against noise coupling and leakage while slowing gate discharge. Therefore, a value like 10 kΩ serves only as a starting estimate: verify the controller's output drive capability, high-temperature leakage, and required behavior during reset.[^infineon-gate-drive]

Example: when a microcontroller boots with its pins in high-impedance mode, an external pull-down keeps `V_GS` near zero until firmware configures the pin as an output. For a P-channel switch, the control polarity is reversed, requiring a pull-up resistor from gate to source to maintain `V_GS ≈ 0` in the off-state. Do not tie the resistor to ground (`GND`) when the off-state reference is a different rail (`source`).[^infineon-gate-drive]
