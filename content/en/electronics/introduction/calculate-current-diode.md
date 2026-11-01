---
id: emb-elintro-0167
title: "Calculate the current: V = 9 V, R = 330 Ω, Si diode (`V_f` = 0.7 V)?"
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
---


## Short answer

Assuming `V_f = 0.7 V`, the resistor will have `V_R = 9 V - 0.7 V = 8.3 V`, so the current is `I = V_R/R = 8.3 V/330 Ω ≈ 25 mA`. This is an estimate for the given model; the actual `V_f` depends on current and the specific diode, so check the datasheet for a more precise calculation.[^aac-direct-current]

## Detailed explanation

The current in a series circuit of a source, a resistor, and a diode is determined using Ohm's law and Kirchhoff's voltage law. The problem statement specifies a 9 V source and a 330 Ω resistor, and the value `V_f = 0.7 V` is an accepted approximation for a forward-biased silicon diode, rather than an exact constant for all currents.[^aac-direct-current] [^aac-semiconductors]

First, the source voltage is divided between the diode and the resistor. If the diode has 0.7 V in this model, the remaining difference across the resistor is 8.3 V. Because the components are connected in series, the same current flows through the diode and the resistor; the resistance of the resistor sets the primary current limitation.[^aac-direct-current]

Worked example for an ideal 9 V source, a 330 Ω resistor, and a fixed diode drop of 0.7 V:

```text
V_R = 9 V - 0.7 V = 8.3 V
I = 8.3 V / 330 Ω = 0.02515 A ≈ 25 mA
```

The answer of approximately 25 mA is an approximation, rather than an exact prediction for a real component. In a real diode, `V_f` varies with current and temperature; after an initial estimate, you can check the operating point against a datasheet graph or table and recalculate the current.[^aac-semiconductors]

A common mistake is dividing the entire 9 V by 330 Ω and getting approximately 27 mA, ignoring the voltage drop across the diode. Another mistake is assuming 0.7 V is a guaranteed value in any mode; this is a simplification suitable for estimation, but the maximum current and power rating of the resistor must also be checked.[^aac-direct-current]
