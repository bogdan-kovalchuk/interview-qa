---
id: emb-elintro-0241
title: "What are the three main operating modes of a MOSFET?"
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

In an enhancement-mode MOSFET, the primary modes are `cutoff`, `linear/triode`, and `saturation`: below threshold `V_GS` the channel barely conducts, in `linear` it exhibits low resistance suitable for switching, and in `saturation` current depends weakly on `V_DS`, which is useful for amplification. The threshold is not a hard cutoff of zero current, and operating conditions depend on polarity and device type.[^toshiba-mosfet-drive]

## Detailed explanation

The operating modes of an enhancement-mode MOSFET describe how the gate-to-source voltage and drain-to-source voltage govern the channel current. The terms `cutoff`, `linear`, and `saturation` refer to different regions of the output characteristic curves rather than three distinct transistor types.[^toshiba-mosfet-drive]

In `cutoff`, `V_GS` is insufficient to establish a conducting channel. In a real component, this translates to a small leakage current rather than mathematically zero current; the `V_th` rating in the datasheet is measured under specific test conditions and does not promise low channel resistance under heavy loads. For a MOSFET to act as an effective switch, its gate must be driven with the voltage at which the datasheet specifies `R_DS(on)`.[^toshiba-mosfet-drive]

In `linear` or `triode`, the channel is formed and `V_DS` is small compared to the gate overdrive. In this region, the channel behaves approximately like a voltage-controlled resistor, which is where a fully turned-on power switch operates. The label `linear` describes this portion of the characteristic curves; it does not mean the component is operating as a linear amplifier.[^toshiba-mosfet-drive]

In `saturation`, the channel undergoes pinch-off near the drain, and as `V_DS` increases, the current in a simplified model changes much more weakly than in the linear region. While this region is useful for amplification, it is not the desired "fully turned-on" state for a power switch: at the same drain current, the voltage across the transistor and the resulting power dissipation can be substantial.[^toshiba-mosfet-drive]

Example: in a typical low-side switch, a sufficient `V_GS` drives the MOSFET into the `linear` region with minimal voltage drop; when gate drive is removed, it transitions into `cutoff`. Always verify the required gate voltage under the conditions for which the manufacturer guarantees on-resistance, and never infer on-state current capability from `V_th` alone.[^toshiba-mosfet-drive]

**Common mistake:** calling the `saturation` mode a "saturated, fully turned-on switch" state. In a MOSFET, this designates the pinch-off region; the low resistance needed for switching is provided by the `linear/triode` region.[^toshiba-mosfet-drive]
