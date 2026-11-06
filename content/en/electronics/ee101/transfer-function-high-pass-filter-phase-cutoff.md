---
id: emb-elee-0109
title: "What is the transfer function of an RC high-pass filter and its phase at the cutoff frequency?"
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
  - source_id: aac-high-pass-transfer-function
    title: "All About Circuits: Understanding the First-Order High-Pass Filter Transfer Function"
    url: https://www.allaboutcircuits.com/technical-articles/understanding-the-first-order-high-pass-filter-transfer-function/
---

## Short answer

For an ideal RC high-pass filter, `H(jω) = jωRC/(1 + jωRC)`, and at the cutoff frequency `f_c = 1/(2*pi*R*C)` the output leads the input by 45°.[^aac-high-pass-transfer-function] This holds when any external load is already accounted for in the effective R.

## Detailed explanation

TODO
