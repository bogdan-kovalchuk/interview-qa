---
id: emb-elee-0099
title: "What do dBm and dBV mean?"
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
  - source_id: rs-decibel-guide
    title: "Rohde & Schwarz: Radar and electronic warfare eGuide"
    url: https://www.allaboutcircuits.com/uploads/articles/Radar-and-electronic-warfare_eGuide-REVISED.pdf
---

## Short answer

`dBm` represents an absolute power level referenced to 1 mW, where 10 mW equals +10 dBm. `dBV` represents a voltage level referenced to 1 V, so for RMS measurements, 0.1 V equals −20 dBV and 1 V equals 0 dBV. Unlike these units, standard dB expresses only a relative ratio without an absolute reference.[^rs-decibel-guide]

## Detailed explanation

`dBm` and `dBV` define absolute levels because their names establish fixed reference quantities: 1 mW for power and 1 V for voltage. The calculations take the form `L_dBm = 10*log10(P/1 mW)` and `L_dBV = 20*log10(V_RMS/1 V)` for RMS voltage. A standard `dB` does not define an absolute quantity on its own: it merely compares two levels. Therefore, stating that 'a signal has 6 dB' is incomplete without the context of what reference that gain or attenuation is measured against.[^rs-decibel-guide]

For `dBm`, 0 dBm means 1 mW; a tenfold increase in power yields +10 dBm. Thus, 10 mW is +10 dBm, and 0.1 mW is −10 dBm. The conversion is based directly on power ratios and does not require assuming a specific impedance if the power is already known. If it is calculated from voltage, the load must be known: for a purely resistive `R`, `P = V_RMS^2/R` is used.[^rs-decibel-guide]

For `dBV`, the reference is 1 V regardless of impedance. A voltage of 1 V RMS equals 0 dBV, and 0.1 V RMS equals `20*log10(0.1) = −20 dBV`. The RMS specification is essential here for AC measurements: the peak voltage of a sine wave has a different numerical value than the RMS value, and it should not be substituted without conversion when an instrument scale or specification defines RMS. Furthermore, `dBV` should not be confused with `dBm`: one scale describes voltage, while the other describes power.[^rs-decibel-guide]

**Common mistakes:**

- Treating dB as an absolute unit without specifying a reference level.
- Believing that 0 dBm equals 0 mW; it is a 1 mW level.
- Calculating power in dBm solely from voltage without load data.
- Confusing RMS and peak voltage when calculating dBV.[^rs-decibel-guide]
