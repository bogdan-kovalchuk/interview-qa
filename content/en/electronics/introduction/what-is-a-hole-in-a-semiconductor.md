---
id: emb-elintro-0035
title: "What is a \"hole\" in a semiconductor?"
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
  - source_id: aac-electrons-and-holes
    title: "All About Circuits: Electrons and Holes"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/chpt-2/electrons-and-holes/
---

## Short answer

A hole is an unoccupied state in the valence band that behaves in a semiconductor model as a mobile carrier with charge `+e`. Its apparent motion is opposite to the transitions of electrons filling adjacent unoccupied states.[^aac-electrons-and-holes]

## Detailed explanation

A hole is the absence of an electron in an available valence state of a crystal, which is conveniently modeled as a mobile carrier with a positive charge.[^aac-semiconductors]

In a covalent crystal such as silicon, valence electrons participate in bonds and occupy valence band states. If an electron acquires sufficient energy and transitions to a conduction state, an unoccupied state remains in the valence band. An electron from a neighboring bond can transition into this vacancy, leaving a new vacancy behind; successive repetitions of such transitions result in an effective movement of the hole through the crystal.[^aac-electrons-and-holes]

A hole is not a standalone proton or a particle physically moving between atoms: it is a quasiparticle, that is, a useful description of the collective motion of electrons. It has an effective positive charge of `+e`, and the corresponding electron motion occurs in the opposite direction. In p-type material, acceptor doping promotes the generation of holes; in such material, they are majority carriers, although electrons can also carry charge as minority carriers.[^aac-electrons-and-holes][^aac-semiconductors]

Example: in a chain of adjacent bonds, suppose an electron repeatedly moves to an empty site to the left. After each transition, a vacancy remains to the right of the previous site, so the sequence of electron hops corresponds to the motion of a hole to the right. This description simplifies the analysis of current and p-n junctions: positive carriers can be tracked without claiming that a separate positive particle is moving through the crystal.[^aac-electrons-and-holes]
