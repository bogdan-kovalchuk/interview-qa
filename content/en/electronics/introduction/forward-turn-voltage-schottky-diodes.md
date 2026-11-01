---
id: emb-elintro-0163
title: "What is the forward turn-on voltage of Si, Ge and Schottky diodes?"
track: electronics
section: introduction
sources:
  - source_id: aac-pn-junction
    title: "All About Circuits: The P-N Junction"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/chpt-2/the-p-n-junction/
  - source_id: st-an4789
    title: "STMicroelectronics AN4789: Monolithic Schottky diode in ST F7 LV MOSFET technology"
    url: https://www.st.com/resource/en/application_note/an4789-monolithic-schottky-diode-in-st-f7-lv-mosfet-technology-improving-application-performance-stmicroelectronics.pdf
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

For standard P-N diodes, the guideline forward voltage is 0.6–0.7 V for Si and about 0.2 V for Ge; a Schottky diode often has a lower drop, about 0.3 V in the example provided by the manufacturer. These are typical guidelines, not fixed thresholds: the value depends on current, temperature, and the specific component.[^aac-pn-junction][^st-an4789]

## Detailed explanation

A diode's forward voltage cannot be determined solely by the name of the material: it is the voltage across the component at a specific forward current, not an immutable switching threshold. In a conventional P-N diode, electrons and holes are injected across the junction, so the current characteristic rises steeply with increasing forward voltage. For educational calculations, approximately 0.6–0.7 V is often assumed for a silicon junction and about 0.2 V for germanium, but these numbers depend on the operating point.[^aac-pn-junction]

In a Schottky diode, a contact is formed between a metal and a semiconductor. Current transport in it is predominantly associated with majority carriers, so less charge accumulates, and the forward drop in many applications is lower than that of a standard Si P-N diode. A value of about 0.3 V is found in the ST example for an integrated Schottky in a specific 60 V MOSFET; it cannot be transferred to every component without checking the datasheet.[^st-an4789]

For an LED, color gives only a rough idea of the emitted photon energy and often correlates with a larger forward drop for short-wavelength light. However, the exact `V_F` and current must be taken from the datasheet of the specific LED, since material, current, and temperature have an effect. An LED is not just a standard red or blue P-N diode: its composition and operating point determine the characteristic.[^aac-pn-junction]

For example, if in a series circuit calculation for a Si diode you assume a drop of 0.65 V, this is only an approximation for estimating current; ultimately you must verify the voltage against the curve or table in the datasheet at the required current and temperature. You should not treat such a drop as a rigid turn-on voltage below which current is always zero.[^aac-pn-junction]

**Common mistakes:**
- Considering the numbers 0.7 V, 0.3 V, or 0.2 V universal for all components of the corresponding type.
- Comparing forward voltages without stating current and temperature.
- Selecting `V_F` for an LED solely by color and not checking the datasheet.[^aac-pn-junction][^st-an4789]
