---
id: emb-elintro-0258
title: "What is gate charge and why does it matter for fast switching?"
track: electronics
section: introduction
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-direct-current
    title: "All About Circuits textbook, Volume I: DC"
    url: https://www.allaboutcircuits.com/textbook/direct-current/
  - source_id: infineon-gate-drive
    title: "Infineon: Gate drive for power MOSFETs in switching applications"
    url: https://www.infineon.com/assets/row/public/documents/24/42/infineon-gate-drive-for-power-mosfets-in-switchtin-applications-applicationnotes-en.pdf?fileId=8ac78c8c80027ecd0180467c871b3622
  - source_id: ti-mosfet-selection
    title: "Texas Instruments: MOSFET Selection Guide for BQ2575x Family"
    url: https://www.ti.com/lit/an/sluaax9/sluaax9.pdf
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
---

## Short answer

`Q_g` is the charge required to transition the gate state under specified test conditions; it dictates required gate driver current and transition times without solely determining them.[^infineon-gate-drive] For a given driver current, larger gate charge extends switching time, while dynamic switching losses also depend on bus voltage, switched current, and operating frequency.[^ti-mosfet-selection]

## Detailed explanation

Gate charge `Q_g` is the amount of charge that the driver must deliver to the gate when switching a MOSFET. The gate is insulated but possesses gate-source and gate-drain capacitances, so switching requires short current pulses to charge and discharge them. Datasheets specify `Q_g` alongside test conditions because the value depends on drain voltage, drain current, and final gate drive voltage.[^infineon-gate-drive]

While the gate charges, `V_GS` rises, and upon reaching the Miller plateau, a significant portion of the drive current goes into changing the drain voltage via the gate-drain capacitance. This interval dictates edge speed, electromagnetic interference (EMI), and switching losses. A higher `Q_g` for the same available gate current generally implies slower switching; a higher switching frequency also increases the average driver current. A rough estimate of the driver power consumption is given by `P_gate ≈ Q_g*V_drive*f_sw`, but this does not equal the total MOSFET losses.[^infineon-gate-drive] [^ti-mosfet-selection]

When selecting a part, do not minimize `Q_g` in isolation. A MOSFET with lower `R_DS(on)` may have a larger die area and higher gate charge, and the optimal trade-off depends on frequency, load, and whether conduction or switching losses dominate. `Q_GD` is also critical because it relates to traversing the Miller plateau, as is the driver's source and sink current capability. Compare candidates under identical test conditions rather than relying solely on a single headline number from the datasheet.[^ti-mosfet-selection]

**Common mistakes:**

- Treating `Q_g` as a constant capacitance: charge depends on voltage trajectories and test conditions.
- Assuming high `Q_g` is the sole cause of slow switching: driver current limits and gate resistance are also critical.
- Conflating the driver power loss estimate with total transistor switching losses.
