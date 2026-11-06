---
id: emb-elcmproj-0052
title: "Why can USB bus power not be considered a stable and precise 5.0 V source?"
track: electronics
section: circuitmaker-projects
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: usb-2-0-spec
    title: "USB Implementers Forum: Universal Serial Bus Specification, Revision 2.0"
    url: https://www.usb.org/document-library/usb-20-specification
  - source_id: horowitz-hill-art-of-electronics
    title: "Paul Horowitz, Winfield Hill: The Art of Electronics (3rd Edition), Cambridge University Press"
    url: https://artofelectronics.net/
  - source_id: ti-slva982
    title: "Texas Instruments Application Report SLVA982: Voltage Reference Selection Basics"
    url: https://www.ti.com/lit/an/slva982a/slva982a.pdf
  - source_id: microchip-an688
    title: "Microchip Technology Application Note AN688: Layout Tips for 12-Bit A/D Converter Applications"
    url: https://ww1.microchip.com/downloads/en/appnotes/00688b.pdf
---

## Short answer

The USB specification allows bus voltage to vary between 4.75 V and 5.25 V (and down to 4.40 V on low-power downstream ports), often with substantial switching noise. In addition, long cables introduce dynamic IR voltage drops under varying loads. Precise analog ADC measurements therefore require a dedicated, stabilized voltage reference rather than raw USB bus power.[^udemy-electronics-course]

## Detailed explanation

TODO
