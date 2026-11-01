---
id: emb-elintro-0111
title: "Why should you check a breadboard for breaks in the power rails?"
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
  - source_id: adafruit-breadboard-split-rails
    title: "Adafruit: Breadboards for Beginners"
    url: https://learn.adafruit.com/breadboards-for-beginners?view=all
---

## Short answer

On some breadboards, the power rails are split into isolated sections, so voltage applied to one section will not necessarily appear on another. Check the connections using the board diagram or a multimeter, and if a continuous bus is needed, bridge the segments with a jumper wire.[^adafruit-breadboard-split-rails]

## Detailed explanation

Power rails on a breadboard are groups of tie-points connected internally to distribute `VCC` and `GND` without running a separate wire to every node. However, this connection is not guaranteed to run the full length: some boards have a break in the middle, and on certain models two adjacent rails are also electrically isolated. Therefore, the colored stripe is merely a visual guide, not proof of electrical contact.[^adafruit-breadboard-split-rails]

If a power source is connected to the upper section of a split rail, the lower section may remain unpowered or "float" – its potential is undefined by that source. In this case, an IC or sensor may fail to start, and input signals may be unstable. This looks like a circuit error, even though the only actual issue is the lack of an electrical connection between the segments.

Before applying power, trace which holes are connected internally on your specific board. With power disconnected, use a multimeter in continuity mode to check contact between points you expect to be on the same rail. If there is no contact, add a jumper wire from one segment to the other; for long rails, it is also worth checking the voltage drop under load. Do not randomly connect `VCC` and `GND` rails together: that will create a short circuit.

Example: a `5 V` power supply is connected to the top half of the red rail, and an LED's resistor is connected to the bottom half. If the rail is split, the bottom half does not receive this `5 V` until it is connected with a jumper wire to the top half or wired directly to the power supply.[^adafruit-breadboard-split-rails]

**Common mistakes:**
- Assuming that a red stripe indicates a continuous conductor along the entire length.
- Connecting rails based solely on color without verifying their actual topology.
- Checking continuity with a multimeter on a board that is still connected to a power supply.
