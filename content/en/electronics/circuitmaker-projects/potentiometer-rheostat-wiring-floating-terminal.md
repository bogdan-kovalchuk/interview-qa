---
id: emb-elcmproj-0014
title: "Why must the unused outer terminal of a potentiometer wired as a rheostat be tied to the wiper?"
track: electronics
section: circuitmaker-projects
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: bourns-trimmer-primer
    title: "Bourns: Trimpot Trimming Potentiometers - Interactive Trimmer Primer"
    url: https://www.bourns.com/docs/technical-documents/technical-library/trimpots/publications/bourns_trimmer_primer.pdf
  - source_id: horowitz-art-of-electronics
    title: "Paul Horowitz, Winfield Hill: The Art of Electronics (3rd Edition), Cambridge University Press"
    url: https://artofelectronics.net/
---

## Short answer

If the unused terminal of the resistive track is left floating, any vibration or wiper oxidation causes an instantaneous open circuit. The oscillator circuit then sees infinite resistance, causing clock oscillation to fail completely. Tying the wiper to the outer terminal limits the fault-condition resistance to the maximum nominal value of the potentiometer.[^udemy-electronics-course]

## Detailed explanation

TODO
