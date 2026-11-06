---
id: emb-elinteg-0067
title: "What steps are involved in formal FSM synthesis from a state transition diagram to a state table?"
track: electronics
section: digital-integration
sources:
  - source_id: mano-digital-design
    title: "M. Morris Mano, Michael D. Ciletti: Digital Design: With an Introduction to the Verilog HDL, 5th Edition. Pearson"
    url: https://www.pearson.com/en-us/subject-catalog/p/digital-design-with-an-introduction-to-the-verilog-hdl/P200000003296
  - source_id: floyd-digital-fundamentals
    title: "Thomas L. Floyd: Digital Fundamentals (11th Edition), Pearson"
    url: https://www.pearson.com/en-us/subject-catalog/p/digital-fundamentals/P200000003290
  - source_id: tocci-digital-systems
    title: "Ronald J. Tocci, Neal S. Widmer, Gregory L. Moss: Digital Systems: Principles and Applications (12th Edition), Pearson"
    url: https://www.pearson.com/en-us/subject-catalog/p/digital-systems-principles-and-applications/P200000003297
---

## Short answer

Synthesis begins by constructing a state transition diagram where nodes represent stable states and directed edges indicate input-driven transition conditions. Next, states are encoded into binary vectors (such as binary or one-hot encoding) to construct a state transition table. From this table, Boolean next-state equations are derived for each flip-flop with respect to current state variables and inputs.[^mano-digital-design]

## Detailed explanation

TODO
