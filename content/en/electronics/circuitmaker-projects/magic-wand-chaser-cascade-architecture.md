---
id: emb-elcmproj-0004
title: "How is the LED driver cascade constructed in a magic wand chaser circuit?"
track: electronics
section: circuitmaker-projects
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: ti-lm555
    title: "Texas Instruments LM555 Precision Timer Datasheet"
    url: https://www.ti.com/lit/ds/symlink/lm555.pdf
  - source_id: ti-sn74hc393
    title: "Texas Instruments SNx4HC393 Dual 4-Bit Binary Counters Datasheet"
    url: https://www.ti.com/lit/ds/symlink/sn74hc393.pdf
  - source_id: ti-sn74hc138
    title: "Texas Instruments SNx4HC138 3-Line to 8-Line Decoders / Demultiplexers Datasheet"
    url: https://www.ti.com/lit/ds/symlink/sn74hc138.pdf
---

## Short answer

A 555 astable timer generates clock pulses at several hertz to drive a 74HC393 binary counter. The upper three bits of the counter feed into a 74HC138 3-to-8 decoder, which sequentially activates one of eight output channels. The active-low output pulls current through the selected LED to ground, creating the chasing light effect.[^udemy-electronics-course]

## Detailed explanation

TODO
