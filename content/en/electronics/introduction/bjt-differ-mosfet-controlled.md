---
id: emb-elintro-0008
title: How does a `BJT` differ from a `MOSFET` in how it is controlled?
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
  - source_id: ti-gate
    title: "TI SLUA618A: Fundamentals of MOSFET and IGBT gate driver circuits"
    url: https://www.ti.com/lit/ug/slua618a/slua618a.pdf
---

## Short answer

A BJT normally needs base current to control collector current; a MOSFET is controlled by gate-to-source voltage. A MOSFET gate draws very little steady-state current, but switching requires charging and discharging its capacitances. Lower overall power loss is application-dependent, not guaranteed by voltage control alone. [^ti-gate] [^aac-semiconductors]

## Detailed explanation

“Current controlled” is a practical introductory description of BJT drive: the driver supplies base current. It is not a complete transistor equation, and current gain is not a constant valid for every operating point, especially saturation. For a MOSFET, the relevant control voltage is gate relative to source, not gate relative to an arbitrary ground. [^aac-semiconductors]

The insulated gate needs little DC current once its voltage is established. At each switching transition, however, the driver must move gate charge. TI gives average gate-drive current approximately `I = Q_G*f` and gate-drive power approximately `P = V_drive*Q_G*f`. Gate charge depends on the stated operating conditions. [^ti-gate]

For an illustrative assumed `Q_G = 20 nC`, `f = 100 kHz` and 10 V drive, these relations give 2 mA average supply current and 20 mW gate-drive power. Peak transition current can be much higher. Total efficiency additionally depends on conduction loss, transition duration, load and driver design; compare complete operating conditions rather than the control label alone.
