---
id: emb-elee-0180
title: "In what order is an assembled transformer power supply tested?"
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
  - source_id: libretexts-fiore-rectification
    title: "Fiore: Semiconductor Devices, 3.2 Rectification (Engineering LibreTexts)"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/03:_Diode_Applications/3.2:_Rectification
  - source_id: fiore-capacitors
    title: "Engineering LibreTexts: DC Electrical Circuit Analysis – A Practical Approach (Fiore), 8.2 Capacitance and Capacitors"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/DC_Electrical_Circuit_Analysis_-_A_Practical_Approach_(Fiore)/08:_Capacitors/8.2:_Capacitance_and_Capacitors
  - source_id: ti-lm340
    title: "TI: LM340, LM340A, LM7805 family wide VIN 1.5-A fixed voltage regulators (datasheet)"
    url: https://www.ti.com/lit/ds/symlink/lm340.pdf
  - source_id: openstax-rc-circuits
    title: "OpenStax University Physics Volume 2: 10.5 RC Circuits"
    url: https://openstax.org/books/university-physics-volume-2/pages/10-5-rc-circuits
---

## Short answer

First measure the secondary AC voltage unloaded without the regulator connected, then verify polarity and DC level across the bridge and filter capacitor, and only then connect the regulator and the design load. Before making any circuit changes, disconnect the AC source and verify that the filter capacitor is fully discharged.[^openstax-rc-circuits]

## Detailed explanation

The first step is measuring the AC voltage across the secondary winding before anything is connected to the rectifier. This verifies the transformer and the mains wiring without risking damage to the regulator, load, or filter capacitor: if the voltage is far from expected or near zero, the root cause is sought before the bridge rather than after it.

Next, the DC voltage level following the bridge rectifier and filter capacitor is verified. The load receives current during both half-cycles, and the peak voltage across the load equals the secondary peak voltage minus two diode forward drops.[^libretexts-fiore-rectification] With a filter capacitor under no-load conditions, the DC voltage approaches this peak value. For a 12 V RMS secondary winding, the peak is approximately `12 * 1.41 ≈ 17 V`. With a typical 0.7 V drop per silicon diode, one expects roughly `17 - 1.4 ≈ 15.6 V`. Polarity is checked at the same step: a polarized electrolytic capacitor installed backward can fail catastrophically.[^fiore-capacitors]

The voltage regulator is connected last, once the rectified DC level is confirmed. The LM340 datasheet specifies a 7.5 V input as required to maintain line regulation for a 5 V output,[^ti-lm340] with a 2 V dropout at 1 A being typical. Therefore, accounting for ripple troughs, the minimum voltage across the capacitor must remain at or above 7.5 V. If only 6 V is measured after the capacitor, the regulator cannot deliver 5 V, and this deficiency must be resolved before connecting the regulator rather than after.

Before modifying the circuit, power is disconnected; however, the capacitor does not lose its charge instantaneously: it discharges through circuit resistance, namely through the load or a bleeder resistor.[^openstax-rc-circuits] Therefore, the voltage across the capacitor must be verified with a meter rather than assuming it is discharged immediately after power-off.

**Common mistakes:**

- Connecting the regulator and load before verifying the DC voltage level and polarity across the filter capacitor.
- Assuming the capacitor is fully discharged immediately upon disconnecting mains power.
- Testing the regulator output without verifying that the input satisfies datasheet requirements: without adequate headroom, regulation fails.
