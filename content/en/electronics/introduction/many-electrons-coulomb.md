---
id: emb-elintro-0033
title: "How many electrons are in 1 coulomb?"
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
  - source_id: nist-elementary-charge
    title: "NIST CODATA: elementary charge"
    url: https://physics.nist.gov/cuu/Constants/Value/e.html
---

## Short answer

Approximately `6.24 × 10¹⁸` electrons have a total charge magnitude of `1 C`, because the charge magnitude of a single electron is exactly `1.602176634 × 10⁻¹⁹ C`. At a current of `1 mA` for `1 s`, approximately `6.24 × 10¹⁵` electrons pass through a cross-section.[^nist-elementary-charge][^aac-direct-current]

## Detailed explanation

The charge magnitude of an electron equals the elementary charge `e = 1.602176634 × 10⁻¹⁹ C`; this value is exact in SI. The charge of the electron itself is negative, `−e`, and the question "how many electrons correspond to one coulomb" typically asks for the number of particles corresponding to that same magnitude of charge, rather than the sign of the net charge.[^nist-elementary-charge]

The number of particles is found by dividing the magnitude of total charge by the magnitude of the charge of a single carrier: `N = |Q|/e`. Since electron charges are discrete, the result for an arbitrary `Q` may not be an integer if it represents a measured average value or an approximation; for counting actual individual electrons, the quantity is an integer. In practical electrical quantities, such rounding does not alter the useful accuracy of the answer.[^nist-elementary-charge]

For direct current, `Q = I*t` applies: `1 mA` over `1 s` transfers `0.001 C`, which corresponds to approximately `6.24 × 10¹⁵` electrons by magnitude. This is the amount of charge that passed through the selected cross-section during that time, not the total number of electrons in the wire. For alternating current or a time-varying signal, calculating the charge requires taking into account the entire time waveform of the current, rather than multiplying an arbitrary instantaneous value by the interval.[^nist-elementary-charge][^aac-direct-current]
