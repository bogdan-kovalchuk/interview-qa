---
id: emb-elintro-0069
title: "What is the photoelectric effect and what does it depend on?"
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
  - source_id: openstax-photoelectric
    title: "OpenStax University Physics Volume 3: Photoelectric Effect"
    url: https://openstax.org/books/university-physics-volume-3/pages/6-2-photoelectric-effect
---

## Short answer

The external photoelectric effect is the ejection of electrons from the surface of a material under the action of light. For a given material, a frequency not lower than the threshold frequency is required; intensity above the threshold primarily affects the number of emitted electrons rather than their maximum kinetic energy.[^openstax-photoelectric]

## Detailed explanation

The external photoelectric effect occurs when an electron absorbs a photon and gains enough energy to leave the surface of the material. The photon's energy is proportional to the frequency of light: `E = h*f`, where `h` is Planck's constant. Part of the energy is spent overcoming the material's work function, and the rest becomes the kinetic energy of the electron.[^openstax-photoelectric]

Therefore, a threshold frequency exists that depends on the material. If light has a lower frequency, the photons do not have the required energy, and increasing the intensity does not initiate external emission. Equivalently, you can speak of a threshold wavelength: since frequency and wavelength are inversely related, a shorter wavelength means higher photon energy.[^openstax-photoelectric]

When the frequency already exceeds the threshold, more intense light means more photons per unit time. Under otherwise identical conditions, this can increase the photocurrent, that is, the number of electrons escaping per unit time. The maximum kinetic energy of photoelectrons, in contrast, increases with frequency rather than simply with brightness.[^openstax-photoelectric]

**Common mistake:** claiming that very bright light of any color is sufficient. Below the threshold frequency, an individual photon cannot dislodge an electron, no matter how many such photons fall on the surface. This external photoelectric effect should also not be equated with the internal photoelectric effect in semiconductors, on which many photodiodes and solar cells operate.[^openstax-photoelectric]
