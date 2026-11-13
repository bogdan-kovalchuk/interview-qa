---
id: emb-elee-0219
title: "Why is a flyback diode placed across a motor, and how is it connected?"
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
  - source_id: fiore-bjt-switching
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 4.7 BJT Switching and Driver Applications"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/04:_Bipolar_Junction_Transistors_(BJTs)/4.7:_BJT_Switching_and_Driver_Applications
  - source_id: fiore-ac-circuit-analysis
    title: "James M. Fiore: AC Electrical Circuit Analysis, A Practical Approach (sections 1.5 and 10.3)"
    url: https://www2.mvcc.edu/users/faculty/jfiore/Circuits2/ACElectricalCircuitAnalysis.pdf
  - source_id: libretexts-fiore-diode-models
    title: "Fiore: Semiconductor Devices, 2.4 Diode Circuit Models (Engineering LibreTexts)"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/02:_PN_Junctions_and_Diodes/2.4:_Diode_Circuit_Models
---

## Short answer

A motor is an inductive load: when the switching transistor turns off, inductor current cannot drop instantaneously to zero, generating a high-voltage inductive spike. Connecting a flyback diode with its cathode to the positive supply and its anode to the collector provides a safe recirculation path for this decaying current; during normal conduction, the diode is reverse-biased.[^fiore-bjt-switching]

## Detailed explanation

**Origin of the spike.** For an inductor, `v = L*di/dt`: faster rates of current change generate higher voltages.[^fiore-ac-circuit-analysis] Current flowing through motor windings cannot collapse instantaneously, so when the switching transistor turns off, the collapsing magnetic field induces a reverse-polarity voltage across the winding that appears directly between collector and emitter.[^fiore-bjt-switching] As an illustrative example: a winding with `L = 10 mH` carrying `I = 1 A` that shuts off in `10 µs` generates `v = 0.01*1/(10*10^-6) = 1000 V`, tens of times higher than a typical 12 V supply. Such inductive spikes easily destroy the switching transistor.[^fiore-bjt-switching]

**Where to place the diode.** The flyback diode is connected in parallel with the motor: cathode to the positive supply rail, anode to the collector. During normal conduction, the transistor is turned on and the collector is pulled near ground; the cathode sits at +12 V while the anode is near ground, keeping the diode reverse-biased and non-conducting.[^fiore-bjt-switching] When the transistor turns off, the collector voltage spikes upward; as soon as it exceeds `V_CC` by approximately 0.7 V, the diode becomes forward-biased.[^libretexts-fiore-diode-models] Winding current then recirculates safely through the diode, clamping the collector voltage to approximately `V_CC + 0.7 V` under the knee-voltage diode model.

**Common mistakes:**

- Installing the diode with reversed polarity (anode to positive rail, cathode to collector): when the transistor turns on, the diode conducts directly from `+V` through the transistor to ground, creating a dead short circuit.
- Assuming the diode interferes with normal motor operation: during normal conduction, the diode is reverse-biased and draws zero current.[^fiore-bjt-switching]
