---
id: emb-elinteg-0062
title: "What states does a universal JK flip-flop generate and why is the J = 1, K = 1 mode fundamental for counters?"
track: electronics
section: digital-integration
sources:
  - source_id: floyd-digital-fundamentals
    title: "Thomas L. Floyd: Digital Fundamentals (11th Edition), Pearson"
    url: https://www.pearson.com/en-us/subject-catalog/p/digital-fundamentals/P200000003290
  - source_id: tocci-digital-systems
    title: "Ronald J. Tocci, Neal S. Widmer, Gregory L. Moss: Digital Systems: Principles and Applications (12th Edition), Pearson"
    url: https://www.pearson.com/en-us/subject-catalog/p/digital-systems-principles-and-applications/P200000003297
  - source_id: ti-sn74ls112a-datasheet
    title: "Texas Instruments: SN54/74LS112A Dual J-K Negative-Edge-Triggered Flip-Flops Datasheet"
    url: https://www.ti.com/lit/ds/symlink/sn74ls112a.pdf
---

## Short answer

A JK flip-flop resolves the invalid state of an SR latch: `J = 0, K = 0` holds state, `J = 1, K = 0` sets the output to `1`, and `J = 0, K = 1` resets it to `0`. The combination `J = 1, K = 1` configures toggle mode, where each clock pulse inverts the output. This toggle behavior makes the JK flip-flop an ideal divide-by-2 frequency divider and a core building block for binary counters.[^floyd-digital-fundamentals]

## Detailed explanation

TODO
