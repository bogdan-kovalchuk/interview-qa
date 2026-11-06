---
id: emb-elee-0245
title: "How does a quartz crystal differ from a ready-made oscillator module?"
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
  - source_id: ti-sn74lvc1gx04-oscillator
    title: "Texas Instruments: SN74LVC1GX04 datasheet (SCES581D), section 9 Application and Implementation"
    url: https://www.ti.com/lit/ds/symlink/sn74lvc1gx04.pdf
  - source_id: abracon-quartz-glossary
    title: "Abracon: Quartz Crystal Oscillators Glossary of Terms"
    url: https://abracon.com/Support/qtzcryoscil_glossary.pdf
---

## Short answer

A quartz crystal resonator sets the frequency, but oscillation requires an active feedback amplifier such as an inverter in a Pierce configuration.[^ti-sn74lvc1gx04-oscillator] A ready-made oscillator module typically outputs a logic-level clock signal (such as TTL or HCMOS), though sine-wave outputs also exist.[^abracon-quartz-glossary] An enable pin, if present, controls the output state: grounding it places the output into a high-impedance state.[^abracon-quartz-glossary]

## Detailed explanation

TODO
