---
id: emb-elinteg-0061
title: "How does the dual-stage Master-Slave architecture eliminate race conditions in pulse-triggered flip-flops?"
track: electronics
section: digital-integration
sources:
  - source_id: floyd-digital-fundamentals
    title: "Thomas L. Floyd: Digital Fundamentals (11th Edition), Pearson"
    url: https://www.pearson.com/en-us/subject-catalog/p/digital-fundamentals/P200000003290
  - source_id: tocci-digital-systems
    title: "Ronald J. Tocci, Neal S. Widmer, Gregory L. Moss: Digital Systems: Principles and Applications (12th Edition), Pearson"
    url: https://www.pearson.com/en-us/subject-catalog/p/digital-systems-principles-and-applications/P200000003297
  - source_id: mano-digital-design
    title: "M. Morris Mano, Michael D. Ciletti: Digital Design: With an Introduction to the Verilog HDL, 5th Edition. Pearson"
    url: https://www.pearson.com/en-us/subject-catalog/p/digital-design-with-an-introduction-to-the-verilog-hdl/P200000003296
---

## Short answer

The master-slave topology consists of two cascaded latches clocked by complementary signals. While the clock pulse is high, the input master latch is transparent and captures the data, whereas the output slave latch remains disabled. When the clock transitions low, the master disconnects from inputs and the slave transfers the captured state to output `Q`, preventing race-around conditions.[^floyd-digital-fundamentals]

## Detailed explanation

TODO
