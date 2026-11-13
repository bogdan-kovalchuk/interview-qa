---
id: emb-elcirc-0007
title: "What is the difference between conventional current and electron flow?"
track: electronics
section: circuit-analysis
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-direct-current
    title: "All About Circuits textbook, Volume I: DC"
    url: https://www.allaboutcircuits.com/textbook/direct-current/
  - source_id: aac-conventional-electron-flow
    title: "All About Circuits: Conventional Versus Electron Flow"
    url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-1/conventional-versus-electron-flow/
---

## Short answer

**Conventional current** is defined as the direction in which positive charge would move, which in metallic conductors is opposite to the average drift of negative electrons. Both conventions yield identical physical calculations, but standard circuit analysis and component schematic symbols adhere to conventional current.[^aac-conventional-electron-flow]

## Detailed explanation

Electric current is defined as the rate and direction of positive charge flow. This convention was established before the discovery of the electron and remains standard across schematic notation, semiconductor device symbols, and engineering calculations. Consequently, a current arrow in a schematic does not necessarily track the trajectory of physical particles; it establishes the sign reference and coordinate direction for circuit analysis.[^aac-conventional-electron-flow]

In metallic conductors, mobile charge carriers are negatively charged electrons. Under an applied electric field, their net drift velocity opposes conventional current. For example, in a simple battery circuit, conventional current flows through the external circuit from the positive terminal to the negative terminal, whereas conduction electrons drift from the negative terminal to the positive terminal. This describes directed drift velocity; the random thermal motion of electrons is orders of magnitude faster, but its zero mean vector produces no net current.[^aac-conventional-electron-flow]

For circuit analysis, mathematical sign consistency is more critical than the physical nature of the charge carriers. If a calculation yields a negative value relative to an assumed arrow, the physical conventional current flows opposite to that arrow. There is no need to reformulate network equations for electron flow; maintaining a consistent sign convention is sufficient. In semiconductors, conduction involves both electrons and holes; the statement that electrons travel from negative to positive describes metallic conduction, rather than all carriers across all materials.[^aac-conventional-electron-flow]

**Common mistakes:**

- Describing the direction of conventional current as the physical direction of electron travel in a metallic wire.
- Treating a negative current calculation as an error rather than an indication of physical flow opposing the assigned reference arrow.
- Applying a purely electronic conduction model to semiconductors without accounting for hole conduction.[^aac-conventional-electron-flow]
