---
id: emb-elintro-0183
title: "Why can the transformer in an SMPS be much smaller?"
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
  - source_id: ti-magnetics-design1
    title: "Magnetics Design for Switching Power Supplies: Section 1, Introduction and Basic Magnetics"
    url: https://www.ti.com/lit/ml/slup123/slup123.pdf
  - source_id: ti-magnetics-design4
    title: "Magnetics Design for Switching Power Supplies: Section 4, Power Transformer Design"
    url: https://www.ti.com/lit/ml/slup126/slup126.pdf
---

## Short answer

An SMPS operates at tens or hundreds of kilohertz rather than 50/60 Hz. All else being equal, increasing operating frequency reduces the required core area product, allowing the transformer to be more compact; the exact size also depends on losses and thermal limits.[^ti-magnetics-design4]

## Detailed explanation

In an isolated SMPS, the transformer operates at the switching frequency, typically much higher than mains 50/60 Hz, so smaller magnetic components can be used for the same power rating. The actual size is also constrained by power, core losses, heating, and insulation requirements.[^ti-magnetics-design1]

A switch-mode power supply converts input voltage into pulses using a power transistor. If the topology is isolated, these pulses are fed to a transformer that transfers energy and provides the required voltage ratio and galvanic isolation. Unlike a transformer connected directly to mains frequency, it operates at the switching frequency of the converter.[^aac-semiconductors]

By Faraday's law, the change in magnetic flux is related to the voltage per turn and the duration of its application. In an initial estimate, the area product depends on output power, allowable flux density swing, and operating frequency; as frequency increases, the required product of core cross-sectional area and winding window area decreases. This does not mean linear dimensions scale inversely with frequency: material, losses, temperature, and structural constraints influence the choice.[^ti-magnetics-design1] [^ti-magnetics-design4]

For example, moving from 50/60 Hz to tens or hundreds of kilohertz allows using a compact ferrite core instead of a large low-frequency core. Frequency is not a universal constant, and increasing it raises switching losses and can worsen electromagnetic interference.[^aac-semiconductors]

**Common mistake:** explaining the size reduction solely by "less magnetic flux." What matters are frequency, waveform and amplitude of voltage across the winding, and allowable flux density; moreover, creepage distances and cooling can dictate dimensions. Not every SMPS has a transformer – this depends on topology and isolation requirements.
