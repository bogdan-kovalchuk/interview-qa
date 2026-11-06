---
id: emb-elinteg-0022
title: "How do parasitic parameters of the 74HC4051 analog switch affect high-frequency signal transmission?"
track: electronics
section: digital-integration
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-digital
    title: "All About Circuits textbook, Volume IV: Digital"
    url: https://www.allaboutcircuits.com/textbook/digital/
  - source_id: ti-cd74hc4051-datasheet
    title: "Texas Instruments: CD74HC4051, CD74HCT4051 High-Speed CMOS Logic 8-Channel Analog Multiplexer/Demultiplexer Datasheet"
    url: https://www.ti.com/lit/ds/symlink/cd74hc4051.pdf
  - source_id: horowitz-hill-art-electronics
    title: "Paul Horowitz, Winfield Hill. The Art of Electronics, 3rd Edition. Cambridge University Press"
    url: https://artofelectronics.net/
---

## Short answer

The switch exhibits finite on-state resistance `R_on` and parasitic capacitances to the substrate and adjacent channels. These parasitics form an `RC` low-pass filter that limits bandwidth and rolls off fast pulse edges. At frequencies of several megahertz and above, square waves suffer overshoot and ringing due to stray inductance in breadboard leads and board traces.[^ti-cd74hc4051-datasheet]

## Detailed explanation

TODO
