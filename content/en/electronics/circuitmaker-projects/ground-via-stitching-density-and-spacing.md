---
id: emb-elcmproj-0064
title: "Why are ground pours on opposite PCB layers connected with via stitching?"
track: electronics
section: circuitmaker-projects
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), картки курсу"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: circuitmaker-docs
    title: "CircuitMaker documentation"
    url: https://www.altium.com/documentation/altium-circuitmaker
  - source_id: bogatin-signal-power-integrity
    title: "Eric Bogatin: Signal and Power Integrity - Simplified (3rd Edition)"
    url: https://www.pearson.com/en-us/subject-catalog/p/signal-and-power-integrity---simplified/P200000003233
  - source_id: ott-emc-engineering
    title: "Henry W. Ott: Electromagnetic Compatibility Engineering"
    url: https://www.wiley.com/en-us/Electromagnetic+Compatibility+Engineering-p-9780470189306
---

## Short answer

Stitching vias spaced at roughly one-inch intervals tie isolated ground copper pours across board layers together. This establishes low-impedance RF return paths and suppresses parasitic cavity or slot resonances between ground planes. The resulting stitching grid improves electromagnetic shielding and reduces radiated emissions.[^udemy-electronics-course][^ott-emc-engineering]

## Detailed explanation

TODO
