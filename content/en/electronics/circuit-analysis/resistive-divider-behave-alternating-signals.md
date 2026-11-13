---
id: emb-elcirc-0033
title: "How does a resistive divider behave with alternating (AC) signals?"
track: electronics
section: circuit-analysis
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-direct-current
    title: "All About Circuits textbook, Volume I: DC"
    url: https://www.allaboutcircuits.com/textbook/direct-current/
  - source_id: aac-voltage-divider
    title: "All About Circuits: Voltage Divider Circuits"
    url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-6/voltage-divider-circuits/
  - source_id: adi-frequency-divider
    title: "Analog Devices: Frequency Compensated Voltage Dividers"
    url: https://ez.analog.com/adiacademy/university-program/a/studentzone-articles/SA1045/adalm1000-smu-training-topic-11-frequency-compensated-voltage-dividers
---

## Short answer

In an ideal circuit consisting only of resistors, the division ratio for an AC signal is independent of frequency. In a real circuit, parasitic capacitance from the load and layout can make transmission frequency-dependent; there is no universal cutoff such as tens of MHz.[^adi-frequency-divider]

## Detailed explanation

An ideal resistor has no reactive impedance component, so in an ideal two-resistor circuit, the ratio of output to input voltage for a sinusoidal signal is the same as for a DC voltage. For an unloaded circuit, it is given by `R_2/(R_1+R_2)`.[^adi-frequency-divider]

A practical circuit does not consist solely of ideal resistors. The input of a subsequent stage often exhibits capacitance; together with the divider's output resistance, it forms an RC network. Parasitic capacitance affects the frequency response, and its impact depends on the specific components and load rather than having a universal cutoff in MHz.[^adi-frequency-divider]

Example:

If the divider's output resistance together with the load input capacitance form equivalent `R` and `C` values, the characteristic time scale is given by `τ = R*C`, and the pole frequency for a simple RC stage is `f_c = 1/(2π*R*C)`. This is an approximation for a single-pole model rather than an off-the-shelf estimate for every board.[^adi-frequency-divider]

**Common mistakes:**

- Applying the DC formula to a real AC circuit without verifying the source and load impedances.
- Stating a fixed frequency, such as tens of MHz, as a universal limit for all dividers: the cutoff is determined by their circuit parameters and layout.
