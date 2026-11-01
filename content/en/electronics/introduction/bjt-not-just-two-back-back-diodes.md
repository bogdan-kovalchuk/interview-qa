---
id: emb-elintro-0205
title: "Why can’t a `BJT` be replaced by two back-to-back diodes?"
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
  - source_id: aac-bjt-junctions
    title: "Bipolar Junction Transistors, All About Circuits"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/chpt-4/bipolar-junction-transistors/
---
## Short answer

In a BJT, the emitter, thin base, and collector form a shared semiconductor structure, so carriers injected by the emitter into the base can pass through it to the collector. Two discrete diodes lack such a thin shared base and junction interaction, which is why they do not reproduce the control of collector current by base current.[^aac-bjt-junctions]

## Detailed explanation

A `BJT` is not equivalent to two discrete diodes because its three regions are parts of a single semiconductor structure with a shared thin base. In an NPN transistor, the emitter is heavily doped and injects electrons into the base; the base is thin enough that most of these electrons do not recombine with holes, but diffuse to the collector junction. The electric field of this junction sweeps the carriers into the collector.[^aac-bjt-junctions]

A small fraction of carriers recombines in the base, forming the base current. Because most carriers reach the collector, this small current can control a much larger collector current. The thin base alone is not a sufficient explanation: doping concentrations and junction bias polarities are also critical. In a real transistor, the current distribution depends on the physical construction and operating point.[^aac-bjt-junctions]

Two discrete diodes are connected only by external leads, not by a shared semiconductor region. Their carriers do not transit a single thin base under the influence of the collector junction field, so the circuit does not exhibit transistor action. Even though a multimeter shows two p-n junctions between the terminals of a BJT, that is merely a basic junction check and does not mean the device can be replaced with a pair of diodes.[^aac-bjt-junctions]

**Example:** in the forward-active mode of an NPN transistor, the base–emitter junction injects electrons and the reverse-biased base–collector junction collects them. In contrast, when considering two standalone diodes, each operates as an independent junction and no such carrier transfer occurs between emitter and collector.[^aac-bjt-junctions]

**Common mistake:** imagining a BJT as two diodes that merely happen to share a common terminal. To explain amplification, you must account for the shared thin base, the small recombination fraction, and carrier collection at the collector.
