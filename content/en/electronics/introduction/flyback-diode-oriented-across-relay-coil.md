---
id: emb-elintro-0219
title: "How should a flyback diode be oriented across a relay coil?"
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
---

## Short answer

The diode cathode is connected to `+V`, and the anode is connected to the side of the coil pulled by the transistor. During normal operation the diode is off, and upon turn-off it turns on to provide a recirculation path for the coil current.[^aac-semiconductors]

## Detailed explanation

A flyback diode is connected in parallel with the coil so that it is reverse-biased during normal operation and can conduct the coil current after the switch turns off. Inductance opposes rapid changes in current: when the switch opens the circuit, the coil reverses its voltage polarity in an effort to maintain the previous current direction. The diode creates a closed path in which this current gradually decays, clamping the transient voltage across the switch.[^aac-semiconductors]

In a typical circuit with a low-side NPN transistor, one end of the coil is connected to `+V` and the other to the collector. The diode cathode is connected to `+V`, and the anode to the collector side of the coil. While the switch is on, the voltage at the anode is lower than the voltage at the cathode, so the diode does not shunt the coil. After turn-off, the polarity reverses, the diode turns on, and it conducts current in the coil loop.[^aac-semiconductors]

This orientation specifically assumes the indicated DC switch topology. If the coil is switched by an H-bridge, carries AC voltage, or the switch is on the other side, the "cathode to supply" rule cannot be mechanically transferred: one must first determine polarity in normal operation and then select the clamping path. The diode ratings must also match the initial coil current and supply voltage. A standard diode provides a low clamping voltage and therefore demagnetizes the coil more slowly; when release time is critical, a higher controlled clamp level can accelerate current decay, but increases voltage stress on the switch.[^aac-semiconductors]

**Common mistake:** installing the diode forward-biased during normal operation. In that case, it conducts supply current instead of waiting for turn-off, which can cause excessive current or a short circuit. Before powering on, verify polarity at the coil itself rather than solely on a schematic symbol, and ensure the diode is connected directly across its terminals.[^aac-semiconductors]
