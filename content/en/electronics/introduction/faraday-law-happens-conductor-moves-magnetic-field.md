---
id: emb-elintro-0066
title: "Faraday's law – what happens when a conductor moves in a magnetic field?"
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
  - source_id: openstax-faraday
    title: "OpenStax University Physics Volume 2: Faraday's Law"
    url: https://openstax.org/books/university-physics-volume-2/pages/13-1-faradays-law
  - source_id: openstax-motional-emf
    title: "OpenStax University Physics Volume 2: Motional Emf"
    url: https://openstax.org/books/university-physics-volume-2/pages/13-3-motional-emf
---

## Short answer

When the magnetic flux through a closed circuit changes, an EMF is induced in it; for a moving conductor, it arises from the magnetic force acting on charges.[^openstax-faraday] Flux change can occur through motion, field variation, or rotation of the circuit.[^openstax-faraday]

## Detailed explanation

Faraday's law describes induced EMF as the result of changing magnetic flux through a circuit. Flux depends on the magnetic field, the circuit area, and its orientation, so it can be changed by moving the conductor or magnet, altering the field, or rotating the circuit.[^openstax-faraday]

For a coil with `N` turns, the contribution of each turn adds up: `EMF = -N*dΦ/dt`. The minus sign expresses Lenz's law: the induced current creates a field that opposes the change in flux that caused it. The direction of current depends on how the flux is changing.[^openstax-faraday]

If a straight conductor of length `L` moves at velocity `v` in a uniform field `B`, with motion, conductor, and field mutually perpendicular, the magnitude of motional EMF equals `EMF = B*L*v`. Charges experience a Lorentz force and separate along the conductor. For different geometries, perpendicular components are taken into account; motion in a field does not guarantee an EMF if the conductor moves parallel to the field.[^openstax-motional-emf]

Example: a conductor of length `0.2 m` moves at a speed of `3 m/s` perpendicular to a `0.5 T` field; under idealized conditions `EMF = 0.5*0.2*3 = 0.3 V`. In a generator, rotation changes flux and produces output EMF. In a transformer, current in the primary winding changes the flux, so conductors do not need to move.[^openstax-faraday]

**Common mistake:** assuming that conductor motion is strictly required for induction. The decisive condition is changing flux through the circuit; a stationary coil also experiences an induced EMF in a time-varying field.[^openstax-faraday]
