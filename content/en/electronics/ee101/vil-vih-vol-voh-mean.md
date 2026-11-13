---
id: emb-elee-0234
title: "What do `V_IL`, `V_IH`, `V_OL` and `V_OH` mean?"
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

`V_IL` is the highest input voltage guaranteed to be recognized as logic 0, while `V_IH` is the lowest input voltage recognized as logic 1. `V_OL` is the maximum output voltage in logic state 0, and `V_OH` is the minimum output voltage in logic state 1.[^auburn-digital-voltages] These parameters are worst-case limits specified in the datasheet rather than nominal voltages.[^ti-hc00]

## Detailed explanation

These four parameters are the limits within which a logic family interprets signals. For inputs, `V_IL` and `V_IH` matter: a voltage below `V_IL` is read as 0, above `V_IH` as 1, and between them the result is undefined.[^auburn-digital-voltages] For outputs, `V_OL` and `V_OH` matter: an output in state 0 must deliver no more than `V_OL`, and in state 1 no less than `V_OH`.[^auburn-digital-voltages]

The output guarantees a voltage level that the receiving input will still interpret correctly, and the difference between them is the noise margin. For the HIGH level, this is written as `V_OH = V_IH + V_noise`: noise can shift the level by `V_noise` without changing the interpreted logic state.[^auburn-digital-voltages] For TTL, `V_OH = 2.4 V`, `V_IH = 2.0 V`, `V_IL = 0.8 V`, and `V_OL = 0.4 V`, giving a 0.4 V margin on both sides.[^auburn-digital-voltages]

These values depend on the logic family and supply voltage. For 74HC at 4.5 V, `V_OH` (min) = 4.4 V and `V_IH` (min) = 3.15 V yield a 1.25 V margin, which is significantly larger than TTL.[^ti-hc00] The parameter names are identical, but the numbers in the datasheet differ, so they must be taken from the specific device datasheet.

Output limits also depend on load current. For 74HC at 20 µA, `V_OL` (max) = 0.1 V, whereas at 4 mA it reaches up to 0.33 V across –40 to 85 °C.[^ti-hc00] A noise margin calculated from a single row of the datasheet table might not match the actual operating load.

**Common mistakes:**

- Confusing `V_IL` (max) with `V_OL` (max): the former belongs to the input, the latter to the output, and their difference defines the margin.
- Assuming that an output delivers exactly 0 V or `V_CC`: datasheets guarantee only limits.
- Using TTL thresholds (2.0 V and 0.8 V) for the HC family at 4.5 V, where `V_IH` (min) = 3.15 V.
