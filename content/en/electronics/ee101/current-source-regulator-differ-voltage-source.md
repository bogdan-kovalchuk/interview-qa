---
id: emb-elee-0223
title: "How does a current source (regulator) differ from a voltage source?"
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
  - source_id: fiore-source-conversions
    title: "Engineering LibreTexts: DC Electrical Circuit Analysis – A Practical Approach (Fiore), 6.2 Source Conversions"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/DC_Electrical_Circuit_Analysis_-_A_Practical_Approach_(Fiore)/06:_Analysis_Theorems_and_Techniques/6.2:_Source_Conversions
---

## Short answer

A voltage source maintains a constant output voltage `V_out` despite variations in load current, up to its maximum current capability.[^fiore-source-conversions] A current source maintains a constant load current `I_load` despite variations in load voltage drop, up to its compliance voltage limit.[^fiore-source-conversions]

## Detailed explanation

An ideal voltage source delivers a specified voltage regardless of what is connected to it, so the current is determined by the load according to Ohm's law. Conversely, an ideal current source always delivers the same current regardless of the load, while the voltage across the load is determined by the circuit itself.[^fiore-source-conversions] Hence the difference: when load resistance changes, a voltage source varies its current, whereas a current source varies its voltage.

Example. A 5 V voltage source: with a 100 Ω load, the current is `5 / 100 = 50 mA`; with 1 kΩ, it is `5 / 1000 = 5 mA`, while the voltage remains 5 V. A 10 mA current source: with 100 Ω, the voltage is `10 mA * 100 Ω = 1 V`; with 1 kΩ, it is `10 mA * 1000 Ω = 10 V`, while the current remains 10 mA. Here the limit is apparent: to maintain 10 mA across 1 kΩ, the source must output 10 V, so with a 9 V supply, maintaining a stable current is not possible.

Real sources are modeled by their internal resistance: for a voltage source, it is connected in series (ideally 0 Ω), whereas for a current source, it is connected in parallel (ideally infinite), limiting open-circuit voltage.[^fiore-source-conversions] In an active low-voltage electronic current source, an open output clamps at its supply/compliance voltage limit, whereas in an ideal current source or high-energy inductive circuits such as current transformers, opening the circuit drives voltage dangerously high until air or insulation breaks down.[^fiore-source-conversions]

**Common mistakes:**

- Believing that a current source maintains current at any voltage: the compliance voltage limit determines when regulation is lost.
- Leaving the output of a current source open: the voltage rises to dangerous levels.
- Shorting the output of a voltage source without calculating the current: the current equals `E / R`, where `R` is the internal resistance of the source.
