---
id: emb-elee-0222
title: "Is one flyback diode enough for a bidirectional H-bridge, and does it remove all motor noise?"
track: electronics
section: ee101
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-alternating-current
    title: "All About Circuits textbook, Volume II: AC"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
  - source_id: ti-slva321a
    title: "Texas Instruments SLVA321A: Current Recirculation and Decay Modes"
    url: https://www.ti.com/lit/an/slva321a/slva321a.pdf
  - source_id: ti-slvae59a
    title: "Texas Instruments SLVAE59A: Using Motor Drivers to Drive Solenoids"
    url: https://www.ti.com/lit/an/slvae59a/slvae59a.pdf
---

## Short answer

No. An H-bridge requires a recirculation path across every switch: either antiparallel freewheeling diodes across all four switches or active synchronous rectification.[^ti-slva321a] Flyback diodes only provide a low-impedance clamp path for inductive flyback, protecting switches from overvoltage spikes.[^ti-slvae59a] They do not eliminate high-frequency electromagnetic noise caused by mechanical brush arcing.

## Detailed explanation

An H-bridge controls current in both directions through an inductive load, and when a switch turns off, this current must have a discharge path. TI notes that without a safe path for the discharge current, the bridge's power switches can be damaged.[^ti-slva321a] The conventional path is freewheeling diodes in parallel with the switches, which begin conducting immediately after the switches turn off.[^ti-slva321a] Synchronously turning on the switches, which utilizes the on-state channel resistance, is considered more efficient.[^ti-slva321a] A single diode across the motor terminals opens a path for current in only one direction, whereas an H-bridge has four switches and two current directions, so a single diode is not enough.

The diode itself performs one function: to provide the coil current with a low-impedance path so that large voltage spikes do not occur across the switch.[^ti-slvae59a] In fast decay, the voltage across the load equals the supply voltage plus two diode drops.[^ti-slva321a] For a 12 V supply and an assumed diode drop of 0.7 V, that is `12 + 2 * 0.7 = 13.4 V`. Therefore, switches and diodes must have a voltage rating higher than the supply voltage.

Regarding noise: the diode addresses the coil energy at the moment of switch turn-off. Brush noise is typically associated with arcing at the motor commutator. The diode does not eliminate brush arcing: it acts only on the voltage spike during switch turn-off. Typically, a capacitor across the motor terminals, ferrite beads, or chokes in the lines are added for this purpose, and power loops are kept short. The effect of such measures must be verified by noise measurements.

**Common mistakes:**

- Placing a single diode for the entire bridge and assuming recirculation is provided in both directions.
- Believing that the diode eliminates all motor noise: it addresses only the spike when switching off.
- Rating switches only for the supply voltage without accounting for two diode drops during fast decay.
