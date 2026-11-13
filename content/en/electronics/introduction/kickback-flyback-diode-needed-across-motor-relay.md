---
id: emb-elintro-0231
title: "Why is a kickback/flyback diode needed across a motor or relay?"
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
  - source_id: ti-inductive-load-clamping
    title: "TI: Switching Inductive Loads with DRV89xx-Q1 Devices"
    url: https://www.ti.com/document-viewer/lit/html/slvaf04
---

## Short answer

Inductance opposes rapid changes in current: when switched off, the coil current cannot drop to zero instantly and generates a voltage spike capable of damaging the switch. A flyback diode provides a recirculation path for the current and clamps the voltage across the switch. Its ratings and circuit topology must match the load current and switch voltage ratings.[^ti-inductive-load-clamping]

## Detailed explanation

A flyback diode protects a transistor or other switch from the transient overvoltage that occurs when switching off a motor or relay. The winding is an inductor: while current flows through it, energy is stored in its magnetic field, and inductance opposes rapid current changes. If the switch opens the only available path, the coil raises its voltage as much as necessary to keep current flowing; in a physical circuit, the upper limit is determined by switch breakdown, parasitic capacitances, and other protection elements.[^ti-inductive-load-clamping]

The diode is connected in parallel with the coil and oriented so that it is reverse-biased during normal operation. After turn-off, the voltage polarity across the coil reverses, the diode turns on, and current circulates through the closed "coil – diode" loop. Stored energy is gradually dissipated as heat in the winding and diode resistance, clamping the switch voltage to approximately the supply level plus the diode forward drop in a typical low-side circuit. The exact transient behavior depends on driver circuitry and the chosen clamping scheme.[^ti-inductive-load-clamping]

A standard diode provides a low clamp voltage and typically slows current decay. In a relay, this can delay contact release; in a motor drive, a solution compatible with the switching profile and braking requirements is needed. A TVS diode or other higher-voltage clamp quenches current faster, but the switch must withstand the resulting voltage. The diode must also be rated for peak coil current, reverse breakdown voltage, and thermal dissipation, not merely average supply current.[^ti-inductive-load-clamping]

**Common mistake:** connecting the diode in series with the motor or orienting it so that it conducts during normal operation. Verify polarity in the switch's off state and ensure the clamp path does not create a short circuit across the power supply.
