---
id: emb-elcirc-0039
title: "What is the typical mega-prefix trap in ngspice?"
track: electronics
section: circuit-analysis
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-direct-current
    title: "All About Circuits textbook, Volume I: DC"
    url: https://www.allaboutcircuits.com/textbook/direct-current/
  - source_id: ngspice-number-suffixes
    title: "ngspice User's Manual: Some naming conventions"
    url: https://nmg.gitlab.io/ngspice-manual/circuitdescription/generalstructureandconventions/somenamingconventions.html
---

## Short answer

In ngspice, the suffix `m` denotes milli (10^-3) and `Meg` denotes mega (10^6), regardless of letter case.[^ngspice-number-suffixes] Therefore, `1M` represents 1 mΩ as a numeric suffix, whereas 1 MΩ must be written as `1Meg`.[^ngspice-number-suffixes] Rules can depend on the specific SPICE-compatible simulator, so they should be checked in its manual.[^ngspice-number-suffixes]

## Detailed explanation

TODO
