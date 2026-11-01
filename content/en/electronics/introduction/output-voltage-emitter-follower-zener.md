---
id: emb-elintro-0195
title: "What is the output voltage of an emitter follower after a Zener?"
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
  - source_id: aac-common-collector
    title: "All About Circuits: The Common-collector Amplifier"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/chpt-4/common-collector-amplifier/
---

## Short answer

For an `NPN` emitter follower, the output at the emitter is approximately equal to the base voltage minus `V_BE`: `V_out ≈ V_Z - V_BE`. If the base is at `5.1 V`, a rough estimate with `V_BE ≈ 0.7 V` gives `4.4 V`; the actual value depends on current, temperature, and the transistor operating point.[^aac-common-collector]

## Detailed explanation

In an `NPN` emitter follower circuit, the base is connected to the Zener diode node, and the load is connected to the emitter. When the transistor conducts, the base–emitter junction has a forward voltage drop, so the emitter voltage is lower than the base voltage by approximately `V_BE`. Hence, for a simple estimate, `V_out ≈ V_Z - V_BE`; this is not an exact constant difference across all currents and temperatures.[^aac-common-collector]

For example, if `V_Z = 5.1 V` and `V_BE ≈ 0.7 V` is taken for a rough estimate, this gives `V_out ≈ 4.4 V`. The value `0.7 V` is an approximation for a silicon transistor, not a fixed voltage regardless of operating conditions. When the load current changes, the emitter current and the required base current change; accordingly, both `V_BE` and the base node voltage can change due to the non-zero output resistance of the regulator.[^aac-common-collector] [^aac-semiconductors]

The output also cannot exceed the limits allowed by the supply and the transistor operating region. With insufficient headroom margin between the collector and emitter voltages, the transistor enters saturation and no longer maintains the standard emitter follower relationship. For a real design, you should check the minimum supply voltage, maximum current, transistor power dissipation, and the condition that the Zener diode maintains the required current under maximum load.[^aac-common-collector] [^aac-semiconductors]

**Common mistake:** assuming `V_BE` is always exactly `0.7 V` and promising an exact `4.4 V` at the output. This is only an engineering estimate; accuracy requirements demand considering the transistor characteristics and the current dependence of the Zener node.[^aac-common-collector]
