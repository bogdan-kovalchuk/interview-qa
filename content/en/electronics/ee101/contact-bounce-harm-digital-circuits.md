---
id: emb-elee-0007
title: "What is contact bounce and why does it harm digital circuits?"
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
  - source_id: ti-switch-debounce
    title: "Texas Instruments: Debounce a Switch, SCEA094"
    url: https://www.ti.com/document-viewer/lit/html/SCEA094
---

## Short answer

During transition, mechanical switch contacts can rapidly make and break connection multiple times, creating several electrical edges instead of a single transition. A fast digital input can register these transitions as multiple events, requiring hardware or software debouncing; bounce duration depends on the specific component.[^ti-switch-debounce]

## Detailed explanation

Contact bounce is a brief sequence of unwanted makes and breaks that occurs when mechanical contacts touch or separate. Due to elasticity and impact dynamics, a contact does not necessarily stabilize immediately upon actuation: the voltage may transition between logic levels multiple times. For a logic circuit, these transitions represent real input events rather than mere visible noise on a waveform plot.[^ti-switch-debounce]

The problem becomes evident when a single button press increments a counter multiple times, triggers multiple interrupts, or repeatedly toggles a state machine. This happens when the system reacts faster than the contact can settle. TI cites examples of mechanical switches with bounce lasting hundreds of microseconds, whereas logic devices can respond in nanoseconds; this illustrates the scale of the difference but does not establish a universal duration for every button.[^ti-switch-debounce]

Debounce introduces a rule under which a state change is accepted only after the signal stabilizes. In hardware implementations, an RC network limits fast transitions while a Schmitt trigger shapes a clean logic edge; dedicated debouncer ICs are also available. In software implementations, after the first edge, the controller samples the signal again after a chosen delay and confirms the event only if the state remains steady. The debounce interval must be matched to the switch characteristics and system response requirements rather than picking a single fixed number for all devices.[^ti-switch-debounce]

Example: for a button press counter, firmware can capture the initial edge, temporarily ignore subsequent transitions, and then read the input again. If it is still active, the press is confirmed; afterward, the logic waits for a stable release, otherwise a prolonged press might be reinterpreted. For an input that must operate without an active MCU, hardware debouncing is appropriate.[^ti-switch-debounce]

**Common mistakes:** assuming that a single mechanical click always produces a single clean edge, or specifying a fixed debounce duration without testing the specific switch. The filter must suppress short transients while remaining fast enough to meet the required system response.[^ti-switch-debounce]
