---
id: emb-elintro-0075
title: "Why is a 9V battery poorly suited to high currents?"
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
  - source_id: energizer-522-datasheet
    title: "Energizer 522 9V Alkaline Battery Product Datasheet"
    url: https://data.energizer.com/pdfs/522_ap.pdf
---

## Short answer

A nine-volt battery has low capacity and relatively high internal resistance. Without a load it may show `9 V`, but under the current of a motor or high-power LED, the voltage quickly sags.[^energizer-522-datasheet]

## Detailed explanation

The `9 V` marking designates nominal voltage, not an ability to deliver arbitrary current while maintaining that voltage. A real battery has internal resistance and chemical processes with limited rates. When a load draws current, internal resistance causes a voltage drop, and cell polarization can further reduce terminal voltage. High current also depletes available capacity faster and increases heating.[^aac-direct-current]

You must compare specific discharge conditions from the datasheet rather than just the voltage on the label. For example, the datasheet for the alkaline Energizer 522 provides curves for loads with `270 Ω` and `620 Ω` resistors and measures discharge to an endpoint voltage of `4.8 V` at `21 °C`; it does not establish a universal characteristic for all 9 V batteries or all loads.[^energizer-522-datasheet]

Example: a `100 Ω` load connected to an ideal `9 V` source would draw `90 mA` by Ohm's law. In a real battery, the voltage across the load will be lower, so current and power will also differ; an exact result requires its discharge curve or measurement. For a motor, inrush current is also critical and can be significantly higher than steady-state current.

**Common mistake:** judging suitability by no-load voltage. You must check the discharge curve for the required current, as well as the operating temperature limit, runtime, and the requirements of the device itself.[^aac-direct-current]
