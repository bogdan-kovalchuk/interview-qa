---
id: emb-elintro-0243
title: "What is R_DS(on) and why does it matter?"
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
  - source_id: toshiba-mosfet-drive
    title: "Toshiba: MOSFET Gate Drive Circuit, Application Note"
    url: https://toshiba.semicon-storage.com/info/TPH4R50ANH1_application_note_en_20180726_AKX00068.pdf?did=59460&prodName=TPH4R50ANH1
---

## Short answer

`R_DS(on)` is the channel resistance between drain and source of an on-state MOSFET under specified conditions, particularly `V_GS` and junction temperature. For continuous current, conduction losses are approximately `P = I²*R_DS(on)`, so lower resistance directly reduces these losses; it does not account for switching, gate drive, or other loss mechanisms.[^toshiba-mosfet-drive]

## Detailed explanation

`R_DS(on)` is the MOSFET channel resistance between drain and source when the transistor is properly driven in the on-state. It is a conduction parameter of a power switch, not a fixed resistor that holds across all voltages and temperatures.[^toshiba-mosfet-drive]

The manufacturer specifies `R_DS(on)` at particular `V_GS` values and junction temperatures. If the driver delivers a voltage close to `V_th`, the MOSFET may begin conducting, but the channel will not yet reach the low resistance listed in the specifications table. When selecting a component, check the guaranteed value at the actual gate voltage available in the circuit; also account for the fact that resistance typically rises with temperature.[^toshiba-mosfet-drive]

When current flows through the channel, its resistance produces a voltage drop and heating. For approximately steady DC current, conduction losses are calculated using `P = I²*R_DS(on)`. For example, at `I = 5 A` and `R_DS(on) = 25 mΩ`, an idealized approximation yields `P = 5²*0.025 = 0.625 W`; this calculation accounts only for conduction loss, assuming a constant 25 mΩ.[^toshiba-mosfet-drive]

In an actual circuit, resistance depends on heating, component tolerance spread, and gate drive conditions. Check the package and PCB thermal resistance alongside the operating point: a low `R_DS(on)` rating by itself does not guarantee an acceptable junction temperature. In pulsed switching applications, switching losses and gate-drive losses arise as well, which this simple formula does not capture.[^toshiba-mosfet-drive]

**Common mistake:** taking the lowest headline `R_DS(on)` value from the front page of a datasheet without verifying test conditions. Ensure that the electrical characteristics table guarantees that value at your available `V_GS`, and evaluate heating under the currents and temperatures of your real-world application.[^toshiba-mosfet-drive]
