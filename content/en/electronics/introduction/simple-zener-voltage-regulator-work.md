---
id: emb-elintro-0186
title: "How does a simple Zener voltage regulator work?"
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
  - source_id: aac-zener-regulator
    title: "All About Circuits: What Are Zener Diodes?"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/chpt-3/zener-diodes/
---

## Short answer

In a simple shunt regulator, a series resistor `R_s` limits current, while a reverse-biased Zener diode conducts current in parallel with the load and holds the output near `V_Z` when operating in its breakdown region.[^aac-zener-regulator] Resistor current divides between the load and the Zener: `I_R = I_load + I_Z`. As the load draws more current, `I_Z` decreases; regulation is maintained only while Zener current remains above the required knee current and power dissipation stays within allowable limits.[^aac-zener-regulator]

## Detailed explanation

A simple Zener regulator is a parallel (shunt) regulator: the load and Zener diode are connected in parallel after `R_s`. The resistor is necessary because a Zener diode in breakdown has a low dynamic resistance, and without current limiting the source could deliver destructive current. The node voltage approaches `V_Z` in the operating region, but the Zener does not generate voltage if the source cannot provide it together with the necessary headroom across the resistor.[^aac-zener-regulator]

By Kirchhoff's current law, the current in `R_s` branches into load current and Zener current: `I_R = I_load + I_Z`. For estimation, `I_R = (V_in - V_out)/R_s`; when the load draws more current, the share `I_Z` decreases. If it drops below the minimum regulation current from the specific Zener datasheet, its voltage ceases to be sufficiently constant, and `V_out` begins to fall. If the load is disconnected or `V_in` rises, almost all excess current can flow through the Zener, so both its power dissipation and the resistor power rating must be checked.[^aac-zener-regulator]

Worked example: for an idealized model with `V_in = 12 V`, `V_Z = 5.1 V`, and `R_s = 330 Ω`, the total resistor current is `20.9 mA`. This does not mean all this current is available to the load: a portion must remain in the Zener diode for regulation. The `5.1 V` value is also the nominal rating of the model, not a guaranteed exact voltage at any current or temperature.

**Common mistakes:**

- Assuming that the output is always exactly `V_Z`; the actual voltage depends on current, component tolerance, and temperature.
- Forgetting to check worst-case conditions: maximum load can pull the Zener out of regulation, while minimum load can cause it to overheat.[^aac-zener-regulator]
