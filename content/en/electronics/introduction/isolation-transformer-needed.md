---
id: emb-elintro-0151
title: "Why is a 1:1 isolation transformer needed?"
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
  - source_id: aac-isolation-transformer
    title: "All About Circuits: Transformer Isolation"
    url: https://www.allaboutcircuits.com/technical-articles/transformer-isolation/
---

## Short answer

An isolation transformer with separate windings transfers energy via magnetic coupling without creating a direct conductive connection between the primary and secondary circuits. This helps break undesirable current paths through common grounding and reduce the risk of certain measurement short circuits. Isolation by itself does not make the secondary circuit safe: touching both of its conductors can complete a hazardous current path through the body.[^aac-isolation-transformer]

## Detailed explanation

An isolation transformer transfers AC energy between separate electrical circuits via magnetic flux, maintaining galvanic isolation between the windings. In a conventional transformer, the primary and secondary windings share a common core but do not share a common conductor; therefore, there is no direct path for direct current between the circuits. A 1:1 transformer has approximately equal turn counts, so its secondary voltage is close to the primary, yet this implies neither regulation nor guaranteed exact voltage equality.[^aac-isolation-transformer]

Such separation is useful on test benches: an oscilloscope's ground lead can connect a point of the circuit under test to protective earth. If this creates an undesirable path around an element, a short circuit occurs or the measurement ceases to reflect the circuit. Isolation can eliminate this specific path and break a ground loop, but the effect depends on how all instruments are grounded and whether other connections exist between the circuits.[^aac-isolation-transformer]

An important limitation: the secondary side remains a voltage source. Touching both of its terminals can complete a current path through the body, while capacitance between windings and insulation defects also affect safety. An autotransformer has a shared winding for input and output, so it does not provide galvanic isolation. Equipment is selected by rated voltage, power rating, and intended application, and safety procedures remain mandatory.[^aac-isolation-transformer]

Example: during diagnostics of a mains power supply, the mere fact of using a 1:1 transformer does not permit touching the secondary circuit or arbitrarily clipping a grounded probe. First determine the grounding points of the instruments and use suitable differential or isolated measurement tools.[^aac-isolation-transformer]

**Common mistakes:**
- treating isolation as a guarantee against electric shock;
- assuming that a 1:1 transformer stabilizes voltage;
- confusing a transformer with separate windings with an autotransformer.
