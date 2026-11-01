---
id: emb-elintro-0070
title: "How does the equivalent internal resistance change when batteries are in series?"
track: electronics
section: introduction
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-direct-current
    title: "All About Circuits textbook, Volume I: DC"
    url: https://www.allaboutcircuits.com/textbook/direct-current/
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
---

## Short answer

In a series connection, the equivalent internal resistance equals the sum of the resistances of the individual batteries, when modeled as ideal EMF sources with series resistance.[^aac-direct-current] The total EMF also adds up for batteries connected in the same direction.[^aac-direct-current]

## Detailed explanation

In a simple model, each battery is represented as an ideal source of electromotive force in series with an internal resistance. In a series connection, the same current passes through each source and its resistance, so the resistances add up just like ordinary resistors in a single series circuit: `R_int,total = R_int1 + R_int2 + ...`.[^aac-direct-current]

If you connect two identical batteries with an EMF of `1.5 V` and an internal resistance of `0.2 Ω` each, the total EMF will be `3.0 V`, and the total internal resistance will be `0.4 Ω`. For a load of `10 Ω`, the idealized current equals `3.0 V/(10 Ω + 0.4 Ω) ≈ 0.288 A`. Part of the voltage is dropped inside the sources, so the terminal voltage under load is less than the total EMF.[^aac-direct-current]

This result applies to a series connection without parallel paths and to a model with constant parameters. Real internal resistance depends on chemistry, temperature, state of charge, and measurement method; batteries connected in series do not automatically become identical. For different cells, you must add their actual effective resistances rather than multiplying a single nominal value by the count.[^aac-direct-current]

**Common mistake:** adding only voltages while forgetting total resistance, thereby overestimating the expected current. In the source model, the load voltage is determined together with the voltage drop across the internal resistance.[^aac-direct-current]
