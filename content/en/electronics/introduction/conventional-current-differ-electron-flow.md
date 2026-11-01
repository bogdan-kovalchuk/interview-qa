---
id: emb-elintro-0031
title: "What is conventional current and how does it differ from electron flow?"
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
  - source_id: aac-conventional-electron-flow
    title: "All About Circuits: Conventional Versus Electron Flow"
    url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-1/conventional-versus-electron-flow/
---

## Short answer

In a metallic conductor, electrons drift opposite to conventional current: this direction is defined as if positive charge were moving. Both conventions yield consistent circuit analysis as long as the convention is not switched mid-calculation; schematics typically use conventional current.[^aac-conventional-electron-flow]

## Detailed explanation

Conventional current is the conventional direction of electric current, defined as the direction in which positive charge would move; in a metallic wire, electrons move in the opposite direction.[^aac-direct-current]

The sign of current is set by convention, not by the trajectory of specific carriers. For a charge `q`, movement with velocity in one direction contributes to conventional current according to the sign of `q`: for an electron it points in the opposite direction, and for a positive carrier – in the same direction. Therefore, the definition based on positive charge also works in media where carriers are not only electrons.[^aac-conventional-electron-flow][^aac-semiconductors]

In circuit analysis, a current arrow is assigned arbitrarily to a branch, and then Ohm's law and Kirchhoff's laws are applied consistently to the chosen signs of voltage and current. A negative result means that the actual conventional current flows opposite to the reference arrow; this does not mean the calculation is broken. Switching to electron flow would require consistently redefining directions across all notations, which typically only adds confusion.[^aac-conventional-electron-flow]

Example: if current in the external branch of a battery is arbitrarily designated as flowing from the positive terminal to the negative terminal, electrons in the metal wire drift in the opposite direction. In an electrolyte solution, current can be carried by ions of both signs, and in a semiconductor – by electrons and holes; conventional current describes the net direction of charge transport, rather than the movement of a single predetermined particle type.[^aac-conventional-electron-flow][^aac-semiconductors]
