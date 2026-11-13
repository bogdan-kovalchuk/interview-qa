---
id: emb-elee-0242
title: "Why can connecting the next gate or an LED change the high output level of a transistor gate?"
track: electronics
section: ee101
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-alternating-current
    title: "All About Circuits textbook, Volume II: AC"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
  - source_id: ti-slaa067
    title: "TI: Understanding Basic Analog – Circuit Equations (SLAA067)"
    url: https://www.ti.com/lit/pdf/slaa067
  - source_id: fiore-bjt-switching
    title: "Fiore: Semiconductor Devices, 4.7 BJT Switching and Driver Applications (LibreTexts)"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/04%3A_Bipolar_Junction_Transistors_(BJTs)/4.7%3A_BJT_Switching_and_Driver_Applications
  - source_id: ti-hc00
    title: "TI SN74HC00 quadruple NAND gates datasheet"
    url: https://www.ti.com/lit/ds/symlink/sn74hc00.pdf
---

## Short answer

When current is drawn from a passive pull-up output, the HIGH level drops by `I*R` to `V_CC - I*R`.[^ti-slaa067] Because LED indicator current and downstream base drive both flow through the pull-up resistor, LED brightness alone does not verify valid logic voltage levels.

## Detailed explanation

A gate with a pull-up resistor has a simple output: when the lower transistor is off, the output is connected to `V_CC` through resistor `R`. Without a load, there is no current through `R`, and the output voltage equals `V_CC`. When a current `I` is drawn from the output, an `I*R` drop appears across the resistor, so the HIGH level decreases to `V_CC - I*R`.[^ti-slaa067]

There are two types of load. The first is the input of the next stage: if it is a BJT base, it draws a base current that also flows through `R`. The second is an LED with its own resistor, which draws current directly from the output. A logic output can source only limited current: in the example from Fiore's book, it can deliver, say, 5 mA, whereas the required LED brightness might need more than 10 mA.[^fiore-bjt-switching]

**Example:** `V_CC = 4.5 V`, `R = 1 kΩ`, an LED with a 330 Ω resistor and a forward voltage of 2 V (an assumption for the example). Without a load, the output yields 4.5 V. With the LED, voltage `V` satisfies `V = 4.5 - 1000*(V - 2)/330`, whence `V` ≈ 2.62 V, and the LED current is `(2.62 - 2)/330` ≈ 1.88 mA. For an SN74HC00 at 4.5 V, the input is guaranteed HIGH only above 3.15 V (VIH min), so 2.62 V no longer guarantees a logic 1.[^ti-hc00]

Conclusion for debugging: one must measure the voltage at the input of the next gate with and without the LED connected, rather than judging by brightness. An illuminated LED does not prove that the HIGH level is sufficient.

**Common mistakes:**

- Assuming that a lit LED indicates a valid HIGH level;
- Calculating the HIGH level as `V_CC` without accounting for load current;
- Failing to account for the base current of an input connected to the output.
