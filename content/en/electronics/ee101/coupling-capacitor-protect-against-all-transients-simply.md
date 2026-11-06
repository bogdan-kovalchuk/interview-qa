---
id: emb-elee-0113
title: "Does a coupling capacitor protect against all transients, and can you simply multiply the H of cascaded filters?"
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
  - source_id: aac-capacitor-transient
    title: "All About Circuits: Capacitor Transient Response"
    url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-16/capacitor-transient-response/
  - source_id: aac-filter-cascading
    title: "All About Circuits: Introduction to Analog Filters"
    url: https://www.allaboutcircuits.com/TEXTBOOK/designing-analog-chips/filters/introduction-to-analog-filters/
---

## Short answer

No: a coupling capacitor is not a universal shield against voltage transients because an input step creates an output spike. Cascaded transfer functions can be multiplied directly only when the stages do not load each other, such as when separated by a buffer; otherwise, the combined circuit must be analyzed as a whole.[^aac-capacitor-transient] [^aac-filter-cascading]

## Detailed explanation

TODO
