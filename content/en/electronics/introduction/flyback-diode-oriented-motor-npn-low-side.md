---
id: emb-elintro-0232
title: "How should a flyback diode be oriented on a motor with an NPN low-side switch?"
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
  - source_id: ti-inductive-load-clamping
    title: "TI: Switching Inductive Loads with DRV89xx-Q1 Devices"
    url: https://www.ti.com/document-viewer/lit/html/slvaf04
---

## Short answer

In a typical circuit with an NPN low-side switch, the flyback diode cathode connects to the positive supply rail of the coil, and the anode connects to the node between the coil and collector. In this configuration, the diode is reverse-biased while the motor is powered and conducts after the switch turns off, when the coil reverses polarity to maintain current flow.[^ti-inductive-load-clamping]

## Detailed explanation

TODO
