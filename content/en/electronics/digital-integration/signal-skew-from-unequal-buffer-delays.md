---
id: emb-elinteg-0037
title: "Why does asymmetrical buffering across parallel lines cause signal skew?"
track: electronics
section: digital-integration
sources:
  - source_id: ti-szza036c
    title: "TI SZZA036C: Understanding and Interpreting Standard-Logic Data Sheets"
    url: https://www.ti.com/lit/an/szza036c/szza036c.pdf
  - source_id: ti-timing-analysis
    title: "Texas Instruments: Understanding Timing Specifications in Digital Logic"
    url: https://www.ti.com/lit/an/szza036b/szza036b.pdf
  - source_id: floyd-digital-fundamentals
    title: "Thomas L. Floyd: Digital Fundamentals (11th Edition), Pearson"
    url: https://www.pearson.com/en-us/subject-catalog/p/digital-fundamentals/P200000003290
  - source_id: horowitz-art-of-electronics
    title: "Paul Horowitz, Winfield Hill: The Art of Electronics (3rd Edition), Cambridge University Press"
    url: https://artofelectronics.net/
---

## Short answer

Every buffer element introduces a finite propagation delay `t_pd` (typically `1 to 10 ns` depending on logic family). When some parallel bus lines pass through buffers while others are routed directly, a timing offset (skew) develops between the lines. If this skew exceeds receiver setup or hold margins, downstream registers latch corrupted or invalid data.[^ti-szza036c]

## Detailed explanation

TODO
