---
id: emb-elee-0153
title: "How do a linear regulator, an LDO, a switching converter and a charge pump differ?"
description: "How do a linear regulator, an LDO, a switching converter and a charge pump differ?"
track: electronics
section: ee101
level: junior
type: concept
tags: []
status: published
updated: 2026-10-06
content_revision: 2
reconciled_with:
  uk: 2
anki:
  export: true
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
    accessed: 2026-09-27
    kind: community
    version: null
    applicability: "Question origin: lecture 60 of the Udemy course; the original card is preserved in imports. The Ukrainian short answer and explanation were checked against cited technical sources on 2026-10-06; the course is not proof of these claims."
  - source_id: aac-alternating-current
    title: "All About Circuits textbook, Volume II: AC"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Authoritative section-level reference: AC circuits, reactance, phasors, impedance, filters and transformers; specific component values and circuits of the course can differ."
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Authoritative section-level reference: diodes, Zener diodes, bipolar and field-effect transistors and power supplies; specific component values and circuits of the course can differ."
  - source_id: ti-slva118a
    title: "Texas Instruments SLVA118A: Linear Regulator Design Guide For LDOs"
    url: https://www.ti.com/lit/an/slva118/slva118.pdf
    accessed: 2026-10-06
    kind: official
    version: "SLVA118A, April 2003, revised June 2008"
    applicability: "A linear regulator has a pass element managed by a feedback controller; input current is roughly equal to output current, the voltage difference is dissipated as heat, P_D = P_I - P_O, and Eff ≈ V_O/V_I (for small quiescent current; the formula does not apply to switching converters); dropout is the minimum V_I - V_O at which the regulator works within specification, and an LDO is a subset of linear regulators with a small dropout. An application report about LDOs, not about switching converters."
  - source_id: ti-slva079
    title: "Texas Instruments SLVA079: Understanding the Terms and Definitions of LDO Voltage Regulators"
    url: https://www.ti.com/lit/an/slva079/slva079.pdf
    accessed: 2026-10-06
    kind: official
    version: "SLVA079, October 1999"
    applicability: "In dropout the PMOS pass element behaves as a resistor, V_dropout = I_o*R_on; LDO stability depends on the series resistance of the output capacitor (CSR = ESR + added resistor) and the manufacturer specifies an allowed range, for example 0.2–9 Ω for the TPS763xx; tantalum, aluminum and ceramic capacitors are suitable if they meet the requirement. The numbers apply to one series; requirements of other LDOs come from their datasheets."
  - source_id: ti-slyt527
    title: "Texas Instruments SLYT527: Linear versus switching regulators in industrial applications with a 24-V bus (Analog Applications Journal, 3Q 2013)"
    url: https://www.ti.com/lit/an/slyt527/slyt527.pdf
    accessed: 2026-10-06
    kind: official
    version: "Analog Applications Journal, 3Q 2013"
    applicability: "Comparison of three 24 V input, 5 V output, 100 mA circuits: a synchronous buck (TPS54061) has 84.5% efficiency and 0.093 W loss, the integrated and discrete linear regulators about 20% and 2 W; the linear circuits have under 10 mV ripple, the buck 75 mV, and linear regulators are used to clean up switching-regulator outputs. Data for one board and one device, not universal numbers."
  - source_id: ti-switching-regulator-fundamentals
    title: "Texas Instruments: Switching regulator fundamentals"
    url: https://www.ti.com/lit/an/snva559c/snva559c.pdf
    accessed: 2026-10-06
    kind: official
    version: "Rev. C"
    applicability: "Sections 1–3: in a buck converter a switch alternately connects the input to an inductor, the inductor current cannot change instantly, so after the switch turns off it keeps flowing through the diode, and the output is regulated by pulse width (PWM); the converters give higher efficiency and can produce a higher or opposite-polarity voltage; fast switching creates EMI. The document does not compare them with charge pumps."
  - source_id: ti-charge-pump-basics
    title: "Texas Instruments SSZTBO1: Pump It up with Charge Pumps – Part 1 (technical article)"
    url: https://www.ti.com/lit/ta/ssztbo1/ssztbo1.pdf
    accessed: 2026-10-06
    kind: official
    version: "SSZTBO1, February 2016"
    applicability: "A charge pump stores energy in a capacitor rather than an inductor: a doubler gives an output of about 2*V_I and an inverter about -V_I; a simple circuit does not regulate its output, and a regulated doubler regulates only between V_I and 2*V_I; pumps are good for output currents of tens of milliamps, less so above 250 mA, and are less efficient than inductor-based converters unless unregulated. A general vendor assessment, not a guarantee for a specific device."
---

## Short answer

TODO

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
