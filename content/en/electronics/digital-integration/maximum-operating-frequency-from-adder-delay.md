---
id: emb-elinteg-0047
title: "How is maximum operating frequency estimated from adder propagation delay?"
track: electronics
section: digital-integration
sources:
  - source_id: floyd-digital
    title: "Thomas L. Floyd: Digital Fundamentals, 11th Edition. Pearson"
    url: https://www.pearson.com/en-us/subject-catalog/p/digital-fundamentals/P200000003254
  - source_id: patterson-hennessy-cod
    title: "David A. Patterson, John L. Hennessy: Computer Organization and Design: The Hardware/Software Interface, 5th Edition. Morgan Kaufmann"
    url: https://www.elsevier.com/books/computer-organization-and-design/patterson/978-0-12-407726-3
  - source_id: tocci-digital-systems
    title: "Ronald J. Tocci, Neal S. Widmer, Gregory L. Moss: Digital Systems: Principles and Applications, 12th Edition"
    url: https://www.pearson.com/en-us/subject-catalog/p/digital-systems-principles-and-applications/P200000003297
---

## Short answer

The maximum clock frequency `f_max` of a synchronous arithmetic datapath is determined by the minimum clock period `T_clk` covering the critical path delay. The required period is `T_clk >= t_cq + t_adder + t_setup + t_skew`, where `t_cq` is source register clock-to-Q delay, `t_adder` is combinational adder delay, `t_setup` is destination setup time, and `t_skew` is clock skew. Maximum frequency is `f_max = 1 / T_clk_min`.[^floyd-digital]

## Detailed explanation

TODO
