---
id: emb-elintro-0246
title: "Why are the source and body commonly connected inside a MOSFET?"
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
  - source_id: infineon-power-mosfet-body-diode
    title: "Infineon: Designing with power MOSFETs – How to avoid common issues and failure modes"
    url: https://www.infineon.com/dgdl/Infineon-Designing_with_power_MOSFETs-ApplicationNotes-v01_02-EN.pdf?fileId=8ac78c8c7ddc01d7017e6c619a490f47
---

## Short answer

The body in a power MOSFET forms part of the semiconductor substrate, and tying it to the source prevents unwanted body effect variations in threshold voltage.[^infineon-power-mosfet-body-diode] This internal connection also allows the device to be packaged with only three external terminals.[^infineon-power-mosfet-body-diode]

## Detailed explanation

In a typical discrete power MOSFET, the body is the semiconductor region beneath the gate in which the controllable channel forms. If its potential remained independent of the source, the voltage difference `V_SB` would modulate the voltage required to form the channel. The manufacturer typically ties the body to the source inside the package, clamping this difference near zero and simplifying the device into three external terminals: gate, drain, and source.[^infineon-power-mosfet-body-diode]

This connection does not eliminate all internal p-n junctions. The junction between body and drain remains, creating an intrinsic body diode between drain and source. For a conventional N-channel MOSFET, this diode conducts current from source to drain when forward-biased; in the off-state, it blocks reverse current only within its rated specifications. Consequently, an off-state MOSFET is not an ideal bidirectional open switch.[^infineon-power-mosfet-body-diode]

This behavior is critical when determining circuit polarity and designing power topologies. For instance, in a half-bridge, the body diode of one switch can temporarily freewheel inductive current, and its reverse recovery affects losses during the subsequent switching transition. In packages with an external body pin or specialized integrated circuit layouts, this connection may differ, so always consult the schematic and datasheet of the specific part.[^infineon-power-mosfet-body-diode]

**Common mistake:** treating a MOSFET as a symmetrical switch and assuming that drain and source can be swapped interchangeably without consequence. Always verify the body diode orientation and trace the current path in both switch states.

Example: if a standard N-channel switch is off, but the source potential exceeds the drain potential enough to forward-bias the body diode, current can flow through the diode even without any gate control signal. This is a distinct conduction path from the channel, and its current and thermal impact must be verified against the datasheet.[^infineon-power-mosfet-body-diode]
