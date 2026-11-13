---
id: emb-elee-0225
title: "Why does the same 10 mA current sink from 9 V not work with a 1 kΩ load?"
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
  - source_id: fiore-ohms-law
    title: "Engineering LibreTexts: DC Electrical Circuit Analysis – A Practical Approach (Fiore), 3.5 Ohm's Law"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/DC_Electrical_Circuit_Analysis_-_A_Practical_Approach_(Fiore)/03:_Series_Resistive_Circuits/3.05:_Ohm's_Law
  - source_id: fiore-bjt-dc-load-line
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 4.6 DC Load Lines"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/04:_Bipolar_Junction_Transistors_(BJTs)/4.6:_DC_Load_Lines
---

## Short answer

**There is insufficient voltage compliance:** sinking 10 mA across 1 kΩ requires `V = I*R = 10 V`, yet the total supply rail is only 9 V.[^fiore-ohms-law] Because the target current is physically unattainable, the transistor saturates, and the sink delivers no more than roughly 9 mA as governed by the circuit resistance.[^fiore-bjt-dc-load-line]

## Detailed explanation

If a 1 kΩ load and the current sink are connected in series between the 9 V rail and ground, the sum of voltage drops across them cannot exceed 9 V. Sinking 10 mA across 1 kΩ requires `0.010 A * 1000 Ω = 10 V` across the load alone. This exceeds the total supply voltage, so this operating point is unattainable with any transistor and any emitter resistor. The limitation follows from Ohm's law `V = I * R` applied to the resistor in the circuit.[^fiore-ohms-law]

The circuit sets the maximum current: `V_CC / R = 9 V / 1 kΩ = 9 mA`. When the programmed current is higher, the transistor saturates and delivers no more than 9 mA.[^fiore-bjt-dc-load-line] Even neglecting the voltage drop across the emitter resistor and assuming `V_CE(sat)` of roughly 0.1 V, the load receives no more than `(9 - 0.1) / 1000 = 8.9 mA`. The ideal limit with zero loss is 9 mA, which is already less than 10 mA.

A current sink maintains the programmed current only when voltage headroom is available. Therefore, the minimum supply voltage for 10 mA through 1 kΩ is 10 V plus the drop across the sink itself. At 9 V, the load must not exceed 900 Ω (`9 V / 10 mA`), and accounting for voltage drops across the sink, it must be even less.

**Common mistakes:**

- Assuming that a current sink delivers the programmed 10 mA regardless of the load: the power supply limits the current.
- Checking only the emitter resistor value rather than the available voltage headroom across the load.
- Failing to account for `V_CE(sat)` and the emitter resistor voltage drop when finding the maximum load.
