---
id: emb-elee-0152
title: "How does filtering differ from voltage regulation?"
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
  - source_id: fiore-rectification
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 3.2 Rectification"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/03:_Diode_Applications/3.2:_Rectification
  - source_id: fiore-capacitors
    title: "Engineering LibreTexts: DC Electrical Circuit Analysis – A Practical Approach (Fiore), 8.2 Capacitance and Capacitors"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/DC_Electrical_Circuit_Analysis_-_A_Practical_Approach_(Fiore)/08:_Capacitors/8.2:_Capacitance_and_Capacitors
  - source_id: ti-slva079
    title: "Texas Instruments SLVA079: Understanding the Terms and Definitions of LDO Voltage Regulators"
    url: https://www.ti.com/lit/an/slva079/slva079.pdf
---

## Short answer

Filtering smoothes rectified voltage by reducing the AC ripple component, though DC output still sags as load current increases.[^fiore-rectification] Voltage regulation actively maintains a stable output level across changing input voltages and load currents while suppressing input ripple via power supply rejection (PSRR).[^ti-slva079]

## Detailed explanation

A filter and a voltage regulator serve different purposes, even though both make voltage "smoother". After a rectifier, the voltage pulses because the capacitor delivers charge to the load between peaks and then recharges; this AC component riding on a DC level constitutes ripple.[^fiore-rectification] A filter (most commonly a capacitor in parallel with the load) reduces this AC component. However, it does not fix the DC voltage level: under light load, the output stays near the peak secondary voltage, whereas as load current increases, ripple grows and the average DC level sags.[^fiore-rectification] Furthermore, secondary peaks are proportional to line voltage, so the post-filter voltage also tracks mains fluctuations.

The ripple estimate for a bridge rectifier is `ΔV_pp ≈ I/(f_ripple*C)`, which follows from `ΔV = I*Δt/C`.[^fiore-capacitors] For `C = 1000 µF` and `f_ripple = 100 Hz`, a 20 mA load current produces `0.02/(100*0.001) = 0.2 V`, whereas 100 mA yields `0.1/(100*0.001) = 1.0 V`. Thus, load current alone changes ripple fivefold, and that same current variation shifts the average output voltage downward.

A regulator operates on a different principle: it compares the output against a reference and modulates a pass element, making the output virtually independent of input variations and load current. This performance is quantified by two standard parameters: line regulation `ΔV_out/ΔV_in` (output response to input voltage changes) and load regulation `ΔV_out/ΔI_out` (output response to load current changes).[^ti-slva079] Secondarily, a regulator also suppresses ripple: PSRR is the ratio of output ripple to input ripple, and it depends on frequency.[^ti-slva079] For instance, if PSRR is -60 dB at the ripple frequency (an illustrative number), then `10^(-60/20) = 0.001`, and 1 V of input ripple becomes roughly 1 mV at the output.

This dictates the sequence and interdependence of these blocks. A regulator does not eliminate the need for a filter: the lowest trough of the ripple at its input must remain above `V_out` plus dropout, where dropout is the input-to-output headroom at which the circuit loses regulation.[^ti-slva079] Conversely, a filter without a regulator does not deliver a constant voltage: the output drifts with line and load changes. Therefore, in a typical power supply, the rectifier and filter capacitor precede the voltage regulator.

**Common mistakes:**

- Assuming that a large capacitor "regulates" voltage: it reduces ripple, but does not fix the average DC level.
- Confusing ripple with line regulation: ripple is a fast AC component at line frequency, whereas line regulation is the steady-state output shift resulting from input voltage changes.
- Expecting flawless ripple rejection from a regulator without verifying its PSRR at the ripple frequency and ensuring adequate dropout margin.
