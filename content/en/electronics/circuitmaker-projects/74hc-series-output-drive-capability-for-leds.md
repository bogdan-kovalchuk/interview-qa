---
id: emb-elcmproj-0018
title: "How does the output drive current limit of 74HC logic affect LED resistor selection?"
track: electronics
section: circuitmaker-projects
sources:
  - source_id: ti-sn74hc00-datasheet
    title: "Texas Instruments: SN74HC00 Quadruple 2-Input Positive-NAND Gates Datasheet"
    url: https://www.ti.com/lit/ds/symlink/sn74hc00.pdf
  - source_id: nexperia-74hc-family-specs
    title: "Nexperia: 74HC/HCT Family Specifications, User Guide"
    url: https://assets.nexperia.com/documents/user-manual/UM10204.pdf
  - source_id: horowitz-art-of-electronics
    title: "Paul Horowitz, Winfield Hill. The Art of Electronics, 3rd Edition, Cambridge University Press"
    url: https://artofelectronics.net/
  - source_id: floyd-electronic-devices
    title: "Thomas L. Floyd: Electronic Devices (Conventional Current Version), 10th Edition. Pearson, 2017"
    url: https://www.pearson.com/en-us/subject-catalog/p/electronic-devices-conventional-current-version/P200000003290
---

## Short answer

The output stages of 74HC logic guarantee a rated drive current of about 4–6 mA, with an absolute maximum limit of 25 mA per pin. Modern indicator LEDs achieve sufficient brightness at only 2–3 mA. Current-limiting resistors of 470–1000 Ω set a safe load current, preventing IC die overheating, damage, and logic level degradation.[^ti-sn74hc00-datasheet]

## Detailed explanation

TODO
