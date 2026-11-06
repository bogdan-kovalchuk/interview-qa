---
id: emb-elinteg-0006
title: "Why is an LED connected with its anode to V_CC and cathode to an active-low decoder output?"
track: electronics
section: digital-integration
sources:
  - source_id: ti-74ls138-datasheet
    title: "Texas Instruments. SN74LS138, SN74S138 3-Line to 8-Line Decoders/Demultiplexers Data Sheet"
    url: https://www.ti.com/lit/ds/symlink/sn74ls138.pdf
  - source_id: sedra-smith-microelectronic-circuits
    title: "Adel S. Sedra, Kenneth C. Smith. Microelectronic Circuits, 7th Edition"
    url: https://global.oup.com/ushe/product/microelectronic-circuits-9780199339143
  - source_id: horowitz-art-of-electronics
    title: "Paul Horowitz, Winfield Hill. The Art of Electronics, 3rd Edition, Cambridge University Press"
    url: https://artofelectronics.net/
---

## Short answer

An active-low output pulls down toward ground when asserted, completing the circuit to sink current. Bipolar TTL logic ICs can sink significantly greater current `I_OL` in the low state than they can source `I_OH` in the high state. Connecting the LED cathode to the output through a current-limiting resistor ensures full brightness without overloading the driving gate.[^ti-74ls138-datasheet]

## Detailed explanation

TODO
