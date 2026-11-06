---
id: emb-elcmproj-0050
title: "What advantages are gained by replicating the Arduino Nano hardware core in a custom device?"
track: electronics
section: circuitmaker-projects
sources:
  - source_id: arduino-nano-schematic
    title: "Arduino: Arduino Nano Reference Design & Schematic"
    url: https://docs.arduino.cc/hardware/nano
  - source_id: microchip-atmega328p-datasheet
    title: "Microchip Technology: ATmega328P 8-bit AVR Microcontroller Datasheet"
    url: https://ww1.microchip.com/downloads/en/DeviceDoc/Atmel-7810-Automotive-Microcontrollers-ATmega328P_Datasheet.pdf
  - source_id: horowitz-art-of-electronics
    title: "Paul Horowitz, Winfield Hill. The Art of Electronics, 3rd Edition, Cambridge University Press"
    url: https://artofelectronics.net/
  - source_id: montrose-emc-pcb
    title: "Mark I. Montrose: EMC and the Printed Circuit Board: Design, Theory, and Layout Made Simple, IEEE Press / Wiley"
    url: https://ieeexplore.ieee.org/book/5265261
---

## Short answer

Replicating the Arduino Nano core schematic guarantees full compatibility with the Optiboot bootloader, existing libraries, and the Arduino IDE ecosystem. The developer gains proven clocking, reset, and flashing circuitry without writing custom hardware drivers. Integrating the core directly onto the main PCB eliminates unreliable header pin contacts, lowers production cost, and optimizes power and analog trace routing.[^arduino-nano-schematic]

## Detailed explanation

TODO
