---
id: emb-elintro-0260
title: "What is a practical MOSFET selection checklist for a load?"
track: electronics
section: introduction
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-direct-current
    title: "All About Circuits textbook, Volume I: DC"
    url: https://www.allaboutcircuits.com/textbook/direct-current/
  - source_id: ti-mosfet-selection
    title: "Texas Instruments: MOSFET Selection Guide for BQ2575x Family"
    url: https://www.ti.com/lit/an/sluaax9/sluaax9.pdf
  - source_id: infineon-mosfet-layout
    title: "Infineon: Designing with power MOSFETs"
    url: https://www.infineon.com/assets/row/public/documents/24/42/infineon-designing-with-power-mosfets-applicationnotes-en.pdf?fileId=8ac78c8c7ddc01d7017e6c619a490f47
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
---

## Short answer

Verify maximum drain-source voltage and operating current under real conditions, guaranteed `R_DS(on)` at available `V_GS`, power dissipation, safe operating area (SOA), and junction temperature.[^ti-mosfet-selection] For switching applications, additionally evaluate `Q_g`, body diode reverse recovery, and package-to-PCB thermal dissipation capabilities.[^infineon-mosfet-layout]

## Detailed explanation

MOSFET selection begins with the load operating conditions: maximum operating voltage including transient spikes, continuous and pulsed currents, switching frequency, ambient temperature, and available gate drive voltage. The `V_DS` rating must withstand actual voltage spikes with a reasonable engineering margin; absolute maximum ratings alone do not replace transient circuit analysis. For an inductive load, separately determine the freewheeling current path during turn-off and the necessary overvoltage protection.[^ti-mosfet-selection]

Check the `R_DS(on)` table at the gate-source voltage actually delivered by the driver. Calculate approximate conduction losses as `P_cond = I_RMS²*R_DS(on)` for the corresponding current profile and adjust the resistance for operating junction temperature. For a switching application, take gate charge, frequency, and voltage/current transitions into account; a low on-resistance alone does not guarantee low total losses.[^ti-mosfet-selection]

Verify the Safe Operating Area (SOA), maximum junction temperature, thermal resistance, and the specific conditions under which the current rating is specified. The datasheet `I_D` may assume a fixed case temperature or ideal cooling, so a real-world PCB design requires a thermal calculation that factors in the package, copper area, and thermal vias. Also verify the absolute maximum `V_GS` rating and the driver's ability to safely charge and discharge the gate.[^infineon-mosfet-layout] [^ti-mosfet-selection]

For inductive or bridge loads, evaluate the body diode forward drop, current rating, and reverse-recovery parameters; determine whether diode conduction occurs during dead time. Finally, verify the pinout, footprint, channel polarity, and specific connection circuit. No single parameter – neither low `R_DS(on)` nor a massive headline current rating – confirms component suitability without meeting all remaining application requirements.[^infineon-mosfet-layout]

**Common mistakes:**

- Selecting a part based solely on the headline `I_D` on the front page of the datasheet while ignoring the thermal conditions required for that rating.
- Using an `R_DS(on)` value specified at a different gate voltage or at room temperature without temperature derating.
- Failing to verify `V_DS` spikes, SOA, gate ratings, and body diode characteristics for inductive loads.
