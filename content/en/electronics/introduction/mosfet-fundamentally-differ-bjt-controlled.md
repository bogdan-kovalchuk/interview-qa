---
id: emb-elintro-0236
title: "How does a MOSFET fundamentally differ from a BJT in how it is controlled?"
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
---

## Short answer

A BJT uses base current to control collector current. A MOSFET is controlled by voltage between gate and source; its insulated gate draws only a small leakage current in steady state, but requires current to charge or discharge capacitance during switching.[^aac-semiconductors]

## Detailed explanation

A MOSFET is controlled by an electric field created by voltage applied between gate and source, whereas in the conventional BJT model, base current controls collector current. In a BJT, currents are coupled across semiconductor junctions, so in normal amplification or switching, the control circuit must continuously supply base current. The required value depends on the operating point and specific transistor.[^aac-semiconductors]

A MOSFET gate is isolated from the channel by an insulating dielectric layer and behaves essentially like a capacitor plate. When gate voltage is held constant, an ideal capacitance draws no DC current; a real device exhibits a minute leakage current bounded by datasheet ratings. During transitions between states, a transient current flows through the gate as the driver supplies or removes gate capacitance charge.[^aac-semiconductors]

Therefore, for slow or static control, a MOSFET places very little load on a logic output, but high-speed switching of a power transistor still requires accounting for gate charge and driver current capability. Comparing these device families solely by the slogans "current-controlled" versus "voltage-controlled" is insufficient: leakage, switching speed, voltage ratings, and losses are equally critical.[^aac-semiconductors]

Example: a conducting BJT requires continuous base current, whereas a MOSFET with a steady gate voltage draws virtually no DC drive current. However, on every signal edge the driver must charge or discharge the gate capacitance.

**Common mistakes:**
- Assuming that current never flows through a MOSFET gate.
- Assuming BJT base current is identical regardless of load and operating region.
- Ignoring gate charge, leakage currents, and maximum operating ratings of the specific component.
