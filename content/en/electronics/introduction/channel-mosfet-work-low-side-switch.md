---
id: emb-elintro-0253
title: "How does an N-channel MOSFET work as a low-side switch?"
track: electronics
section: introduction
sources:
  - source_id: ti-mosfet-selection
    title: "Texas Instruments: Avoid Common Mistakes When Selecting and Designing with Power MOSFETs"
    url: https://www.ti.com/lit/an/slpa021/slpa021.pdf
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

The load is connected between the supply and drain, while the source connects to common `GND`. When the control signal applies a sufficiently positive `V_GS`, the N-channel MOSFET conducts current from load to ground; `V_GS(th)` marks only the onset of conduction rather than guaranteeing a low `R_DS(on)`.[^ti-mosfet-selection]

## Detailed explanation

In a low-side switch configuration, the N-channel MOSFET is placed between the load and ground: the load connects to the positive supply rail, the drain connects to the load's lower terminal, and the source connects to common `GND`. The control signal establishes a voltage specifically between gate and source. When `V_GS` is sufficiently positive, the channel creates a conductive path from drain to source, current flows through the load, and the voltage across the load approximately equals the supply voltage assuming low switch losses.[^ti-mosfet-selection]

When the gate returns to the source potential, the channel turns off and load current ceases, aside from any paths through other circuit components. For an inductive load, current cannot drop to zero instantaneously, so an appropriate freewheeling path or voltage clamp is required. A common ground between the controller and the power circuit is essential to establish a defined control `V_GS`; otherwise, pin voltage relative to logic ground does not correspond to the actual gate-to-source voltage.[^ti-mosfet-selection]

A critical distinction is that `V_GS(th)` is not the recommended drive voltage. This parameter is specified at a minuscule current where the MOSFET only begins to conduct. For the switch to operate with low conduction losses, look in the datasheet for an `R_DS(on)` value specified at the `V_GS` that the controller can realistically deliver. For instance, one cannot automatically assume that a MOSFET with `V_GS(th) = 2 V` is fully on when driven by a 3.3 V GPIO: a guaranteed on-resistance specification at that gate voltage is required.[^ti-mosfet-selection]

In practical design, verify power dissipation via `P = I²*R_DS(on)`, thermal heating, maximum allowable `V_DS` and `V_GS`, and load transients. A common mistake is connecting a MOSFET as a switch while rating it solely by its `V_GS(th)` threshold or headline maximum current from the datasheet front page. Ratings must be evaluated under specified test conditions, taking package constraints and actual cooling into account.[^ti-mosfet-selection]
