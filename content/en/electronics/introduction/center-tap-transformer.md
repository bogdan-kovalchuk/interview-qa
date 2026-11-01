---
id: emb-elintro-0160
title: "What is a center tap on a transformer?"
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
  - source_id: electronics-tutorials-multiple-windings
    title: "Electronics Tutorials: Multiple Winding Transformers with Multiple Coils"
    url: https://www.electronics-tutorials.ws/transformer/multiple-winding-transformers.html
---

## Short answer

`Center tap` is a connection from the midpoint of the secondary winding; for a symmetrical winding, it provides two AC voltages equal in magnitude in antiphase relative to this point.[^electronics-tutorials-multiple-windings] For example, the `12-0-12 V` designation means `12 V` RMS from each end to the tap and `24 V` between the ends; these are not ready-made `+12 V` and `−12 V` DC rails.[^electronics-tutorials-multiple-windings]

## Detailed explanation

`Center tap` is a connection attached to the middle of the transformer's secondary winding. It divides the winding into two sections; if they have the same number of turns, the voltage of each section relative to the tap has an equal magnitude.[^electronics-tutorials-multiple-windings]

When alternating magnetic flux passes through the winding, voltages across the two halves have opposite instantaneous polarities relative to the center tap. If the center point is made the circuit common wire, the ends of the secondary winding form two AC outputs shifted in phase by 180 degrees. The voltage between the extreme ends equals the sum of the magnitudes of the half-voltages at each instant, rather than the voltage of a single half.[^electronics-tutorials-multiple-windings]

For example, for a symmetrical winding designated `12-0-12 V`, each half nominally has `12 V` RMS relative to the tap, and between the outer terminals there will be `24 V` RMS. The `12-0-12 V` label describes an AC winding; to obtain stable DC rails, rectifiers and, if needed, filtering and regulation are required.[^electronics-tutorials-multiple-windings]

The tap is not necessarily located exactly in the middle. If the number of turns or the loading of the halves differs, the voltages will be asymmetrical; even with a symmetrical winding, unequal loads can shift the midpoint potential in a real circuit.[^electronics-tutorials-multiple-windings]

**Common mistake:** calling the two ends of the secondary winding `+12 V` and `−12 V` without clarifying the reference point and rectification. These are antiphase AC voltages relative to the center tap; the polarity of DC outputs is determined by the rectification circuit.[^electronics-tutorials-multiple-windings]
