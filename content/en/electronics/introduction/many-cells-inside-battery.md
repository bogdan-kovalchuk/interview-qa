---
id: emb-elintro-0068
title: "How many cells are inside a 9V battery?"
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
  - source_id: energizer-9v
    title: "Energizer 6LR61 Alkaline Power: Product Datasheet"
    url: https://data.energizer.com/pdfs/alk-power-9v.pdf
  - source_id: energizer-522-datasheet
    title: "Energizer 522 9V alkaline battery datasheet"
    url: https://data.energizer.com/pdfs/522.pdf
  - source_id: battery-nomenclature
    title: "Wikipedia: Battery nomenclature (IEC 60086 designation system)"
    url: https://en.wikipedia.org/wiki/Battery_nomenclature
---

## Short answer

An alkaline 9 V battery has the IEC designation `6LR61` (or `6LF22`), and the first digit of such a code indicates the number of series-connected cells – that is, six cells.[^energizer-522-datasheet] [^battery-nomenclature] The nominal voltages of series cells add up: `6 × 1.5 V = 9 V`.[^aac-direct-current] Batteries of the 9 V format with different chemistry, such as lithium or NiMH, may have a different number of cells.

## Detailed explanation

A 9 V format battery is a battery pack, not necessarily a single electrochemical cell. In the common alkaline design, there are six cells connected in series inside. Each has a nominal voltage of about 1.5 V, so the sum of the nominal values gives 9 V.[^energizer-522-datasheet] [^battery-nomenclature]

A series connection means that the positive terminal of one cell is connected to the negative terminal of the next. The same current flows through all cells, and their electromotive forces add together. For example, for six identical cells, `V_total = 6*1.5 V = 9 V` by nominal values.[^aac-direct-current]

However, the 9 V marking on the case is a nominal designation, not a promise of constant voltage. Terminal voltage depends on chemistry, charge, temperature, load, and internal resistance. Not all batteries of this format have the same internal construction: a manufacturer may use different chemistry or cell arrangement. Therefore, the answer "six" applies to the common alkaline variant, not to every possible 9-volt pack.[^energizer-9v]

**Common mistake:** assuming the number of cells is universal based solely on the voltage rating. You should consult the documentation for a specific model, because the same nominal voltage does not guarantee the same chemistry or internal structure.[^energizer-9v]
