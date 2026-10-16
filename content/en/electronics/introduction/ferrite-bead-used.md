---
id: emb-elintro-0012
title: What is a ferrite bead and where is it used?
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
  - source_id: adi-bead
    title: "Analog Devices AN-1368: Ferrite bead demystified"
    url: https://www.analog.com/en/resources/app-notes/an-1368.html
---

## Short answer

A ferrite bead adds frequency-dependent impedance to attenuate unwanted high-frequency current or noise. It typically has low DC resistance and a resistive high-frequency region that dissipates noise energy as heat, but its behavior depends on frequency, bias current and the surrounding circuit. [^adi-bead]

## Detailed explanation

A bead is not simply an ideal inductor. Its impedance has resistive and reactive components: it can behave inductively at lower frequencies, dissipatively in a useful suppression band, and capacitively beyond resonance. Select it from impedance-versus-frequency curves rather than a single quoted impedance. [^adi-bead]

For example, a specification at 100 MHz does not tell you the impedance at 100 kHz. DC bias can substantially reduce effective inductance and filtering performance, so check the operating current as well as the thermal current rating. The DC resistance also causes voltage drop and power loss under load. [^adi-bead]

A bead with a shunt capacitor can form a supply filter, but the network can resonate and amplify noise in part of the spectrum. AN-1368 shows why damping and the surrounding source/load impedances matter. Therefore a bead is a component in a designed filter, not a guaranteed noise-removal device independent of placement and loading. [^adi-bead]
