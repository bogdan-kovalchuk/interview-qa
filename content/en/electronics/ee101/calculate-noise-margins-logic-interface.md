---
id: emb-elee-0235
title: "How do you calculate the noise margins of a logic interface?"
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
  - source_id: ti-szza036c
    title: "TI SZZA036C: Understanding and Interpreting Standard-Logic Data Sheets"
    url: https://www.ti.com/lit/an/szza036c/szza036c.pdf
  - source_id: ti-hc00
    title: "TI SN74HC00 quadruple NAND gates datasheet"
    url: https://www.ti.com/lit/ds/symlink/sn74hc00.pdf
  - source_id: ti-sn74ls00
    title: "TI SDLS025D: SNx400, SNx4LS00, SNx4S00 quadruple 2-input NAND gates datasheet"
    url: https://www.ti.com/lit/ds/symlink/sn74ls00.pdf
---

## Short answer

Noise margins are defined as `NM_L = V_IL,max - V_OL,max` and `NM_H = V_OH,min - V_IH,min` for LOW and HIGH levels, respectively.[^ti-szza036c] A positive margin indicates that the guaranteed driver output maintains a safety margin before reaching the input voltage limit of the receiving gate.

## Detailed explanation

The output of a logic gate does not deliver ideal zeros and ones: the manufacturer guarantees only worst-case boundary levels. For the output, these are `V_OL,max` and `V_OH,min`; for the input of the downstream stage, they are `V_IL,max` and `V_IH,min`.[^ti-szza036c] The noise margin is the gap between them: noise adding voltage to the signal will not alter the logical state as long as the signal does not cross the input threshold. LOW and HIGH noise margins are calculated separately because they are not necessarily equal.

Example with the 74HC00 at `V_CC = 4.5 V` (values for `V_OH` and `V_OL` at 25 °C): `V_IH,min = 3.15 V`, `V_IL,max = 1.35 V`.[^ti-hc00] Under light load (20 µA), `V_OL,max = 0.1 V` and `V_OH,min = 4.4 V`, so `NM_L = 1.35 - 0.1 = 1.25 V` and `NM_H = 4.4 - 3.15 = 1.25 V`. At a current of 4 mA, the same datasheet gives `V_OL,max = 0.26 V` and `V_OH,min = 3.98 V`,[^ti-hc00] so `NM_L = 1.35 - 0.26 = 1.09 V` and `NM_H = 3.98 - 3.15 = 0.83 V`. The smaller of the two margins, 0.83 V, governs overall noise immunity: output loading degrades the HIGH-level margin most significantly.

By comparison, the 7400 TTL series guarantees `V_OH,min = 2.4 V` and `V_OL,max = 0.4 V`, while its inputs recognize `V_IH,min = 2 V` and `V_IL,max = 0.8 V`.[^ti-sn74ls00] Then `NM_H = 2.4 - 2.0 = 0.4 V` and `NM_L = 0.8 - 0.4 = 0.4 V`. The test conditions differ here (`V_OL = 0.4 V` applies at a current of 16 mA), so a direct comparison with CMOS is approximate, but the 0.4 V margin in TTL is substantially lower than the 0.83–1.25 V of the 74HC00.

Noise margin is a static concept: it describes DC levels and does not account for transient spikes, ringing after edge transitions, or simultaneous switching noise. The datasheet figures hold only under test conditions (supply voltage, temperature, current), so they cannot be applied to a different `V_CC` or different load current without consulting the tables.

**Common mistakes:**

- Using typical (TYP) values instead of guaranteed MIN and MAX specifications.
- Calculating only one margin and assuming the device is robust, even though the other margin may be much smaller.
- Ignoring load conditions: `V_OH` and `V_OL` are specified for particular currents, and they differ at other current levels.[^ti-hc00]
