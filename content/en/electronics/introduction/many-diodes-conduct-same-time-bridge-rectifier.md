---
id: emb-elintro-0181
title: "How many diodes conduct at the same time in a bridge rectifier?"
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
  - source_id: bridge-rectifier-operation
    title: "Full Wave Rectifier and Bridge Rectifier Theory"
    url: https://www.electronics-tutorials.ws/diode/diode_6.html
---

## Short answer

During each half-cycle, a pair of diodes conducts, so there are two `V_F` drops in the current path. This is significant for low-voltage supplies where a loss of `2V_F` can be substantial.[^bridge-rectifier-operation] [^aac-semiconductors]

## Detailed explanation

In a bridge rectifier, during each half-cycle two diagonally positioned diodes conduct, while the other two block current. The direction of current through the load remains the same, even though the polarity of the source voltage alternates.[^aac-semiconductors]

When the input voltage has one polarity, current flows from one AC input through the first diode to the positive output, passes through the load, and returns through the second diode to the other input. On the next half-cycle, the other diagonal pair becomes conductive. Therefore, both half-cycles create pulses of the same polarity.[^aac-semiconductors]

This does not mean all four diodes conduct simultaneously. In each current path, two diodes operate in series, so their forward voltage drops add up and reduce the voltage available to the load. The actual drop depends on current, temperature, and diode type; calculating with a constant value is only an approximation.[^aac-semiconductors]

Example: during the positive half-cycle, the pair D1–D2 conducts, and during the negative, D3–D4. If each diode has approximately a 0.7 V drop at a given current, the path loses about 1.4 V; this is an illustration, not a guaranteed parameter.[^aac-semiconductors]

**Common mistake:** assuming that current flows through all four diodes in the bridge simultaneously, or subtracting the drop of only a single diode. To verify the circuit, trace the closed loop for both source polarities.
