---
id: emb-elee-0222
title: "Is one flyback diode enough for a bidirectional H-bridge, and does it remove all motor noise?"
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
  - source_id: ti-slva321a
    title: "Texas Instruments SLVA321A: Current Recirculation and Decay Modes"
    url: https://www.ti.com/lit/an/slva321a/slva321a.pdf
  - source_id: ti-slvae59a
    title: "Texas Instruments SLVAE59A: Using Motor Drivers to Drive Solenoids"
    url: https://www.ti.com/lit/an/slvae59a/slvae59a.pdf
---

## Short answer

No. An H-bridge requires a recirculation path across every switch: either antiparallel freewheeling diodes across all four switches or active synchronous rectification.[^ti-slva321a] Flyback diodes only provide a low-impedance clamp path for inductive flyback, protecting switches from overvoltage spikes.[^ti-slvae59a] They do not eliminate high-frequency electromagnetic noise caused by mechanical brush arcing.

## Detailed explanation

TODO
