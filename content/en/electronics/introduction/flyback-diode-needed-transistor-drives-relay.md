---
id: emb-elintro-0216
title: "Why is a flyback diode needed when a transistor drives a relay?"
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
  - source_id: aac-inductor-commutating
    title: "All About Circuits: Inductor commutating circuits"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/chpt-3/inductor-commutating-circuits/
  - source_id: ti-inductive-clamp
    title: "Texas Instruments: Designing for Loss of Ground and Loss of Battery on Texas Instruments High-Side Switches"
    url: https://www.ti.com/lit/pdf/slvaes9
---

## Short answer

A relay coil is an inductive load, so its current cannot drop to zero instantaneously when the transistor turns off: the coil generates a voltage that maintains current, and without clamping it can damage the switch. A diode in parallel with the coil provides a recirculation path for the current; in a typical low-side switch circuit, its cathode connects to `+V` and its anode to the coil side near the transistor.[^aac-inductor-commutating]

## Detailed explanation

A flyback diode protects the switch from the transient voltage that occurs when turning off a relay coil. The coil stores energy in a magnetic field, and the relationship between voltage and the rate of current change is described by `v = L*di/dt`. When the transistor opens the circuit, the coil current tends to continue in the same direction, so the voltage polarity across the coil reverses. Without a path for the current, the voltage can rise to a level dangerous for the transistor; its magnitude depends on the circuit and parasitic parameters, rather than being a constant "hundred volts."[^aac-inductor-commutating]

The diode is mounted directly in parallel with the coil and oriented in reverse polarity relative to the operating voltage. During turn-on, it is reverse-biased and has virtually no effect on the coil current. After turn-off, the polarity across the coil reverses, the diode forward-biases, and the current gradually decays in the local "coil–diode" loop. This clamps the voltage across the switch to approximately one diode forward drop above the supply voltage, but makes demagnetization slower; for a relay, this can increase contact release time.[^aac-inductor-commutating]

For a typical low-side NPN switch, the cathode of the diode is connected to the supply end of the coil (`+V`), and the anode to the end leading to the collector. The "in parallel" specification is important: the diode is not placed in series with the coil. Nor should any diode be considered automatically suitable: you check the allowable forward current, pulsed conditions, and reverse voltage of the specific component. Faster current decay is sometimes needed for faster relay release; then a higher clamp level is used, such as a properly calculated combination of a diode and a Zener diode, taking into account the transistor's limiting voltage.[^ti-inductive-clamp]

**Common mistake:** leaving the coil unclamped or reversing the diode polarity. In the first case, turn-off creates a large inductive spike; in the second, the diode conducts during normal operation and effectively shorts the supply through itself and the switch, bypassing the coil. Before applying power, verify that in normal operation the cathode has a higher potential than the anode, and that the protection parameters are matched to the coil and switch.[^aac-inductor-commutating]
