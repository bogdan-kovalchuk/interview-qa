---
id: emb-elee-0183
title: "What capacitance is needed so that a 100 mA, 1 ms load pulse causes a sag of no more than 0.1 V?"
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
  - source_id: fiore-ac-circuit-analysis
    title: "James M. Fiore: AC Electrical Circuit Analysis, A Practical Approach (sections 1.5 and 10.3)"
    url: https://www2.mvcc.edu/users/faculty/jfiore/Circuits2/ACElectricalCircuitAnalysis.pdf
  - source_id: ti-switching-regulator-fundamentals
    title: "Texas Instruments: Switching regulator fundamentals"
    url: https://www.ti.com/lit/an/snva559c/snva559c.pdf
---

## Short answer

Neglecting ESR, the capacitor equation `i = C*dv/dt` yields `C = I*t/V`, so 0.1 A × 1 ms / 0.1 V = 1000 µF.[^fiore-ac-circuit-analysis] If the capacitor has an ESR of 0.2 Ω, the instantaneous step `I*ESR = 20 mV` uses part of the allowable voltage margin, requiring at least 1250 µF.

## Detailed explanation

The calculation starts from the capacitor governing equation `i = C*dv/dt`: voltage changes at a rate of `i/C`.[^fiore-ac-circuit-analysis] If the load current I is constant throughout a pulse of duration t, the voltage drop is linear and equals `dV = I*t/C`, yielding `C = I*t/dV`. For 100 mA and 1 ms neglecting ESR: `C = 0.1 A * 0.001 s / 0.1 V = 0.001 F = 1000 µF`. This is a conservative estimate because it assumes the upstream power source supplies zero current during the transient pulse.

A practical capacitor exhibits equivalent series resistance (ESR) through which this same load current must pass.[^ti-switching-regulator-fundamentals] The initial voltage step `I*ESR` is independent of capacitance and develops immediately at the onset of the current pulse. For an ESR of 0.2 Ω, this step is `0.1 A * 0.2 Ω = 0.02 V = 20 mV`. The allowable 0.1 V margin is then split: 20 mV across the ESR and 80 mV across capacitive discharge, requiring `C = 0.1 A * 0.001 s / 0.08 V = 0.00125 F = 1250 µF`. Verification: capacitive sag is `0.1 * 0.001 / 0.00125 = 0.08 V`, plus 0.02 V across ESR, totaling 0.1 V.

Application constraints. ESR is strongly temperature dependent: for a typical aluminum electrolytic capacitor, ESR can increase by a factor of roughly 40 as temperature drops from 25 °C down to –40 °C.[^ti-switching-regulator-fundamentals] Therefore, at low temperatures the resistive step across ESR and overall voltage sag can be substantially larger than calculated at room temperature. Conversely, if a voltage regulator with adequate loop bandwidth supplies part of the pulse current during the transient, a smaller capacitance suffices; the formula represents a worst-case design margin.

**Common mistakes:**

- Neglecting ESR and assuming the entire voltage tolerance budget is available for capacitive discharge.
- Sizing ESR without considering temperature variation, even though cold temperatures can increase ESR manifold.
- Treating the formula as an exact prediction for all circuits: in practice, the upstream regulator and source may deliver current during the pulse, reducing required capacitance.
