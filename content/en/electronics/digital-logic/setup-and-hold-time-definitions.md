---
id: emb-eldig-0017
title: "What are setup time and hold time in synchronous digital logic?"
track: electronics
section: digital-logic
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-digital
    title: "All About Circuits textbook, Volume IV: Digital"
    url: https://www.allaboutcircuits.com/textbook/digital/
  - source_id: ti-sn74hc74a
    title: "Texas Instruments: SN74HC74A Dual Positive-Edge-Triggered D-Type Flip-Flops Datasheet"
    url: https://www.ti.com/lit/ds/symlink/sn74hc74a.pdf
  - source_id: harris-harris-ddca
    title: "David Money Harris, Sarah L. Harris. Digital Design and Computer Architecture. Morgan Kaufmann"
    url: https://www.elsevier.com/books/digital-design-and-computer-architecture/harris/978-0-12-394424-5
---

## Short answer

Setup time `t_su` is the minimum time window that input data must remain stable BEFORE the active clock transition. Hold time `t_h` is the minimum duration that data must remain unchanged AFTER the active clock edge. Violating either requirement can trigger flip-flop metastability or cause corrupt data capture.[^ti-sn74hc74a] [^harris-harris-ddca]

## Detailed explanation

TODO
