---
id: emb-elinteg-0065
title: "What core hardware building blocks constitute a sequential finite state machine (FSM)?"
track: electronics
section: digital-integration
sources:
  - source_id: harris-harris-ddca
    title: "David Money Harris, Sarah L. Harris: Digital Design and Computer Architecture, 2nd Edition. Morgan Kaufmann"
    url: https://www.elsevier.com/books/digital-design-and-computer-architecture/harris/978-0-12-394424-5
  - source_id: floyd-digital-fundamentals
    title: "Thomas L. Floyd: Digital Fundamentals (11th Edition), Pearson"
    url: https://www.pearson.com/en-us/subject-catalog/p/digital-fundamentals/P200000003290
  - source_id: tocci-digital-systems
    title: "Ronald J. Tocci, Neal S. Widmer, Gregory L. Moss: Digital Systems: Principles and Applications (12th Edition), Pearson"
    url: https://www.pearson.com/en-us/subject-catalog/p/digital-systems-principles-and-applications/P200000003297
---

## Short answer

A hardware finite state machine comprises a state register (synchronous flip-flops), next-state combinational logic, and output logic. The state register stores the current state, next-state logic computes the upcoming state based on current state and external inputs, and a clock signal synchronizes transitions. Output logic maps internal states and inputs into control signals.[^harris-harris-ddca]

## Detailed explanation

TODO
