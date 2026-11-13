---
id: emb-elee-0184
title: "Why does a large electrolytic capacitor not always remove fast noise?"
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
  - source_id: ti-switching-regulator-fundamentals
    title: "Texas Instruments: Switching regulator fundamentals"
    url: https://www.ti.com/lit/an/snva559c/snva559c.pdf
  - source_id: fiore-ac-circuit-analysis
    title: "James M. Fiore: AC Electrical Circuit Analysis, A Practical Approach (sections 1.5 and 10.3)"
    url: https://www2.mvcc.edu/users/faculty/jfiore/Circuits2/ACElectricalCircuitAnalysis.pdf
---

## Short answer

At high frequencies, the effectiveness of an electrolytic capacitor is degraded by its equivalent series resistance (ESR), equivalent series inductance (ESL), and long lead or trace inductances.[^ti-switching-regulator-fundamentals] Local ceramic bypass capacitors placed close to the chip's power pins are therefore required to shunt high-frequency noise.[^ti-switching-regulator-fundamentals]

## Detailed explanation

A bulk electrolytic capacitor effectively filters low-frequency ripple, but at high frequencies it ceases to behave as an ideal capacitor. Parasitic equivalent series resistance (ESR), equivalent series inductance (ESL), and nominal capacitance C form a resonant tank circuit, where ESL strictly limits filtering effectiveness at high frequencies.[^ti-switching-regulator-fundamentals] Consequently, an electrolytic capacitor on its own cannot suppress fast transient noise, regardless of how large its capacitance is.

For large pulsed currents, TI recommends combining an aluminum electrolytic capacitor with film and ceramic capacitors.[^ti-switching-regulator-fundamentals] An illustrative calculation (values do not represent a specific physical component): at a frequency of 100 MHz, a parasitic inductance of 10 nH produces an inductive reactance of `2*pi*f*L ≈ 6.3 Ω`, whereas the capacitive reactance of 100 µF at that same frequency is only about `0.000016 Ω`. At this frequency, the electrolytic capacitor behaves predominantly as an inductor, and its capacitance contributes virtually nothing to high-frequency shunting.

For this reason, high frequencies must be shunted by low-inductance ceramic or film capacitors placed directly adjacent to the IC. All power pins of an IC should be bypassed to a clean, low-inductance ground.[^ti-switching-regulator-fundamentals] A long trace running to a bulk capacitor adds parasitic inductance, and rapid transient currents across it induce an `L*di/dt` voltage drop that a distant electrolytic capacitor cannot compensate.[^fiore-ac-circuit-analysis]

**Common mistakes:**

- Assuming that a bulk electrolytic capacitor at the board power entry eliminates the need for local bypass capacitors near the IC.
- Placing a ceramic capacitor far from the IC with a long trace to ground: trace inductance drastically reduces its filtering effectiveness.
- Deeming electrolytic capacitors obsolete: for handling large ripple currents they are recommended alongside film and ceramic capacitors, but cannot cover high frequencies alone.
