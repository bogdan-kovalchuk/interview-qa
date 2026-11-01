---
id: emb-elintro-0209
title: "How do you measure a transistor's β with a multimeter?"
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
  - source_id: meter-beta
    title: "Fluke 8050A Instruction Manual"
    url: https://assets.fluke.com/manuals/8050a___imeng0200.pdf
---

## Short answer

In `hFE` mode, the multimeter estimates gain under its own small-signal test conditions; insert the disconnected transistor into the correct `E`, `B`, `C` sockets after checking the instrument manual and the component pinout.[^meter-beta] The reading is not a universal standard for 2N2222 and does not guarantee parameters in an operating circuit; zero can have several causes and by itself does not prove a defect.[^meter-beta]

## Detailed explanation

A multimeter's `hFE` function provides an approximate measurement of the BJT small-signal current gain under conditions set by the instrument itself, rather than a universal transistor value.[^meter-beta]

If the multimeter has a dedicated socket, disconnect the transistor from the circuit, identify its `NPN` or `PNP` type and pinout from the datasheet, and insert it into the `E`, `B`, `C` sockets according to the markings on that specific instrument. The instrument supplies a small test current and estimates the ratio of collector current to base current. Other models may have a different socket arrangement or not support such a test at all, so the multimeter manual is decisive.[^meter-beta]

The reading is useful for quick comparison or finding an obvious defect, but it is not a verification that an amplifier or switch is suitable. The datasheet specifies gain for defined `I_C`, `V_CE`, and temperature; the multimeter test may use an entirely different operating point. β also depends on temperature, so heating from fingers can alter the result.[^meter-beta]

You cannot conclude that a reading of `0` necessarily means a broken transistor: incorrect orientation, swapped pins, the wrong type, poor contact, or an out-of-range value are all possible. Check the manual, polarity, and pinout, and then, if necessary, test both junctions separately in diode-test mode. Such a check also does not replace measuring the transistor under its operating load.[^meter-beta]

**Common mistake:** taking the number from the display as guaranteed `hFE` in any circuit. Record it only together with the instrument model and understand it as a comparative measurement.
