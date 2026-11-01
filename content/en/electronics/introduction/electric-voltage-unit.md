---
id: emb-elintro-0042
title: "What is electric voltage and what is its unit?"
track: electronics
section: introduction
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-voltage-current-resistance
    title: "All About Circuits: Ohm’s Law - How Voltage, Current, and Resistance Relate"
    url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-2/voltage-current-resistance-relate/
  - source_id: aac-direct-current
    title: "All About Circuits textbook, Volume I: DC"
    url: https://www.allaboutcircuits.com/textbook/direct-current/
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
---

## Short answer

Voltage between two points is the change in electric potential energy per unit charge: `V = ΔW/Q`. The unit is the volt (V): `1 V = 1 J/C`. Voltage is meaningful only between a pair of points, and the analogy with "height" is merely a simplified model.[^aac-voltage-current-resistance]

## Detailed explanation

Voltage characterizes the difference in electric potential between two points. It can be understood as the work or change in potential energy per unit charge when transferring charge between these points: `V = ΔW/Q`. A volt equals a joule per coulomb, meaning a difference of `1 V` corresponds to `1 J` of energy for each coulomb of transferred charge.[^aac-voltage-current-resistance]

Voltage is not an amount of charge and does not in itself imply that charge is moving: in an open circuit, a voltage can exist between the terminals of a source even though no current flows across the break. To describe a voltage, two points are always required – for example, the terminals of a resistor, or a node and a reference node. In formulas and measurements, the sign depends on the order in which these points are chosen; swapping the probes reverses the sign of the reading, but does not change the physical pair of points.[^aac-voltage-current-resistance]

Example: if there is `9 V` between the terminals of a source, then for a charge of `2 C` the corresponding magnitude of energy change is `18 J`. This does not mean that any charge will automatically receive this exact amount of energy: it must actually travel between these terminals, and the real transfer depends on the circuit and the direction of motion. The height analogy helps visualize the potential difference, but current should not be interpreted literally as water that always "flows downhill" – in a circuit, the source maintains the motion of charges, while the direction is determined by polarity and the convention for conventional current.[^aac-voltage-current-resistance]

**Common mistake:** calling `GND` the absolute zero of voltage. In a schematic, `GND` is typically a chosen reference point assigned `0 V` for convenience; another point, including earth ground, may have a different potential relative to it.
