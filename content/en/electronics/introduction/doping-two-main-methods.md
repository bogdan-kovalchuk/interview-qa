---
id: emb-elintro-0036
title: "What is doping and what are its two main methods?"
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
  - source_id: aac-dopant-process
    title: "Analog Devices, Semiconductor Processing of NPN Transistors"
    url: https://www.allaboutcircuits.com/textbook/designing-analog-chips/analog-devices/semiconductor-processing-of-npn-transistors/
---

## Short answer

Doping is the controlled introduction of impurity atoms into a semiconductor to alter its charge carrier concentration and conductivity.[^aac-dopant-process] The primary methods are thermal diffusion of dopants at elevated temperatures and ion implantation, in which accelerated ions are introduced into the crystal; after implantation, annealing is typically required.[^aac-dopant-process] Implantation offers more precise dose control, but method selection depends on the target doping profile and manufacturing process.

## Detailed explanation

Doping is the introduction of a controlled quantity of impurity atoms into a semiconductor crystal to regulate the number of electrons or holes available for charge transport.[^aac-semiconductors] For silicon, the choice of dopant also determines the conductivity type: donor atoms provide excess electrons, whereas acceptor atoms create holes.[^aac-semiconductors]

During thermal diffusion, a wafer is heated in an environment containing the dopant. Atoms diffuse from the surface into the silicon; heating affects both depth and concentration distribution, so the boundary of the doped region is not perfectly sharp.[^aac-dopant-process]

During ion implantation, dopant atoms are ionized and accelerated by an electric field, then driven into the wafer. Both the dose and penetration depth are controlled more precisely, but collisions damage the crystal lattice. Therefore, thermal annealing is performed after implantation to restore the crystal lattice and activate the dopants.[^aac-dopant-process]

Example: to form a localized region with a specified profile, a process engineer may apply implantation through a mask and tune annealing to activate the dopants while limiting their further diffusion. Exact parameters are defined by the specific manufacturing process rather than a universal rule.

The concentration profile is critical because it determines where the junction forms and how the resistance of the region varies. During diffusion, temperature and cycle duration influence both penetration depth and boundary spreading. Implantation makes it possible to set ion dose and energy independently, but it does not eliminate the subsequent thermal process: dopant atoms must occupy appropriate lattice sites to become electrically active.[^aac-dopant-process]
