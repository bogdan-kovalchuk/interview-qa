---
id: emb-elcmproj-0056
title: "Why is an ISP header retained on a board when USB bootloader programming is available?"
track: electronics
section: circuitmaker-projects
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), картки курсу"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: circuitmaker-docs
    title: "CircuitMaker documentation"
    url: https://www.altium.com/documentation/altium-circuitmaker
  - source_id: microchip-avr042
    title: "Microchip Technology: AVR042 - AVR Hardware Design Considerations Application Note"
    url: https://www.microchip.com/
  - source_id: microchip-atmega328p
    title: "Microchip Technology: ATmega328P Datasheet"
    url: https://www.microchip.com/
---

## Short answer

Programming via USB requires a functional bootloader already residing in microcontroller flash memory. Factory-fresh microcontrollers ship blank and can be initially flashed only over SPI via the ISP header. Additionally, the ISP interface is required to configure hardware fuse bits and recover bricked devices after firmware corruption.[^udemy-electronics-course][^microchip-avr042]

## Detailed explanation

TODO
