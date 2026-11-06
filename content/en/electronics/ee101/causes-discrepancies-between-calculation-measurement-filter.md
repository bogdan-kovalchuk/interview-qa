---
id: emb-elee-0126
title: "What causes discrepancies between the calculation and the measurement of an RL filter?"
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
  - source_id: vishay-inductors-primer
    title: "Vishay: Inductors 101 – Primer Instructional Guide"
    url: https://www.vishay.com/docs/49782/49782.pdf
  - source_id: vishay-ihlp-2525cz-l7
    title: "Vishay Dale: IHLP-2525CZ-L7 inductors datasheet"
    url: https://www.vishay.com/docs/34254/ihlp-2525cz-l7.pdf
  - source_id: tektronix-abcs-probes
    title: "Tektronix: ABCs of Probes Primer"
    url: https://download.tek.com/document/02_ABCs-of-Probes-Primer.pdf
---

## Short answer

Winding resistance (DCR) and generator output resistance add to the series resistance, reducing low-frequency transmission in a low-pass filter and shifting `f_c`. Inductance tolerance also shifts `f_c` because `f_c` is inversely proportional to L; inductor datasheets often specify tolerances up to ± 20%.[^vishay-ihlp-2525cz-l7] Long leads and probe capacitance introduce parasitic elements causing additional poles or resonance;[^tektronix-abcs-probes] inter-turn coil capacitance produces self-resonance (SRF).[^vishay-inductors-primer]

## Detailed explanation

TODO
