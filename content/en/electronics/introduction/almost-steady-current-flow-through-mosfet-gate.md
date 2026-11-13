---
id: emb-elintro-0237
title: "Why does almost no steady current flow through a MOSFET gate?"
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
---

## Short answer

A MOSFET gate is isolated from the channel by an insulating dielectric layer, forming a capacitive structure. In steady state, only a tiny leakage current flows, while noticeable current is drawn primarily when charging or discharging gate capacitance during transitions.[^aac-semiconductors]

## Detailed explanation

The MOSFET gate is separated from the semiconductor channel by an insulating layer, so to a first approximation it can be modeled as one plate of a capacitor, with the channel and substrate acting as the other plate. A steady voltage creates an electric field that alters the number of charge carriers near the semiconductor surface and controls channel conductivity. For an ideal capacitor, once the voltage is established, no steady current is required.[^aac-semiconductors]

A real MOSFET is not ideal: the datasheet specifies gate leakage as well as capacitances and gate charge. During turn-on, the driver supplies charge to raise the gate voltage; during turn-off, it removes this charge. Consequently, the current is transient, and its magnitude depends on edge rate, driver impedance, and the transistor's nonlinear capacitances.[^aac-semiconductors]

For example, when driving the gate slowly and waiting for steady state, a GPIO output delivers no significant DC current into the gate. However, rapid switching repeats this charging process many times, so the average driver current increases proportionally with switching frequency and required charge. This also explains why a power MOSFET may require a dedicated gate driver.[^aac-semiconductors]

**Common mistakes:**
- Claiming that the gate consumes no current at all: leakage and transient currents do exist.
- Confusing the absence of steady DC current with zero power consumption during switching.
- Assuming the gate behaves as an ideal capacitor across all voltages and frequencies.
