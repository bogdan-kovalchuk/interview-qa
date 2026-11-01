---
id: emb-elintro-0029
title: "Why is silicon a semiconductor?"
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
  - source_id: mit-semiconductor-physics
    title: "MIT OpenCourseWare: 6.012, Lecture 2 – Semiconductor Physics (I)"
    url: https://ocw.mit.edu/courses/6-012-microelectronic-devices-and-circuits-fall-2005/resources/lec2/
---

## Short answer

In crystalline silicon, valence electrons form covalent bonds; thermal energy can free some electrons and create mobile electron-hole pairs. Their quantity depends on temperature, which allows the conductivity of silicon to be controlled, notably through doping.[^mit-semiconductor-physics]

## Detailed explanation

Silicon is a semiconductor due to its crystal structure and the energy states of its electrons, not simply because the atom has "four valence electrons." In a crystal, each Si atom shares valence electrons with its neighbors and forms covalent bonds; at very low temperatures, nearly all of these electrons remain bound.[^mit-semiconductor-physics]

At finite temperatures, some bonds can break due to thermal energy. This generates a mobile electron and a hole – the absence of an electron in a bond, which behaves like a positive charge carrier. An electric field can cause both types of carriers to move, producing an electric current.[^mit-semiconductor-physics]

In intrinsic silicon, thermal generation produces electrons and holes in pairs. Introducing impurities during doping makes it possible to control carrier concentrations: donor dopants increase the electron concentration, whereas acceptor dopants increase the hole concentration. It is precisely this controllability that makes silicon suitable for diodes and transistors; the claim that it is a semiconductor solely because of an intermediate number of valence electrons misses the crucial role of crystal structure and carrier energy.[^mit-semiconductor-physics]

Thus, valence electrons explain how the lattice is formed, but electrons and holes that have become mobile can transport charge.
