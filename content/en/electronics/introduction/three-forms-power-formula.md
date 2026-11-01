---
id: emb-elintro-0090
title: "What are the three forms of the power formula?"
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
  - source_id: aac-power
    title: "All About Circuits: Calculating Electric Power"
    url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-2/calculating-electric-power/
---

## Short answer

For a resistive load, power can be calculated in three equivalent ways: `P = V*I`, `P = I²*R`, or `P = V²/R`. Choose the form based on which quantities are known; the latter two are derived from `P = V*I` and Ohm's law.[^aac-power]

## Detailed explanation

Electric power indicates the rate at which energy is transferred or converted. For instantaneous quantities, the fundamental relationship is `p = v*i`; in a simple DC resistive circuit, it is used as `P = V*I`. The unit of power is the watt, where `1 W = 1 J/s`.[^aac-power]

If the load is a resistor, Ohm's law allows current or voltage to be substituted into the power formula. Substituting `I = V/R` leads to `P = V²/R`, and substituting `V = I*R` leads to `P = I²*R`. These are not three distinct laws, but three forms applicable under the same resistive model. For alternating current, in the general case you cannot simply multiply arbitrary RMS voltage and current: the phase shift and waveform shape are also essential in the real power formula.[^aac-power]

**Worked example:** a `1 kΩ` resistor is connected to `5 V DC`. The current is `5 mA`, so the power is `P = 5 V*5 mA = 25 mW`; the same result is given by `P = 5²/1000 = 0.025 W`. When evaluating heating, compare the calculation to the power rating of the resistor and account for cooling conditions.[^aac-power]

**Common mistake:** squaring the resistance or confusing the formulas. You multiply the square of the current by resistance, and divide the square of the voltage by resistance; checking the units helps catch the error before component selection.[^aac-power]
