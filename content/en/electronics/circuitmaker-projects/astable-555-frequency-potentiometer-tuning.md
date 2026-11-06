---
id: emb-elcmproj-0012
title: "How do potentiometers regulate pulse frequency in a 555 astable oscillator?"
track: electronics
section: circuitmaker-projects
sources:
  - source_id: ti-lm555-datasheet
    title: "Texas Instruments: LM555 Timer Datasheet"
    url: https://www.ti.com/lit/ds/symlink/lm555.pdf
  - source_id: horowitz-art-of-electronics
    title: "Paul Horowitz, Winfield Hill. The Art of Electronics, 3rd Edition, Cambridge University Press"
    url: https://artofelectronics.net/
  - source_id: floyd-electronic-devices
    title: "Thomas L. Floyd: Electronic Devices (Conventional Current Version), 10th Edition. Pearson, 2017"
    url: https://www.pearson.com/en-us/subject-catalog/p/electronic-devices-conventional-current-version/P200000003290
---

## Short answer

A 555 astable oscillator frequency depends on capacitor charge and discharge times: `f approx 1.44 / ((R_A + 2 * R_B) * C)`. Wiring potentiometers as rheostats in series with fixed resistors smoothly adjusts equivalent timing resistance. This allows tuning oscillation rates from fractions of a hertz to hundreds of kilohertz while fixed series resistors protect the discharge transistor against short circuits.[^ti-lm555-datasheet]

## Detailed explanation

TODO
