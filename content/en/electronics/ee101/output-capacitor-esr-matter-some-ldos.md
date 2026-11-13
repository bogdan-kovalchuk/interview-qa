---
id: emb-elee-0170
title: "Why does the output capacitor's ESR matter for some LDOs?"
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
  - source_id: ti-slva115
    title: "Texas Instruments SLVA115A: ESR, Stability, and the LDO Regulator"
    url: https://www.ti.com/lit/an/slva115/slva115.pdf
  - source_id: ti-tps752q1-datasheet
    title: "Texas Instruments TPS752-Q1 datasheet"
    url: https://www.ti.com/lit/ds/symlink/tps752-q1.pdf
  - source_id: ti-slva079
    title: "Texas Instruments SLVA079: Understanding the Terms and Definitions of LDO Voltage Regulators"
    url: https://www.ti.com/lit/an/slva079/slva079.pdf
---

## Short answer

In an LDO with a `PMOS` or `PNP` pass element, the output capacitor's ESR introduces a zero that compensates for poles in the feedback loop, so the datasheet specifies an allowable ESR range and a minimum capacitance.[^ti-slva115][^ti-tps752q1-datasheet] An ESR that is too low (such as in ceramic capacitors) can leave the loop uncompensated, while an excessively high ESR can disrupt it at high frequencies; both cases risk instability. A high ESR also increases voltage sag during a load current step.[^ti-tps752q1-datasheet]

## Detailed explanation

An LDO is a closed-loop system: an error amplifier compares the output against a voltage reference and controls the pass element, while the output capacitor and the load form an integral part of this feedback loop. In an LDO with a PMOS or PNP pass element, the open-loop response has three significant poles: the dominant pole (inside the error amplifier), the load pole (determined by the output capacitor and load resistance, meaning it shifts with load current), and the pass-element pole (caused by the parasitic capacitance of the pass element). Three poles combined with high loop gain without compensation do not provide sufficient phase margin, and the most straightforward source of compensation is the zero created by the capacitor's ESR, which the LDO requires in any case.[^ti-slva115]

The frequency of this zero is `f_Z = 1/(2*pi*ESR*C_out)`. The ESR must be large enough to place the zero low enough so that the Bode magnitude slope at the 0 dB crossover becomes –20 dB/dec rather than –40 dB/dec, yet small enough that loop gain drops below 0 dB before reaching the pass-element pole.[^ti-slva115] For `C_out = 2.2 µF` and `ESR = 1 Ω`, `f_Z ≈ 72 kHz`, whereas for a ceramic capacitor with `ESR = 10 mΩ`, `f_Z ≈ 7.2 MHz`, which is 100 times higher. Where the unity-gain frequency of a specific loop falls depends on the IC; thus, in the latter case the zero is likely too high in frequency to alter the loop slope at crossover.

Consequently, datasheets specify not only a minimum capacitance but also an acceptable ESR range. For the TPS752-Q1, this is at least 47 µF with an ESR of 100 mΩ to 10 Ω, where ESR denotes total series resistance including external resistors and PCB trace resistance to the capacitor.[^ti-tps752q1-datasheet] In application note SLVA079, this sum is termed compensation series resistance, `CSR = R_ESR + R_add`, and its stable operating boundary is plotted against load current (the "tunnel of death"); if the capacitor ESR is too low, an external series resistor is added.[^ti-slva079] In SLVA115, a TPS76050 with a 2.2 µF ceramic capacitor exhibits pronounced ringing following a load step, whereas adding a 1 Ω resistor renders the transient response stable; the minimum ESR over frequency is used in such plots because ESR varies with frequency.[^ti-slva115]

There is also a trade-off. At the instant of a load current step, the LDO loop cannot react immediately, and the capacitor supplies the transient current; this current produces a voltage drop across its ESR of `V_ESR = I*ESR`, meaning higher ESR results in a larger initial voltage sag.[^ti-tps752q1-datasheet] For a 0.5 A step, this is 0.5 V with `ESR = 1 Ω`, but only 5 mV with `ESR = 10 mΩ`. Modern LDOs are designed to be stable with ceramic capacitors without requiring supplemental ESR, so the ESR window generally does not constrain capacitor selection for newer parts, but this must be verified in the specific IC datasheet rather than assumed.[^ti-slva115]

**Common mistakes:**

- Replacing a tantalum or electrolytic capacitor with a ceramic capacitor of equal capacitance on an older LDO type without verifying ESR stability requirements.[^ti-slva115]
- Assuming that lower ESR is always better: in such LDOs, ESR has a strict lower bound.[^ti-tps752q1-datasheet]
- Failing to account for trace resistance and external resistors as part of the datasheet ESR specification, evaluating stability based solely on capacitor nominal ratings.[^ti-tps752q1-datasheet]
- Assuming stability without verifying transient response: repeated ringing after a load step indicates insufficient phase margin.[^ti-slva115]
