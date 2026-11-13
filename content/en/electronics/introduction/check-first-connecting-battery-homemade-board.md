---
id: emb-elintro-0301
title: "What should you check before first connecting a battery to a homemade board?"
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
  - source_id: fluke-continuity-test
    title: "Fluke: A Guide to Continuity Testing with a Multimeter"
    url: https://www.fluke.com/en-us/learn/blog/digital-multimeters/how-to-test-for-continuity
---

## Short answer

Verify the polarity of connectors and LEDs, component values, series resistor placement, and inspect the solder joints for bridges. With the board unpowered, verify that there is no short circuit between `+9V` and `GND` and confirm continuity along intended traces; note that continuity alone does not prove full schematic correctness.[^fluke-continuity-test]

## Detailed explanation

Before connecting a battery, inspect the board without power applied so that an assembly mistake does not cause excessive current draw or component damage. First, verify the polarity of the battery connector against the `+9V` and `GND` labels, and check polarized components, particularly LEDs, against the schematic and footprint markings. Ensure that an appropriate current-limiting resistor is placed in series with the LED, rather than a jumper or a resistor in an unrelated branch.[^aac-semiconductors]

Inspect both sides of the board: look for solder bridges between adjacent pads, stray solder balls, reversed components, and fragile mechanical joints. Perform continuity or resistance measurements between power rails only on an unpowered board. A reading near zero may indicate a short circuit, but charging capacitors from the multimeter test current, semiconductor junctions, and parallel branches affect the reading; an audible continuity beep is not definitive proof of either a defect or proper operation. If necessary, isolate the specific branch under test.[^fluke-continuity-test]

During initial power-up, use a current-limited bench supply or a series protective resistor if available, and verify voltages at key nodes. Disconnect power immediately if current draw significantly exceeds expected levels, a component heats up rapidly, or a burning odor is detected. Such a staged turn-on procedure helps isolate polarity mistakes, short circuits, and wiring errors; a simple multimeter check before power-up cannot verify circuit operation under full operating load.
