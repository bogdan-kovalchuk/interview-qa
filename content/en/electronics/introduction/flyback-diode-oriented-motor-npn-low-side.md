---
id: emb-elintro-0232
title: "How should a flyback diode be oriented on a motor with an NPN low-side switch?"
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
  - source_id: ti-inductive-load-clamping
    title: "TI: Switching Inductive Loads with DRV89xx-Q1 Devices"
    url: https://www.ti.com/document-viewer/lit/html/slvaf04
---

## Short answer

In a typical circuit with an NPN low-side switch, the flyback diode cathode connects to the positive supply rail of the coil, and the anode connects to the node between the coil and collector. In this configuration, the diode is reverse-biased while the motor is powered and conducts after the switch turns off, when the coil reverses polarity to maintain current flow.[^ti-inductive-load-clamping]

## Detailed explanation

In a low-side circuit, one end of the motor or relay is connected to the positive supply rail and the other to the collector of the NPN transistor; the emitter is usually connected to ground. When turned on, the transistor pulls the collector node toward ground, applying nearly the full supply voltage across the coil while the diode is properly oriented. The diode cathode is tied to the positive supply and the anode to the collector node, making the diode reverse-biased in this state.[^ti-inductive-load-clamping]

When the transistor turns off, winding current cannot change instantaneously. The coil drives the collector node potential above the positive supply rail until the diode becomes forward-biased. Current then circulates through the coil and diode in a local loop, clamping collector voltage and mitigating voltage stress on the transistor. In applications where relay dropout speed or motor current decay rate is critical, note that the low clamping voltage of a standard diode slows this process.[^ti-inductive-load-clamping]

**Common mistake:** orienting the diode based on the cathode band marking without verifying connection nodes on the schematic. The band on the package indicates the cathode, so it must connect to the positive side of the coil. Confirm that the diode does not conduct when the switch is on and that its rated current handles coil current prior to turn-off. For other driver topologies, such as an H-bridge, polarity and clamp location may differ – do not transfer this rule without analyzing the circuit.[^ti-inductive-load-clamping]
