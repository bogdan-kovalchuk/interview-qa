---
id: emb-elintro-0154
title: "What is a transformer's \"reflected impedance\"?"
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
  - source_id: aac-transformer-impedance
    title: "All About Circuits: Special Transformers and Applications"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-9/special-transformers-applications/
---

## Short answer

For an ideal transformer, the load referred to the primary winding equals `Z_primary = (N_primary/N_secondary)^2*Z_load`. Thus, the transformer changes the apparent load impedance according to the square of the turns ratio. For example, to match an 8 Ω speaker to an 8 kΩ source requires a turns ratio of approximately `sqrt(8000/8) = 31.6:1`; real losses and frequency bandwidth limit accuracy.[^aac-transformer-impedance]

## Detailed explanation

Reflected impedance is the secondary winding load expressed as the impedance seen by the source on the primary winding. In an ideal transformer, the voltage ratio equals the turns ratio, while currents follow an inverse ratio. Because impedance is the ratio of voltage to current, these two transformations yield the square of the turns ratio: `Z_primary = (N_primary/N_secondary)^2*Z_load`.[^aac-transformer-impedance]

From this it follows that a step-up voltage transformer reflects secondary load as a lower impedance on the primary side; a step-down transformer reflects it as a higher impedance. This allows matching a source to a load, such as an audio amplifier to a speaker. The formula is an approximation for an ideal transformer: winding resistance, leakage inductance, core losses, and frequency dependence alter the actual input impedance.[^aac-transformer-impedance]

Worked example for an ideal device:

```text
Z_load = 8 kΩ
N_primary/N_secondary = 1/31.6
Z_primary = (1/31.6)^2 * 8000 Ω ≈ 8 Ω
```

Thus, an 8 kΩ load on the secondary side is reflected approximately as 8 Ω on the primary. This requires a turns ratio of around 1:31.6 rather than 1:1000: impedance changes as the square of the turns ratio.[^aac-transformer-impedance]

**Common mistakes:**
- multiplying impedance by the turns ratio only to the first power;
- inverting the ratio without specifying to which winding the load is being referred;
- considering the calculation exact for a real transformer across any frequency range.
