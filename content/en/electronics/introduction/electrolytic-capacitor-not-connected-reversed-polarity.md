---
id: emb-elintro-0010
title: Why must an electrolytic capacitor not be connected with reversed polarity?
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
  - source_id: nichicon-polarity
    title: "Nichicon: Technical notes for aluminum electrolytic capacitors"
    url: https://www.nichicon.co.jp/english/products/pdf/aluminum.pdf
  - source_id: vishay-tantalum
    title: "Vishay: Solid tantalum capacitor FAQ"
    url: https://www.vishay.com/docs/40110/faq.pdf
---

## Short answer

Reverse voltage can damage a polarized electrolytic capacitor’s dielectric, causing leakage, heat and gas generation. Identify polarity from the exact component markings and datasheet: typical radial aluminum parts mark the negative side, whereas the bar on molded SMD tantalum capacitors marks the positive anode. [^nichicon-polarity] [^vishay-tantalum]

## Detailed explanation

In a polarized aluminum electrolytic capacitor, the thin oxide dielectric is formed for the intended polarity. Nichicon explains that reverse voltage can increase leakage and produce heat and gas, with possible venting or failure. An explosion is a possible severe outcome, not a guaranteed response to every momentary reversal. [^nichicon-polarity]

On typical radial aluminum parts, a negative stripe and an uncut longer positive lead help orientation. Lead length is no longer reliable after trimming. Do not turn the negative-stripe convention into a rule for all electrolytics: Vishay explicitly states that the white bar on molded SMD tantalum parts identifies the positive anode. [^vishay-tantalum]

Before installation, match the body marking and datasheet pinout to the schematic and PCB polarity. Also check the applied waveform: a positive average voltage does not make reverse excursions acceptable automatically. Observe rated voltage and permitted ripple current. Bipolar electrolytics are a distinct specified part type; do not assume an ordinary polarized part behaves like one. [^nichicon-polarity]
