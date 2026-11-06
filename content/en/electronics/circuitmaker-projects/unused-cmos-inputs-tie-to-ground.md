---
id: emb-elcmproj-0015
title: "What must be done with the inputs of an unused section of a 74HC393 CMOS counter?"
track: electronics
section: circuitmaker-projects
sources:
  - source_id: ti-74hc393
    title: "Texas Instruments: SN74HC393 Dual 4-Bit Binary Counters Datasheet (SCLS098)"
    url: https://www.ti.com/lit/ds/symlink/sn74hc393.pdf
  - source_id: ti-scba004
    title: "Texas Instruments Application Report SCBA004D: Implications of Slow or Floating CMOS Inputs"
    url: https://www.ti.com/lit/an/scba004d/scba004d.pdf
  - source_id: nexperia-74hc393
    title: "Nexperia: 74HC393; 74HCT393 Dual 4-bit binary ripple counter Datasheet"
    url: https://www.nexperia.com/products/logic/counters/74HC393.html
  - source_id: horowitz-art-of-electronics
    title: "Paul Horowitz, Winfield Hill: The Art of Electronics (3rd Edition), Cambridge University Press"
    url: https://artofelectronics.net/
---

## Short answer

All input pins of the unused half of a 74HC393 binary counter, namely clock input `2CP` and master reset `2MR`, must be tied to a defined logic level, typically `GND`. Floating CMOS inputs drift into the linear threshold region near `V_CC / 2` due to picked-up noise, turning both internal MOSFETs partially on. This causes shoot-through current, overheating, and high-frequency oscillation that can disrupt the active counter half. Unused outputs are left unconnected.[^ti-74hc393]

## Detailed explanation

TODO
