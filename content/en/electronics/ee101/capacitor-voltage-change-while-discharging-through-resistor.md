---
id: emb-elee-0034
title: "How does the capacitor voltage change while discharging through a resistor?"
track: electronics
section: ee101
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-alternating-current
    title: "All About Circuits textbook, Volume II: AC"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
  - source_id: gatech-rc-charging-discharging
    title: "Georgia Tech Physics Book: Charging and Discharging a Capacitor"
    url: https://physicsbook.gatech.edu/Charging_and_Discharging_a_Capacitor
---

## Short answer

When a charged capacitor discharges through a resistor, its voltage decays according to `V_C(t) = V_0*e^(-t/τ)`, where `τ = R*C` for a simple RC loop. After `1τ`, `3τ`, and `5τ`, approximately 36.8%, 5.0%, and 0.7% of the initial voltage remains, respectively.[^gatech-rc-charging-discharging]

## Detailed explanation

TODO
