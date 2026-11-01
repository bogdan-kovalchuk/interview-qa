---
id: emb-elintro-0071
title: "How does the equivalent internal resistance of identical batteries change in parallel?"
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

For `N` identical batteries with independent internal resistances, the equivalent resistance equals `R_int/N`. Therefore, two identical parallel batteries have approximately half the internal resistance, and the voltage sags less under the same load.[^aac-direct-current]

## Detailed explanation

When two identical batteries with the same open-circuit voltage are connected in parallel, their equivalent internal resistance is half the resistance of a single battery. The terminal voltage across both batteries is identical, and the total load current divides between the branches according to their internal resistances. For two identical branches, the current divides equally, so the voltage drop inside the equivalent model is reduced for a given total current.[^aac-direct-current]

This is the result of a parallel connection of resistances: both ideal sources have the same voltage, so there is no voltage difference between them and no balancing current arises in this idealized model. Real batteries differ in state of charge, temperature, aging, and internal resistance, so currents can divide unequally. Wire and contact resistance also affect the distribution, especially when currents are large; identical wire length and cross-section help equalize the external current path.[^aac-direct-current]

Example: if each battery has an internal resistance model of `0.2 Ω`, the parallel combination has `0.1 Ω`. Under a load of `2 A`, the drop across this equivalent resistance equals `0.2 V`; each identical battery delivers approximately `1 A`.

**Common mistake:** believing that voltage doubles in a parallel connection. It remains the voltage of a single battery; the available capacity and, under proper conditions, the current capability of the bank increase.[^aac-direct-current]
