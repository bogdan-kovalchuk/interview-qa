---
id: emb-elintro-0259
title: "When can a MOSFET's body diode be a problem in a switching circuit?"
track: electronics
section: introduction
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-direct-current
    title: "All About Circuits textbook, Volume I: DC"
    url: https://www.allaboutcircuits.com/textbook/direct-current/
  - source_id: infineon-mosfet-layout
    title: "Infineon: Designing with power MOSFETs"
    url: https://www.infineon.com/assets/row/public/documents/24/42/infineon-designing-with-power-mosfets-applicationnotes-en.pdf?fileId=8ac78c8c7ddc01d7017e6c619a490f47
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
---

## Short answer

A power MOSFET contains an intrinsic body diode that conducts when forward-biased even if the gate channel is turned off.[^infineon-mosfet-layout] In bridge topologies, dead time and reverse recovery behavior are critical, and in reverse-polarity protection a single MOSFET cannot block current in both directions.[^infineon-mosfet-layout]

## Detailed explanation

The body diode is an intrinsic PN junction between the body and drain in a conventional power MOSFET; the body is typically internally connected to the source. Therefore, even with the gate turned off, the diode still forms a directional conduction path whenever its anode and cathode are forward-biased. In an N-channel MOSFET, the typical body diode conduction path is directed from source to drain, but always verify the schematic symbol and pinout polarity of the specific component.[^infineon-mosfet-layout]

In a half-bridge, inductive load current cannot drop to zero instantaneously. During dead time, this current can commutate into the body diode of either the low-side or high-side switch. When the opposing MOSFET turns on, the conducting diode must cease conduction; the accumulated stored charge creates reverse-recovery current, additional power losses, and voltage/current spikes. The severity depends on current, switching speed, dead time, and the diode's `Q_rr` and `t_rr` parameters, which is why real-world designs examine switching waveforms alongside datasheet limits.[^infineon-mosfet-layout]

Another scenario is a single-switch protection circuit or high-side power switch. When the MOSFET is turned off, the body diode can leave a conduction path in an unwanted direction, such as from the load back into the power source. If bidirectional current blocking is required, an appropriate topology must be used, often employing two MOSFETs with back-to-back oriented body diodes; the specific implementation depends on operating voltages, gate drive control, and the expected operating modes.[^infineon-mosfet-layout]

**Common mistakes:**

- Assuming that `V_GS = 0` provides complete electrical isolation between drain and source in both directions.
- Overlooking brief body diode conduction during dead time and subsequent reverse recovery during commutation.
- Treating the body diode as a free ideal diode: always verify forward voltage drop, rated current, and recovery characteristics.
