---
id: emb-elee-0262
title: "Why does a ferrite bead in a supply line pass DC but suppress noise?"
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
  - source_id: wuerth-ferrite-bead-behavior
    title: "Würth Elektronik Application Note ANP008: The Real Behavior of Ferrite Beads"
    url: https://www.we-online.com/catalog/media/o109033v410%20AppNotes_ANP008_TheRealBehaviorOfFerriteBeads_EN.pdf
  - source_id: analog-devices-ferrite-beads
    title: "Analog Devices Tutorial MT-101: Decoupling Techniques"
    url: https://www.analog.com/media/en/training-seminars/tutorials/MT-101.pdf
  - source_id: art-of-electronics
    title: "Horowitz P., Hill W. The Art of Electronics. 3rd ed. Cambridge University Press, 2015"
    url: https://artofelectronics.net/
---

## Short answer

A ferrite bead acts as an inductor whose inductive reactance `X_L = 2*pi*f*L` increases with frequency. For direct current (DC), the reactance is near zero, but for high-frequency noise in the kilohertz and megahertz range, the impedance is substantial and dissipative. It is therefore placed in series with the power rail, often at the input and output of a voltage regulator.[^udemy-electronics-course]

## Detailed explanation

TODO
