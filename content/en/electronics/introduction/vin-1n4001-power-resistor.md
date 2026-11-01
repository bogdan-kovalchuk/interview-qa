---
id: emb-elintro-0192
title: "`V_in` = 12 V, R = 100 Ω, 1N4001. What is the power in the resistor?"
track: electronics
section: introduction
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-direct-current
    title: "All About Circuits textbook, Volume I: DC"
    url: https://www.allaboutcircuits.com/textbook/direct-current/
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
  - source_id: onsemi-1n4001-datasheet
    title: "onsemi: 1N4001–1N4007 Axial-Lead Glass Passivated Standard Recovery Rectifiers"
    url: https://www.onsemi.com/pdf/datasheet/1n4001-d.pdf
---

## Short answer

Using the 0.7 V forward-biased diode approximation, the current is `(12 V - 0.7 V)/100 Ω ≈ 113 mA`, and the power dissipated by the resistor is `I²*R ≈ 1.28 W`. This calculated operating condition exceeds the rating of a 0.25 W resistor; a practical rating must be chosen considering temperature derating and thermal mounting.[^aac-direct-current] [^aac-semiconductors]

## Detailed explanation

In this series circuit, the current through the resistor and diode is identical. For an initial estimate, take a silicon diode with a forward drop of around `0.7 V`; then `12 V - 0.7 V = 11.3 V` remains across the resistor, and by Ohm's law the current equals `11.3 V/100 Ω = 0.113 A`.[^aac-direct-current] [^aac-semiconductors]

The resistor power can be found as the product of the voltage across it and the current, or as `P = I²*R`. For the given approximation, this is `0.113²*100 ≈ 1.28 W`. Therefore, a `0.25 W` resistor is not suitable: it would dissipate more than five times its rated power. A `2 W` rating exceeds the calculated value, but the required margin is determined by ambient temperature, ventilation, PCB mounting, and manufacturer derating rules; it is not an automatic guarantee for every package.[^aac-direct-current]

The `0.7 V` drop is an approximate model, not a fixed property of the 1N4001. The onsemi datasheet specifies a maximum of `1.1 V` at `1 A`; this cannot be transferred as an exact value at `113 mA`, so the precise current requires the diode characteristic under matching conditions. This difference slightly alters the result, but does not change the conclusion that a 0.25 W resistor is insufficient.[^onsemi-1n4001-datasheet]

Worked example for the model `V_F = 0.7 V`:

```text
I = (12 V - 0.7 V)/100 Ω = 0.113 A
P_R = I²*R = 0.113²*100 Ω ≈ 1.28 W
```

**Common mistake:** calculating `12²/100 = 1.44 W` as if all 12 V dropped across the resistor. Part of the voltage falls across the diode; at the same time, the datasheet maximum diode drop should not be assumed as its typical exact drop in this circuit.[^aac-direct-current] [^onsemi-1n4001-datasheet]
