---
id: emb-elintro-0041
title: "What is electric current and what is its unit?"
track: electronics
section: introduction
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-voltage-current-resistance
    title: "All About Circuits: Ohm’s Law - How Voltage, Current, and Resistance Relate"
    url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-2/voltage-current-resistance-relate/
  - source_id: aac-direct-current
    title: "All About Circuits textbook, Volume I: DC"
    url: https://www.allaboutcircuits.com/textbook/direct-current/
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
---

## Short answer

Current is the rate of electric charge transfer through a cross-section: `I = ΔQ/Δt` for the average value. The unit of current is the ampere (A), where `1 A = 1 C/s`; one coulomb corresponds to approximately `6.24×10¹⁸` elementary charges.[^aac-voltage-current-resistance]

## Detailed explanation

Electric current describes how quickly charge passes through a chosen surface, such as a wire cross-section. If during a time interval `Δt` a charge `ΔQ` passes through this cross-section, the average current equals `I = ΔQ/Δt`. For the instantaneous value, the limit of this ratio is used, that is, the time derivative of charge; in simple problems with constant current, the average ratio suffices.[^aac-voltage-current-resistance]

The ampere is the SI unit of current. The equality `1 A = 1 C/s` means that one coulomb of charge passes through the cross-section per second, not that exactly one electron moves. The magnitude of the elementary charge of an electron is approximately `1.602×10⁻¹⁹ C`, so one coulomb corresponds to approximately `6.24×10¹⁸` electrons in magnitude. In a metal, the electrons themselves drift in the direction opposite to the conventional direction of current, but the sign and direction of current are defined by convention with respect to positive charge.[^aac-voltage-current-resistance]

Example: if over `2 s` a charge of `6 C` passes through the cross-section, the average current is `3 A`. Such a calculation requires the charge that specifically crossed the chosen cross-section during the specified interval; it should not be confused with the amount of charge stored in a component or with voltage. In an AC circuit, current can vary with time and direction, so a single average value over a long interval may be insufficient to describe the signal.[^aac-voltage-current-resistance]

**Common mistake:** equating the ampere with the number of electrons or assuming that `1 A` means one electron per second. The ampere measures the rate of charge flow over time, while the number of carriers depends on the charge of each carrier and the measurement interval.
