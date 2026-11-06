---
id: emb-elcmproj-0061
title: "Why is LED resistor selection constrained by total microcontroller package current limits?"
track: electronics
section: circuitmaker-projects
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), картки курсу"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: microchip-atmega328p-datasheet
    title: "Microchip Technology: ATmega328P 8-bit AVR Microcontroller Datasheet (DS40002061B)"
    url: https://www.microchip.com/en-us/product/ATmega328P
  - source_id: horowitz-hill-art-electronics
    title: "Horowitz, P., & Hill, W. (2015). The Art of Electronics (3rd ed.). Cambridge University Press"
    url: https://artofelectronics.net/
---

## Short answer

An individual GPIO pin can handle 20–40 mA, but the total supply current through the MCU power and ground pins is capped at 200 mA. Illuminating multiple LEDs simultaneously risks exceeding this cumulative package budget and overheating internal bond wires and silicon. Increasing current-limiting resistors to 330–1000 Ω maintains the aggregated draw well within safe limits.[^udemy-electronics-course]

## Detailed explanation

TODO
