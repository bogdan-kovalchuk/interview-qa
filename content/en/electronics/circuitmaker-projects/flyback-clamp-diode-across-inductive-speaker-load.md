---
id: emb-elcmproj-0042
title: "Why is a diode connected across a speaker coil in a single-ended amplifier?"
track: electronics
section: circuitmaker-projects
sources:
  - source_id: horowitz-hill-art-of-electronics
    title: "Horowitz P., Hill W. The Art of Electronics. 3rd Edition. Cambridge University Press, 2015"
    url: https://artofelectronics.net/
  - source_id: sedra-smith-microelectronic-circuits
    title: "Sedra A. S., Smith K. C. Microelectronic Circuits. 7th Edition. Oxford University Press, 2014"
    url: https://global.oup.com/ushe/product/microelectronic-circuits-9780199339143
  - source_id: onsemi-1n4148-datasheet
    title: "onsemi 1N4148 / 1N4448 Small Signal Fast Switching Diodes Datasheet"
    url: https://www.onsemi.com/pdf/datasheet/1n4148-d.pdf
---

## Short answer

A speaker voice coil has inductance that generates an inductive flyback voltage spike when the switching transistor turns off abruptly: `v_L = -L * (di / dt)`. This high-voltage spike can easily exceed the collector-emitter breakdown rating `V_CEO` of the transistor, causing avalanche breakdown. A flyback diode recirculates the coil discharge current, clamping the spike to the supply rail and protecting the transistor.[^horowitz-hill-art-of-electronics]

## Detailed explanation

TODO
