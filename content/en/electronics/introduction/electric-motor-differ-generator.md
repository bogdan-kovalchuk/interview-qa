---
id: emb-elintro-0067
title: "How does an electric motor differ from a generator?"
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
  - source_id: openstax-motors
    title: "OpenStax University Physics Volume 2: Electric Generators and Back Emf"
    url: https://openstax.org/books/university-physics-volume-2/pages/13-6-electric-generators-and-back-emf
---

## Short answer

An electric motor converts electrical energy into mechanical work, while a generator converts mechanical work into electrical energy.[^openstax-motors] Structurally, they are similar, and many machines can operate in both modes: a motor rotated from the outside generates EMF itself.[^openstax-motors] Whether the generator outputs alternating current or direct current depends on its design, such as the presence of a commutator.

## Detailed explanation

An electric motor converts electrical energy into mechanical energy, while a generator converts mechanical energy into electrical energy. In a motor, current in the rotor conductors interacts with the magnetic field to produce torque; in a generator, mechanical rotation changes the magnetic flux through the windings and induces EMF.[^openstax-motors]

These are reciprocal directions of energy conversion, and many electrical machines can operate in both modes. The distinction is determined by which port receives energy and which port delivers it. A real machine has losses in the windings, magnetic core, bearings, and ventilation, so the conversion is not completely efficient.[^openstax-motors]

For example, a DC motor driven by an external mechanism generates voltage across its terminals. If a load is connected, it can supply electrical power and brake the rotation; the direction of current depends on polarity and the excitation circuit. An induction machine can also feed energy back into the grid when its shaft is driven faster than synchronous speed.[^openstax-motors]

**Common mistake:** saying that a generator always produces alternating current or that a motor and a generator are necessarily different construction types. The output will be alternating or direct current depending on the design and rectifier, and the fundamental difference lies in the direction of energy flow.[^openstax-motors]
