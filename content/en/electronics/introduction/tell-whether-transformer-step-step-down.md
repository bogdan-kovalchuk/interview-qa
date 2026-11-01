---
id: emb-elintro-0157
title: "How do you tell whether a transformer is step-up or step-down?"
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
  - source_id: electronics-tutorials-transformer-basics
    title: "Electronics Tutorials: Transformer Basics and Transformer Principles"
    url: https://www.electronics-tutorials.ws/transformer/transformer-basics.html
---

## Short answer

Compare the number of turns of the secondary and primary windings: `N2 > N1` means step-up, and `N2 < N1` means step-down.[^electronics-tutorials-transformer-basics] For an ideal transformer, voltage is proportional to the number of turns; actual voltage under load also depends on losses and internal resistance.[^electronics-tutorials-transformer-basics]

## Detailed explanation

A transformer is called step-up or step-down depending on whether the secondary voltage is higher or lower than the primary voltage. In the basic model, the voltage across a winding is proportional to its number of turns, because the same alternating magnetic flux passes through the turns of both windings.[^electronics-tutorials-transformer-basics]

Therefore, the primary and secondary windings satisfy the relationship `V2/V1 = N2/N1` for an ideal transformer. If the secondary has more turns than the primary, the voltage increases and this is step-up; if fewer, the voltage decreases and this is step-down. With an equal number of turns, this gives a transformer with approximately equal voltages across the windings.[^electronics-tutorials-transformer-basics]

For example, if `N1 = 500` and `N2 = 1000`, the ideal voltage ratio is `V2/V1 = 2`; for a primary `12 V`, you expect about `24 V` on the secondary winding without a load. This is a calculation assuming ideal coupling of the windings, not a guarantee of the exact value for any real device.[^electronics-tutorials-transformer-basics]

Carefully determine which is the primary and which is the secondary winding: the designations are determined by the connection and the direction of energy transfer in a specific circuit, not by which winding is physically larger. For multi-tap transformers, you also need to clarify between which specific terminals the voltage is measured; a tapped winding can have different effective numbers of turns.[^electronics-tutorials-transformer-basics]

**Common mistake:** treating the number of turns as the sole condition for the actual output voltage. It sets the ideal ratio; sag under load, frequency, and power rating depend on the transformer design.[^electronics-tutorials-transformer-basics]
