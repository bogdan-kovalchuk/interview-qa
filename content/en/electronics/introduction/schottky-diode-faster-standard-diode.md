---
id: emb-elintro-0165
title: "Why is a Schottky diode faster than a standard Si diode?"
track: electronics
section: introduction
sources:
  - source_id: st-an4789
    title: "STMicroelectronics AN4789: Monolithic Schottky diode in ST F7 LV MOSFET technology"
    url: https://www.st.com/resource/en/application_note/an4789-monolithic-schottky-diode-in-st-f7-lv-mosfet-technology-improving-application-performance-stmicroelectronics.pdf
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

In a standard P-N diode, minority carriers accumulate during forward conduction and must be removed when transitioning to reverse blocking; this causes reverse recovery. A Schottky diode has a metal-semiconductor barrier and primarily majority-carrier conduction, so the accumulated charge and reverse recovery are usually smaller, and switching is faster. Actual losses and transients still depend on the component and circuit.[^st-an4789]

## Detailed explanation

A Schottky diode forms a barrier at a metal-semiconductor contact, whereas a standard silicon diode typically has a P-N junction. This difference is important during turn-off: in a P-N diode under forward conduction, minority carriers are injected and part of the charge is stored in the junction. When the voltage is quickly changed to reverse, this charge must disappear before the diode fully blocks current; during this time, a reverse recovery current arises.[^st-an4789]

In a Schottky diode, current is predominantly carried by majority carriers, so the same accumulation of minority-carrier charge does not occur or is significantly smaller. Accordingly, when switching from forward to reverse mode, a Schottky diode usually has a lower `Q_rr` and stops forward current faster. That is why it is often chosen in rectifiers and converters where the diode switches at high frequency: a smaller recovery charge can reduce losses, current spikes, and switching noise.[^st-an4789]

The word "faster" refers primarily to reverse recovery, not to every possible transient process. Junction capacitance, stray inductance, applied voltage, temperature, and the construction of the specific component also affect waveforms. The datasheet may indicate capacitive current even when carrier recovery charge is small; therefore, complete switching does not mean the instantaneous absence of any current.[^st-an4789]

In the ST example, a standard 60 V MOSFET is compared with a device of the same class with an integrated Schottky: the table shows `Q_rr` of 100 nC and 90 nC respectively under the given conditions, and a forward drop of 600 mV and 250 mV. These are specific device results, not universal numbers for every Schottky; comparisons should be made under identical test conditions and with manufacturer data.[^st-an4789]

**Common mistakes:**
- Saying that reverse recovery in any Schottky is absolutely zero without checking the datasheet and parasitic capacitance.
- Assuming that speed automatically means the best choice: you should also compare maximum reverse voltage, leakage current, forward drop, and thermal limits.
- Confusing the mechanism of lower accumulated charge with the claim that the circuit will have no transient spikes.[^st-an4789]
