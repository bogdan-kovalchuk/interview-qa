---
id: emb-elintro-0297
title: "Why are wires often tinned before soldering?"
track: electronics
section: introduction
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-direct-current
    title: "All About Circuits textbook, Volume I: DC"
    url: https://www.allaboutcircuits.com/textbook/direct-current/
  - source_id: adafruit-wire-tinning
    title: "Adafruit: First Steps, UNTZtrument"
    url: https://learn.adafruit.com/untztrument-trellis-midi-instrument/first-steps
  - source_id: nasa-wire-tinning
    title: "NASA-STD-8739.4A: Workmanship Standard for Crimping, Interconnecting Cables, Harnesses, and Wiring"
    url: https://s3vi.ndc.nasa.gov/ssri-kb/static/resources/nasa-std-8739.4a.pdf
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
---

## Short answer

Tinning stranded wire bonds its individual fine strands together so they do not fray or cause accidental short circuits. Apply only enough solder to wet and wick between the strands, as excess solder can make the wire end too stiff or oversized for a terminal.[^nasa-wire-tinning]

## Detailed explanation

Tinning is the pre-wetting of a bare conductor with solder. In stranded wire, the individual fine strands easily fray after stripping insulation; solder bonds them together, making the wire end easier to insert into a through-hole, terminal, or connector. This also reduces the risk that a stray strand will splay outside the contact area and touch an adjacent conductor.[^nasa-wire-tinning]

During tinning, heat the conductor itself and apply solder to the heated strands so that it wicks between them rather than merely forming a ball on the surface. Keep the contours of the individual strands visible and avoid letting solder wick far beneath the insulation: the tinned section becomes stiff, whereas the remainder of the wire must remain flexible.[^nasa-wire-tinning]

Tinning is required only where specified by the joining method: NASA-STD-8739.4A describes it for stranded conductors that form part of a soldered termination in a solder cup. Because the requirements of this specification apply to its specific manufacturing context, check the manufacturer instructions for any other connector or terminal. Tinning itself does not guarantee a shorter final soldering time. For example, before installing flexible stranded wire into a solder cup, a thin, uniform coating of solder should cover the working length, but strand contours must remain discernible and solder must not wick beneath the insulation; do not automatically apply this guideline to spring-loaded or screw terminals.[^nasa-wire-tinning]
