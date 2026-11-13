---
id: emb-elee-0221
title: "Why is the typical active-mode β not used for a switch, and which motor current matters for component selection?"
track: electronics
section: ee101
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-alternating-current
    title: "All About Circuits textbook, Volume II: AC"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
  - source_id: rohm-bjt-basics
    title: "ROHM: Bipolar Junction Transistor (BJT) Basics: Operation and Applications (NPN & PNP)"
    url: https://techweb.rohm.com/product/transistors-diodes/transistors/27319/
  - source_id: fiore-bjt-basics
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 4.2 The Bipolar Junction Transistor"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/04:_Bipolar_Junction_Transistors_(BJTs)/4.2:_The_Bipolar_Junction_Transistor
  - source_id: mit-6071-bjt-notes
    title: "MIT OCW 6.071/22.071 (Spring 2006): Transistors: Bipolar Junction Transistors (BJT), lecture notes"
    url: https://ocw.mit.edu/courses/6-071j-introduction-to-electronics-signals-and-measurement-spring-2006/b30aa58fb0c9915da21e5a5855384818_19_bjt_1.pdf
  - source_id: ti-drv8231a
    title: "Texas Instruments DRV8231A: 3.7-A Brushed DC Motor Driver datasheet"
    url: https://www.ti.com/lit/ds/symlink/drv8231a.pdf
  - source_id: ti-tida00786
    title: "Texas Instruments TIDA-00786: Ultra Small Brushed DC Motor Current Regulation (reference design)"
    url: https://www.ti.com/lit/ug/tiduay8/tiduay8.pdf
---

## Short answer

To guarantee saturation, base current is designed using a forced gain `β_forced` (typically 10) below the datasheet minimum `h_FE`, because effective current gain drops sharply in saturation and active-mode β does not apply.[^rohm-bjt-basics] During startup and stall conditions, a motor draws high stall current.[^ti-drv8231a] The transistor, flyback diode, and power supply must therefore be sized for peak stall and inrush current rather than steady-state running current alone.

## Detailed explanation

The typical active-mode β gives `I_C = β * I_B`, but for a switch this is not the operating mode. In saturation, the relationship between `I_C` and `I_B` becomes nonlinear.[^mit-6071-bjt-notes] In this mode, the collector current is determined by the load and the power supply.[^rohm-bjt-basics] Effective gain drops noticeably during such switching, so `β_forced` is specified with a safety margin.[^rohm-bjt-basics] For a small-signal transistor, typical β is 100–200; for a power transistor, it is 25–50.[^fiore-bjt-basics] If β = 100 is used for a 100 mA switch, `I_B = 100 mA / 100 = 1 mA`. For `β_forced = 10`, 10 mA is required, so the base current would be underestimated by a factor of ten, and the transistor might fail to saturate.

Inrush current is critical precisely at the start of motion. When the motor rotates, the back EMF is subtracted from the supply voltage, and the current equals `(V - E) / R`, where `R` is the winding resistance.[^ti-tida00786] While the rotor is stationary, there is no back EMF, and the initial current is estimated as `V / R`.[^ti-tida00786] For illustration, assume a 10 Ω winding and a 5 V supply. A running current of 100 mA means a back EMF of 4 V: `(5 - 4) / 10 = 0.1 A`. With a stalled rotor, the current is `5 / 10 = 0.5 A`, which is five times higher than the running current.

Therefore, the transistor is sized for 0.5 A, the recirculation diode is sized for the same current, and to saturate at `β_forced = 10`, the base current must be 50 mA: `R_B = (5 - 0.8) / 0.05 = 84 Ω`. If the driver delivers only 10 mA, there is not enough base current for 0.5 A: 50 mA is required. The `V / R` estimate is an upper bound rather than a measured value: the motor begins to rotate before the current reaches `V / R`, so the actual inrush current drawn from the source is lower.[^ti-tida00786]

**Common mistakes:**

- Selecting the transistor, diode, and power supply based on the 100 mA running current without checking the inrush or stall current.
- Calculating base current using the typical active-mode β: with β = 100, the result is 1 mA, and the transistor may not saturate.
- Taking `V / R` as the exact inrush current value, even though it is an upper bound.
