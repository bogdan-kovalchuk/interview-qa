---
id: emb-elcmproj-0017
title: "What is the advantage of using named ports and net labels over long schematic wires?"
track: electronics
section: circuitmaker-projects
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: altium-connectivity
    title: "Altium Designer Documentation: Creating Connectivity across Schematic Sheets"
    url: https://www.altium.com/documentation/altium-designer/creating-connectivity
  - source_id: horowitz-art-of-electronics
    title: "Paul Horowitz, Winfield Hill: The Art of Electronics (3rd Edition), Cambridge University Press"
    url: https://artofelectronics.net/
---

## Short answer

Routing long wires across an entire schematic sheet clutters the drawing and makes it difficult to read. Named net labels and ports partition the schematic into clear, autonomous functional modules. EDA software automatically groups nets with identical names into a single electrical netlist without messy wire crossings.[^udemy-electronics-course]

## Detailed explanation

TODO
