---
id: emb-elinteg-0020
title: "Why is a separate `V_EE` power supply pin provided on the 74HC4051 analog multiplexer?"
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

The `V_EE` pin serves as the negative supply rail for the internal analog switches, enabling bipolar analog signals such as audio to pass through without distortion. Analog signal voltages may swing from `V_EE` to `V_CC`, while digital control inputs remain referenced to `GND`. When switching only single-supply positive voltages, `V_EE` is tied directly to system ground `GND`.[^ti-cd74hc4051-datasheet]

## Detailed explanation

TODO
