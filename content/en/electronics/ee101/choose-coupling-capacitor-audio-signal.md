---
id: emb-elee-0022
title: "How do you choose a coupling capacitor for an audio signal (20 Hz–20 kHz) with R = 10 kΩ?"
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
  - source_id: aac-capacitor-highpass
    title: "All About Circuits: High-pass Filters"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-8/high-pass-filters/
---

## Short answer

For a targeted attenuation limit, choose an RC high-pass cutoff frequency safely below 20 Hz and calculate `C = 1/(2*π*R*f_c)`. Assuming `R = 10 kΩ` and `f_c = 2 Hz`, this yields `C ≈ 8.0 µF`; a standard 8.2 µF value provides a close match.[^aac-capacitor-highpass]

## Detailed explanation

TODO
