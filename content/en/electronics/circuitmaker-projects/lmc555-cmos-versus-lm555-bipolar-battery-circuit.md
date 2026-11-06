---
id: emb-elcmproj-0011
title: "Why is the CMOS LMC555 chosen over the classic bipolar LM555 for battery-powered devices?"
track: electronics
section: circuitmaker-projects
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: circuitmaker-docs
    title: "CircuitMaker documentation"
    url: https://www.altium.com/documentation/altium-circuitmaker
  - source_id: ti-lmc555-datasheet
    title: "Texas Instruments: LMC555 CMOS Timer Datasheet"
    url: https://www.ti.com/lit/ds/symlink/lmc555.pdf
  - source_id: ti-lm555-datasheet
    title: "Texas Instruments: LM555 Timer Datasheet"
    url: https://www.ti.com/lit/ds/symlink/lm555.pdf
---

## Short answer

The CMOS LMC555 timer operates down to `1.5 V` and draws only a fraction of a milliampere of supply current. It also eliminates the large shoot-through current spikes that occur during output stage switching in bipolar 555 timers. This protects battery rails from high-frequency switching noise and dramatically extends battery life.[^udemy-electronics-course][^ti-lmc555-datasheet]

## Detailed explanation

TODO
