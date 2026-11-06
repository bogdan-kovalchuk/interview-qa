---
id: emb-elee-0144
title: "What is a Zener diode's dynamic resistance `r_Z`?"
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
  - source_id: nexperia-an90031
    title: "Nexperia AN90031: Zener diodes – physical basics, parameters and application examples"
    url: https://assets.nexperia.com/documents/application-note/AN90031.pdf
  - source_id: nexperia-bzx84
    title: "Nexperia BZX84 series: voltage regulator diodes (datasheet)"
    url: https://assets.nexperia.com/documents/data-sheet/BZX84_SER.pdf
---

## Short answer

Dynamic (differential) resistance `r_Z = ΔV_Z/ΔI_Z` is the inverse slope of the Zener breakdown curve at an operating point, giving small-signal changes `ΔV_Z ≈ r_Z*ΔI_Z`.[^nexperia-an90031] It is non-zero and current-dependent: for a BZX84-C5V1, maximum `r_Z` is 480 Ω at 1 mA and 60 Ω at 5 mA.[^nexperia-bzx84] Because of `r_Z`, regulator output drifts slightly with load and input voltage; smaller `r_Z` produces tighter regulation.

## Detailed explanation

TODO
