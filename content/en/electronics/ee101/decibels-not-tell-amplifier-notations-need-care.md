---
id: emb-elee-0102
title: "What do decibels not tell you about an amplifier, and which notations need care?"
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
  - source_id: aac-decibels
    title: "All About Circuits: Decibels for Voltage and Power Ratios"
    url: https://www.allaboutcircuits.com/textbook/designing-analog-chips/analog-measurements/db-for-voltage-add-power-ratios/
  - source_id: keysight-db-reference
    title: "Keysight U1271A/U1272A Handheld Digital Multimeter User's Guide"
    url: https://www.keysight.com/am/en/assets/9018-03364/user-manuals/9018-03364.pdf
---

## Short answer

Decibels describe gain magnitude rather than phase: a voltage gain of −10 has a magnitude of 10 (20 dB) but also implies a 180° phase inversion. The `dBV` notation designates a voltage level relative to 1 V. The `dBm` notation designates a power level relative to 1 mW, requiring a reference impedance to convert from a measured voltage.[^aac-decibels] [^keysight-db-reference]

## Detailed explanation

Decibels describe a logarithmic ratio of levels, but the sign of such a ratio does not encode phase. For voltage gain, `G_dB = 20*log10(|V_out/V_in|)` is used. If a stage has a gain factor of `-10`, its magnitude equals 10, so amplitude gain is `20 dB`; the minus sign indicates that the sinusoidal signal is inverted by 180°, not that the gain in dB is negative.[^aac-decibels]

This is important when cascading stages: decibel values allow adding gain magnitudes, but reconstructing the signal waveform and sign requires knowing the phase or polarity. Negative dB values indicate amplitude attenuation relative to a reference level, whereas inversion is a distinct phase property. For example, an inverting stage with a gain factor of `-10` provides `20 dB` in magnitude, even though the sinusoidal output is opposite in phase.[^aac-decibels]

Absolute levels also have different notations. `dBV` is a voltage level relative to 1 V RMS. `dBm` is a power level relative to 1 mW; when converting a measured voltage to dBm, an instrument must use a specified reference resistance. Therefore, a single number in dBm does not determine voltage without this resistance. Notations such as `dBv` should be checked against the documentation of the specific instrument or source rather than treated as a universal standard notation.[^keysight-db-reference]

**Common mistake:** Interpreting `-10` as a negative gain in dB, or drawing a conclusion about phase from a decibel value alone. This leads to a false prediction of the output signal level or waveform shape. Record the gain magnitude in dB and the phase/inversion separately; for absolute units, specify the reference level and, for dBm, the resistance used during measurement.[^aac-decibels] [^keysight-db-reference]
