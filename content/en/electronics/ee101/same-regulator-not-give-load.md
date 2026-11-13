---
id: emb-elee-0143
title: "Why does the same regulator (9 V, 5.1 V, 390 Ω) not give 5.1 V into a 100 Ω load?"
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
  - source_id: nexperia-an90031
    title: "Nexperia AN90031: Zener diodes – physical basics, parameters and application examples"
    url: https://assets.nexperia.com/documents/application-note/AN90031.pdf
  - source_id: nexperia-bzx84
    title: "Nexperia BZX84 series: voltage regulator diodes (datasheet)"
    url: https://assets.nexperia.com/documents/data-sheet/BZX84_SER.pdf
  - source_id: fiore-rectification
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 3.2 Rectification"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/03:_Diode_Applications/3.2:_Rectification
---

## Short answer

Delivering 5.1 V into 100 Ω requires `5.1/100 = 51 mA`, but the 390 Ω resistor at `V_out = 5.1 V` can supply only `(9 - 5.1)/390 = 10 mA`. Assuming `V_out ≈ V_Z` would imply a negative Zener current, which is impossible because a reverse-biased diode cannot source current. The Zener cuts off, and the output is determined by a resistive divider: `9*100/(390 + 100) ≈ 1.84 V`.[^fiore-rectification]

## Detailed explanation

**What is needed and what is possible.** To obtain `5.1 V` across `100 Ω`, the load requires `5.1/100 = 51 mA`. The maximum current the resistor can supply when the output sits at `V_Z` is `I_R = (9 - 5.1)/390 = 10 mA`; this is also the maximum load current in such a circuit when zero current flows through the Zener diode.[^fiore-rectification] The shortfall is substantial: 51 mA required versus 10 mA available. Substituting into the node equation yields `I_Z = I_R - I_load = 10 - 51 = -41 mA`. A Zener diode conducts in breakdown in only one direction, so a negative result is not a physical current, but an indicator that the starting premise ("the output remains at `V_Z`") has failed.

**What actually occurs.** The heavy load pulls the output below `V_Z`, taking the Zener diode out of breakdown. Below its breakdown voltage, it behaves as a normal reverse-biased diode with tiny leakage current: for a BZX84-C5V1, no more than 2 µA at `V_R = 2 V`.[^nexperia-bzx84] Compared to tens of milliamperes, this leakage is negligible, leaving simply the 390 Ω resistor and 100 Ω load. The output is governed by a voltage divider: `V_out = 9*100/(390 + 100) = 900/490 ≈ 1.84 V`, and current is `9/490 ≈ 18.4 mA`. Consistency check: `1.84 V < 5.1 V`, confirming that the Zener diode is indeed out of breakdown and the assumption that it does not conduct holds true.[^fiore-rectification]

**Power dissipation.** A voltage of `9 - 1.84 = 7.16 V` drops across the resistor, so `P_R = 7.16²/390 ≈ 132 mW`, while the load dissipates `1.84²/100 ≈ 34 mW`; together they total `≈ 165 mW`, consistent with `9*18.4 mA`. A standard 1/8 W (125 mW) resistor is already overloaded in this condition, meaning the non-regulating circuit is also prone to overheating.

**How to fix it.** The intuitive impulse is to decrease R. Using Nexperia's formula `R1 = (V_IN - V_Z)/(I_Z(min) + I_LOAD(max))`, with a 5 mA minimum Zener current and 51 mA load, we obtain `3.9/(0.005 + 0.051) ≈ 69.6 Ω`, or 68 Ω.[^nexperia-an90031] However, at no load the entire current flows through the Zener: `3.9/68 ≈ 57 mA`, resulting in `P_Z = 5.1*0.057 ≈ 293 mW` – which exceeds the 250 mW maximum allowable rating for the BZX84.[^nexperia-bzx84] Nexperia itself points out that the basic shunt topology is suited only for low power levels, and for heavier loads recommends adding a bipolar transistor.[^nexperia-an90031] Another approach is using a regulator topology that does not shunt the load current through the reference diode.

**Common mistakes:**

- Assuming `V_out = V_Z` always holds without verifying whether the series resistor can deliver the required current.
- Treating a negative calculated `I_Z` as a real physical operating state rather than a disproof of the initial assumption.
- Calculating the divider output without verifying that `V_out < V_Z`.
- "Fixing" the shortfall by reducing R without checking Zener power dissipation under no-load conditions.
