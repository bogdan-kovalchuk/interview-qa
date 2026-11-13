---
id: emb-elintro-0242
title: "Why can the term `saturation` in a MOSFET be confusing after the BJT?"
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

In a BJT, `saturation` means that both junctions are forward-biased and the switching transistor exhibits a low `V_CE`; it is not simply a synonym for being fully on. In a MOSFET, `saturation` means channel pinch-off near the drain and typically corresponds to the amplification region. An on-state MOSFET switch operates in the `linear/triode` region with low `R_DS(on)`.[^aac-semiconductors] [^toshiba-mosfet-drive]

## Detailed explanation

The word `saturation` carries different meanings in a BJT and a MOSFET, so mechanically transferring the term from one to the other easily leads to an improper operating point. In a BJT, saturation describes the state where both the base-emitter and base-collector junctions are forward-biased. In a typical low-side switch, this results in a low `V_CE`, though the exact voltage drop depends on collector current and base drive.[^aac-semiconductors]

For an enhancement-mode MOSFET, the `saturation` region is defined when `V_DS` reaches approximately `V_GS - V_th`, causing channel pinch-off near the drain. In a simplified model, the current thereafter varies much more weakly with increasing `V_DS`, so this region is frequently used for amplification. It does not imply zero resistance or a "fully turned-on" switch state.[^toshiba-mosfet-drive]

An on-state power MOSFET typically operates at a low `V_DS`, below the pinch-off boundary, in the `linear/triode` region. There, the channel exhibits a low `R_DS(on)`, whose value the manufacturer specifies for particular `V_GS` and measurement conditions. It is this mode that yields a low voltage drop across the transistor during conduction.[^toshiba-mosfet-drive]

Example: in a switching circuit with sufficient `V_GS` where the load determines current, the MOSFET settles at a small `V_DS` dictated by the current and effective channel resistance. If the load voltage instead forces the transistor to support a large `V_DS`, it can enter `saturation`; sizing it as a low-loss switch requires checking the load conditions and datasheet rather than relying on the mode name alone.[^toshiba-mosfet-drive]

**Common mistake:** assuming saturation means the same thing for both transistor types. To avoid confusion, relate the term to the characteristic curves and physical conditions of the specific device: forward-biased junctions in a BJT versus channel pinch-off in a MOSFET.[^aac-semiconductors] [^toshiba-mosfet-drive]
