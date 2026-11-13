---
id: emb-elintro-0251
title: "Which MOSFET parameters should you check first in a datasheet?"
track: electronics
section: introduction
sources:
  - source_id: ti-mosfet-selection
    title: "Texas Instruments: Avoid Common Mistakes When Selecting and Designing with Power MOSFETs"
    url: https://www.ti.com/lit/an/slpa021/slpa021.pdf
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

**Start with voltage and current limits.** Check `V_DS`, rated `I_D`, `R_DS(on)` specifically at your available `V_GS`, package thermal limits, and the absolute maximum `V_GS`. `V_GS(th)` indicates only the onset of slight conduction rather than guaranteed full enhancement; for fast switching, also check `Q_g`.[^ti-mosfet-selection]

## Detailed explanation

MOSFET datasheet parameters must be evaluated in the context of the specific circuit: first voltage ratings, current, and required drive conditions, followed by losses and thermal dissipation. `V_DS` must withstand the highest voltage that can appear between drain and source, including voltage transients. Rated `I_D` is not a standalone promise of current capability: allowable current depends on case temperature, cooling, pulse width, and package bond-wire limitations.

For switching operation, the critical parameter is `R_DS(on)` at the actual `V_GS` delivered by your GPIO or gate driver. Do not select a device based on `V_GS(th)`: this threshold is measured at a tiny current where the transistor merely begins to conduct. For example, the TI datasheet for the CSD18541F5 specifies `R_DS(on)` separately at `V_GS = 4.5 V` and `10 V`; if your drive circuitry supplies a lower voltage, the published resistance limit may not apply.[^ti-mosfet-selection]

Next, estimate conduction losses using `P = I²*R_DS(on)` and verify thermal resistance, maximum permissible junction temperature, and the actual heat dissipation path. In absolute maximum ratings tables, drain currents are typically distinguished by differing cooling conditions; a headline maximum `I_D` never substitutes for a thermal calculation.[^ti-mosfet-selection]

`Q_g` helps determine whether the controller can charge and discharge the gate at the required speed; higher gate charge can demand a more powerful driver and increase switching losses. Also check the absolute maximum `V_GS` rating, resistance increase over temperature, the safe operating area, and body diode parameters if relevant to your topology. Values in curves and tables are meaningful only when evaluated alongside their specific test conditions.[^ti-mosfet-selection]
