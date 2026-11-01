---
id: emb-elintro-0113
title: "How does an `LED` differ from a resistor in how its voltage changes with current?"
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

Across a resistor, voltage increases proportionally to current, whereas in an `LED`, after the knee of the curve, current increases sharply with a small change in forward voltage `V_f`. Therefore, `V_f` is not constant: it is taken from the datasheet for the required current and conditions, using a typical value for the initial calculation.[^digikey-rgb-led-forward-voltage]

## Detailed explanation

A resistor and an `LED` have different current-voltage characteristics. For an ideal resistor, Ohm's law gives the linear relationship `V = I*R`: if resistance is constant, doubling the current doubles the voltage drop. An `LED` is a semiconductor diode, and after reaching the forward "knee", its current changes rapidly even with a small change in applied voltage.[^digikey-rgb-led-forward-voltage]

This does not mean that the voltage across an `LED` is strictly constant. `V_f` depends on current, temperature, color, and the specific model; a datasheet usually specifies a typical or maximum value under defined conditions. For selecting a series resistor, a typical `V_f` helps estimate the operating point, but checking the maximum current must account for power supply tolerances, component parameter variations, and heating. The current value should be limited by a resistor or a dedicated driver.[^digikey-rgb-led-forward-voltage]

For example, for the specific Adafruit 2739 RGB module cited in the article, typical values are given at `20 mA`: about `2.0 V` for the red channel and `3.2 V` for the green and blue channels. At `15 mA`, the values are listed as `1.9 V` and `3.1 V`. This shows that the value changes with current and belongs to a specific product, rather than being a universal threshold for all LEDs.[^digikey-rgb-led-forward-voltage]

**Common mistakes:**
- Calling `V_f` fixed regardless of current.
- Using the resistor formula as proof that an `LED` behaves linearly.
- Transferring the typical `V_f` of one color or model to any other `LED`.
