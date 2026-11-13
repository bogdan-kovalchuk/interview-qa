---
id: emb-elintro-0277
title: "What does the `AWG` rule \"a larger number is a thinner wire\" mean?"
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
  - source_id: nist-awg-wire-diameter
    title: "NIST: Evaluation of Wire Detection in X-Ray Images"
    url: https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=919567
---

## Short answer

In the American Wire Gauge system, a higher gauge number designates a smaller conductor diameter and, for identical material and length, higher electrical resistance. For example, 30 AWG is substantially thinner than 22 AWG; maximum allowable ampacity depends on insulation, thermal conditions, and bundling rather than AWG number alone.[^nist-awg-wire-diameter]

## Detailed explanation

American Wire Gauge (AWG) is a wire diameter designation system in which the numerical gauge behaves counterintuitively: the larger the number, the thinner the conductor. For example, in the NIST table, the diameter of 24 AWG wire is listed as `0.511 mm`, while 30 AWG is given as `0.255 mm`; therefore, 30 AWG wire has approximately half the diameter.[^nist-awg-wire-diameter]

A smaller diameter means a smaller cross-sectional area. For the same material and length, the resistance of such a wire is higher because the current flows through a smaller conductor area. This is one reason why a thinner wire typically heats up more at the same current. However, a specific allowable current should not be inferred from AWG alone: it also depends on the conductor material, insulation, temperature rating, length, routing, cooling, and the requirements of the applicable standard.[^nist-awg-wire-diameter]

Practical comparison: for short copper wires of identical construction, 22 AWG is thicker than 24 AWG, and 24 AWG is thicker than 30 AWG. For stranded wire, it is important to clarify whether the specified AWG refers to each individual strand or the entire conductor; the outer diameter of the insulation is not the copper diameter. Likewise, AWG must not be confused with another gauge system where the numbering direction may differ.[^nist-awg-wire-diameter]

**Common mistake:** assuming that a "larger number" means a "larger wire" or that a safe current can be determined directly from the gauge number alone. To select a cross-section, first determine the wire material and type, installation conditions, and load current, and then check the allowable ampacity table for those conditions. AWG helps identify the geometric size, but by itself does not establish a universal current rating.[^nist-awg-wire-diameter]
