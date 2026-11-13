---
id: emb-elee-0036
title: "What fraction of the source energy is dissipated in the resistor when a capacitor charges through R from a constant voltage?"
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
  - source_id: openstax-rc-circuits
    title: "OpenStax University Physics Volume 2: 10.5 RC Circuits"
    url: https://openstax.org/books/university-physics-volume-2/pages/10-5-rc-circuits
  - source_id: openstax-capacitor-energy
    title: "OpenStax University Physics Volume 2: 8.3 Energy Stored in a Capacitor"
    url: https://openstax.org/books/university-physics-volume-2/pages/8-3-energy-stored-in-a-capacitor
---

## Short answer

When an initially discharged capacitor is charged from an ideal constant-voltage source `V_0` through a resistor, half the energy delivered by the source is stored in the capacitor and half is dissipated in the resistor. The final capacitor energy equals `E_C = C*V_0^2/2`; this result is independent of `R` once charging is complete.[^openstax-rc-circuits]

## Detailed explanation

For this result, it is important to clearly define what energy is being compared: the source delivers a total of `E_source = C*V_0^2`, not `C*V_0^2/2`. Half of this energy remains stored in the electric field of the capacitor, while the other half is converted to heat in the resistor during the transient.[^openstax-rc-circuits]

Suppose the capacitor is initially uncharged, an ideal source maintains a constant voltage `V_0`, and a resistor `R` is placed in series between them. Once charging is complete, the stored charge is `Q = C*V_0`. The work performed by the source equals its constant voltage multiplied by the total transferred charge: `E_source = V_0*Q = C*V_0^2`.[^openstax-rc-circuits]

The energy stored in the capacitor is calculated as `E_C = C*V_0^2/2`.[^openstax-capacitor-energy] The difference between the energy supplied by the source and the final energy stored in the capacitor represents the dissipation in the resistor: `E_R = E_source - E_C = C*V_0^2/2`. Thus, the fraction of dissipated energy relative to the total source energy is `E_R/E_source = 1/2`.[^openstax-rc-circuits]

**Calculation example:** for `C = 100 µF` and `V_0 = 10 V`, the source delivers `E_source = 0.0001*10^2 = 0.01 J`; the capacitor stores `0.005 J`, and the resistor dissipates `0.005 J`. The value of `R` determines the charging time `τ = R*C`, but does not affect this energy partition, provided the process is integrated to steady state.[^openstax-rc-circuits]

In a real circuit, part of the energy may be lost in the source internal resistance, wiring, and other parasitic elements, and source impedance also affects where the heat is dissipated. Therefore, the phrase "half is dissipated in the resistor" strictly describes an ideal circuit with a single series resistor and a constant-voltage source, rather than every practical charging arrangement.[^openstax-rc-circuits]

**Common mistake:** referring to `C*V_0^2/2` as the energy supplied by the source. That is the final energy stored in the capacitor; the source delivers twice as much in this idealized circuit.
