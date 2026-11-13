---
id: emb-elintro-0266
title: "What does the continuity function of a multimeter check?"
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
  - source_id: fluke-continuity-test
    title: "Fluke: A Guide to Continuity Testing with a Multimeter"
    url: https://www.fluke.com/en-us/learn/blog/digital-multimeters/how-to-test-for-continuity
---

## Short answer

The continuity function injects a small test current, evaluates resistance, and sounds an audible beeper when resistance is below a model-dependent threshold.[^fluke-continuity-test] Testing must be performed on de-energized circuits, and components often require isolation to prevent parallel circuit paths from giving false continuity readings.[^fluke-continuity-test]

## Detailed explanation

The continuity function tests whether a continuous conductive path with resistance below a model-specific threshold exists between the test probes. The multimeter injects a small test current, measures the resulting voltage response, and sounds an audible beeper when the detected resistance is sufficiently low; an audible tone does not mean the path resistance is exactly zero.[^fluke-continuity-test]

This allows rapid verification of fuses, closed switches, cables, and PCB traces for opens. The absence of a beeper tone indicates that the path is open or exceeds the continuity resistance threshold, but does not conclusively prove a component is defective: always verify probe contact quality and the selected meter range first.[^fluke-continuity-test]

The circuit must be fully de-energized and capacitors discharged before testing. External live voltage can damage the multimeter or invalidate readings. If a component remains soldered in place, parallel sneak paths through adjacent circuitry can trigger the beeper even when the component itself is open; therefore, isolating at least one lead is necessary for definitive results.[^fluke-continuity-test]

Example: to test a fuse, de-energize the circuit, touch the probes across its terminals, and correlate the audible beeper with the displayed resistance reading. A beeper tone along with a low resistance reading indicates an intact fuse; infinite resistance or `OL` indicates an open circuit. Do not infer the exact resistance value from the beeper tone alone – read the multimeter's numeric display.

**Common mistakes:**

- Assuming that every multimeter beeps at the same universal resistance threshold.
- Testing live energized circuits or neglecting stored capacitor charge.
- Diagnosing a component as shorted without isolating it from parallel circuit paths.
