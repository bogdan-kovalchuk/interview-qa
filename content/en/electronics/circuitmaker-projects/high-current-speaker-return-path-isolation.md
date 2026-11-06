---
id: emb-elcmproj-0049
title: "Why is the high-current speaker return path isolated from the 555 oscillator ground return?"
track: electronics
section: circuitmaker-projects
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), картки курсу"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: circuitmaker-docs
    title: "CircuitMaker documentation"
    url: https://www.altium.com/documentation/altium-circuitmaker
  - source_id: ti-lm555-datasheet
    title: "Texas Instruments: LM555 Timer Datasheet"
    url: https://www.ti.com/lit/ds/symlink/lm555.pdf
  - source_id: ott-emc-engineering
    title: "Henry W. Ott: Electromagnetic Compatibility Engineering"
    url: https://www.wiley.com/en-us/Electromagnetic+Compatibility+Engineering-p-9780470189306
---

## Short answer

Heavy pulsed currents drawn by the speaker load produce transient voltage drops across the finite resistance of ground traces. If this current flows through the shared ground track of the 555 timer, unwanted ground bounce creates parasitic feedback. This causes frequency modulation, audio distortion, and low-frequency motorboating oscillation.[^udemy-electronics-course][^ti-lm555-datasheet]

## Detailed explanation

TODO
