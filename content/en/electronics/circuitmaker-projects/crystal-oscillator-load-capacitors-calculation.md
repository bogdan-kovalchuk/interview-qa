---
id: emb-elcmproj-0053
title: "How are load capacitor values calculated for an ATmega328P crystal oscillator?"
track: electronics
section: circuitmaker-projects
sources:
  - source_id: atmel-avr042
    title: "AVR042: AVR Hardware Design Considerations (Application Note)"
    url: https://ww1.microchip.com/downloads/en/Appnotes/Atmel-2521-AVR-Hardware-Design-Considerations_ApplicationNote_AVR042.pdf
  - source_id: microchip-atmega328p-datasheet
    title: "ATmega328P 8-bit AVR Microcontroller with 32K Bytes In-System Programmable Flash Datasheet"
    url: https://ww1.microchip.com/downloads/en/DeviceDoc/Atmel-7810-Automotive-Microcontrollers-ATmega328P_Datasheet.pdf
  - source_id: ti-crystal-selection
    title: "Texas Instruments Application Report SZZA043: Crystal Oscillator Basics and Crystal Selection"
    url: https://www.ti.com/lit/an/szza043/szza043.pdf
---

## Short answer

The effective crystal load capacitance is given by `C_L = (C1 * C2) / (C1 + C2) + C_stray`. For symmetrical capacitors, this simplifies to `C1 = C2 = 2 * (C_L - C_stray)`. Assuming a typical PCB stray capacitance `C_stray ≈ 3–5 pF` and a standard 16 MHz crystal rated at `C_L = 15 pF`, standard 22 pF ceramic capacitors are selected.[^atmel-avr042]

## Detailed explanation

TODO
