---
id: emb-elcirc-0036
title: "Name typical applications of a voltage divider."
track: electronics
section: circuit-analysis
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-direct-current
    title: "All About Circuits textbook, Volume I: DC"
    url: https://www.allaboutcircuits.com/textbook/direct-current/
  - source_id: adi-voltage-divider
    title: "Analog Devices: Voltage Divider"
    url: https://www.analog.com/en/resources/glossary/voltage-divider.html
  - source_id: ti-voltage-divider-adc
    title: "Texas Instruments: Interfacing 5V Sensors and Signals to 3.3V Input SAR ADCs"
    url: https://www.ti.com/lit/an/sprad89/sprad89.pdf
---

## Short answer

A voltage divider scales down a signal level for an ADC input and enables measuring battery voltage if its output matches the allowed input range. A potentiometer is used as an adjustable divider to set a signal level; a passive divider itself is not a stable power source.[^adi-voltage-divider] For an ADC, one must consider its input loading, source resistance, and settling time rather than only the ideal resistor ratio.[^ti-voltage-divider-adc]

## Detailed explanation

TODO
