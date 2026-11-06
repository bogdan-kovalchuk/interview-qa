---
id: emb-elcmproj-0055
title: "Why is the AVCC analog power pin of a microcontroller connected through an LC filter?"
track: electronics
section: circuitmaker-projects
sources:
  - source_id: microchip-atmega328p-datasheet
    title: "Microchip Technology: ATmega328P 8-bit AVR Microcontroller Datasheet"
    url: https://ww1.microchip.com/downloads/en/DeviceDoc/Atmel-7810-Automotive-Microcontrollers-ATmega328P_Datasheet.pdf
  - source_id: microchip-avr040-emc
    title: "Microchip Application Note AVR040: EMC Design Considerations for AVR Microcontrollers"
    url: https://ww1.microchip.com/downloads/en/Appnotes/Atmel-1619-EMC-Design-Considerations_ApplicationNote_AVR040.pdf
  - source_id: horowitz-art-of-electronics
    title: "Paul Horowitz, Winfield Hill. The Art of Electronics, 3rd Edition, Cambridge University Press"
    url: https://artofelectronics.net/
---

## Short answer

High-speed switching in digital CPU cores injects high-frequency noise and voltage ripple onto the primary `VCC` bus. A low-pass filter composed of a 10 µH inductor (or ferrite bead) and a decoupling capacitor attenuates these transients. Providing clean supply voltage to `AVCC` prevents digital rail noise from entering the internal ADC comparator and sample network, preserving conversion accuracy.[^microchip-atmega328p-datasheet]

## Detailed explanation

TODO
