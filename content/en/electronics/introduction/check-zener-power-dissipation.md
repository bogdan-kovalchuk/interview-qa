---
id: emb-elintro-0194
title: "How do you check a Zener's power dissipation?"
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

In the worst-case scenario with no load, nearly all the current through `R_s` flows through the Zener diode. Calculate `P_Z = V_Z*I_Z` and compare it with the allowable power rating, taking temperature and mounting into account.[^aac-zener-regulator]

## Detailed explanation

To check the power dissipation of a Zener diode, determine the voltage across it and the highest current that can flow through it across the expected operating conditions. In a simple shunt regulator, the current through `R_s` is divided between the load and the Zener diode. In the absence of a load, nearly all of this current flows into the Zener diode, so no-load operation is often the worst-case condition for its heating.[^aac-zener-regulator]

To a first approximation, the power equals `P_Z = V_Z*I_Z`. To find the maximum, substitute the maximum source voltage, the minimum load current, and the actual breakdown voltage at the corresponding current. At the same time, check the resistor: an increase in input voltage also increases its dissipation. Compare the calculated power with the datasheet conditions – the allowable rating may derate with increasing temperature, and the board layout and package affect heat removal.[^aac-zener-regulator]

Example: for a hypothetical `5.1 V` Zener diode carrying `20 mA`, this gives `P_Z = 5.1 V*0.020 A = 0.102 W`. This is only an estimate of electrical power; it does not prove that any Zener diode labeled `0.5 W` will operate safely under these conditions. You must check the thermal derating, ambient temperature, and mounting of the specific package.[^aac-zener-regulator]

**Common mistake:** checking only maximum load. It typically diverts part of the current away from the Zener diode and reduces its dissipation; to find the maximum power, analyze also the minimum load or no-load condition.[^aac-zener-regulator]
