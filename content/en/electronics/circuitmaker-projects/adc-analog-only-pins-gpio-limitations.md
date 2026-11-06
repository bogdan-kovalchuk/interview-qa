---
id: emb-elcmproj-0060
title: "Why can pins ADC6 and ADC7 of the ATmega328P not be used to drive indicator LEDs?"
track: electronics
section: circuitmaker-projects
sources:
  - source_id: microchip-atmega328p-datasheet
    title: "Microchip Technology: ATmega328P 8-bit AVR Microcontroller Datasheet"
    url: https://ww1.microchip.com/downloads/en/DeviceDoc/Atmel-7810-Automotive-Microcontrollers-ATmega328P_Datasheet.pdf
  - source_id: arduino-nano-schematic
    title: "Arduino: Arduino Nano Reference Design & Schematic"
    url: https://docs.arduino.cc/hardware/nano
  - source_id: horowitz-art-of-electronics
    title: "Paul Horowitz, Winfield Hill. The Art of Electronics, 3rd Edition, Cambridge University Press"
    url: https://artofelectronics.net/
---

## Short answer

On ATmega328P TQFP-32 and QFN-32 packages, pins `ADC6` and `ADC7` are dedicated exclusively as analog inputs to the internal ADC multiplexer. They lack internal digital output driver FETs, Schmitt triggers, and GPIO port registers (`PORT`, `DDR`, `PIN`). Attempting to configure them as digital outputs has no effect, so indicator LEDs must be connected to standard GPIO pins instead.[^microchip-atmega328p-datasheet]

## Detailed explanation

TODO
