---
id: emb-elcmproj-0035
title: "How does the equal-temperament scale determine note frequencies in a musical synthesizer?"
track: electronics
section: circuitmaker-projects
sources:
  - source_id: ti-ne555-datasheet
    title: "Texas Instruments NE555 Precision Timers Datasheet"
    url: https://www.ti.com/lit/ds/symlink/ne555.pdf
  - source_id: horowitz-hill-art-of-electronics
    title: "Horowitz P., Hill W. The Art of Electronics. 3rd Edition. Cambridge University Press, 2015"
    url: https://artofelectronics.net/
  - source_id: allaboutcircuits-555-astable
    title: "All About Circuits: 555 Timer Astable Multivibrator"
    url: https://www.allaboutcircuits.com/tools/555-timer-astable-circuit/
---

## Short answer

In a 12-tone equal-temperament tuning system, the frequency of each successive semitone increases by a constant geometric ratio: `f_(n+1) = f_n * 2^(1/12) ≈ f_n * 1.05946`. A full octave of twelve semitones doubles the audio frequency. Calculating precise resistor values in synthesizer timing circuits relies directly on this exponential progression.[^ti-ne555-datasheet]

## Detailed explanation

TODO
