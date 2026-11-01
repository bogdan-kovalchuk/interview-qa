---
id: emb-elintro-0040
title: "Why are N-type impurities called donors and P-type impurities acceptors?"
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
---

## Short answer

In silicon, an impurity with five valence electrons can donate a weakly bound fifth electron for conduction, so it is called a donor; the material becomes `n`-type.[^openstax-semiconductor-doping] An impurity with three valence electrons can accept an electron to complete a bond, leaving a mobile hole, so it is called an acceptor; the material becomes `p`-type.[^openstax-semiconductor-doping] The type names indicate the majority charge carriers, not the net charge of the crystal.

## Detailed explanation

In a silicon crystal, atoms form four covalent bonds because silicon has four valence electrons. If a silicon atom is replaced with an atom having five valence electrons, such as phosphorus, four electrons participate in the bonds, while the fifth is weakly held by the lattice. It can transition to the conduction band; the impurity is called a donor, and the semiconductor is `n`-type.[^openstax-semiconductor-doping]

An atom with three valence electrons, such as aluminum, lacks an electron for one of the bonds with neighboring silicon atoms. Such a state can accept an electron from the valence band, leaving behind a hole that acts as a mobile positive carrier. This impurity is called an acceptor, and the material is `p`-type.[^openstax-semiconductor-doping]

Example: phosphorus in silicon is a typical donor impurity, while boron is a typical acceptor impurity. The letters `n` and `p` describe the sign of the majority mobile carriers, not that the entire doped crystal carries a negative or positive charge, respectively.[^openstax-semiconductor-doping]

After donating an electron, the donor becomes a fixed positive ion in the lattice, while the electron can transport charge through the crystal. When an acceptor captures an electron from a valence bond, the fixed acceptor ion carries a negative charge, and the unfilled bond manifests as a mobile hole. In a typical sample, the net charge remains practically neutral: the fixed charged impurities balance out the mobile carriers.[^openstax-semiconductor-doping]
