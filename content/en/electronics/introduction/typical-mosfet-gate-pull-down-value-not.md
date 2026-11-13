---
id: emb-elintro-0261
title: "What is a typical gate-to-source pull-down value for an N-channel MOSFET, and why avoid a very low value?"
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
  - source_id: infineon-mosfet-gate-drive
    title: "Infineon: Gate drive for power MOSFETs in switching applications"
    url: https://www.infineon.com/assets/row/public/documents/24/42/infineon-gate-drive-for-power-mosfets-in-switchtin-applications-applicationnotes-en.pdf
---

## Short answer

For an N-channel MOSFET, 10 kΩ between gate and source is a common starting point, but it is a guideline rather than a universal requirement.[^infineon-mosfet-gate-drive] The resistor holds the gate near source potential when the driver output is disconnected or high-impedance, draining residual charge. A smaller value pulls down more strongly, but consumes unnecessary drive current whenever the driver turns the transistor on.[^infineon-mosfet-gate-drive]

## Detailed explanation

A pull-down resistor is necessary because the MOSFET gate possesses capacitance and can remain charged when the driving control output transitions into a high-impedance state. For an N-channel switch, a resistor placed between gate and source establishes a `V_GS` close to zero in this floating condition; without it, noise coupling or leakage currents could trigger unintentional partial turn-on. Infineon recommends an RGS resistor in the kΩ range and cites 10 kΩ as a typical choice, though the optimal value depends on the specific circuit and driver.[^infineon-mosfet-gate-drive]

This resistor is not equivalent to a series gate resistor. A series resistor limits the pulsed charging current into the gate capacitance and controls switching speed; the pull-down is tied between gate and source to define the off-state whenever the driver is unasserted or disconnected. During active driven turn-off, the gate driver typically pulls the gate down to source potential directly, so the pull-down does not dictate normal switching speed.[^infineon-mosfet-gate-drive]

An excessively small pull-down resistor can overload the GPIO or driver: when the output asserts a logic high, continuous current flows through the resistor. For example, at 3.3 V and 10 kΩ, this current is `I = V / R = 0.33 mA`; at 1 kΩ, it would be 3.3 mA. This estimate applies to direct output driving without factoring in other series resistances. Conversely, in environments with strong noise pickup, high parasitic capacitance, or fast unpowered turn-off requirements, the specific circuit must be analyzed rather than mechanically defaulting to 10 kΩ.[^infineon-mosfet-gate-drive]

Selection example: if the switch operates at low speeds and a GPIO pin drives the gate directly, 10 kΩ provides a sensible starting point for a pull-down to source. Verify that the pin can supply this extra current in the on-state and that `V_GS` remains within rated operating limits. For a P-channel MOSFET in a typical off-state, the gate is pulled up to the source (which is a pull-up relative to ground), so the term "pull-down" is not universal across all channel polarities.[^infineon-mosfet-gate-drive]
