---
id: emb-elintro-0174
title: "What is `RoHS` and what is it for?"
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
  - source_id: eu-rohs-directive
    title: "Directive 2011/65/EU on the restriction of the use of certain hazardous substances in electrical and electronic equipment"
    url: https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=CELEX:32011L0065
---


## Short answer

`RoHS` is EU legislation restricting certain hazardous substances in covered electrical and electronic equipment. Maximum concentration values apply to each homogeneous material individually, while scope and exemptions depend on the product category and the current edition of the rules.[^eu-rohs-directive]

## Detailed explanation

`RoHS` is the abbreviated name for EU regulations restricting certain hazardous substances in electrical and electronic equipment. The requirements are established by Directive 2011/65/EU as amended. It applies to equipment falling within defined categories, rather than being a blanket ban on any quantity of a substance in any product.[^eu-rohs-directive]

Restrictions are evaluated by concentration in homogeneous material, not averaged across the entire device. For example, solder in a joint and wire insulation are separate materials for this analysis. For six substances, including lead, mercury, and Cr(VI), the typical threshold limit is 0.1 % by weight; for cadmium, 0.01 %. Amendment (EU) 2015/863 added four phthalates to the list, so the current Annex II contains ten restricted substances.[^eu-rohs-directive]

The directive provides exemptions for specific applications and timeframes, so compliance determinations must be made for the specific product, materials, and target market. A component marked RoHS compliant does not on its own prove compliance of the fully assembled device: the end-equipment manufacturer must account for components, supplier documentation, and applicable exemptions.[^eu-rohs-directive]

**Common mistake:** treating RoHS as an electrical safety standard or as an absolute claim of "zero lead." It is a requirement restricting specific substances with numerical thresholds and exemptions; it does not replace verification of other safety and environmental regulations.
