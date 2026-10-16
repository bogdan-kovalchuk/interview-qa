---
id: emb-elintro-0011
title: How do you decode the `SMD` component size "0805"?
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
  - source_id: vishay-sizes
    title: "Vishay D/CRCW e3 standard thick film chip resistors"
    url: https://www.vishay.com/docs/20035/dcrcwe3.pdf
---

## Short answer

For common rectangular chip resistors, an imperial 0805 size code describes roughly 0.08 by 0.05 inches; the usual nominal dimensions are 2.0 by 1.25 mm, corresponding to metric 2012. Confirm the code system and actual package drawing because imperial and metric codes can be confused. [^vishay-sizes]

## Detailed explanation

Split the imperial code into length and width, each in hundredths of an inch. The exact conversion of 0.08 inch is 2.032 mm and of 0.05 inch is 1.270 mm. Package naming is nominal, however: the Vishay drawing for CRCW0805 specifies nominal 2.0 mm length and 1.25 mm width, with manufacturing tolerances. [^vishay-sizes]

The corresponding metric code 2012 indicates an approximately 2.0 by 1.2 mm naming class; it is not a demand that width equal exactly 1.20 mm. Similarly, imperial 0402 commonly corresponds to nominal 1.0 by 0.5 mm and metric 1005 in this resistor family. [^vishay-sizes]

Body size alone is not the PCB land pattern. Pad dimensions, termination geometry, clearance and assembly recommendations must come from the applicable drawing or footprint specification. Size also does not uniquely determine resistance or power rating. Write the unit system explicitly when selecting a component to avoid confusing an imperial 0805 with a metric designation.
