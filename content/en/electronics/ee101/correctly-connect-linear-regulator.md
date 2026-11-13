---
id: emb-elee-0163
title: "How do you correctly connect a 7805 linear regulator?"
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
  - source_id: ti-ua78
    title: "TI: uA7805, uA7808, uA7810, uA7812, uA7815, uA7824 positive-voltage regulators (datasheet)"
    url: https://www.ti.com/lit/ds/symlink/ua78.pdf
  - source_id: ti-lm340
    title: "TI: LM340, LM340A, LM7805 family wide VIN 1.5-A fixed voltage regulators (datasheet)"
    url: https://www.ti.com/lit/ds/symlink/lm340.pdf
---

## Short answer

In a TO-220 package, the standard 7805 pinout is: pin 1 is input, pin 2 is common (ground), and pin 3 is output; verify pinouts in the manufacturer datasheet for alternative packages.[^ti-ua78] Decoupling capacitors must be placed close to the device pins: TI specifies 0.33 µF at the input and 0.1 µF at the output for the uA7805.[^ti-ua78] If the regulator sits more than approximately six inches from the bulk supply filter, a local input capacitor is mandatory, as a distant electrolytic capacitor cannot replace it.[^ti-lm340]

## Detailed explanation

For the 7805 in a TO-220 package, the pinout is identical in TI's uA7805 and LM7805 datasheets: pin 1 is input, pin 2 is ground (COMMON or GND), and pin 3 is output.[^ti-ua78][^ti-lm340] In every 7805 package shown in these datasheet pinout diagrams, the metal mounting tab or case connects internally to ground (although the first page of the LM340 datasheet prints a generic note reading "Tab/Case is Ground or Output"), so always verify the specific datasheet before mounting the regulator on a shared heatsink.[^ti-ua78][^ti-lm340] Recommended input voltage for the uA7805 is 7 to 25 V, the absolute maximum is 35 V, and dropout is typically 2 V at 1 A load current.[^ti-ua78] Therefore, a 9 V source is entirely suitable: it provides 4 V of headroom above the 5 V output.

Capacitors are part of the standard application circuit. In the typical uA78xx schematic, 0.33 µF is placed at the input and 0.1 µF at the output. TI recommends the input capacitor to filter input noise, and the output capacitor for output decoupling and noise limiting; the output capacitor is not required for loop stability, and published datasheet parameters are characterized with these capacitances.[^ti-ua78] Input decoupling capacitors must be placed as close as possible to the IC pins.[^ti-ua78] Exact values depend on the specific datasheet: the LM340 datasheet specifies parameters measured with 0.22 µF at the input and 0.1 µF at the output, states that an output capacitor is not required for stability but improves transient response, and notes that an input capacitor is mandatory if the regulator is located more than approximately six inches from the power-supply filter.[^ti-lm340] Therefore, capacitance values should be taken from the datasheet of the specific part rather than recalled from memory.

Practical protection details are often overlooked in basic implementations. If a large capacitance sits at the output and the input is shorted to ground, the stored charge discharges through the regulator, potentially damaging it; the LM340 datasheet recommends a reverse protection diode between output and input, noting that below 10 µF output capacitance a diode is generally unnecessary.[^ti-lm340] If the ground pin is disconnected while power remains applied, the output voltage rises toward the unregulated input voltage, potentially destroying the load; the datasheet advises shutting off power first or ensuring ground connects first.[^ti-lm340]

**Common mistakes:**

- Assuming pinout is identical across all package types and manufacturers instead of verifying the datasheet.
- Relying on a distant bulk electrolytic capacitor rather than placing local decoupling capacitors adjacent to regulator pins.
- Installing a large output capacitor without an output-to-input protection diode, ignoring datasheet thresholds.[^ti-lm340]
- Allowing the regulator ground pin to disconnect while input power remains applied.[^ti-lm340]
