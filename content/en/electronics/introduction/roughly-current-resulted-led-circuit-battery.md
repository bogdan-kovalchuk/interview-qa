---
id: emb-elintro-0304
title: "Roughly what current resulted in the LED circuit with a 9 V battery and 220 Ω?"
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
  - source_id: adafruit-led-forward-voltage-kvl
    title: "Adafruit Learning System: Forward Voltage and KVL"
    url: https://learn.adafruit.com/all-about-leds/forward-voltage-and-kvl
---

## Short answer

With a measured drop of 6.55 V across a 220 Ω resistor, the current is approximately 29.8 mA by Ohm's law. The value of around 30 mA is the specific result of the lecture example; a nominal 9 V battery and resistor value alone do not determine the exact current, because actual battery terminal voltage and LED forward drop must be known.[^udemy-electronics-course] [^adafruit-led-forward-voltage-kvl]

## Detailed explanation

In a series circuit consisting of a battery, an LED, and a resistor, the identical current flows through all components. The source voltage is divided between the LED and the resistor, so the resistor current can be determined using Ohm's law: divide the voltage across the resistor by its resistance. The voltage drop across the resistor, rather than the full nominal 9 V battery voltage, must be used in the formula.[^adafruit-led-forward-voltage-kvl]

In the bench measurement described, the voltage across the resistor was approximately 6.55 V, and its nominal resistance was 220 Ω. The calculation yields approximately 0.0298 A, or 29.8 mA; rounded, this is about 30 mA, as reported in the lecture example.[^udemy-electronics-course] To verify the power dissipated by the resistor, calculate `P = V*I`: with these measured values, dissipation is approximately 0.195 W, meaning a 0.25 W resistor operates with very little safety margin under ideal conditions; in a practical assembly, consider temperature derating and actual component tolerance.[^aac-direct-current]

The exact current cannot be calculated simply as `9 V / 220 Ω` because a portion of the source voltage drops across the LED. Similarly, this result is not universal for any 9 V battery: its terminal voltage under load depends on its state of charge and internal resistance, while the LED forward voltage varies with diode chemistry, current, and operating temperature. Therefore, the measured 6.55 V and approximately 30 mA correspond to this specific bench example; for an individual circuit, measure the actual voltage across the resistor or calculate it from measured parameters.[^adafruit-led-forward-voltage-kvl]
