---
id: emb-elintro-0102
title: "Find I, V_R1, and V_R2 for R_1 = 100 Ω, R_2 = 330 Ω, and a 3 V source?"
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
  - source_id: aac-series-circuits
    title: "All About Circuits: Series Circuits and the Application of Ohm’s Law"
    url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-5/simple-series-circuits/
---

## Short answer

For an ideal 3 V source and series resistors of 100 Ω and 330 Ω, the total resistance equals `R_total = 430 Ω`, and the current is `I = 3 V/430 Ω ≈ 6.98 mA`. The voltage drops are `V_R1 ≈ 0.698 V` and `V_R2 ≈ 2.30 V`; their sum equals 3 V taking rounding into account.[^aac-series-circuits]

## Detailed explanation

In a series circuit, the resistors form a single path, so the same current passes through both. First, replace them with an equivalent resistance: `R_total = R_1 + R_2 = 100 Ω + 330 Ω = 430 Ω`. Next, apply Ohm's law to the whole circuit: `I = V/R_total = 3 V/430 Ω ≈ 0.00698 A = 6.98 mA`.[^aac-series-circuits]

To find the voltage across each resistor, multiply this same current by its resistance: `V_R1 = I*R_1 ≈ 0.698 V`, and `V_R2 = I*R_2 ≈ 2.30 V`. Checking with Kirchhoff's law gives `V_R1 + V_R2 ≈ 0.698 V + 2.30 V = 3.00 V`. A slight difference in the final decimal places arises from rounding; in a physical circuit, resistor tolerances and the source internal resistance will also contribute.[^aac-series-circuits]

**Common mistakes:**
- Do not divide the source voltage individually by each resistor to obtain current. For the current of the entire series circuit, use total resistance.
- Do not confuse mA with A: `0.00698 A` equals `6.98 mA`.
- The source voltage is applied across both resistors together, and individual drops are determined by `V = I*R`.[^aac-series-circuits]
