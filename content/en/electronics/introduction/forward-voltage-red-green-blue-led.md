---
id: emb-elintro-0114
title: "What is the forward voltage `V_f` of red, green, and blue `LED`s?"
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
  - source_id: digikey-rgb-led-forward-voltage
    title: "DigiKey: RGB LEDs Provide Multicolor Display Solutions"
    url: https://www.digikey.com/en/articles/how-to-drive-multicolor-leds
---

## Short answer

Typical `V_f` depends on the model and current. For example, for the Adafruit 2739 RGB LED at `20 mA`, approximately `2.0 V` is given for the red channel and `3.2 V` for the green and blue channels; this is a value for a specific product, not a universal color chart.[^digikey-rgb-led-forward-voltage]

## Detailed explanation

Forward voltage `V_f` is the voltage across an LED at a given forward current. In red LEDs it is often lower than in blue LEDs because semiconductor materials for different wavelengths have different bandgap widths. However, color alone does not set an exact value: material, design, current, and temperature all matter, so you need to consult the datasheet for the specific component.[^digikey-rgb-led-forward-voltage]

Tables with approximate ranges are useful only for estimation. Even a value from a single specification is tied to a specific test current: in the example of the Adafruit 2739 RGB LED, the article cites `2.0 V` at `20 mA` for the red channel and `3.2 V` for green and blue; at `15 mA`, the channels are already listed at `1.9 V` and `3.1 V`. You should not treat these as guaranteed limits for any LED of that color.[^digikey-rgb-led-forward-voltage]

`V_f` is needed, in particular, to estimate the resistance of a series resistor: the power supply must provide the voltage drop across both the LED and the resistor. If a multicolor component has separate dies, each channel uses its own characteristic. Replacing a red LED with a blue one without recalculating can change the current and brightness.[^digikey-rgb-led-forward-voltage]

Example: if the datasheet of a specific red LED specifies a typical `V_f = 2.0 V` at `20 mA`, that value can be used as an initial estimate for that current; for a guaranteed calculation, check the limits in the specification.

**Common mistakes:**
- Assuming that the ranges given for a color are exact guaranteed limits.
- Ignoring the test current at which the manufacturer measured `V_f`.
- Assuming that all green LEDs have the same forward voltage.
