---
id: emb-elintro-0294
title: "What is an antiparallel connection of two LEDs?"
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
  - source_id: kingbright-led-ratings
    title: "Kingbright: 2022–2023 Catalog, Technical Notes"
    url: https://www.kingbrightusa.com/webimages/2021/ecatalog/files/basic-html/page63.html
---

## Short answer

Antiparallel LEDs share the same two circuit nodes but are connected with opposite polarities. For either supply polarity, forward current flows through one LED while the other is reverse-biased; ensure the applied reverse voltage does not exceed the maximum rating in the datasheet.[^kingbright-led-ratings]

## Detailed explanation

An antiparallel connection consists of two diodes connected between the same two circuit nodes with opposing anode and cathode polarities. For one voltage polarity, one LED is forward-biased and can emit light, while the other is reverse-biased. When the polarity is reversed, their roles swap. Such a pair can be used to indicate both directions of current, such as under alternating control polarity.[^kingbright-led-ratings]

The circuit itself does not limit current: a current-limiting element is required, typically a resistor in series with the pair. Operating forward current flows through one LED, while the other experiences approximately that LED's forward drop in the reverse direction. Whether this is safe for the non-conducting LED is determined by its maximum reverse voltage rating. A Kingbright catalog lists a 5 V limit for certain types, but the parameter depends on the specific component model.[^kingbright-led-ratings]

**Common mistake:** assuming that each LED unconditionally protects the other. The pair clamps reverse voltage to roughly the conducting LED's forward drop only within allowable current limits and with properly matched component characteristics. Always check the component datasheet for the specific part; if necessary, add a dedicated protection diode.

Example: with a positive voltage on the first node, the LED whose anode connects there is forward-biased and conducts current, while the opposing LED is reverse-biased. Under negative polarity, the opposing LED becomes the conducting path. Pinout polarity and maximum reverse voltage ratings should be verified in the selected component's datasheet.[^kingbright-led-ratings]
