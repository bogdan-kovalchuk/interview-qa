---
id: emb-elintro-0119
title: "What is a bi-color `LED` and how does it produce yellow?"
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
  - source_id: aac-led-colour-mixing
    title: "All About Circuits: Special-purpose Diodes"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/chpt-3/special-purpose-diodes/
---

## Short answer

A bi-color `LED` contains emitters of different colors in a single package; in a common red-green pair, simultaneous emission can be perceived as yellow due to additive color mixing.[^aac-led-colour-mixing] The specific pinout and drive method depend on the model, so check them in the datasheet.

## Detailed explanation

A bi-color `LED` combines two LED dies of different colors in a single package; red and green light components together can create a yellow impression for the observer.[^aac-led-colour-mixing]

The color of an individual `LED` depends on the material and structure of its semiconductor junction. In a bi-color component, there may be two separate emitters, such as red and green, with their own anodes and cathodes or with a shared electrode. The manufacturer determines the specific pinout; the name bi-color by itself does not indicate whether both dies can be turned on simultaneously.[^aac-led-colour-mixing]

When red and green light enter the eye simultaneously, their spectral contributions add up, and visual perception can approach yellow. This is additive color mixing, not pigment mixing. The hue is not guaranteed to be identical across different parts: it depends on the emitter spectra, their relative brightness, the package optics, and viewing conditions. Therefore, practical indication must be evaluated on the actual component.[^aac-led-colour-mixing]

In some bi-color models, the dies are connected anti-parallel: reversing polarity turns on one color or the other, but such a configuration typically does not allow forward current to be applied independently to both dies at the same time. Other components have separate controllable leads or a common anode/cathode and allow both colors to be illuminated. The number of pins and the internal circuit must be taken from the datasheet of the specific model.[^aac-led-colour-mixing]

**Example:** if a red-green component has separate pins, a controller can supply current to both dies in a controlled manner. Changing their relative intensity changes the perceived hue; equal current does not necessarily produce a visually balanced blend, because luminous efficacy and eye sensitivity differ for these colors.[^aac-led-colour-mixing]

**Common mistake:** thinking that the package physically emits a single new yellow color or that every bi-color `LED` can light up both colors simultaneously. In reality, the yellow impression arises from the sum of light at the level of visual perception, and the available operating modes are determined by the electrical connection of the dies.[^aac-led-colour-mixing]
