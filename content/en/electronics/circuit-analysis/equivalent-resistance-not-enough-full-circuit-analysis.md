---
id: emb-elcirc-0027
title: "Why is the equivalent resistance not enough for a full circuit analysis?"
track: electronics
section: circuit-analysis
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-direct-current
    title: "All About Circuits textbook, Volume I: DC"
    url: https://www.allaboutcircuits.com/textbook/direct-current/
  - source_id: ti-slaa067
    title: "Texas Instruments: Understanding Basic Analog – Circuit Equations"
    url: https://www.ti.com/lit/pdf/slaa067
---

## Short answer

An equivalent resistance `R_eq` characterizes port behavior seen by the source, but conceals individual voltages and currents across internal elements. To determine local branch currents and internal node potentials, you must unwrap the original circuit topology and apply Ohm's law, KCL, and KVL.[^ti-slaa067]

## Detailed explanation

Equivalent resistance is a convenient simplification of a network portion that preserves the relationship between voltage and current at its external terminals. For a source connected to this network, this substitution is sufficient to solve for total current. However, internal network structure is concealed, meaning a single value of `R_eq` cannot by itself reveal all internal component voltages and currents.[^ti-slaa067]

For example, different pairs of parallel resistors can yield the exact same equivalent resistance while having completely different individual values. Total current through the pair is determined by the equivalent, but the fraction of current carried by each branch depends on its specific resistance. KCL requires that branch currents sum to the total entering node current. Similarly, in a series branch, the current is known for the entire branch, but the voltage across each resistor depends on its share of total resistance and is verified through KVL.[^ti-slaa067]

For a complete analysis, define what must be solved: source current, a specific node potential, or an individual component current. The circuit can initially be simplified to find total quantities. Then unwrap the substitutions in reverse order: the voltage across a parallel block appears across every one of its branches, and the current through a series block passes through every one of its elements. Ohm's law translates known voltages and currents into the desired quantities.[^ti-slaa067]

Example: for 12 V and two parallel resistors of 6 kΩ and 3 kΩ, equivalent resistance is 2 kΩ, yielding a total current of 6 mA. The value of `R_eq` alone does not indicate that branch currents are 2 mA and 4 mA respectively; these values are obtained separately from the 12 V drop across each branch. Their sum matches total current, as required by KCL.[^ti-slaa067]

**Common mistakes:**

- Treating `R_eq` as a complete description of the circuit. It is merely an external terminal equivalent for specific terminals and conditions.
- Assigning identical current to all parallel branches, or differing voltages to branches connected across the same nodes.
- Ignoring external loading that alters the equivalent network and source current.

For more complex circuits that cannot be reduced by simple series-parallel combinations, nodal or mesh equations are required. An equivalent circuit remains useful, but only for the specific question it preserves: terminal behavior across chosen ports.[^ti-slaa067]
