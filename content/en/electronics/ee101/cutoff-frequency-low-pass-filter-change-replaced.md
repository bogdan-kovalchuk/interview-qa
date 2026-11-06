---
id: emb-elee-0106
title: "How does the cutoff frequency of an RC low-pass filter change if 100 nF is replaced with 1 µF at R = 1 kΩ?"
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
  - source_id: aac-rc-low-pass-cutoff
    title: "All About Circuits: Introduction to Analog Filters"
    url: https://www.allaboutcircuits.com/TEXTBOOK/designing-analog-chips/filters/introduction-to-analog-filters/
---

## Short answer

For an unchanged effective R, the cutoff frequency drops tenfold, from approximately 1.59 kHz to 159 Hz, because `f_c = 1/(2*pi*R*C)`.[^aac-rc-low-pass-cutoff] This represents an ideal calculation without additional loading.

## Detailed explanation

TODO
