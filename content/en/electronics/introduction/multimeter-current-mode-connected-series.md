---
id: emb-elintro-0265
title: "Why must a multimeter in current mode be connected in series?"
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
  - source_id: fluke-current-measurement-fuses
    title: "Fluke: Choosing the correct fuse for your tester"
    url: https://www.fluke.com/en-us/learn/blog/digital-multimeters/choosing-the-correct-fuse-for-your-tester
---

## Short answer

In current mode, a multimeter must be connected in series: the circuit is broken, and load current is routed through the meter's measuring input.[^fluke-current-measurement-fuses] Because this input has very low shunt resistance, connecting it in parallel across a voltage source causes a massive fault current that blows the fuse or damages the instrument.

## Detailed explanation

An ammeter measures current by passing it through an internal, low-resistance current shunt. To measure load current, you must break the circuit branch and insert the meter into the break; the exact same current then flows through both the multimeter and the load. This is why series connection is the required method for current measurement.[^fluke-current-measurement-fuses]

In voltage mode, a multimeter has very high input impedance and connects in parallel across components. Applying that parallel connection method to current mode is dangerous: the low-resistance shunt is placed directly across the voltage source terminals, conducting a massive fault current limited only by the source impedance, lead resistance, and internal shunt. Such a fault current can blow the internal fuse or severely damage the equipment.[^fluke-current-measurement-fuses]

Example: to measure lamp current, shut off the power, disconnect one lead between the power supply and the lamp, and insert the multimeter into the break, selecting the proper current jack and range. Verify that the expected current is well below the meter's input jack and fuse ratings; after completing the measurement, return the test lead to the voltage jack before taking any voltage readings. For currents exceeding the multimeter's maximum rating, use an appropriate current clamp or external shunt rather than attempting a direct connection.[^fluke-current-measurement-fuses]

A common mistake is to finish a current measurement and forget to move the red lead from the `A` or `mA` jack back to the `V` jack before measuring voltage. In that configuration, touching the probes across circuit nodes creates an effective dead short through the shunt. Always verify both the rotary switch position and the physical lead jack assignments before probing, rather than relying solely on the display icon.[^fluke-current-measurement-fuses]
