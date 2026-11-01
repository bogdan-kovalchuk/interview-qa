---
id: emb-elintro-0039
title: "What is a valence electron and why does it matter in electronics?"
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
  - source_id: openstax-semiconductor-doping
    title: "OpenStax University Physics Volume 3, 9.6 Semiconductors and Doping"
    url: https://openstax.org/books/university-physics-volume-3/pages/9-6-semiconductors-and-doping
  - source_id: aac-conductors-valence
    title: "All About Circuits: Introduction to Conductance and Conductors"
    url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-12/introduction-conductance-and-conductors/
---

## Short answer

Valence electrons are the electrons in the outermost shell of an atom that participate in chemical bonding and influence the electronic properties of a material.[^aac-semiconductors] In silicon, four valence electrons form bonds within the crystal lattice; adding impurities changes the number of available charge carriers.[^openstax-semiconductor-doping] However, conductivity is not determined solely by the number of valence electrons – the material structure and energy states are also important.[^aac-conductors-valence]

## Detailed explanation

Valence electrons are the electrons in the outer electron shell that participate in bonds between atoms. Their behavior, together with the structure of the substance, determines how readily charge can be transported through the material.[^aac-conductors-valence]

In a silicon crystal, each atom has four valence electrons and forms covalent bonds with neighboring atoms. Given sufficient energy, an electron can transition to a state where it participates in conduction, leaving behind a hole in the valence band.[^openstax-semiconductor-doping]

Doping makes it possible to purposefully alter carrier concentration: donor impurities add electrons, while acceptor impurities promote the appearance of holes. This is how the properties of the semiconductor are controlled in diodes and transistors.[^openstax-semiconductor-doping]

Example: a phosphorus atom has five valence electrons. In a silicon lattice, four of them participate in bonds, while the fifth is more weakly bound and can transition into the conduction band at room temperature.[^openstax-semiconductor-doping]

It is precisely the ability to alter the number of mobile carriers that makes impurities an important circuit design tool. Different regions of a single crystal can be doped differently, creating areas with distinct electrical properties. At the boundaries of such regions, junctions are formed whose behavior underpins diodes and transistors. Valence electrons help explain bond formation and the initial carriers, but they do not fully describe device geometry or its operation in a circuit.[^openstax-semiconductor-doping]
