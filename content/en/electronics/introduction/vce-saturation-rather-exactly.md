---
id: emb-elintro-0211
title: "Why is `V_CE` of a saturated transistor not zero?"
track: electronics
section: introduction
sources:
  - source_id: aac-bjt-saturation
    title: "All About Circuits: Transistor Ratings and Packages (BJT)"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/chpt-4/transistor-ratings-packages-bjt/
  - source_id: aac-bjt-active-mode
    title: "All About Circuits: Active-mode Operation (BJT)"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/chpt-4/active-mode-operation-bjt/
  - source_id: aac-bjt-beta-terms
    title: "All About Circuits: What Is BJT Beta? Understanding the Current Gain of a Bipolar Junction Transistor"
    url: https://www.allaboutcircuits.com/technical-articles/all-about-bjt-beta-understanding-terminology/
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

**Saturation does not mean zero voltage drop.** A real BJT has a non-zero `V_CE(sat)`, the value of which depends on the component, `I_C`, and base current; a range of 0.1–0.2 V is not a universal guarantee. Higher base current usually reduces the drop within the operating region and safe limits from the documentation.[^aac-bjt-saturation]

## Detailed explanation

A saturated bipolar junction transistor conducts current with a non-zero voltage drop between collector and emitter.

The ideal switch model closes contacts with zero resistance, but a BJT is a semiconductor device with internal junctions. Therefore, even when the transistor is turned on enough that the load limits the collector current, `V_CE` remains positive. In documentation, it is given as `V_CE(sat)` for specified collector and base currents; the value depends on the transistor type and measurement conditions.[^aac-bjt-saturation]

Values of 0.1–0.2 V are often used as an approximate model for simple calculations, but this is not a universal physical threshold. For a different component, current, or temperature, the drop may be different. Increasing the base current often reduces `V_CE(sat)`, but is limited by the allowable base currents and power dissipation.[^aac-bjt-saturation]

**Example:** if the calculation assumes `V_CC` = 5 V, `R_C` = 1 kΩ, and `V_CE(sat)` = 0.2 V, then the collector current is estimated as `I_C = (V_CC - V_CE(sat))/R_C = 4.8 mA`. This value is a consequence of the assumed model, not an inherent characteristic of every transistor.

**Common mistake:** considering "saturated" a synonym for "ideally closed". In a practical switch, you must account for the voltage drop across the transistor, its power dissipation, and the corresponding line in the datasheet.[^aac-bjt-saturation]
