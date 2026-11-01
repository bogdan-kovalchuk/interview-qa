---
id: emb-elintro-0166
title: "Why does a blue `LED` need a higher `V_f` than a red one?"
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
  - source_id: aac-leds
    title: "All About Circuits: Light Emitting Diodes"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/chpt-7/light-emitting-diodes-leds/
---

## Short answer

Photon energy is proportional to frequency: `E = h*f`. Blue light has a higher frequency, so the corresponding semiconductor has a larger band gap than a red one; this is typically associated with a higher `V_f`.[^aac-leds] The exact value depends on the material, current, and temperature.

## Detailed explanation

The forward voltage `V_f` of an LED is related to the energy released by charge carriers during recombination in the active region. The energy difference between states in the material's band structure determines the characteristic photon energy; the frequency of light is related to it by the relationship `E = h*f`. Therefore, materials that emit blue light typically have a larger band gap than red LED materials and require a higher forward voltage.[^aac-leds]

This is a qualitative relationship, not a method to determine `V_f` precisely by color alone. The voltage also depends on semiconductor composition, crystal design, current, and temperature; for circuit design, you should use the manufacturer's `I-V` graph or table for the specific LED. The value in the datasheet is typically given for a specified test current, rather than being a universal constant.[^aac-leds]

In an LED circuit, current is limited by a resistor or driver: the source must not supply unlimited current simply because the diode has a specific `V_f`. For a series resistor, an estimate is made using `R = (V_supply - V_f)/I`; if `V_f` changes significantly, the current will change as well. This is especially important when temperature changes or when using several LEDs in series.[^aac-leds]

Example: if for a red LED in a given operating mode the typical `V_f` is lower than for a blue one, then with the same source and resistor, less voltage will remain across the resistor with the blue LED, so the current will be lower. A common mistake is treating color as an exact voltage specification; color only indicates an order of magnitude, whereas the design value is taken from the datasheet of the specific part.[^aac-leds]
