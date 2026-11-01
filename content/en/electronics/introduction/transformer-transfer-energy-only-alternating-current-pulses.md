---
id: emb-elintro-0156
title: "Why does a transformer transfer energy only with alternating current or pulses?"
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
  - source_id: electronics-tutorials-transformer-basics
    title: "Electronics Tutorials: Transformer Basics and Transformer Principles"
    url: https://www.electronics-tutorials.ws/transformer/transformer-basics.html
---

## Short answer

Secondary voltage arises when the magnetic flux through the winding changes; it is created by AC or pulses, not by steady DC after the transient.[^electronics-tutorials-transformer-basics] Applying DC to the primary winding can cause excessive current and overheating because, after the transient, inductive reactance does not limit it as it does with AC.[^electronics-tutorials-transformer-basics]

## Detailed explanation

A transformer transfers energy between windings through an alternating magnetic flux in a shared core. Current in the primary winding creates flux, and the law of electromagnetic induction relates the induced voltage in each winding to the rate of change of this flux and the turn count.[^electronics-tutorials-transformer-basics]

Under sinusoidal voltage, the flux changes periodically, so voltage is continuously induced in the secondary winding. Pulse excitation also works: each rising or falling edge changes the flux and creates a momentary voltage, while the switching circuit defines pulse repetition and an energy path.[^electronics-tutorials-transformer-basics] Thus, the expression "only AC" would be too narrow: what matters is flux change, not strictly the sinusoidal waveform itself.

After the transient from direct current settles, the magnetic flux becomes constant. Then `dΦ/dt = 0`, so no secondary voltage is induced; a short voltage pulse is possible during connection or disconnection of the source while the flux is changing.[^electronics-tutorials-transformer-basics]

For a conventional transformer, direct prolonged connection of DC voltage is hazardous: inductive reactance, which limits alternating current, does not act for steady DC, and current is determined primarily by the low resistance of the copper wire. This can overheat the winding; in practical converters, DC is first switched, creating an alternating flux.[^electronics-tutorials-transformer-basics]

**Common mistake:** saying that a transformer "transfers AC". It transfers energy through an alternating magnetic flux, which can be created by either a periodic signal or pulses; a constant flux does not sustain induced voltage.[^electronics-tutorials-transformer-basics]
