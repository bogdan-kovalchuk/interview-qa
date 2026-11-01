---
id: emb-elintro-0198
title: "What is the basic `BJT` formula in the active mode?"
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
---
## Short answer

For a `BJT` in the forward-active mode, approximately `I_C = β*I_B`, where `β` is the current gain for the specific operating conditions. This is not a universal constant: β varies between individual devices and depends on current, voltage, and temperature. In saturation, the load limits the current, so the formula no longer determines the actual `I_C`.[^aac-semiconductors]

## Detailed explanation

In the forward-active mode, the base–emitter junction is forward-biased, and the collector–base junction is reverse-biased. In this region, simplified analysis uses the relationship `I_C = β*I_B`, where β (also `h_FE` in a DC context) is the ratio of collector current to base current.[^aac-semiconductors]

Physically, the thin base allows most of the carriers injected by the emitter to reach the collector; a smaller fraction recombines in the base and forms the base current. The β model is convenient for estimation, but it is not an exact proportionality under all conditions. The value of β is taken from the datasheet for the corresponding collector current and voltage; guaranteed limits can be wide, and the parameter varies with temperature.[^aac-semiconductors]

When the transistor is saturated, the external circuit cannot provide the current that the β*I_B estimate would demand. In this case, both junctions are forward-biased, and the current is determined by the power supply and the load. That is why switching a transistor usually involves providing a sufficient base current margin rather than relying on a typical β from a single table row.[^aac-semiconductors]

Example: if you assume β = 100 and `I_B = 20 µA` for calculation, the model yields `I_C = 2 mA`. This is only an estimate for the active mode; a real transistor may have a different β, and the load may limit the current below 2 mA.[^aac-semiconductors]

**Common mistakes:** treating β as a guaranteed constant; applying the formula in saturation or cutoff; confusing DC `h_FE` with small-signal gain.[^aac-semiconductors]
