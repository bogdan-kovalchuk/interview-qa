---
id: emb-elcmproj-0020
title: "What error types can schematic compilation in EDA detect, and what can it not detect?"
track: electronics
section: circuitmaker-projects
sources:
  - source_id: altium-schematic-compilation
    title: "Altium LLC: Compiling and Verifying the Design in Altium EDA Systems"
    url: https://www.altium.com/documentation/altium-designer
  - source_id: ipc-2221b
    title: "IPC: IPC-2221B Generic Standard on Printed Board Design, 2012"
    url: https://www.ipc.org/
  - source_id: horowitz-art-of-electronics
    title: "Paul Horowitz, Winfield Hill: The Art of Electronics, 3rd Edition. Cambridge University Press, 2015"
    url: https://artofelectronics.net/
  - source_id: floyd-digital-fundamentals
    title: "Thomas L. Floyd: Digital Fundamentals, 11th Edition. Pearson, 2015"
    url: https://www.pearson.com/en-us/subject-catalog/p/digital-fundamentals/P200000003294
---

## Short answer

The schematic compiler and Electrical Rules Check (ERC) detect topological and syntax errors: duplicate designators, unconnected pins, pin-type matrix conflicts such as output-to-output shorts, and invalid net names. However, the compiler does not perform physical or circuit simulation. It cannot verify component values, power dissipation, overall functional correctness, or whether component operating points were calculated properly.[^altium-schematic-compilation]

## Detailed explanation

TODO
