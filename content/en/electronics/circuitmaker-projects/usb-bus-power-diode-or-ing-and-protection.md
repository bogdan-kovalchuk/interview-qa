---
id: emb-elcmproj-0059
title: "How does Schottky diode OR-ing protect a device under simultaneous USB and battery power?"
track: electronics
section: circuitmaker-projects
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: usb-2-0-spec
    title: "USB Implementers Forum: Universal Serial Bus Specification, Revision 2.0"
    url: https://www.usb.org/document-library/usb-20-specification
  - source_id: ti-slvae57
    title: "Texas Instruments Application Report SLVAE57: Basics of Ideal Diodes"
    url: https://www.ti.com/lit/an/slvae57b/slvae57b.pdf
  - source_id: horowitz-hill-art-of-electronics
    title: "Paul Horowitz, Winfield Hill: The Art of Electronics (3rd Edition), Cambridge University Press"
    url: https://artofelectronics.net/
  - source_id: vishay-bat54-datasheet
    title: "Vishay Semiconductors: BAT54 / BAT54A / BAT54C / BAT54S Small Signal Schottky Diodes Datasheet"
    url: https://www.vishay.com/docs/85614/bat54.pdf
---

## Short answer

Diodes placed in series with the USB bus and battery supply rails form a diode-OR power multiplexer. Current is drawn automatically from whichever source provides higher potential, reverse-biasing the lower-voltage source. Reverse blocking prevents battery back-feeding into the host USB port, while the low forward voltage drop of Schottky diodes minimizes supply voltage loss.[^udemy-electronics-course]

## Detailed explanation

TODO
