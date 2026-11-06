---
id: emb-elinteg-0019
title: "How does the 74HC4051 IC operate in analog multiplexer and demultiplexer modes?"
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

The 74HC4051 contains eight bidirectional CMOS transmission gates that connect a selected channel `Y0–Y7` to a common pin `Z`. Because the internal switches are bidirectional, the device functions either as a multiplexer (routing 8 inputs to 1 output) or as a demultiplexer (routing 1 input to 8 destinations). Channel selection is controlled by three digital address lines `S0–S2`.[^ti-cd74hc4051-datasheet]

## Detailed explanation

TODO
