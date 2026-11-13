---
id: emb-elee-0151
title: "Which functional blocks make up a typical linear AC power supply?"
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
  - source_id: fiore-rectification
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 3.2 Rectification"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/03:_Diode_Applications/3.2:_Rectification
  - source_id: fiore-capacitors
    title: "Engineering LibreTexts: DC Electrical Circuit Analysis – A Practical Approach (Fiore), 8.2 Capacitance and Capacitors"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/DC_Electrical_Circuit_Analysis_-_A_Practical_Approach_(Fiore)/08:_Capacitors/8.2:_Capacitance_and_Capacitors
  - source_id: ti-slva118a
    title: "Texas Instruments SLVA118A: Linear Regulator Design Guide For LDOs"
    url: https://www.ti.com/lit/an/slva118/slva118.pdf
---

## Short answer

A step-down transformer reduces line AC voltage, a rectifier (diode bridge) converts it to unipolar pulsing DC, and a reservoir capacitor smoothes the ripple.[^fiore-rectification] A linear regulator at the final stage maintains a steady output voltage despite variations in line voltage and load current.[^ti-slva118a]

## Detailed explanation

A typical AC-line linear power supply is a chain of four stages, each addressing a specific task. The transformer scales the AC voltage according to its turns ratio: the secondary winding provides a lower AC voltage, while its physical size bounds the product of rated voltage and current, the VA rating.[^fiore-rectification] It is the transformer that steps mains voltage down to a level from which the required DC voltage can be derived.

The rectifier, most commonly a four-diode bridge, conducts current through the load in a single direction during both half-cycles: two diodes conduct during each half-cycle, producing a pulsating DC voltage whose peak is two diode forward drops below the secondary peak.[^fiore-rectification] This is not yet a steady DC voltage: between peaks, it collapses almost to zero. Thus, the next stage is a reservoir (filter) capacitor: it charges while the diodes conduct and supplies charge to the load between peaks. Higher load current increases ripple, whereas larger capacitance decreases it, though the diodes then conduct for shorter intervals with higher peak currents.[^fiore-rectification] For a bridge rectifier, assuming the capacitor supplies a nearly constant current between peaks, ripple is estimated as `ΔV_pp ≈ I/(f_ripple*C)`, where `f_ripple = 2*f_mains` because peaks occur in both half-cycles. The underlying relation `ΔV = I*Δt/C` derives from `i = C*dv/dt`.[^fiore-capacitors]

The final stage is the voltage regulator. A linear regulator employs a pass element controlled by feedback circuitry to maintain a constant output voltage despite fluctuations in input voltage and load current.[^ti-slva118a] The cost is heat: the difference `V_in - V_out` at a given current is dissipated inside the regulator, `P_D ≈ (V_in - V_out)*I_out`.[^ti-slva118a] Consequently, the regulator requires headroom: even the lowest ripple trough at its input must remain above `V_out` plus dropout. Without this stage, the power supply remains unregulated: its output shifts with line and load variations.

**Example (illustrative, neglecting secondary winding sag).** Secondary winding 12 V RMS, bridge with a 0.7 V drop per diode, 50 Hz mains, 100 mA current, 1000 µF capacitor. Secondary peak `12*√2 ≈ 17.0 V`, after two diodes `17.0 - 1.4 ≈ 15.6 V`. Ripple `ΔV_pp ≈ 0.1/(100*0.001) = 1.0 V`, so regulator input fluctuates between ≈ 14.6 V and ≈ 15.6 V, averaging ≈ 15.1 V. For a 5 V output, dissipation is `P_D ≈ (15.1 - 5)*0.1 ≈ 1.0 W`, and stage efficiency is ≈ `5/15.1 ≈ 33%`.[^ti-slva118a] If mains voltage sags by 10% (12 V becomes 10.8 V RMS), the peak drops to `10.8*√2 - 1.4 ≈ 13.9 V`, the trough drops to ≈ 12.9 V, and 5 V regulation is preserved, whereas without a regulator the output would drop by roughly 11%.

**Common mistakes:**

- Treating a filter capacitor as a regulator: it smoothes ripple, but output level still varies with mains line and load.
- Forgetting voltage headroom: at the lowest ripple trough, the regulator input must still exceed the output by the dropout voltage.
- Overlooking heating: a linear regulator dissipates `(V_in - V_out)*I_out`, so a large input voltage at substantial current requires heat sinking.
