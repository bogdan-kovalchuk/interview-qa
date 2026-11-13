---
id: emb-elintro-0250
title: "Why must a MOSFET not be chosen by `V_th` alone?"
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
  - source_id: onsemi-fds2582-datasheet
    title: "onsemi: FDS2582 N-Channel MOSFET datasheet"
    url: https://www.onsemi.com/download/data-sheet/pdf/fds2582-d.pdf
---

## Short answer

`V_th` is specified at a tiny test current, so it does not guarantee a low `R_DS(on)`.[^onsemi-fds2582-datasheet] For switching applications, verify `R_DS(on)` at the actual available `V_GS` in the datasheet.[^onsemi-fds2582-datasheet]

## Detailed explanation

The gate-to-source threshold voltage `V_th` (designated `V_GS(th)` in many datasheets) defines the condition under which the channel only begins to conduct a specified tiny test current. It is neither the voltage for full enhancement nor a guarantee that the MOSFET will pass rated current with low conduction losses. The exact definition and test current are specified in the datasheet; the value varies with unit tolerance and temperature.[^onsemi-fds2582-datasheet]

For switching operation, the critical parameter is `R_DS(on)` at the actual available `V_GS`. Conduction losses approximately equal `P = I_D²*R_DS(on)` when the MOSFET operates as a low-resistance switch; if the gate receives insufficient voltage, the transistor may remain in the `saturation` region (not fully enhanced as a switch), where both current and `V_DS` are simultaneously significant, causing substantial heating. In datasheet tables, these two parameters are often measured under vastly different conditions, so the threshold voltage cannot be substituted for drive voltage.[^onsemi-fds2582-datasheet]

For example, in the FDS2582 datasheet, the threshold is measured at `I_D = 250 µA`, whereas `R_DS(on)` is specified at `V_GS = 10 V` and several amperes of current. This is a specific example rather than a universal test across all transistors; it demonstrates why a single `V_GS(th)` number is insufficient for component selection. If a microcontroller outputs only 3.3 V, look for a guaranteed `R_DS(on)` row at that voltage or choose a different device.[^onsemi-fds2582-datasheet]

**Common mistake:** seeing `V_th = 2 V` and concluding that the switch is guaranteed to turn on fully from 3.3 V. Always verify `V_GS(th)` limits, `R_DS(on)` test conditions, drain current, temperature, and package thermal resistance before estimating losses.[^onsemi-fds2582-datasheet]

Verification example: if a load draws `2 A` and the table guarantees `R_DS(on) = 0.1 Ω` at your specific drive voltage, an idealized estimate of channel conduction loss is `P = 2²*0.1 = 0.4 W`. If no such row exists for your available gate voltage, the datasheet does not support that calculation for this drive level.
