---
id: emb-elintro-0092
title: "When is P &gt; 0 and when is P &lt; 0 in a circuit element?"
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
  - source_id: aac-polarity-voltage-drops
    title: "All About Circuits: Polarity of voltage drops"
    url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-2/polarity-voltage-drops/
---

## Short answer

Under the passive sign convention `P = V*I`, positive power means the element absorbs energy: reference current enters the terminal marked positive for voltage. Negative power means the element delivers energy to the circuit; the sign is determined by the chosen reference directions and polarity, not by component type.[^aac-polarity-voltage-drops]

## Detailed explanation

The sign of power describes the direction of energy transfer relative to the chosen reference frame. In the passive sign convention, you first assign the reference voltage polarity across a two-terminal element, and the reference current direction is defined as positive when entering the terminal marked with '+'. The product `P = V*I` is then positive when the element absorbs power, and negative when it delivers power.[^aac-polarity-voltage-drops]

The convention does not require guessing the actual physical direction prior to calculation. If the chosen reference current direction turns out to be opposite to the actual flow, the circuit solution simply yields a negative value for current. Similarly, the sign of the product of voltage and current indicates the power flow. It is essential to keep the initial reference directions unchanged throughout the entire calculation and interpret the signs consistently at the end.[^aac-direct-current] [^aac-polarity-voltage-drops]

For example, a resistor with a positive `V` and current entering its positive terminal has `P > 0` and converts electrical energy into heat. For a battery supplying a circuit, if voltage is defined from its positive terminal to its negative terminal, current typically leaves the positive terminal; under the passive convention, this yields `P < 0`, meaning the battery supplies energy. During charging, the current direction through the battery reverses, and it will have positive power because it absorbs energy.[^aac-direct-current]

**Common mistakes:**
- Calling any source element negative by definition. A source can absorb power in charging or regenerative braking modes.
- Assuming that the direction of conventional current alone determines the sign of power, without clarifying the reference voltage polarity across the terminals of the element.[^aac-polarity-voltage-drops]
