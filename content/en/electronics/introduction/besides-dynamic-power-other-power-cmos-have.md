---
id: emb-elintro-0100
title: "Besides dynamic power, what other power does CMOS have?"
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
  - source_id: ti-cmos-power
    title: "CMOS Power Consumption and CPD Calculation"
    url: https://www.ti.com/lit/an/scaa035b/scaa035b.pdf
---

## Short answer

Besides dynamic power during switching, CMOS logic has static power, primarily due to leakage current even at stable logic levels. During a transition, a brief through current can occur when both inverter transistors are partially on; load capacitance also adds dynamic consumption.[^ti-cmos-power]

## Detailed explanation

In CMOS logic, besides switching power, there is static consumption. In a simple CMOS inverter model at a stable logic level, one transistor is on and the other is off, so a continuous path from supply to ground is virtually absent. A real IC still has leakage current, and some internal blocks may consume quiescent current; the product of this current and the supply voltage contributes to static power.[^ti-cmos-power]

During a change of logic state, nodes charge and discharge. Part of the energy is expended on internal parasitic transistor capacitances, and part on output load capacitance, such as traces, inputs of other ICs, or a cable. An input with a slow edge can keep PMOS and NMOS partially on simultaneously for longer, creating a brief current directly from supply to ground. This through current also belongs to transient switching consumption rather than being identical to static leakage.[^ti-cmos-power]

To a first approximation, dynamic consumption increases with switching frequency, the square of the supply voltage, and total switched capacitance. Thus, it can dominate in an active high-speed device, whereas in standby mode, leakage or the consumption of analog and other specialized blocks more often becomes prominent. The ratio depends on technology, temperature, frequency, load, and the specific IC, so "CMOS consumes no power at rest" is merely a simplification.[^ti-cmos-power]

Example: if an inverter switches an output connected to a large capacitance, the supply must charge and discharge it on each transition. Reducing transition frequency or load capacitance reduces this contribution; halting switching does not eliminate leakage or the quiescent current of other blocks. An exact estimate is taken from the datasheet and the manufacturer's methodology for the required voltage, temperature, and operating mode.[^ti-cmos-power]

**Common mistake:** reducing all losses to dynamic power or, conversely, regarding through current as a constant current in a steady-state logic state. Separate quiescent losses from losses that arise during edges and capacitance charging.
