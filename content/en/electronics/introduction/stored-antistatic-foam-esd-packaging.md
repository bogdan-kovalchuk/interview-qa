---
id: emb-elintro-0028
title: "Why are `IC`s stored in antistatic foam or `ESD` packaging?"
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
  - source_id: ti-esd-packaging
    title: "Texas Instruments: Electrostatic Discharge (ESD) Protective Semiconductor Packing Materials and Configurations"
    url: https://www.ti.com/lit/an/szza027a/szza027a.pdf
---

## Short answer

ESD packaging limits charge accumulation and protects electrostatic discharge-sensitive components during storage and handling. Its material and construction must match the required level of protection; not every antistatic foam shields against discharge.[^ti-esd-packaging]

## Detailed explanation

The leads and internal structures of an integrated circuit can be damaged by electrostatic discharge, even if the component remains partially functional afterward. Protection is therefore necessary not only during transport: handle components in an appropriate ESD-protected area and use packaging designed for ESD-sensitive devices.[^ti-esd-packaging]

Packaging can serve different functions. Low-charging material reduces the charge generated during friction or separation; dissipative material allows charge to bleed off in a controlled manner, while a shielding enclosure attenuates external electric fields or discharges. A specific package may combine these properties, but the word "antistatic" alone does not prove that it provides full protection against direct discharge.[^ti-esd-packaging]

Foam for components also varies in its electrical properties; conductive foam can short leads together, so it is used only when that is safe for the specific component. Do not touch the leads and do not rely on packaging material as a substitute for workstation grounding and proper ESD procedures.[^ti-esd-packaging]

**Practical rule:** keep the IC in packaging marked for ESD protection until working with it in a prepared area. Do not replace such packaging with ordinary styrofoam padding or a plastic bag.[^ti-esd-packaging]
