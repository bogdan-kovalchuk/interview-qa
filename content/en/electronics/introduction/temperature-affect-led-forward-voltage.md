---
id: emb-elintro-0124
title: "How does temperature affect an LED's forward voltage?"
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
  - source_id: kingbright-wp154a4
    title: "Kingbright WP154A4SEJ3VBDZGC/CA datasheet"
    url: https://www.kingbrightusa.com/images/catalog/SPEC/WP154A4SEJ3VBDZGC-CA.pdf
---

## Short answer

With heating, the `V_f` of many LEDs decreases; for the red Kingbright WP154A4SEJ3VBDZGC/CA, a coefficient of −2.0 mV/°C is specified at `I_F = 20 mA`.[^kingbright-wp154a4] In a circuit with a voltage source and a resistor, this can increase current, whereas a constant-current driver maintains the set current within its operating range.[^kingbright-wp154a4]

## Detailed explanation

The forward voltage `V_f` depends on junction temperature, and for many LEDs it decreases with heating. The sign and magnitude of the coefficient depend on component type and operating current, so the numerical value should be taken from the datasheet rather than extrapolated from one LED to all others.[^aac-semiconductors]

In a simple circuit with a voltage source and a series resistor, the current is approximately set by the difference between the supply voltage and `V_f`, divided by the resistance. If `V_f` drops, more voltage remains across the resistor, and the current increases. This can create positive feedback through heating, but its magnitude depends on the resistor, heat sinking, and operating mode; thermal runaway is not inevitable in every circuit.[^aac-semiconductors]

As a specific example, the Kingbright WP154A4SEJ3VBDZGC/CA datasheet gives a coefficient of `−2.0 mV/°C` for the red variant at `I_F = 20 mA`. A change in junction temperature of 10 °C corresponds to approximately `−20 mV` of `V_f` change under datasheet conditions; this cannot be applied without verification to other colors, currents, or parts.[^kingbright-wp154a4]

A current-regulated driver compensates for changes in `V_f` as long as it has sufficient output voltage headroom. It does not eliminate the reduction in permissible current at high temperature: thermal design and compliance with manufacturer limits are required.[^aac-semiconductors]
