---
id: emb-elintro-0027
title: "How do you orient a `DIP` chip and find pin 1?"
track: electronics
section: introduction
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-direct-current
    title: "All About Circuits textbook, Volume I: DC"
    url: https://www.allaboutcircuits.com/textbook/direct-current/
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
  - source_id: ti-sn74hc04-pinout
    title: "Texas Instruments: SNx4HC04 Hex Inverters datasheet, Rev. H"
    url: https://www.ti.com/lit/ds/symlink/sn74hc04.pdf
---

## Short answer

A notch or dot often marks the pin 1 side, but verify the exact orientation in the datasheet for the specific chip. For the TI CDIP package in the manufacturer's example, pin 1 is marked; do not assume the notch position is a universal rule.[^ti-sn74hc04-pinout]

## Detailed explanation

Pin 1 is the starting point for pin numbering, and its position is defined by the manufacturer for the specific package and component. On the package, it is often marked with a dot, notch, or other index, but the appearance and placement of the mark can vary; first locate the corresponding package drawing or pin configuration in the datasheet for that exact chip.[^ti-sn74hc04-pinout]

For a standard dual in-line `DIP` package with a notch at the top, a typical top view shows pin 1 in the upper left corner, and the sequence of numbers proceeds counterclockwise around the package. This is a helpful rule of thumb rather than a substitute for documentation: some packages use a dot instead of a notch, while special variants or other package types may indicate the index differently.[^ti-sn74hc04-pinout]

Before installation, align the pin 1 marker on the board with the package drawing in the documentation; do not orient the component based solely on the direction of the text on the top cover. In the TI datasheet for the SNx4HC04, the position of pin 1 for the CDIP package is shown separately, illustrating why verifying the specific package drawing is more reliable than relying on a general rule.[^ti-sn74hc04-pinout]

**Common mistake:** confusing the top of the package with the pin 1 side. If markings are unclear or missing, stop and look up the part number and its pinout in the documentation prior to assembly.
