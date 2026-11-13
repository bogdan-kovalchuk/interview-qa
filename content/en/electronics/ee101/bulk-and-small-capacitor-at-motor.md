---
id: emb-elee-0261
title: "Why place both a large reservoir capacitor and a 0.1 µF capacitor at a motor?"
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
  - source_id: ti-motor-driver-capacitors
    title: "Texas Instruments Application Report SLVA797: Capacitor Selection for Motor Drivers"
    url: https://www.ti.com/lit/an/slva797/slva797.pdf
  - source_id: murata-capacitor-characteristics
    title: "Murata Manufacturing: Basics of Capacitors – Impedance and ESR Characteristics"
    url: https://article.murata.com/en-us/article/impedance-esr-frequency-characteristics-in-capacitors
  - source_id: art-of-electronics
    title: "Horowitz P., Hill W. The Art of Electronics. 3rd ed. Cambridge University Press, 2015"
    url: https://artofelectronics.net/
---

## Short answer

A large reservoir capacitor (2200 µF in the lecture) delivers high motor starting currents, preventing rail sags and avoiding heavy transient currents across supply wiring from the regulator. A small 0.1 µF ceramic capacitor across the motor terminals shunts high-frequency brush noise right where it is generated. Together, they suppressed supply rail noise from several volts down to approximately ±50 mV.[^udemy-electronics-course]

## Detailed explanation

Paralleling a large-capacitance electrolytic capacitor with a small-capacitance ceramic capacitor (0.1 µF) directly at the motor terminals is dictated by fundamental differences in their frequency responses and the physical non-idealities of real passive components[^udemy-electronics-course][^murata-capacitor-characteristics].

### Non-ideality of real capacitors: parasitic inductance and resistance

A real capacitor is represented by an equivalent series circuit containing ideal capacitance `C`, equivalent series resistance (ESR), and equivalent series inductance (ESL)[^murata-capacitor-characteristics]. The total impedance of the capacitor is given by:
`Z = sqrt(ESR^2 + (2 * pi * f * ESL - 1 / (2 * pi * f * C))^2)`.

At the self-resonant frequency (SRF `f_0 = 1 / (2 * pi * sqrt(ESL * C))`), capacitive and inductive reactances cancel each other, and impedance reaches a minimum equal to the ESR. At frequencies above `f_0`, reactance becomes inductive (`Z ≈ 2 * pi * f * ESL`): its inductive reactance rises with frequency, so the shunt capacitor loses its ability to bypass high-frequency noise to ground[^murata-capacitor-characteristics].

### Role of the reservoir electrolytic capacitor (bulk capacitor)

1. **Source of local pulsed current:** During motor startup, sudden speed changes, or PWM duty cycle transitions, a substantial load current surge occurs, which the capacitor supplies as a discharge current (`I = C * (dV/dt)`) to limit bus voltage droop. A high-capacitance electrolytic capacitor (for example, 470–2200 µF) stores substantial electrical energy `E = (C * V^2) / 2` and delivers it directly into the load node[^ti-motor-driver-capacitors].
2. **Preventing voltage drops across supply wiring:** If the reservoir capacitor were omitted, this pulsed current would travel through the entire power line from a remote power supply or linear regulator. The parasitic inductance of PCB traces and connecting wires (roughly 1 nH/mm) would induce deep voltage sags on the shared rail.
3. **High-frequency limitations:** Aluminum electrolytic capacitors feature a rolled (wound) foil construction with large plate surface area, resulting in high internal inductance ESL (from several nanohenries to tens of nanohenries) and elevated ESR. Consequently, their self-resonant frequency SRF typically lies in the tens to several hundreds of kilohertz range. For high-frequency switching noise, the high inductive impedance above the SRF prevents such a bulk capacitor from providing a low-impedance shunt path to ground[^murata-capacitor-characteristics][^art-of-electronics].

### Role of the small ceramic capacitor (0.1 µF MLCC)

1. **High-frequency noise shunting:** Multilayer ceramic capacitors (MLCC) of X7R or NP0 dielectric with 0.1 µF (100 nF) capacitance have a monolithic, leadless construction with minimal parasitic inductance (ESL < 0.5 nH) and extremely low ESR (units or tens of milliohms). Their self-resonant frequency SRF reaches tens and hundreds of megahertz[^murata-capacitor-characteristics].
2. **Suppressing brush arcing:** Commutation on a motor's commutator generates steep voltage edges with nanosecond rise times `di/dt`, corresponding to frequency spectrum components in the tens and hundreds of megahertz. A ceramic capacitor mounted directly across the motor terminals (with the shortest leads possible) bypasses these high-frequency currents locally, preventing them from radiating through cables as an antenna or conducting into the power rail[^ti-motor-driver-capacitors][^art-of-electronics].

### Practical component combination

Comprehensive protection is achieved precisely by their parallel operation: the large electrolytic capacitor maintains average rail voltage in the low-frequency range (from rotation frequency and PWM up to hundreds of kilohertz), while the 0.1 µF ceramic suppresses the high-frequency spectrum of commutation sparks (from units to hundreds of megahertz)[^ti-motor-driver-capacitors]. Professional designs often use three ceramic capacitors: one directly across the motor terminals (differential filtering) and one from each terminal to the motor's metal chassis (common-mode filtering)[^art-of-electronics].
