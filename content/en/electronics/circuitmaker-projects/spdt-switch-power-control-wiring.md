---
id: emb-elcmproj-0009
title: "How is an SPDT slide switch wired for battery power control?"
track: electronics
section: circuitmaker-projects
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: circuitmaker-docs
    title: "CircuitMaker documentation"
    url: https://www.altium.com/documentation/altium-circuitmaker
  - source_id: horowitz-hill-art-of-electronics
    title: "Paul Horowitz, Winfield Hill: The Art of Electronics (3rd Edition), Cambridge University Press"
    url: https://artofelectronics.net/
  - source_id: littelfuse-ck-switch-handbook
    title: "Littelfuse C&K: Switch Selection and Contact Rating Guidelines"
    url: https://www.ckswitches.com/
  - source_id: e-switch-basics
    title: "E-Switch: Switch Terminology and Contact Configurations Technical Reference"
    url: https://www.e-switch.com/
---

## Short answer

The central common terminal of the switch connects to the system power rail. One outer throw connects to the positive battery terminal, while the opposite throw is left unconnected or pulled to ground through a bleeder resistor. In the active position, battery power feeds the circuit, while the open position disconnects and unpowers the device.[^udemy-electronics-course][^e-switch-basics]

## Detailed explanation

TODO
