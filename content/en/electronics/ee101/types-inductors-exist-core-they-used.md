---
id: emb-elee-0043
title: "What types of inductors exist by core material, and where are they used?"
track: electronics
section: ee101
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-alternating-current
    title: "All About Circuits textbook, Volume II: AC"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
---

## Short answer

Inductors are made with air, ferrite, powdered iron, and other core materials; core selection and geometry depend on frequency, current rating, losses, and size constraints. An air-core coil eliminates core losses, whereas ferrite and powdered-iron cores achieve higher inductance in compact footprints, though subject to their own frequency and saturation limits.[^aac-alternating-current]

## Detailed explanation

An inductor is defined not solely by its core material: geometry, winding technique, frequency range, current rating, and allowable losses are equally critical. Names such as "toroidal" describe shape rather than material: a toroid can be wound on a variety of magnetic materials, and its performance cannot be deduced from geometry alone.[^aac-alternating-current]

An air-core coil lacks a magnetic core, eliminating core losses and saturation. It is often useful at high frequencies, but achieving a target inductance typically requires more turns and greater physical volume. Ferrite cores offer high magnetic permeability and are widely used in high-frequency chokes and transformers. Powdered iron and composite materials exhibit different loss and saturation characteristics; they are chosen based on specific manufacturer curves and ratings rather than a crude rule like "iron is only for line-frequency mains".[^aac-alternating-current]

A toroidal shape can reduce external stray magnetic flux compared to an open-core coil when properly wound, but it is not a guarantee of zero radiated emissions. Inductors are deployed in LC filters, DC-DC converters, chokes, and transformers. Operating frequency, saturation current, thermal limits, and losses must be validated against the manufacturer datasheet for the specific component.[^aac-alternating-current]

Example selection: for an inductor in a switching converter, one first determines the operating frequency, average and peak currents, and required inductance, then evaluates core losses, saturation current, and temperature rise. For a mains filter, operating frequency and current profile differ substantially, so core types cannot be mechanically copied from one application to another.[^aac-alternating-current]

**Common mistakes:**

- Assuming all ferrite cores are suitable for arbitrary frequencies or currents.
- Inferring core material solely from a toroidal shape.
- Treating core selection guidelines as universal rules when specific choices depend on winding construction and component datasheets.[^aac-alternating-current]
