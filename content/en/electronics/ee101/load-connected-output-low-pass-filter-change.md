---
id: emb-elee-0096
title: "What does a load connected to the output of an RC low-pass filter change?"
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
  - source_id: aac-low-pass-filters
    title: "All About Circuits: Low-pass Filters"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-8/low-pass-filters/
---

## Short answer

Assuming an ideal source, a load `R_L` connected in parallel with C changes both the passband gain and the cutoff frequency. For a resistive load, the effective resistance in the time constant becomes `R||R_L`, shifting the cutoff to `f_c = 1/(2π*C*(R||R_L))`. The standard formula `1/(2π*R*C)` applies only to an unloaded filter.[^aac-low-pass-filters]

## Detailed explanation

TODO
