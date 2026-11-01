---
id: emb-elintro-0072
title: "Why can only batteries with close voltages be connected in parallel?"
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
  - source_id: discover-helios-parallel
    title: "Discover Battery Helios Installation and Operation Manual"
    url: https://assets.discoverbattery.com/documents/helios/opm-helios-manual.pdf
---

## Short answer

If the voltages are different, a balancing current will flow between the batteries, limited mainly by their internal resistance. Even a small difference can cause a large current, and the permissible value depends on the specific battery and manufacturer guidelines.[^discover-helios-parallel]

## Detailed explanation

A parallel connection enforces the same terminal voltage across all batteries. If their open-circuit voltages differ, the battery with higher voltage delivers current into the battery with lower voltage until the difference decreases. In a simple model with series internal resistance, the current approximately equals the voltage difference divided by the sum of the internal resistances of the batteries and the connection resistance.[^aac-direct-current]

Therefore, the requirement of "close voltages" is a precautionary rule rather than a universal numerical threshold. The acceptable difference depends on chemistry, construction, state of charge, protection, and manufacturer instructions. For lithium batteries with a BMS, you must also consider whether the manufacturer permits parallel operation of those specific models; compatibility cannot be deduced solely from an identical nominal voltage.[^aac-direct-current]

Example: batteries with a potential difference of `0.5 V` and a total equivalent resistance of `0.1 Ω` would yield an initial estimate of `5 A` by Ohm's law. This is merely a linear estimate for the given model: actual resistance depends on temperature, charge, chemical polarization, and wiring, and the current can be dangerously large.

**Common mistake:** assuming that identical labeling of "12 V" implies identical actual voltage or automatically allows connection. You must check actual voltages and manufacturer documentation; batteries of different chemistries or designs should never be connected in parallel without explicit manufacturer permission.[^aac-direct-current]
