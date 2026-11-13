---
id: emb-elee-0090
title: "Which safety rules follow from the demonstration of an RC circuit on mains voltage?"
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
  - source_id: osha-basic-electricity-safety
    title: "OSHA: Basic Electricity Safety"
    url: https://www.osha.gov/sites/default/files/2019-04/Basic_Electricity_Materials.pdf
---

## Short answer

Mains circuits are lethal, so use a simulator or a safe isolated low-voltage source for exercises. Never touch an energized circuit; de-energize and verify zero voltage with an instrument before touching. Never float the oscilloscope ground: an autotransformer does not provide galvanic isolation, and an isolation transformer does not eliminate shock hazards between its secondary terminals. Measure component temperatures with instruments, never with fingers.[^osha-basic-electricity-safety]

## Detailed explanation

Demonstrating an RC circuit connected to the mains is not a safe setup for self-replication: mains conductors can establish dangerous voltages between a person and earth ground or between two contact points. Electric current passing through the body can cause burns, cardiac arrest, or death; the risk depends not only on the voltage, but also on the current path and duration.[^osha-basic-electricity-safety]

To study frequency response, a simulator or a low-voltage source with proper isolation is sufficient. Do not connect a standard bench generator or oscilloscope to a circuit where nodes sit at mains potential. The ground clip of a standard oscilloscope is typically connected to protective earth (PE); attaching it to a 'hot' (live) node can cause a short circuit. The protective ground wire must never be disconnected to bypass this issue. An autotransformer adjusts the voltage level, but provides no galvanic isolation from the mains. Even an isolation transformer does not make touching components safe: simultaneous contact with both output conductors still completes a circuit through the body.[^osha-basic-electricity-safety]

After disconnecting the power source, residual charge can remain in the capacitor. Verify the absence of voltage with an appropriate meter and discharge capacitors only using the method designated for the circuit; never treat an open power switch as definitive proof that the circuit is de-energized.[^osha-basic-electricity-safety]

**Common mistakes:**
- Replicating the demonstration on a breadboard under the assumption that a small current through the resistor guarantees safety.
- Disconnecting the oscilloscope's protective earth ground or assuming an autotransformer provides galvanic isolation.
- Touching components to judge temperature or residual charge.

To avoid these mistakes, never replicate mains experiments without proper qualifications, protective equipment, and formal safety procedures. Use low voltage or simulation for educational purposes; any mains-level work must be performed by a qualified professional following applicable electrical safety codes.[^osha-basic-electricity-safety]
