---
id: emb-elintro-0248
title: "What does `I_G ≈ 0` mean for a microcontroller driving a MOSFET?"
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
  - source_id: infineon-gate-driver-working-principle
    title: "Infineon: How Does a Gate Driver Work?"
    url: https://www.infineon.com/product-information/how-does-a-gate-driver-work
---

## Short answer

Gate current is drawn primarily during brief switching intervals to charge or discharge parasitic gate capacitances.[^infineon-gate-driver-working-principle] Average drive current increases proportionally with gate charge and switching frequency.[^infineon-gate-driver-working-principle]

## Detailed explanation

The MOSFET gate is separated from the channel by an insulating layer, so in the steady-state ideal model no continuous current is required to maintain its conduction state. A real component has leakage, and its input contains parasitic capacitances, making the assertion `I_G ≈ 0` an approximation rather than a guarantee of zero current across all operating conditions. Datasheets typically specify leakage and gate charge as separate parameters.[^infineon-gate-driver-working-principle]

During switching transitions, the microcontroller output sources or sinks charge. The switching time depends on the total gate charge and the available peak current: a rough estimate is `t ≈ Q_g/I_g`. For example, with `Q_g = 20 nC` and an average current of `10 mA`, this estimate yields approximately `2 µs`; the actual waveform shape, Miller plateau, supply voltage, and driver output impedance modify this result. Recharging the gate on every cycle imposes an average load on the power supply, even though the static DC current is negligible.[^infineon-gate-driver-working-principle]

Whether a GPIO pin is sufficient cannot be decided from the MCU's headline peak current rating alone. Verify the maximum pin current limit, the available `V_GS` voltage level, the required switching speed, the gate charge of the specific MOSFET, and transitional losses. A gate driver can source and sink substantially higher current to minimize switching times; while a slower transition may be completely acceptable when driving a relay coil or an indicator LED, at high PWM frequencies it causes excessive switching dissipation.[^infineon-gate-driver-working-principle]

**Common mistake:** assuming that near-zero DC current implies the gate can switch instantaneously or with no load on the GPIO. Always evaluate gate charge under application conditions and confirm that the drive voltage is sufficient to achieve low on-resistance.

Example: if a MOSFET has `Q_g = 20 nC` and switches at `10 kHz`, charge must be delivered on every cycle; the simple product `Q_g*f = 200 µA` estimates the average charging current component for one edge, but reflects neither the peak current nor total driver power. Both edges and the realistic drive profile must be accounted for.[^infineon-gate-driver-working-principle]
