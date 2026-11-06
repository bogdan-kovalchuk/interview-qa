---
id: emb-elee-0082
title: "How can one series RL circuit be both a low-pass and a high-pass filter?"
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
  - source_id: aac-series-rl
    title: "All About Circuits: Series Resistor-Inductor Circuits"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-3/series-resistor-inductor-circuits/
---

## Short answer

The output tapping point determines the filter type. In a series RL circuit, taking the output across R forms a low-pass filter, because as frequency increases, a greater fraction of the input voltage drops across the inductor. Taking the output across L forms a high-pass filter, as inductive impedance increases and the inductor voltage approaches the input. This holds for ideal components and an unloaded output.[^aac-series-rl]

## Detailed explanation

TODO
