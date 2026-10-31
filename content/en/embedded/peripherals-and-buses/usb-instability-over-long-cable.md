---
id: emb-periph-0014
title: "A USB device is unstable over a 5–10 metre distance. Which USB, cable, power, and alternative-interface limits should you check?"
track: embedded
section: peripherals-and-buses
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: zephyr-peripherals
    title: "Zephyr Project documentation: Peripherals"
    url: https://docs.zephyrproject.org/latest/hardware/peripherals/index.html
  - source_id: usb-20-spec
    title: "Universal Serial Bus Specification Revision 2.0"
    url: https://www.usb.org/document-library/usb-20-specification
---

## Short answer

Check the specification length limit for the required USB speed, cable quality, shielding, hubs/repeaters, and VBUS drop under load. At 5–10 m, signal integrity problems, ground potential difference, and device power below the minimum often appear. Alternatives: powered hub/active cable, USB extender, RS-485/CAN/Ethernet, or move the MCU closer to the sensor.[^dou-embedded-interview]

## Detailed explanation

TODO
