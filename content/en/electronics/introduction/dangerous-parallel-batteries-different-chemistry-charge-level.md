---
id: emb-elintro-0060
title: "Why is it dangerous to parallel batteries of different chemistry or charge level?"
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
  - source_id: energizer-alkaline-faq
    title: "Energizer: Alkaline Batteries FAQ"
    url: https://data.energizer.com/pdfs/alkaline_faq.pdf
  - source_id: libretexts-battery-networks
    title: "Physics LibreTexts: Networks of Batteries and Resistors"
    url: https://phys.libretexts.org/Courses/University_of_California_Davis/UCD:_Physics_9C__Electricity_and_Magnetism/3:_Direct_Current_Circuits/3.3:_Networks_of_Batteries_and_Resistors
---

## Short answer

Directly paralleling batteries with different voltages produces a current between them, whose magnitude depends on the voltage difference and the total circuit resistance. Mixing batteries of different chemistries or states of charge without specially designed management is dangerous: excessive current, heating, damage, or leakage can occur.[^libretexts-battery-networks] [^energizer-alkaline-faq]

## Detailed explanation

The danger of a direct parallel connection is that both sources are placed across common terminals. If their voltages differ, the potential difference drives a current between the batteries. In a simple model, this current is determined by that difference and the sum of the internal resistances and connection resistances; a small total resistance can produce a large current even with no external load connected.[^libretexts-battery-networks]

State of charge affects voltage, but matching voltages at a single moment does not prove compatibility: different chemical systems have different operating limits and charging requirements. Excessive current can overheat cells and wiring. For lithium batteries, an improper operating regime can cause a hazardous condition, so manufacturer-specified configuration, protection, and management are required; internal resistance cannot be assumed to provide sufficient protection on its own.[^libretexts-battery-networks]

Manufacturer warnings against mixing new and used batteries or different chemical types also apply to standard multi-cell devices: a weaker cell can be driven into deep discharge by stronger ones, increasing the risk of leakage. This is a distinct mechanism from the balancing current in direct paralleling, but the practical takeaway is the same – use only manufacturer-specified compatible cells.[^energizer-alkaline-faq]

**Common mistake:** assuming that parallel batteries are safe as long as the labels show the same nominal voltage. Paralleling requires identical compatible chemistry, closely matched state of charge, and a manufacturer-approved circuit with proper protection.
