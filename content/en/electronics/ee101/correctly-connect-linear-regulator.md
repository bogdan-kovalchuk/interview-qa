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

TODO
