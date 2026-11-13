---
id: emb-elee-0240
title: "How many input combinations must be checked in a two-input gate, and what should be recorded?"
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
  - source_id: ti-hc00
    title: "TI SN74HC00 quadruple NAND gates datasheet"
    url: https://www.ti.com/lit/ds/symlink/sn74hc00.pdf
  - source_id: fiore-bjt-switching
    title: "Fiore: Semiconductor Devices, 4.7 BJT Switching and Driver Applications (LibreTexts)"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/04%3A_Bipolar_Junction_Transistors_(BJTs)/4.7%3A_BJT_Switching_and_Driver_Applications
---

## Short answer

All four input combinations must be tested: 00, 01, 10, and 11 (`2^2 = 4`), even if the circuit appears to work. For each state, record the actual measured output voltage rather than simply observing an indicator LED, verifying that the level complies with the logic input thresholds of the downstream gate.[^ti-hc00]

## Detailed explanation

A two-input gate has four input states because each input can be in one of two logic states: `2^2 = 4`. The truth table contains all four rows: 00, 01, 10, and 11. Testing only the rows where the output "should be 1" or testing only two rows does not prove correctness: a fault may manifest precisely in the row that was skipped. For three inputs, the table has eight rows (`2^3 = 8`), so exhaustive checking grows exponentially, but the principle remains the same.

Voltage must be recorded rather than merely a conclusion of "lit / unlit", because a logic level is defined by a voltage range, not a single number. For the SN74HC00 at `V_CC = 4.5 V`, an input is recognized as HIGH from 3.15 V (`V_IH` min) and LOW up to 1.35 V (`V_IL` max).[^ti-hc00] Between these limits lies a region that a downstream gate cannot reliably interpret as either 0 or 1; its span is `3.15 - 1.35 = 1.80 V`. For rows where the NAND output should be in state 1, the datasheet specifies a minimum of 4.4 V under light load.[^ti-hc00]

An LED is no substitute for measurement. LED brightness depends on current through it, not on logic thresholds. In the example from Fiore's book, a logic output might deliver, say, 5 mA, whereas achieving the desired LED brightness might require over 10 mA.[^fiore-bjt-switching] Consequently, an LED might glow dimly even when the voltage already falls in the forbidden region of the downstream input.

**Example:** NAND should yield 1 in rows 00, 01, and 10, and 0 in row 11. Suppose that in row 11 the output is near 0.1 V, in rows 00 and 10 it is around 4.4 V, and in row 01 under LED loading it sags to 2.9 V. The output in row 01 should be HIGH, but 2.9 V lies between 1.35 V and 3.15 V, so the next gate will not read it unambiguously. Meanwhile, an active-high LED wired to ground remains lit, creating the false impression that the output is a valid 1 and everything is fine. Recording merely "0" or "1" without voltage values will not catch this error.

**Common mistakes:**

- Testing only those rows where 1 is expected, or testing only a few rows while assuming the rest are obvious.
- Assuming that a lit LED signifies a valid logic level.
- Recording "0" or "1" without measuring voltage and without comparing to the input thresholds of the downstream stage.
