---
id: emb-elee-0185
title: "Which breadboard measures reduce motor noise on the supply?"
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
  - source_id: ti-slva959b-motor-driver-layout
    title: "TI: Best Practices for Board Layout of Motor Drivers (SLVA959B)"
    url: https://www.ti.com/lit/an/slva959b/slva959b.pdf
  - source_id: ti-slvaft0-bulk-capacitor-sizing
    title: "TI: Bulk Capacitor Sizing for DC Motor Drive Applications (SLVAFT0)"
    url: https://www.ti.com/lit/an/slvaft0/slvaft0.pdf
---

## Short answer

Key measures include bulk capacitance to buffer low-frequency motor current transients, local ceramic decoupling capacitors near ICs, short power loops, a separate return path for motor current, and small ceramics directly across the power stage.[^ti-slva959b-motor-driver-layout] A separate return path prevents motor switching currents from modulating the ground reference of sensitive logic stages.[^ti-slva959b-motor-driver-layout]

## Detailed explanation

A motor draws large current surges from the power supply during every PWM switching event. Because conductors have inductance, a rapid change in current causes a voltage spike on the power supply pins that propagates into adjacent stages. Countermeasures operate across different timescales: a bulk capacitor suppresses low-frequency surges, while ceramic capacitors handle fast edges.

The bulk capacitor sits near the board power input and delivers high currents to the driver during switching. According to TI, such capacitors are typically larger than 10 µF and feature low ESR.[^ti-slva959b-motor-driver-layout] Sizing can be estimated using the formula `C > ΔI · T_PWM / ΔV`: with `ΔI = 200 mA`, `T_PWM = 50 µs`, and `ΔV = 0.1 V`, we obtain `C ≥ 0.2 A · 50 µs / 0.1 V = 100 µF`. This is an idealized estimate without ESR, so the actual capacitance is chosen with a safety margin.[^ti-slvaft0-bulk-capacitor-sizing]

Ceramic capacitors for fast edges are placed as close to the pins as possible: TI recommends a distance of less than 0.5 cm and no vias between the capacitor and the pin. A smaller capacitor is placed closer than a larger one. Trace inductance at high frequencies causes voltage ringing at the power pin, which becomes a source of EMI.[^ti-slva959b-motor-driver-layout] On a breadboard the root cause is identical: long jumper wires also have inductance.

The high-current loop runs from the positive supply rail through the high-side switch, the motor winding, and the low-side switch back to the negative rail. During switching, its inductance causes voltage spikes, so traces must be short and wide.[^ti-slva959b-motor-driver-layout] Motor current return must follow a separate path: common ground impedance creates a voltage drop that sensitive stages see as common-mode noise (ground bounce). Single-point power routing provides each load with its own path to the source.[^ti-slva959b-motor-driver-layout] For the power stage, TI recommends small ceramic capacitors that suppress high-frequency currents caused by MOSFET switching.[^ti-slva959b-motor-driver-layout]

**Common mistakes:**
- Assuming that a single large electrolytic capacitor replaces ceramic decoupling near the IC: a bulk capacitor handles low-frequency surges, while fast edges require a short connection to ceramic capacitors.[^ti-slva959b-motor-driver-layout]
- Routing motor power along the same trace as logic signals: common impedance couples interference into sensitive inputs.[^ti-slva959b-motor-driver-layout]
- Placing a capacitor on a long jumper wire or through a via: it becomes ineffective at high frequencies.[^ti-slva959b-motor-driver-layout]
