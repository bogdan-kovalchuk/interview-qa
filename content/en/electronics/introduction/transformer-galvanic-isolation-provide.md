---
id: emb-elintro-0159
title: "What does a transformer's galvanic isolation provide?"
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
  - source_id: aac-transformer-isolation
    title: "All About Circuits: Transformer Isolation"
    url: https://www.allaboutcircuits.com/technical-articles/transformer-isolation/
---

## Short answer

There is no direct conductive path between separate primary and secondary windings: energy is transferred by magnetic coupling.[^aac-transformer-isolation] This can break a ground loop and reduce shock hazard, but safety depends on insulation ratings, construction, and system connections.[^aac-transformer-isolation]

## Detailed explanation

Galvanic isolation of a transformer means that the primary and secondary windings are not connected by a direct conductor. Energy transfers between them through alternating magnetic flux in the core, rather than through a shared conductive path between circuits.[^aac-transformer-isolation]

Such separation allows powering the secondary circuit without a shared ground point with the primary. This is useful, for example, to avoid an unwanted ground loop or to isolate a measurement circuit from another circuit that has a shared ground.[^aac-transformer-isolation] Galvanic isolation does not mean that a signal or energy does not pass at all: they are transferred via the magnetic field, and the transformer can simultaneously change the AC voltage level.

Isolation does not guarantee automatic protection against any electric shock. The secondary side remains electrically active, and its voltage can be hazardous relative to ground or between terminals; breakdown, incorrect wiring, or another conductive path can destroy the expected separation.[^aac-transformer-isolation] For a protective function, appropriate clearances, creepage distances, materials, operating voltage, and the application category of the specific device are essential.

**Common mistake:** assuming that any transformer automatically ensures safety. An autotransformer has a shared winding for input and output, and thus does not provide the same galvanic separation as a transformer with separate windings.[^aac-transformer-isolation]

In practice, you must check the schematic and component documentation rather than relying only on the word "transformer" in the name. If the secondary side is additionally connected to the primary via ground, a shield, a measuring instrument, or another circuit, this path can alter the isolation behavior of the entire system.[^aac-transformer-isolation]
