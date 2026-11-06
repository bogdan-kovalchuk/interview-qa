---
id: emb-elee-0156
title: "Which regulator input voltage is compared with the dropout if the input has ripple?"
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
  - source_id: ti-slva079
    title: "Texas Instruments SLVA079: Understanding the Terms and Definitions of LDO Voltage Regulators"
    url: https://www.ti.com/lit/an/slva079/slva079.pdf
  - source_id: ti-tps752q1-datasheet
    title: "Texas Instruments TPS752-Q1 datasheet"
    url: https://www.ti.com/lit/ds/symlink/tps752-q1.pdf
---

## Short answer

The minimum instantaneous input voltage (the ripple trough) is compared against dropout rather than the average voltage: `V_in,min > V_out + V_dropout` is required. Dropout depends on load current and junction temperature, so worst-case maximum current numbers must be taken from the datasheet. If the ripple trough falls below this threshold, regulation ceases during troughs and input ripple passes straight to the output.[^ti-slva079][^ti-tps752q1-datasheet]

## Detailed explanation

TODO
