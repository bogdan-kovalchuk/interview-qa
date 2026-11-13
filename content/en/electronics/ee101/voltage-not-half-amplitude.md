---
id: emb-elee-0101
title: "Why is −3 dB in voltage not half the amplitude?"
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
---

## Short answer

A −3 dB voltage ratio corresponds to `10^(-3/20) ≈ 0.708`, which is approximately 70.8% rather than half. Halving the voltage corresponds to roughly −6.02 dB. Halving the power corresponds to −3 dB when impedances are equal.[^aac-decibels]

## Detailed explanation

The decibel value for a voltage ratio is calculated using the formula `G_dB = 20*log10(V_out/V_in)`. Therefore, −3 dB yields `V_out/V_in = 10^(-3/20) ≈ 0.708`: the output amplitude is about 70.8% of the input, not 50%. The voltage formula relies on equal resistances; only then does the power ratio equal the square of the voltage ratio.[^aac-decibels]

The figure of 3 dB originates from power: `10*log10(0.5) ≈ -3.01 dB`, representing half power. When resistances are equal, power is proportional to the square of voltage, so half power corresponds to a voltage of `sqrt(0.5) ≈ 0.707` of the initial value. For half voltage, the calculation is different: `20*log10(0.5) ≈ -6.02 dB`.[^aac-decibels]

Example for a signal with an initial amplitude of 2 V: after an attenuation of 3 dB, the amplitude will be approximately `2*0.708 = 1.416 V`, not 1 V. If the source and load have equal resistances, the signal power will be approximately half of its initial value.[^aac-decibels]

**Common mistake:** Interpreting 'half power' as 'half voltage'. This manifests as measuring −6 dB instead of −3 dB for the cutoff point of a simple RC filter. To avoid this, first determine whether you are comparing voltage, current, or power, and for voltage ratios, verify whether resistances are equal across both measurements.[^aac-decibels]
