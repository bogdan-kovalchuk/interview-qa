---
id: emb-elintro-0210
title: "What is the 2N2222/PN2222 pinout in a `TO-92` package, and why check the datasheet?"
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
  - source_id: pn2222-datasheet
    title: "onsemi PN2222A datasheet"
    url: https://www.onsemi.com/pdf/datasheet/pn2222a-d.pdf
---

## Short answer

There is no universal pinout for all 2N2222/PN2222 variants in `TO-92`: it depends on the specific part number and manufacturer.[^pn2222-datasheet] Check the package drawing and pin numbering in its datasheet, orienting the part exactly as shown in the drawing.[^pn2222-datasheet]

## Detailed explanation

The pinout of a 2N2222 or PN2222 is determined from the specific manufacturer and package datasheet: similar part names do not guarantee the same pin order.[^pn2222-datasheet]

The markings 2N2222, PN2222, and PN2222A often denote related NPN transistors, but can correspond to different variants. For example, onsemi publishes separate documents for the P2N2222A and the PN2222A, although both come in a plastic TO-92 package; the pinout scheme and the way the package is shown in the mechanical drawing apply specifically to the part number described by the manufacturer.[^pn2222-datasheet]

To identify the pins, verify the full marking, manufacturer, and package, find the `Pin Configuration` section or package drawing in the datasheet, and then orient the part exactly as shown in the drawing. Do not assume that looking at the flat side facing you always yields `E-B-C`: the drawing may be shown from the bottom, top, or the pin side. Match the direction and pin numbering, not just the external shape.[^pn2222-datasheet]

Incorrect connection may prevent the expected switching or amplification and, under unfavorable conditions, exceed the allowable junction voltages or currents. Even if a transistor with swapped collector and emitter sometimes conducts in the reverse-active region, its gain and absolute maximum ratings there are not equivalent to normal operation. Before applying power, verify the pinout, polarity, current limits, and power dissipation in the datasheet.[^pn2222-datasheet]

**Common mistake:** copying a pinout from an arbitrary drawing to a different marking or package. For a prototype, record the part number and manufacturer, and for a replacement, repeat the verification using the new component document.
