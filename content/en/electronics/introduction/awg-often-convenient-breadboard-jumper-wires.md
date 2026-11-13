---
id: emb-elintro-0289
title: "Which AWG is often convenient for breadboard jumper wires?"
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
  - source_id: busboard-breadboard-wire-gauge
    title: "What wire gauge should I use with a solderless breadboard?"
    url: https://busboard.com/faq/breadboard-wire-gauge
  - source_id: adafruit-breadboard-jumpers
    title: "Jumper Wires | Breadboards for Beginners"
    url: https://learn.adafruit.com/breadboards-for-beginners/diy-jumper-wires
---

## Short answer

Solid-core 22 AWG wire is often convenient for solderless breadboards; BusBoard also recommends solid wire in the 22–26 AWG range. The optimal choice depends on the specific spring clips: wire that is too thick can permanently deform them, while wire that is too thin makes unreliable contact.[^busboard-breadboard-wire-gauge] The exact allowable gauge depends on the geometry and condition of the spring contacts on a given board.[^busboard-breadboard-wire-gauge]

## Detailed explanation

AWG is a gauge system in which a smaller number denotes a thicker wire. For many solderless breadboards, solid 22 AWG is a practical choice because it is stiff enough to insert reliably into internal spring clips; manufacturer BusBoard specifies a suitable range of 22–26 AWG.[^busboard-breadboard-wire-gauge]

The key distinction here is "solid." Flexible stranded wire without a crimped or soldered pin frays at the stripped end, so loose strands can fail to enter the contact clip or accidentally bridge adjacent rows. Solid wire retains its shape after bending, helping route short jumpers neatly and predictably. The insulation should be stripped back just enough for the bare conductor to seat fully in the spring clip, without leaving excess exposed wire that risks short circuits.[^adafruit-breadboard-jumpers]

Wire should never be forced into breadboard tie points. An oversized conductor can permanently stretch or deform spring contacts, whereas an undersized wire can seat loosely and produce intermittent connections. Even a single breadboard may exhibit clips with varying tension and wear, so a general gauge recommendation does not eliminate the need to verify physical fit.[^busboard-breadboard-wire-gauge]

Example: if breadboard tie points accept 22 AWG, cut a length of insulated solid wire, strip a short section from both ends, and insert the bare ends into the desired rows. For another board rated for 24 or 26 AWG, thinner wire is equally suitable; there is no single universal gauge for all solderless breadboards.[^busboard-breadboard-wire-gauge]

**Common mistake:** treating 22 AWG as a mandatory standard for every breadboard or using stranded wire merely because it is flexible and easy to handle. Always check the recommended contact gauge range and use solid wire of the appropriate diameter.
