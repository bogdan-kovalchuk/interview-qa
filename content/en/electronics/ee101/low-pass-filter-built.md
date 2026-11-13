---
id: emb-elee-0114
title: "How is an RL low-pass filter built?"
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
  - source_id: aac-low-pass-filters
    title: "All About Circuits: Low-pass Filters"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-8/low-pass-filters/
---

## Short answer

In an RL low-pass filter, the inductor is connected in series with the input, and the load resistor is connected between the output node and common ground; the output is taken across the resistor. At high frequencies, the inductive impedance increases, so the fraction of voltage across the load drops.[^aac-low-pass-filters]

## Detailed explanation

A passive RL low-pass filter is formed by an inductor in series with the input and a resistive load connected from the output node to common ground. The output voltage is measured across the load resistor. At low frequencies, an ideal inductor has low inductive reactance, so the signal appears predominantly across the load. As frequency increases, the inductor's impedance `X_L = 2π*f*L` increases, so a larger fraction of the input voltage drops across it, and the output decreases.[^aac-low-pass-filters]

For an ideal source with zero output resistance and a resistive load, the pole is given by `f_c = R/(2π*L)`. Here R is precisely the resistance seen by the inductor; if there is additional loading or source resistance, the equivalent circuit may alter the calculation. At the cutoff frequency, the output magnitude equals `1/sqrt(2)` of the low-frequency level, or approximately 70.7 percent.[^aac-low-pass-filters]

Calculation example: with `L = 10 mH` and `R = 1 kΩ`, the ideal model gives `f_c = 1000/(2π*0.01) ≈ 15.9 kHz`. Well below this frequency, the voltage across R is close to the input; well above it, the signal rolls off roughly in inverse proportion to frequency for a single-pole filter. This calculation assumes a sinusoidal steady state and is not a guarantee of a specific component's performance.[^aac-low-pass-filters]

A practical inductor has winding resistance, parasitic capacitance, and possible core losses. These can cause insertion loss even at low frequencies and alter behavior near self-resonance. Therefore, while the circuit ideally explains the topology, a real design requires verifying the DC resistance, current rating, core saturation, and frequency limits of the inductor using the component's datasheet.[^aac-low-pass-filters]
