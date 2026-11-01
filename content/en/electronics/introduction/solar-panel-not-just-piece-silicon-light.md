---
id: emb-elintro-0076
title: "Why is a solar panel not just a piece of silicon in the light?"
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
  - source_id: doe-pv-cells
    title: "U.S. Department of Energy: PV Cells 101"
    url: https://www.energy.gov/cmei/systems/articles/pv-cells-101-primer-solar-photovoltaic-cell
---

## Short answer

The `P-N` junction and electrical contacts help separate photogenerated charge carriers and collect them into an external circuit. Light transfers energy to electrons in the semiconductor; the cell design allows extracting current rather than merely heating the silicon.[^doe-pv-cells]

## Detailed explanation

A solar cell is a semiconductor device in which absorbed light creates mobile charge carriers, and the internal structure helps produce a useful current. Silicon by itself is not a ready source of electrical energy: doped regions, the junction, contacts, and an external circuit are all essential.[^doe-pv-cells]

A photon with sufficient energy for the material can excite an electron, leaving behind a hole. In a typical silicon cell, the electric field in the `P-N` junction region helps separate electrons and holes before they recombine. Contacts collect the charges, and a closed external circuit provides electrons with a path through the load. It is the light's energy that sustains this process; the cell does not create charge out of nothing.[^doe-pv-cells]

Not all of the light energy is converted into electrical energy: some photons are not absorbed, and the excess energy of absorbed photons can turn into heat. Therefore, voltage and current depend on material, irradiance, temperature, and load. A single cell delivers limited power, so cells are combined into modules, and modules into a system. An inverter can convert the array's direct current to alternating current for compatibility with the utility grid.[^doe-pv-cells]

**Common mistake:** believing that light simply "knocks electricity out" of any piece of silicon. Extracting current reliably requires a semiconductor structure and contacts, and power depends on how well the photons and operating conditions match the cell.[^doe-pv-cells]
