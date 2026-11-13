---
id: emb-elee-0100
title: "One stage halves the voltage and the next amplifies it 10 times. What is the total gain in dB?"
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

The first stage has a voltage gain of 0.5 (−6.02 dB) and the second has a gain of 10 (+20 dB), yielding a net gain of 5 or +13.98 dB. In cascaded stages, voltage gain factors multiply while their decibel values add together.[^aac-decibels]

## Detailed explanation

The decibel is a logarithmic way to express the ratio of two power levels; for a voltage ratio across equal input and output resistances, `G_dB = 20*log10(V_out/V_in)` is used. The inverse conversion yields `V_out/V_in = 10^(G_dB/20)`. Due to the logarithm, multiplying the gain factors of cascaded stages turns into adding their values in dB.[^aac-decibels]

In the first stage, the ratio of output voltage to input voltage equals `0.5`, so `20*log10(0.5) ≈ -6.02 dB`. For the second stage, the ratio equals `10`, giving `20*log10(10) = 20 dB`. These are voltage gain factors; the fact that the second stage 'amplifies' does not cancel out the attenuation of the first: both factors must be accounted for.[^aac-decibels]

Calculation example:

```text
V_total/V_in = 0.5*10 = 5
G_total = 20*log10(5) ≈ 13.98 dB
G_total = -6.02 dB + 20 dB = 13.98 dB
```

Thus, the cascaded stages together provide a fivefold increase in voltage, or approximately `13.98 dB`. The result in dB is calculated as a voltage ratio across equal resistances; if the resistances differ, this figure does not by itself determine the power gain. A common mistake is adding 0.5 to 10 or adding the absolute values of both changes in dB. One must multiply the linear gain factors or add their signed values in dB.[^aac-decibels]

Rounding to the nearest hundredth is sufficient for these given integer factors; measured stages may deviate from them due to loading and component tolerances.
