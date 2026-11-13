---
id: emb-elee-0052
title: "Why does current lead voltage in a capacitor?"
track: electronics
section: ee101
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-alternating-current
    title: "All About Circuits textbook, Volume II: AC"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/
  - source_id: aac-ac-capacitor
    title: "All About Circuits: AC Capacitor Circuits"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-4/ac-capacitor-circuits/
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
---

## Short answer

For an ideal capacitor, `i = C*dv/dt`, meaning current is proportional to the rate of change of voltage. In sinusoidal steady state, current leads voltage by 90°; this is a phase shift rather than a universal sequence of events for an arbitrary signal.[^aac-ac-capacitor]

## Detailed explanation

The voltage across a capacitor is related to its stored charge, and current changes that charge. For an ideal capacitor, `i = C*dv/dt`: the faster the voltage changes, the larger the required current. Capacitance `C` is measured in farads; under constant voltage its derivative is zero, so an ideal capacitor does not conduct current in steady-state DC. A real component exhibits leakage and other non-idealities. [^aac-ac-capacitor]

When voltage varies, current charges or discharges the capacitor, altering the charge on its plates and the energy in its electric field. Consequently, instantaneous current is greatest where voltage changes most rapidly. This explains the relationship between current and voltage without resorting to the flawed analogy that current somehow "passes first" through the dielectric. [^aac-ac-capacitor]

In sinusoidal steady state, the derivative of voltage shifts current forward by 90°. When voltage reaches its peak, its instantaneous rate of change is zero, so the current of an ideal capacitor at that instant is zero. When voltage crosses zero and changes most rapidly, current reaches its maximum. [^aac-ac-capacitor]

**Example:** if the voltage varies as a sinusoid at a frequency of 1 kHz, the current of an ideal capacitor leads the voltage by a quarter period, which is 0.25 ms. This calculation describes sinusoidal steady state; for a transient process, the initial voltage and external circuit are also critical.

**Common mistakes:**

- Stating that a capacitor blocks all current. It blocks steady current after charging in an ideal model, but passes alternating current with a frequency-dependent reactance.
- Transferring the 90° phase shift to a complete RC circuit. Resistance alters the overall angle between voltage and current. [^aac-ac-capacitor]
