---
id: emb-elintro-0022
title: "What is an ampere?"
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
  - source_id: nist-sp330-section2
    title: "NIST Special Publication 330: The International System of Units, Section 2"
    url: https://www.nist.gov/pml/special-publication-330/sp-330-section-2
---

## Short answer

The ampere (A) is the unit of electric current; `1 A = 1 C/s`. This means that a charge of one coulomb passes through the cross-section of a conductor per second.[^nist-sp330-section2]

## Detailed explanation

The ampere measures the rate of transfer of electric charge. One ampere corresponds to a flow of one coulomb per second, written as `I = Q/t` for steady current.[^nist-sp330-section2]

In the modern SI, the ampere is defined in terms of the fixed numerical value of the elementary charge and the second. Therefore, the statement of a coulomb per second is consistent with the modern definition of the unit, rather than just an everyday analogy.[^nist-sp330-section2]

Conventional current direction is defined as the direction of motion of positive charge. In a metal wire, the carriers are typically electrons moving in the opposite direction; this does not change the magnitude of the measured current.[^aac-direct-current]

For a time-varying current, the ratio of total charge to the duration of the interval yields an average value. Instantaneous current describes the rate of charge transfer at that exact moment, so it cannot always be recovered from the final total charge alone. This distinction is useful, for example, when measuring a pulsed signal or charging a capacitor.[^nist-sp330-section2]

**Example:** if a charge of `6 C` is transferred through a cross-section in `2 s`, the average current equals `I = Q/t = 6 C/2 s = 3 A`.

**Common mistake:** confusing current with charge itself. Charge is measured in coulombs, and current in amperes, that is, in coulombs per second.
