---
id: emb-elintro-0056
title: "Why is Wh better than mAh for comparing the energy stored in batteries?"
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
  - source_id: iata-lithium-guidance-2023
    title: "IATA Lithium Battery Guidance Document 2023"
    url: https://data.energizer.com/wp-content/uploads/2023/04/IATA-Lithium-Guidance-2023.pdf
---

## Short answer

mAh indicates charge, but not energy without taking voltage into account: nominal energy is estimated as `Ah*V`. Therefore, a 2400 mAh battery at 1.2 V has about 2.88 Wh, while a 2000 mAh battery at 3.7 V has about 7.4 Wh; the exact accessible energy depends on discharge conditions.[^iata-lithium-guidance-2023]

## Detailed explanation

Wh describes stored electrical energy more accurately than mAh when comparing batteries with different voltages. An ampere-hour is the integral of current over time and measures electric charge; by itself, it does not specify the work a power source can perform. To estimate nominal energy, charge is multiplied by nominal voltage: `E(Wh) = C(Ah)*V(V)`. To convert from mAh to Ah, the value is divided by 1000.[^iata-lithium-guidance-2023]

For example, 2400 mAh is 2.4 Ah. At a nominal voltage of 1.2 V, this gives `2.4*1.2 = 2.88 Wh`. A 2000 mAh cell at 3.7 V has `2.0*3.7 = 7.4 Wh`: its capacity in mAh is lower, but its nominal stored energy is greater. Such a calculation is an approximation: voltage changes during discharge, and rated capacity is determined under manufacturer-specified load, temperature, and cut-off voltage conditions.[^iata-lithium-guidance-2023]

One should not interpret Wh as a guarantee of identical runtime in any device. A power converter has losses, loads consume power unevenly, and accessible charge depends on the discharge profile and cut-off voltage. However, Wh normalizes comparisons of batteries with different nominal voltages better than mAh. For identical chemistry, voltage, and test conditions, comparing mAh can be sufficient.

**Common mistake:** comparing only the number of mAh and treating the larger number as proof of greater stored energy. First check the nominal voltage and the conditions under which the manufacturer specified capacity.[^iata-lithium-guidance-2023]
