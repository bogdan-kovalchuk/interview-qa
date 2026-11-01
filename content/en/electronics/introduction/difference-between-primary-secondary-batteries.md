---
id: emb-elintro-0054
title: "What is the difference between primary and secondary batteries?"
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
  - source_id: doe-primary-secondary-batteries
    title: "U.S. Department of Energy: Primer on Lead-Acid Storage Batteries"
    url: https://www.energy.gov/documents/doe-hdbk-1084-95
---

## Short answer

Primary batteries are not designed for recharging; secondary batteries, or rechargeable batteries, can be recharged with current in the reverse direction under manufacturer-specified conditions.[^doe-primary-secondary-batteries] Examples of primary cells include alkaline AA and zinc-carbon; secondary include NiMH and Li-ion.[^doe-primary-secondary-batteries]

## Detailed explanation

The division into primary and secondary batteries concerns primarily whether recharging is intended. In a primary cell, discharge consumes reactants such that it is not designed to be restored to a working charged state by passing reverse current. After exhausting usable capacity, such a cell is replaced and disposed of in an appropriate manner.[^doe-primary-secondary-batteries]

In a secondary cell, electric current during charging is directed so as to restore the charged state of the chemical system. This does not mean the battery is restored indefinitely: charge and discharge cycles gradually degrade it, while allowable voltage, current, temperature, and charging algorithms depend on chemical composition and specific model. For Li-ion, for example, compatible charge control is required; the claim that "any battery can be recharged" is hazardous.[^doe-primary-secondary-batteries]

Typical primary household cells include alkaline AA and zinc-carbon cells. Common secondary chemical systems include NiMH and Li-ion. The package format itself does not determine the type: batteries of identical size can have different chemistries, nominal voltages, and permissible charging regimes, so one must check manufacturer markings.[^doe-primary-secondary-batteries]

Example: a standard alkaline AA battery is not connected to a charger for NiMH AA simply because they share the same physical size. Proper charging depends on matching chemistry and an appropriate charging regime. A NiMH battery can be recharged with a compatible charger, yet operating lifetime and accessible capacity depend on usage conditions.[^doe-primary-secondary-batteries]
