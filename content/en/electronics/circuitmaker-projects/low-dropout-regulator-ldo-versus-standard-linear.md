---
id: emb-elcmproj-0037
title: "Why is an LDO voltage regulator required instead of an LM7805 when powering from a 9 V battery?"
track: electronics
section: circuitmaker-projects
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: ti-ldo-basics
    title: "Texas Instruments Application Report SLVA072: Understanding LDO Dropout"
    url: https://www.ti.com/lit/an/slva072/slva072.pdf
  - source_id: onsemi-lm7805
    title: "onsemi LM78XX / MC78XX Series 1.0 A Positive Voltage Regulators Datasheet"
    url: https://www.onsemi.com/pdf/datasheet/mc7800-d.pdf
  - source_id: ti-lm2940
    title: "Texas Instruments LM2940-N / LM2940C 1-A Low Dropout Regulator Datasheet"
    url: https://www.ti.com/lit/ds/symlink/lm2940-n.pdf
---

## Short answer

The standard LM7805 linear regulator requires an input-to-output headroom of at least 2.0–2.5 V. An LDO regulator with a dropout of only 0.2–0.65 V maintains a regulated 5 V output until the battery discharges down to roughly 5.65 V. This extracts nearly all usable energy from the battery, whereas an LM7805 drops out of regulation once the battery falls below 7.0–7.5 V.[^ti-ldo-basics]

## Detailed explanation

TODO
