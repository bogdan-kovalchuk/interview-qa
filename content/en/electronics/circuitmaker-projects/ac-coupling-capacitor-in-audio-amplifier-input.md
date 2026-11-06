---
id: emb-elcmproj-0041
title: "Why is an AC coupling capacitor placed between the 555 timer output and the amplifier transistor base?"
track: electronics
section: circuitmaker-projects
sources:
  - source_id: ti-lm555-datasheet
    title: "Texas Instruments: LM555 Timer Datasheet"
    url: https://www.ti.com/lit/ds/symlink/lm555.pdf
  - source_id: horowitz-art-of-electronics
    title: "Paul Horowitz, Winfield Hill. The Art of Electronics, 3rd Edition, Cambridge University Press"
    url: https://artofelectronics.net/
  - source_id: sedra-smith-microelectronic-circuits
    title: "Adel S. Sedra, Kenneth C. Smith: Microelectronic Circuits, 8th Edition. Oxford University Press, 2020"
    url: https://global.oup.com/ushe/product/microelectronic-circuits-9780190853464
---

## Short answer

The square-wave output of a 555 timer carries a substantial DC offset of roughly half the supply voltage. A coupling capacitor blocks this DC level, passing only the AC audio-frequency signal to the amplifier stage. This prevents the driver transistor from being driven into hard saturation or thermal overload and keeps the amplifier operating point properly biased.[^horowitz-art-of-electronics]

## Detailed explanation

TODO
