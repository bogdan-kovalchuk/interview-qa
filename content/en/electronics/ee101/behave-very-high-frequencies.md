---
id: emb-elee-0061
title: "How do X_C and X_L change at DC and as frequency increases?"
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
  - source_id: aac-capacitor-reactance
    title: "All About Circuits: AC Capacitor Circuits"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-4/ac-capacitor-circuits/
  - source_id: aac-inductor-reactance
    title: "All About Circuits: AC Inductor Circuits"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-3/ac-inductor-circuits/
  - source_id: aac-inductor-quirks
    title: "All About Circuits: Inductor Quirks"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-3/inductor-quirks/
---

## Short answer

In an ideal model at DC after transients settle, a capacitor has infinite `X_C` and an inductor has zero `X_L`. For a sinusoidal signal, `X_C = 1/(2π*f*C)` decreases with increasing frequency, whereas `X_L = 2π*f*L` increases.[^aac-capacitor-reactance] Real components do not become ideal short circuits or open circuits, as parasitic parameters alter their behavior, especially near self-resonance.[^aac-inductor-quirks]

## Detailed explanation

TODO
