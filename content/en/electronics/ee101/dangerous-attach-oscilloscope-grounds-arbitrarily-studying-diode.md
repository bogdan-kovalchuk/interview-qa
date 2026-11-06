---
id: emb-elee-0140
title: "Why is it dangerous to attach oscilloscope grounds arbitrarily when studying a diode bridge?"
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
  - source_id: tektronix-abcs-probes
    title: "Tektronix: ABCs of Probes Primer"
    url: https://download.tek.com/document/02_ABCs-of-Probes-Primer.pdf
  - source_id: fiore-rectification
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 3.2 Rectification"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/03:_Diode_Applications/3.2:_Rectification
---

## Short answer

Probes of a standard oscilloscope share earth ground through the line cord safety conductor, so connecting ground clips to two different bridge nodes, such as the negative DC rail and an AC input terminal, shorts out part of the bridge.[^tektronix-abcs-probes] If the bridge is fed directly from the AC mains, the ground lead also creates a dangerous short to earth ground.[^tektronix-abcs-probes] Bridges are safely studied in simulation or from an isolated low-voltage transformer secondary, keeping all ground clips on the negative DC output.

## Detailed explanation

TODO
