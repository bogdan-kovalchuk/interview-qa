---
id: emb-elintro-0087
title: "What is ripple after a rectifier?"
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
  - source_id: aac-rectifier-ripple
    title: "All About Circuits: Full-wave Bridge Rectifier With Output Filtering"
    url: https://www.allaboutcircuits.com/textbook/experiments/chpt-5/rectifier-filter-circuit/
---

## Short answer

`Ripple` is the residual voltage fluctuation after converting `AC` to `DC`. The filter capacitor charges near the peaks of the sine wave and discharges between them, so the voltage is not perfectly smooth.[^aac-rectifier-ripple]

## Detailed explanation

Ripple is the periodic voltage component that remains at the rectifier output alongside the average DC component. A rectifier changes polarity or passes a single half-wave, but on its own it does not produce a perfectly steady voltage. A capacitor placed in parallel with the load charges near the peaks of the rectified voltage, and between peaks it discharges into the load, causing the output voltage to droop gradually until the next peak.[^aac-rectifier-ripple]

The ripple magnitude depends on the load current, filter capacitance, and peak repetition frequency. A heavier load consumes charge faster and increases the droop; a larger capacitance, all else being equal, reduces it. In a full-wave rectifier, peaks appear twice per mains cycle, whereas in a half-wave rectifier they appear once, so under otherwise identical conditions a full-wave circuit generally has lower ripple.[^aac-rectifier-ripple]

**Worked example:** for a rough estimate of a capacitor filter, you use `ΔV ≈ I_load/(f_ripple*C)`. If the load draws `0.1 A`, the ripple frequency is `100 Hz`, and the capacitor is `1000 µF`, the peak-to-peak droop is about `1 V`. This is an approximation for an approximately constant load current; it does not account for capacitor ESR, diode drops, or the shape of the charging pulses.[^aac-rectifier-ripple]

**Common mistake:** calling any voltage after diodes pure DC. For sensitive loads, ripple must be evaluated under load and verified with an oscilloscope or a suitable meter; a regulator can only suppress it within the limits of its input voltage headroom.[^aac-rectifier-ripple]
