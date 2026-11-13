---
id: emb-elee-0233
title: "What do logic 0 and 1 really mean in a digital circuit?"
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
  - source_id: auburn-digital-voltages
    title: "Auburn University ELEC 3040/3050: Digital system voltages/currents and reading component data sheets (lab lecture notes)"
    url: https://www.eng.auburn.edu/~nelson/courses/elec3040_3050/LabLectures/DigitalElectricalQuantities_ARM.pdf
  - source_id: ti-hc00
    title: "TI SN74HC00 quadruple NAND gates datasheet"
    url: https://www.ti.com/lit/ds/symlink/sn74hc00.pdf
---

## Short answer

Logic 0 and 1 are voltage ranges rather than exact numbers: an input recognizes LOW up to `V_IL` (maximum) and HIGH from `V_IH` (minimum), while voltages between them produce an undefined state.[^auburn-digital-voltages] Half of the supply voltage is not the threshold: for 74HC at `V_CC = 4.5 V`, the input limits are 1.35 V and 3.15 V, so 2.25 V falls entirely in the undefined region.[^ti-hc00]

## Detailed explanation

A logic value is an interpretation of the voltage at a pin, not the voltage itself. A device interprets input voltage using thresholds: `V_IL` is the highest voltage it recognizes as 0, and `V_IH` is the lowest voltage it recognizes as 1. Voltages between them are not interpreted unambiguously.[^auburn-digital-voltages] An output is defined by different boundaries: `V_OL` is the maximum voltage in state 0, and `V_OH` is the minimum voltage in state 1.[^auburn-digital-voltages]

**Example:** for the 74HC00 at `V_CC = 4.5 V`, the datasheet specifies `V_IL` (max) = 1.35 V and `V_IH` (min) = 3.15 V. For the output, it specifies `V_OL` (max) = 0.1 V and `V_OH` (min) = 4.4 V at a current of 20 µA.[^ti-hc00] A voltage of 2.25 V, which is half of the supply, lies entirely inside the undefined region, so the threshold cannot be assumed to be half of `V_CC`. Noise margin is defined as `V_OH - V_IH` for HIGH and `V_IL - V_OL` for LOW.[^auburn-digital-voltages] For 74HC at 4.5 V, this is `4.4 - 3.15 = 1.25 V` and `1.35 - 0.1 = 1.25 V`.[^ti-hc00]

These numbers apply under specified test conditions. Output levels depend on load current: at 4 mA, `V_OL` (max) reaches 0.33 V across the range from –40 to 85 °C.[^ti-hc00] Thresholds also depend on the logic family: standard TTL has `V_IH = 2.0 V` and `V_IL = 0.8 V`, and values between 0.8 and 2.0 V produce unpredictable results.[^auburn-digital-voltages] Therefore, logic levels must be taken from the datasheet for the specific family and supply voltage.

**Common mistakes:**

- Assuming that 0 is exactly 0 V and 1 is exactly `V_CC`: only the limits `V_IL`, `V_IH`, `V_OL`, and `V_OH` are guaranteed.
- Placing the threshold at half of the supply voltage: for 74HC at 4.5 V, that is 2.25 V, which falls in the undefined zone.
- Leaving an input floating or supplying a signal that transitions very slowly through the region between thresholds.
