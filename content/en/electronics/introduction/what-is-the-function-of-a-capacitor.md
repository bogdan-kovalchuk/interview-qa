---
id: emb-elintro-0004
title: What is the function of a capacitor?
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
  - source_id: aac-capacitor
    title: "All About Circuits: Capacitors and calculus"
    url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-13/capacitors-and-calculus/
  - source_id: nichicon-polarity
    title: "Nichicon: Technical notes for aluminum electrolytic capacitors"
    url: https://www.nichicon.co.jp/english/products/pdf/aluminum.pdf
---

## Short answer

A capacitor stores energy in an electric field and holds opposite charges on its electrodes. In the ideal model `i = C*dv/dt`: it carries current while voltage changes, but no current under steady DC voltage. It is used for filtering, decoupling and coupling changing signals. [^aac-capacitor]

## Detailed explanation

Capacitance relates charge to voltage through `Q = C*V`; stored energy is `E = C*V²/2`. Charge resides on the electrodes, while energy is associated with the electric field in the dielectric. A calculated 100 nF capacitor at 5 V holds 0.5 µC in magnitude on each electrode and stores 1.25 µJ. [^nichicon-polarity]

“Blocks DC” describes ideal steady state after charging, not the instant a DC supply is connected. During charging, voltage changes and current flows. For an ideal capacitor and a sinusoidal signal, the magnitude of impedance decreases with frequency; this supports coupling and filtering, but does not make every capacitor a short circuit at every AC frequency. [^aac-capacitor]

A supply decoupling capacitor near an IC supplies transient current locally and limits supply-voltage changes. Real capacitors also have leakage, ESR and parasitic inductance, so placement and component characteristics matter. A polarized capacitor must additionally obey its polarity and voltage limits. [^nichicon-polarity]
