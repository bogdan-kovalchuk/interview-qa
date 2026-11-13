---
id: emb-elee-0018
title: "How does a capacitor behave in a DC and an AC circuit?"
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
  - source_id: aac-capacitor-transient
    title: "All About Circuits: Capacitor Transient Response"
    url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-16/capacitor-transient-response/
  - source_id: aac-capacitor-reactance
    title: "All About Circuits: AC Capacitor Circuits"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-4/ac-capacitor-circuits/
---

## Short answer

After transients settle in an ideal DC circuit, a capacitor maintains constant voltage and carries zero current, effectively behaving as an open circuit. During charging, current decays over time; in an AC circuit, continuous voltage changes cause cyclic charging and discharging, with ideal reactance decreasing as frequency rises.[^aac-capacitor-transient] [^aac-capacitor-reactance]

## Detailed explanation

A capacitor consists of two conductive plates separated by a dielectric and stores energy in an electric field. The current through its terminals is proportional to the rate of voltage change: when voltage changes, the stored charge changes, producing current in the external circuit. In a simple RC circuit with a DC voltage source, an initially uncharged capacitor charges through a resistor. The voltage across it gradually approaches the source voltage while current decays to zero; the process does not happen instantaneously.[^aac-capacitor-transient]

The rate of the transient response is determined by the time constant `τ = R*C`, where `R` is the charging resistance and `C` is capacitance. After one time constant, the capacitor voltage during charging reaches approximately 63% of the difference between its initial and final values. Therefore, the statement "a capacitor blocks DC" applies to the steady state of an ideal circuit, not the instant of connection. Physical capacitors exhibit leakage, ESR, and voltage limits, so current does not necessarily become strictly zero.[^aac-capacitor-transient]

Example: if `R = 10 kΩ` and `C = 100 µF`, then `τ = 1 s`. When connected to 5 V starting from zero charge, after one second the capacitor voltage reaches approximately 3.16 V, continuing toward 5 V; current through the resistor branch decays accordingly. This behavior accounts for timing delays, filtering, and smoothing of voltage variations in RC circuits.[^aac-capacitor-transient]

Under sinusoidal excitation, the capacitor continuously charges and discharges cyclically, resulting in an alternating current in the external circuit. In an ideal model, the magnitude of capacitive reactance `X_C = 1/(2π*f*C)` decreases as frequency or capacitance increases. While this is a useful approximation for AC analysis, parasitic inductance at high frequencies and leakage and dielectric losses at low frequencies can become significant; verify the usable frequency range in the component datasheet.[^aac-capacitor-reactance]

**Common mistake:** stating that a capacitor is always an open circuit to DC or that current literally flows through the insulating dielectric layer. Charging and discharging currents flow through the external conductors, but once steady state is reached, an ideal capacitor passes no DC; a physical capacitor has a small leakage current.[^aac-capacitor-transient]
