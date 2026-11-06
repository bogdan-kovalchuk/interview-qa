---
id: emb-eldig-0034
title: "Why must unused CMOS inputs never be left floating?"
track: electronics
section: digital-logic
sources:
  - source_id: ti-scba004
    title: "Texas Instruments Application Report SCBA004: Implications of Slow or Floating CMOS Inputs"
    url: https://www.ti.com/lit/an/scba004d/scba004d.pdf
  - source_id: nexperia-an10832
    title: "Nexperia Application Note AN10832: Input and Output Characteristics of Logic Families"
    url: https://www.nexperia.com/applications/white-papers/an10832-input-and-output-characteristics-of-logic-families.html
  - source_id: horowitz-art-of-electronics
    title: "Paul Horowitz, Winfield Hill: The Art of Electronics (3rd Edition), Cambridge University Press"
    url: https://artofelectronics.net/
---

## Short answer

CMOS inputs have extremely high insulated-gate impedance and easily pick up electrostatic noise. A floating potential inevitably drifts into the intermediate threshold region near `V_CC / 2`, partially turning on both complementary transistors of the input inverter simultaneously. This causes excessive shoot-through current between supply rails, overheating, and erratic oscillation, so all unused inputs must be tied to `V_CC` or `GND`.[^ti-scba004]

## Detailed explanation

TODO
