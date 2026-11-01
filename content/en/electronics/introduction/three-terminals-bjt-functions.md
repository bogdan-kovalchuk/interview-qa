---
id: emb-elintro-0197
title: "What are the three terminals of a `BJT` and their functions?"
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

A `BJT` has a base, an emitter, and a collector: the base controls conduction, the emitter injects carriers, and the collector collects most of the carriers that have passed through the thin base. For a given operating mode, the emitter and collector are not interchangeable, although some circuits can operate in the reverse active mode with degraded parameters.[^aac-semiconductors]

## Detailed explanation

A bipolar junction transistor has three electrical terminals: the base (B), the emitter (E), and the collector (C). In the standard active mode, the base–emitter junction is forward-biased, and the base–collector junction is reverse-biased. This creates the conditions for controlled carrier transport from the emitter through the base to the collector.[^aac-semiconductors]

The emitter is heavily doped and injects charge carriers into the thin base. A small fraction of them recombines in the base, forming the base current; the majority passes through the base and is collected by the collector. Therefore, a small base current can control a larger collector current. This description applies to the normal mode and current directions for the corresponding transistor type; in PNP, polarities are opposite relative to NPN.[^aac-semiconductors]

The terminal functions do not mean that they can be swapped during assembly. The emitter and collector have different designs and doping levels, so connecting them in reverse usually results in lower gain and does not match datasheet specifications. Package pinouts also do not have a universal arrangement: you should verify the pinout against the datasheet for that specific component.[^aac-semiconductors]

Example: in a typical NPN stage, the emitter is often connected to the lower potential, the base receives a signal through a bias circuit, and the collector is connected to the load and power supply. Varying the base–emitter voltage changes the base current, and therefore the collector current within the active mode.[^aac-semiconductors]

**Common mistakes:** calling the base the output of the controlled current; assuming the collector and emitter are symmetrical; transferring NPN current directions to PNP without reversing polarities.[^aac-semiconductors]
