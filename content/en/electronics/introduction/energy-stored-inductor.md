---
id: emb-elintro-0137
title: "Where is energy stored in an inductor?"
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
  - source_id: openstax-inductance-energy
    title: "OpenStax College Physics 2e: 23.9 Inductance"
    url: https://openstax.org/books/college-physics-2e/pages/23-9-inductance
---

## Short answer

An inductor's energy is stored in the magnetic field created by the current in its winding. For a linear inductor, `E = L*I²/2`, where `L` is the inductance and `I` is the instantaneous current.[^openstax-inductance-energy]

## Detailed explanation

An inductor stores energy in its magnetic field, which forms around the winding when current flows through it. For a linear inductor, the energy equals `E = L*I²/2`: it depends on the inductance `L` and the square of the current `I`.[^openstax-inductance-energy]

The dependence on the square of the current is important: if the current is doubled for an unchanged inductance, the stored energy increases fourfold. For example, for an idealized coil with `L = 10 mH` and current `I = 2 A`, this gives `E = 0.01*2²/2 = 0.02 J`. In a real component, allowable current is limited by winding heating and, for cores, by saturation; during saturation, inductance can change, so the simple linear model becomes less accurate.[^openstax-inductance-energy]

This energy is not the "energy of current" as a separate substance: current maintains the magnetic field, and the field is the site of energy storage. When current decreases, the field weakens, and energy is transferred back into the circuit or dissipated in its resistances. Because of this, breaking the coil's circuit without a current path can induce a significant voltage opposing the rapid drop in current.[^openstax-inductance-energy]

**Common mistake:** Confusing the location of energy storage with the copper of the winding. The winding creates the field and conducts current, but in an ideal model, the stored energy is described by the magnetic field itself.
